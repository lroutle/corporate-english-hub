import sys
import math
import pygame

# ==========================================
# 1. CONSTANTS & THERMODYNAMIC MODEL
# ==========================================
WIDTH, HEIGHT = 1280, 720
FPS = 60

# Colors
BG_DARK = (24, 24, 32)
PANEL_BG = (38, 38, 50)
TEXT_WHITE = (240, 240, 245)
TEXT_MUTED = (170, 175, 190)
ACCENT_BLUE = (77, 166, 255)
ACCENT_ORANGE = (255, 153, 51)
ACCENT_RED = (255, 90, 90)
CRANK_GOLD = (255, 204, 0)
PISTON_SILVER = (180, 186, 195)
CYLINDER_WALL = (210, 215, 222)

# Geometry (in pixels for screen rendering)
R_PX = 55.0        # Crank radius
L_PX = 185.0       # Connecting rod length
BORE_PX = 130.0    # Cylinder bore width
PISTON_H = 44.0    # Piston height

# Thermodynamic constants
GAMMA = 1.35
P_ATM = 1.0  # bar


def piston_offset_y(theta_deg):
    """Return vertical distance from crank center to piston pin (pixels)."""
    rad = math.radians(theta_deg)
    return R_PX * math.cos(rad) + math.sqrt(L_PX**2 - (R_PX * math.sin(rad))**2)


def norm_volume(theta_deg, cr):
    """Normalized cylinder volume V / V_c ranging from 1.0 (TDC) to CR (BDC)."""
    y = piston_offset_y(theta_deg)
    y_tdc = L_PX + R_PX
    stroke_frac = (y_tdc - y) / (2.0 * R_PX)
    return 1.0 + (cr - 1.0) * stroke_frac


def compute_4s_state(angle_deg, cr4):
    """Return (phase_str, rgb_color, in_open, ex_open, spark, pressure_bar, norm_vol)."""
    a = angle_deg % 720.0
    v = norm_volume(a, cr4)

    if 0.0 <= a < 180.0:
        return "1. INTAKE", (70, 155, 245), True, False, False, P_ATM * 0.9, v
    elif 180.0 <= a < 360.0:
        prog = (a - 180.0) / 180.0
        col = (
            int(70 + 185 * prog),
            int(155 - 65 * prog),
            int(245 - 200 * prog),
        )
        p = P_ATM * ((cr4 / v) ** GAMMA)
        spark = a >= 350.0
        if spark:
            p += 38.0 * ((a - 350.0) / 10.0)
        return "2. COMPRESSION", col, False, False, spark, p, v
    elif 360.0 <= a < 540.0:
        prog = (a - 360.0) / 180.0
        col = (
            int(255 - 110 * prog),
            int(65 + 75 * prog),
            int(35 + 95 * prog),
        )
        p_peak = (P_ATM * (cr4 ** GAMMA)) + 38.0
        p = p_peak * ((1.0 / v) ** GAMMA)
        return "3. POWER", col, False, False, (a <= 372.0), p, v
    else:
        p_peak = (P_ATM * (cr4 ** GAMMA)) + 38.0
        p_end = p_peak * ((1.0 / cr4) ** GAMMA)
        blowdown = math.exp(-(a - 540.0) / 15.0)
        p = P_ATM * 1.1 + (p_end - P_ATM * 1.1) * blowdown
        return "4. EXHAUST", (135, 138, 145), False, True, False, p, v


def compute_2s_state(angle_deg, cr2):
    """Return (phase_str, rgb_color, tr_open, ex_open, spark, pressure_bar, norm_vol)."""
    a = angle_deg % 360.0
    v = norm_volume(a, cr2)
    v_close = norm_volume(250.0, cr2)

    ex_open = 110.0 <= a <= 250.0
    tr_open = 130.0 <= a <= 230.0
    spark = (a <= 12.0) or (a >= 350.0)

    if 0.0 <= a < 110.0:
        prog = a / 110.0
        col = (int(255 - 50 * prog), int(75 + 60 * prog), 35)
        p_peak = (P_ATM * (cr2 ** GAMMA)) + 30.0
        p = p_peak * ((1.0 / v) ** GAMMA)
        return "POWER (EXPANSION)", col, tr_open, ex_open, spark, p, v
    elif 110.0 <= a < 130.0:
        p_peak = (P_ATM * (cr2 ** GAMMA)) + 30.0
        p_110 = p_peak * ((1.0 / norm_volume(110.0, cr2)) ** GAMMA)
        prog = (a - 110.0) / 20.0
        p = p_110 * (1.0 - 0.8 * prog) + P_ATM * 1.2 * (0.8 * prog)
        return "BLOWDOWN", (165, 125, 105), tr_open, ex_open, spark, p, v
    elif 130.0 <= a <= 230.0:
        return "SCAVENGING", (77, 166, 255), tr_open, ex_open, spark, P_ATM * 1.15, v
    elif 230.0 < a <= 250.0:
        return "EXHAUST CLOSING", (95, 150, 225), tr_open, ex_open, spark, P_ATM * 1.05, v
    else:
        prog = (a - 250.0) / 110.0
        col = (
            int(95 + 160 * prog),
            int(150 - 65 * prog),
            int(225 - 185 * prog),
        )
        p = P_ATM * ((v_close / v) ** GAMMA)
        if a >= 350.0:
            p += 30.0 * ((a - 350.0) / 10.0)
        return "COMPRESSION", col, tr_open, ex_open, spark, p, v


# ==========================================
# 2. UI SLIDER CLASS
# ==========================================
class Slider:
    def __init__(self, x, y, w, label, min_val, max_val, start_val, fmt="{:.1f}"):
        self.rect = pygame.Rect(x, y, w, 10)
        self.label = label
        self.min_val = min_val
        self.max_val = max_val
        self.val = start_val
        self.fmt = fmt
        self.dragging = False

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            knob_x = self.get_knob_x()
            knob_rect = pygame.Rect(knob_x - 10, self.rect.centery - 12, 20, 24)
            if knob_rect.collidepoint(event.pos) or self.rect.collidepoint(event.pos):
                self.dragging = True
                self.update_val(event.pos[0])
                return True
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            self.dragging = False
        elif event.type == pygame.MOUSEMOTION and self.dragging:
            self.update_val(event.pos[0])
            return True
        return False

    def update_val(self, mouse_x):
        rel = max(0.0, min(1.0, (mouse_x - self.rect.x) / self.rect.width))
        self.val = self.min_val + rel * (self.max_val - self.min_val)

    def get_knob_x(self):
        rel = (self.val - self.min_val) / (self.max_val - self.min_val)
        return int(self.rect.x + rel * self.rect.width)

    def draw(self, surf, font):
        # Label & Value
        txt = f"{self.label}: {self.fmt.format(self.val)}"
        lbl_surf = font.render(txt, True, TEXT_WHITE)
        surf.blit(lbl_surf, (self.rect.x, self.rect.y - 24))

        # Track
        pygame.draw.rect(surf, (65, 68, 85), self.rect, border_radius=5)
        active_w = self.get_knob_x() - self.rect.x
        pygame.draw.rect(surf, ACCENT_BLUE, (self.rect.x, self.rect.y, active_w, self.rect.height), border_radius=5)

        # Handle
        pygame.draw.circle(surf, TEXT_WHITE, (self.get_knob_x(), self.rect.centery), 9)
        pygame.draw.circle(surf, ACCENT_BLUE, (self.get_knob_x(), self.rect.centery), 6)


# ==========================================
# 3. ENGINE & P-V DIAGRAM RENDERING
# ==========================================
def draw_engine(surf, cx, cy, angle_deg, cr, is_two_stroke, fonts):
    font_title, font_body, font_small = fonts
    half_bore = BORE_PX / 2.0

    # Clearance height scales inversely with Compression Ratio (CR)
    clearance_px = (2.0 * R_PX) / (cr - 1.0)
    y_tdc_screen = cy - (L_PX + R_PX)
    y_bdc_screen = cy - (L_PX - R_PX)
    y_head_screen = y_tdc_screen - clearance_px

    # Evaluate thermodynamic state
    if is_two_stroke:
        phase, gas_col, port_in, port_ex, spark, p, v = compute_2s_state(angle_deg, cr)
        title = "2-Stroke Engine (360° Cycle)"
        disp_angle = int(angle_deg % 360)
        max_angle = 360
    else:
        phase, gas_col, port_in, port_ex, spark, p, v = compute_4s_state(angle_deg, cr)
        title = "4-Stroke Engine (720° Cycle)"
        disp_angle = int(angle_deg % 720)
        max_angle = 720

    # Title & Metrics
    t_surf = font_title.render(title, True, TEXT_WHITE)
    surf.blit(t_surf, (cx - t_surf.get_width() // 2, 22))

    # Crankcase circle
    pygame.draw.circle(surf, (30, 30, 38), (cx, cy), int(R_PX + 22))
    pygame.draw.circle(surf, (105, 110, 125), (cx, cy), int(R_PX + 22), 3)

    # Piston & Crank Kinematics
    rad = math.radians(angle_deg)
    pin_x = cx + int(R_PX * math.sin(rad))
    pin_y = cy - int(R_PX * math.cos(rad))
    piston_top_y = cy - piston_offset_y(angle_deg)

    # Combustion gas fill
    gas_h = max(2, int(piston_top_y - y_head_screen))
    gas_rect = pygame.Rect(int(cx - half_bore), int(y_head_screen), int(BORE_PX), gas_h)
    pygame.draw.rect(surf, gas_col, gas_rect)

    # 2-Stroke Wall Ports OR 4-Stroke Overhead Valves
    if is_two_stroke:
        y_ex_port = cy - piston_offset_y(110.0)
        y_tr_port = cy - piston_offset_y(130.0)
        tr_col = ACCENT_BLUE if port_in else (55, 75, 100)
        ex_col = ACCENT_RED if port_ex else (100, 55, 60)

        pygame.draw.rect(surf, tr_col, (int(cx - half_bore - 22), int(y_tr_port), 22, 18), border_radius=3)
        pygame.draw.rect(surf, ex_col, (int(cx + half_bore), int(y_ex_port), 22, 24), border_radius=3)

        surf.blit(font_small.render("Transfer", True, ACCENT_BLUE), (int(cx - half_bore - 78), int(y_tr_port)))
        surf.blit(font_small.render("Exhaust", True, ACCENT_RED), (int(cx + half_bore + 26), int(y_ex_port + 2)))
    else:
        in_lift = 9 if port_in else 0
        ex_lift = 9 if port_ex else 0
        in_col = ACCENT_BLUE if port_in else (110, 130, 155)
        ex_col = ACCENT_RED if port_ex else (155, 110, 115)

        pygame.draw.line(surf, in_col, (int(cx - 42), int(y_head_screen + in_lift)),
                         (int(cx - 14), int(y_head_screen + in_lift)), 6)
        pygame.draw.line(surf, ex_col, (int(cx + 14), int(y_head_screen + ex_lift)),
                         (int(cx + 42), int(y_head_screen + ex_lift)), 6)

    # Cylinder walls & head roof
    wall_pts = [
        (cx - half_bore, y_bdc_screen + PISTON_H),
        (cx - half_bore, y_head_screen),
        (cx + half_bore, y_head_screen),
        (cx + half_bore, y_bdc_screen + PISTON_H),
    ]
    pygame.draw.lines(surf, CYLINDER_WALL, False, wall_pts, 4)

    # Piston Body
    piston_rect = pygame.Rect(int(cx - half_bore + 3), int(piston_top_y), int(BORE_PX - 6), int(PISTON_H))
    pygame.draw.rect(surf, PISTON_SILVER, piston_rect, border_radius=4)
    pygame.draw.rect(surf, (70, 75, 85), piston_rect, 2, border_radius=4)

    # Connecting Rod & Crank Arm
    wrist_y = int(piston_top_y + PISTON_H * 0.45)
    pygame.draw.line(surf, (225, 228, 235), (pin_x, pin_y), (cx, wrist_y), 7)
    pygame.draw.line(surf, CRANK_GOLD, (cx, cy), (pin_x, pin_y), 10)
    pygame.draw.circle(surf, (90, 90, 100), (cx, cy), 8)
    pygame.draw.circle(surf, TEXT_WHITE, (pin_x, pin_y), 6)
    pygame.draw.circle(surf, (70, 75, 85), (cx, wrist_y), 5)

    # Spark plug & Ignition flash
    pygame.draw.rect(surf, TEXT_WHITE, (cx - 4, int(y_head_screen - 14), 8, 14))
    if spark:
        pygame.draw.circle(surf, (255, 255, 80), (cx, int(y_head_screen + 6)), 11)
        pygame.draw.circle(surf, (255, 120, 0), (cx, int(y_head_screen + 6)), 11, 3)

    # Status Readouts below Crankcase
    p_lbl = font_title.render(phase, True, gas_col if sum(gas_col) > 260 else TEXT_WHITE)
    surf.blit(p_lbl, (cx - p_lbl.get_width() // 2, cy + 92))

    eff = (1.0 - (cr ** (1.0 - GAMMA))) * 100.0
    stat_str = f"Angle: {disp_angle:03d}°/{max_angle}°  |  P: {p:5.1f} bar  |  Ideal Eff: {eff:.1f}%"
    s_lbl = font_small.render(stat_str, True, TEXT_MUTED)
    surf.blit(s_lbl, (cx - s_lbl.get_width() // 2, cy + 122))

    return p, v


def draw_pv_diagram(surf, rect, cr4, cr2, cur_4s, cur_2s, fonts):
    font_title, font_body, font_small = fonts
    pygame.draw.rect(surf, PANEL_BG, rect, border_radius=10)
    pygame.draw.rect(surf, (70, 72, 90), rect, 2, border_radius=10)

    t_surf = font_title.render("Live P-V Indicator Diagram", True, TEXT_WHITE)
    surf.blit(t_surf, (rect.centerx - t_surf.get_width() // 2, rect.y + 14))

    plot_rect = pygame.Rect(rect.x + 58, rect.y + 55, rect.width - 80, rect.height - 105)
    pygame.draw.rect(surf, BG_DARK, plot_rect)
    pygame.draw.rect(surf, (90, 95, 115), plot_rect, 1)

    max_v = max(cr4, cr2, 12.0)
    max_p = 115.0  # Fixed bar ceiling so compressing ratio growth is visually obvious

    def to_screen(v, p):
        sx = plot_rect.x + ((v - 1.0) / (max_v - 1.0)) * plot_rect.width
        sy = plot_rect.bottom - (min(p, max_p) / max_p) * plot_rect.height
        return int(sx), int(sy)

    # Grid lines
    for p_tick in [25, 50, 75, 100]:
        _, gy = to_screen(1.0, p_tick)
        pygame.draw.line(surf, (45, 48, 62), (plot_rect.x, gy), (plot_rect.right, gy), 1)
        lbl = font_small.render(f"{p_tick}", True, TEXT_MUTED)
        surf.blit(lbl, (plot_rect.x - 32, gy - 8))

    # Trace 4-Stroke Curve
    pts_4 = [to_screen(compute_4s_state(a, cr4)[6], compute_4s_state(a, cr4)[5]) for a in range(0, 720, 4)]
    pygame.draw.lines(surf, ACCENT_BLUE, True, pts_4, 2)

    # Trace 2-Stroke Curve
    pts_2 = [to_screen(compute_2s_state(a, cr2)[6], compute_2s_state(a, cr2)[5]) for a in range(0, 360, 3)]
    pygame.draw.lines(surf, ACCENT_ORANGE, True, pts_2, 2)

    # Active Operating Dots
    p4, v4 = cur_4s
    p2, v2 = cur_2s
    pygame.draw.circle(surf, ACCENT_BLUE, to_screen(v4, p4), 7)
    pygame.draw.circle(surf, TEXT_WHITE, to_screen(v4, p4), 7, 2)

    pygame.draw.circle(surf, ACCENT_ORANGE, to_screen(v2, p2), 7)
    pygame.draw.circle(surf, TEXT_WHITE, to_screen(v2, p2), 7, 2)

    # Axis captions
    surf.blit(font_small.render("Normalized Volume (V / V_c)", True, TEXT_MUTED),
              (plot_rect.centerx - 75, plot_rect.bottom + 12))
    surf.blit(font_small.render("4-Stroke (Blue) vs 2-Stroke (Orange)", True, TEXT_WHITE),
              (plot_rect.x + 12, plot_rect.y + 10))


# ==========================================
# 4. MAIN APPLICATION LOOP
# ==========================================
def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Interactive 4-Stroke vs 2-Stroke Engine Simulator")
    clock = pygame.time.Clock()

    font_title = pygame.font.SysFont("Segoe UI, Arial", 19, bold=True)
    font_body = pygame.font.SysFont("Segoe UI, Arial", 15, bold=True)
    font_small = pygame.font.SysFont("Segoe UI, Arial", 13)
    fonts = (font_title, font_body, font_small)

    # Interactive Controls (Sliders)
    # Note: Visual RPM is scaled by 1/60th so individual strokes are easy to observe
    s_rpm = Slider(60, 650, 310, "Visual Speed (Engine RPM)", 10, 240, 60, fmt="{:.0f} RPM")
    s_cr4 = Slider(460, 650, 310, "4-Stroke Compression Ratio", 6.0, 14.0, 9.5, fmt="{:.1f} : 1")
    s_cr2 = Slider(860, 650, 310, "2-Stroke Compression Ratio", 5.5, 12.0, 7.5, fmt="{:.1f} : 1")
    sliders = [s_rpm, s_cr4, s_cr2]

    crank_angle = 0.0
    paused = False

    while True:
        dt = clock.tick(FPS) / 1000.0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                paused = not paused
            for s in sliders:
                s.handle_event(event)

        if not paused:
            # Advance crank angle: 1 RPM = 6 deg/sec
            crank_angle = (crank_angle + s_rpm.val * 6.0 * dt) % 720.0

        screen.fill(BG_DARK)

        # Draw Left (4-Stroke) and Center (2-Stroke) Engines
        cur_4s = draw_engine(screen, 210, 415, crank_angle, s_cr4.val, False, fonts)
        cur_2s = draw_engine(screen, 580, 415, crank_angle, s_cr2.val, True, fonts)

        # Draw Right P-V Diagram
        draw_pv_diagram(screen, pygame.Rect(790, 20, 460, 545), s_cr4.val, s_cr2.val, cur_4s, cur_2s, fonts)

        # Draw Control Bar Panel
        pygame.draw.rect(screen, PANEL_BG, (25, 595, WIDTH - 50, 105), border_radius=12)
        for s in sliders:
            s.draw(screen, font_body)

        hint = font_small.render("Press [SPACE] to Pause/Resume  |  Drag sliders to adjust RPM and Compression Ratio", True, TEXT_MUTED)
        screen.blit(hint, (WIDTH // 2 - hint.get_width() // 2, 602))

        pygame.display.flip()


if __name__ == "__main__":
    main()