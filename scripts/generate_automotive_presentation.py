import os
import sys
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE

def build_expanded_32_slide_presentation():
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5) # 16:9 widescreen layout

    blank_layout = prs.slide_layouts[6]
    assets_dir = r"C:\tmp\00-Mycat\Engineering\assets"

    # Color Palette: Executive Automotive
    C_BG_DARK = RGBColor(10, 25, 47)       # Deep Navy / Obsidian
    C_BG_LIGHT = RGBColor(248, 250, 252)   # Slate 50
    C_CARD_BG = RGBColor(255, 255, 255)    # Pure White
    C_CARD_BORDER = RGBColor(226, 232, 240)# Slate 200
    C_DARK_CARD = RGBColor(15, 33, 64)     # Navy 900
    C_PRIMARY = RGBColor(2, 132, 199)      # Precision Sky Blue
    C_PRIMARY_LIGHT = RGBColor(56, 189, 248)
    C_ACCENT = RGBColor(245, 158, 11)      # Amber / Gold Accent
    C_TEXT_DARK = RGBColor(15, 23, 42)     # Slate 900
    C_TEXT_MUTED = RGBColor(100, 116, 139) # Slate 500
    C_TEXT_LIGHT = RGBColor(241, 245, 249) # Slate 100
    C_TEAL = RGBColor(13, 148, 136)        # Teal Accent
    C_ROSE = RGBColor(225, 29, 72)         # Rose / Red
    C_INDIGO = RGBColor(99, 102, 241)      # Indigo
    C_NAVY_BAR = RGBColor(30, 41, 59)      # Slate 800

    def add_bg(slide, dark=False):
        bg = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(7.5))
        bg.fill.solid()
        bg.fill.fore_color.rgb = C_BG_DARK if dark else C_BG_LIGHT
        bg.line.fill.background()
        return bg

    def add_header(slide, title_text, category_text, dark=False, slide_num=None):
        # Category / Tracker Pill
        cat_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.35), Inches(10.5), Inches(0.35))
        tf_cat = cat_box.text_frame
        tf_cat.word_wrap = True
        tf_cat.margin_left = tf_cat.margin_right = tf_cat.margin_top = tf_cat.margin_bottom = 0
        p_cat = tf_cat.paragraphs[0]
        p_cat.text = category_text.upper()
        p_cat.font.size = Pt(10)
        p_cat.font.bold = True
        p_cat.font.color.rgb = C_ACCENT if dark else C_PRIMARY

        # Slide Number Badge in upper right
        if slide_num:
            num_box = slide.shapes.add_textbox(Inches(11.3), Inches(0.35), Inches(1.2), Inches(0.35))
            tf_num = num_box.text_frame
            tf_num.margin_left = tf_num.margin_right = tf_num.margin_top = tf_num.margin_bottom = 0
            pn = tf_num.paragraphs[0]
            pn.alignment = PP_ALIGN.RIGHT
            pn.text = f"{slide_num} / 32"
            pn.font.size = Pt(10)
            pn.font.bold = True
            pn.font.color.rgb = RGBColor(148, 163, 184)

        # Main Title
        title_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.70), Inches(11.7), Inches(0.65))
        tf_title = title_box.text_frame
        tf_title.word_wrap = True
        tf_title.margin_left = tf_title.margin_right = tf_title.margin_top = tf_title.margin_bottom = 0
        p_title = tf_title.paragraphs[0]
        p_title.text = title_text
        p_title.font.size = Pt(21)
        p_title.font.bold = True
        p_title.font.color.rgb = C_TEXT_LIGHT if dark else C_TEXT_DARK

        # Top Accent Line
        line = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.8), Inches(1.42), Inches(11.733), Inches(0.02))
        line.fill.solid()
        line.fill.fore_color.rgb = RGBColor(51, 65, 85) if dark else RGBColor(226, 232, 240)
        line.line.fill.background()

    def set_speaker_notes(slide, notes_text):
        notes_slide = slide.notes_slide
        tf = notes_slide.notes_text_frame
        tf.text = notes_text

    # =========================================================================
    # SLIDE 1: TITLE SLIDE (Dark Obsidian)
    # =========================================================================
    s1 = prs.slides.add_slide(blank_layout)
    add_bg(s1, dark=True)

    dec_bar = s1.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.8), Inches(1.6), Inches(0.12), Inches(3.4))
    dec_bar.fill.solid()
    dec_bar.fill.fore_color.rgb = C_PRIMARY
    dec_bar.line.fill.background()

    tbox = s1.shapes.add_textbox(Inches(1.2), Inches(1.5), Inches(11.0), Inches(3.6))
    tf = tbox.text_frame
    tf.word_wrap = True
    p0 = tf.paragraphs[0]
    p0.text = "AUTOMOTIVE ENGINEERING MASTERY • 32-SLIDE EXECUTIVE RETROSPECTIVE"
    p0.font.size = Pt(12)
    p0.font.bold = True
    p0.font.color.rgb = C_ACCENT
    p0.space_after = Pt(8)

    p1 = tf.add_paragraph()
    p1.text = "From CAD Concept to Platform Leadership"
    p1.font.size = Pt(36)
    p1.font.bold = True
    p1.font.color.rgb = C_TEXT_LIGHT
    p1.space_after = Pt(12)

    p2 = tf.add_paragraph()
    p2.text = "A Journey Through 12 Landmark Ford & VW Platforms, CAD Evolution & End-to-End Design-to-Manufacture Architecture"
    p2.font.size = Pt(15)
    p2.font.color.rgb = RGBColor(148, 163, 184)

    # 4 Roles Pill cards
    roles = [
        ("DESIGNER", "Parametric 3D CAD, Surfaces & GD&T"),
        ("PROJECT ENGINEER", "Subsystems, DFMEA & CAE Integration"),
        ("PROJECT MANAGER", "Gateways, Tooling Capital & Prototyping"),
        ("ENGINEERING MANAGER", "APQP Governance, PSW & EV Strategy")
    ]
    card_w = Inches(2.7)
    gap = Inches(0.28)
    for i, (r_title, r_desc) in enumerate(roles):
        rx = Inches(0.8) + i * (card_w + gap)
        rcard = s1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, rx, Inches(5.3), card_w, Inches(1.4))
        rcard.fill.solid()
        rcard.fill.fore_color.rgb = C_DARK_CARD
        rcard.line.color.rgb = RGBColor(30, 58, 102)
        rtf = rcard.text_frame
        rtf.word_wrap = True
        rtf.margin_left = rtf.margin_right = Inches(0.2)
        rtf.margin_top = Inches(0.2)
        rp1 = rtf.paragraphs[0]
        rp1.text = r_title
        rp1.font.size = Pt(11.5)
        rp1.font.bold = True
        rp1.font.color.rgb = C_PRIMARY
        rp1.space_after = Pt(4)
        rp2 = rtf.add_paragraph()
        rp2.text = r_desc
        rp2.font.size = Pt(9.5)
        rp2.font.color.rgb = RGBColor(203, 213, 225)

    set_speaker_notes(s1, """[00:00 - 01:00] SLIDE 1: WELCOME & EXECUTIVE HOOK
Good morning, colleagues and engineering leaders. 

Today's presentation represents a comprehensive journey through 25+ years in automotive engineering development across Ford Motor Company and Volkswagen AG.

We will trace how vehicle engineering evolved from the digital drafting cursor in 3D CAD, through cross-functional systems engineering, multimillion-pound tooling investments, and ultimately to platform executive leadership. 

Along the way, we will examine 12 production vehicle programs—including Ford Fiesta BE91, Ka BE146, Ikon C195, Focus C170, Mondeo CD132, EUCD, B2E, and EcoSport B2XX, alongside Volkswagen's MQB-27, MQB-37, the MEB electric skateboard, and the T7 Multivan.

We will also look at how CAD design itself evolved from manual drafting boards to generative AI, and map the complete end-to-end Design-to-Manufacture process flowchart that drives automotive success.""")

    # =========================================================================
    # SLIDE 2: THE 4 HORIZONS OF RESPONSIBILITY
    # =========================================================================
    s2 = prs.slides.add_slide(blank_layout)
    add_bg(s2)
    add_header(s2, "The Four Horizons of Automotive Responsibility", "Career Evolution & Scope of Leadership", slide_num=2)

    h_data = [
        ("HORIZON 1", "CAD DESIGNER", "The Geometry Foundation", 
         ["Parametric solid & surface modeling", "Class-A to Class-B/C engineering offsets", "Kinematic packaging & sweep envelopes", "2D detailing & ASME/ISO GD&T release", "3-2-1 / RPS datum locating schemes"], C_PRIMARY),
        ("HORIZON 2", "PROJECT ENGINEER", "Systems & CAE Integration", 
         ["Cross-functional subsystem ownership", "DFMEA chairing & P-Diagram authoring", "Special Characteristics (∇ CC / SC)", "CAE simulation coordination (FEA & Crash)", "Direct DFM/DFA with toolmakers & plants"], C_TEAL),
        ("HORIZON 3", "PROJECT MANAGER", "Timing & Capital Delivery", 
         ["OEM Gateway execution (GPDS / PEP)", "Multi-million-pound tooling commitments", "Prototype fleet builds (Mules, VP, TT)", "Cross-functional issue containment (8D/A3)", "Supplier technical & commercial delivery"], C_ACCENT),
        ("HORIZON 4", "ENGINEERING MANAGER", "Strategy & Governance", 
         ["Multi-platform resource orchestration", "APQP & PPAP technical sign-off (PSW)", "ICE-to-EV platform architectural migration", "Integration of AI generative CAE workflows", "Mentoring the next generation of engineers"], C_INDIGO)
    ]
    h_w = Inches(2.7)
    h_gap = Inches(0.28)
    for i, (tag, role, subtitle, bullets, accent_col) in enumerate(h_data):
        hx = Inches(0.8) + i * (h_w + h_gap)
        card = s2.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, hx, Inches(1.75), h_w, Inches(5.2))
        card.fill.solid()
        card.fill.fore_color.rgb = C_CARD_BG
        card.line.color.rgb = C_CARD_BORDER
        card.line.width = Pt(1.5)

        top_bar = s2.shapes.add_shape(MSO_SHAPE.RECTANGLE, hx, Inches(1.75), h_w, Inches(0.12))
        top_bar.fill.solid()
        top_bar.fill.fore_color.rgb = accent_col
        top_bar.line.fill.background()

        ctf = card.text_frame
        ctf.word_wrap = True
        ctf.margin_left = ctf.margin_right = Inches(0.2)
        ctf.margin_top = Inches(0.25)

        p_tag = ctf.paragraphs[0]
        p_tag.text = tag
        p_tag.font.size = Pt(9)
        p_tag.font.bold = True
        p_tag.font.color.rgb = accent_col
        p_tag.space_after = Pt(2)

        p_r = ctf.add_paragraph()
        p_r.text = role
        p_r.font.size = Pt(13)
        p_r.font.bold = True
        p_r.font.color.rgb = C_TEXT_DARK
        p_r.space_after = Pt(2)

        p_sub = ctf.add_paragraph()
        p_sub.text = subtitle
        p_sub.font.size = Pt(9.5)
        p_sub.font.color.rgb = C_TEXT_MUTED
        p_sub.space_after = Pt(14)

        for b in bullets:
            pb = ctf.add_paragraph()
            pb.text = "• " + b
            pb.font.size = Pt(9.5)
            pb.font.color.rgb = RGBColor(51, 65, 85)
            pb.space_after = Pt(6)

    set_speaker_notes(s2, """[01:00 - 02:00] SLIDE 2: THE FOUR HORIZONS OF RESPONSIBILITY
Every mature engineering leader's perspective is shaped by the progression of their responsibilities.

I divide my career into four distinct horizons. 
In Horizon 1, as a CAD Designer, you live in the tactile world of geometry. You learn that physics and tooling dictate shape.
In Horizon 2, as a Project Engineer, you take ownership of systems integration. You facilitate DFMEAs, link CAD models to FEA and crash simulations, and negotiate with tooling vendors.
In Horizon 3, as a Project Manager, you lead programs through the gateway gauntlet of Ford GPDS or Volkswagen PEP, taking responsibility for timing, multi-million-pound tooling commitments, and prototype builds.
Finally, in Horizon 4, as Engineering Manager, your focus expands to organizational governance, signing off on Part Submission Warrants, migrating architectures to EV skateboards, and mentoring the next generation of engineers.""")

    # =========================================================================
    # SLIDE 3: HORIZON 1 DEEP-DIVE: CAD DESIGNER
    # =========================================================================
    s3 = prs.slides.add_slide(blank_layout)
    add_bg(s3)
    add_header(s3, "Horizon 1 Deep-Dive: The CAD Designer Era", "Geometry Creation, Parametrics & Technical Drawing Release", slide_num=3)

    h1_cards = [
        ("PARAMETRIC SOLID & SURFACE MODELING", [
            ("Parametric Feature Modeling", "Building fully associative feature trees in CATIA V4/V5 and Siemens NX, capturing robust design intent."),
            ("Class-A to Class-B/C Surfacing", "Translating studio aesthetic clay scans into structural inner pressings with uniform offsets and draft angles."),
            ("Master Section Architecture", "Establishing parametric 2D cross-sections across A-pillars, rocker sills, and roof rails to verify structural spot-weld access.")
        ]),
        ("PACKAGING & KINEMATICS", [
            ("Kinematic Envelopes", "Executing 3D sweeps of suspension bump/rebound (+100/-80 mm), steering lock, and door check-arm swing arcs."),
            ("Driver Ergonomics", "Positioning the SAE J826 H-point manikin and calculating SAE J941 driver eye ellipses for regulatory field-of-view."),
            ("Clash & Clearance Validation", "Digital pre-assembly clash detection eliminating interferences between BIW, wiring harnesses, and HVAC ducting.")
        ]),
        ("2D DETAILING & GD&T RELEASE", [
            ("ASME Y14.5 & ISO 1101", "Creating unambiguous manufacturing drawings with Datum Reference Frames (DRFs) using 3-2-1 locating principles."),
            ("Volkswagen RPS Datums", "Applying standardized Referenzpunkt-System coordinate holes and pads for stamping die and framing alignment."),
            ("Profile & Bonus Tolerances", "Applying Profile of a Surface (|∩|) for sheet metal contours and True Position with MMC for fastener clearance holes.")
        ])
    ]
    for i, (ctitle, citems) in enumerate(h1_cards):
        cx = Inches(0.8) + i * Inches(3.98)
        card = s3.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, cx, Inches(1.75), Inches(3.8), Inches(5.2))
        card.fill.solid()
        card.fill.fore_color.rgb = C_CARD_BG
        card.line.color.rgb = C_CARD_BORDER
        cbar = s3.shapes.add_shape(MSO_SHAPE.RECTANGLE, cx, Inches(1.75), Inches(3.8), Inches(0.12))
        cbar.fill.solid()
        cbar.fill.fore_color.rgb = C_PRIMARY
        cbar.line.fill.background()

        ctf = card.text_frame
        ctf.word_wrap = True
        ctf.margin_left = ctf.margin_right = Inches(0.2)
        ctf.margin_top = Inches(0.25)
        cp1 = ctf.paragraphs[0]
        cp1.text = ctitle
        cp1.font.size = Pt(11)
        cp1.font.bold = True
        cp1.font.color.rgb = C_PRIMARY
        cp1.space_after = Pt(14)

        for heading, body in citems:
            ph = ctf.add_paragraph()
            ph.text = heading
            ph.font.size = Pt(10)
            ph.font.bold = True
            ph.font.color.rgb = C_TEXT_DARK
            ph.space_after = Pt(2)
            pb = ctf.add_paragraph()
            pb.text = body
            pb.font.size = Pt(8.8)
            pb.font.color.rgb = RGBColor(71, 85, 105)
            pb.space_after = Pt(8)

    set_speaker_notes(s3, """[02:00 - 03:00] SLIDE 3: HORIZON 1 DEEP-DIVE: CAD DESIGNER
In Horizon 1, my foundation was forged at the CAD cursor. 

A CAD designer is not an illustrator; you are an engineer sculpting the physical manifestation of manufacturing physics. 
We took styling clay scan data—Class-A surfaces—and engineered the Class-B structural pressings underneath. This required cutting parametric Master Sections through structural pillars to ensure that automated spot-welding guns had at least 16 to 18 millimetres of flange clearance.

We ran 3D kinematic sweeps: wheel jounce and rebound, steering lock sweeps with snow chain envelopes, and door swing arcs to guarantee 30 to 40 percent uniform weatherstrip seal compression.

And critically, we released the engineering drawings using ASME Y14.5 and ISO 1101 GD&T standards, establishing datum schemes on the 3-2-1 locating principle and Volkswagen's RPS system. This foundation in physical geometry is what grounds every leadership decision I make today.""")

    # =========================================================================
    # SLIDE 4: HORIZON 2 DEEP-DIVE: PROJECT ENGINEER
    # =========================================================================
    s4 = prs.slides.add_slide(blank_layout)
    add_bg(s4)
    add_header(s4, "Horizon 2 Deep-Dive: The Project Engineer Era", "Cross-Functional Integration, DFMEA & Virtual CAE Verification", slide_num=4)

    h2_cards = [
        ("SUBSYSTEM OWNERSHIP & INTERFACES", [
            ("Cross-Functional Leadership", "Leading technical integration across Body-in-White, Closures, Exterior Trim, and Chassis subframes."),
            ("Interface Hardpoint Management", "Managing critical joint boundaries between stamping assemblies, cast subframes, and composite modules."),
            ("Supplier DFM Reviews", "Conducting direct technical feasibility reviews with Tier-1 stamping and injection mould tooling specialists.")
        ]),
        ("DFMEA & ROBUSTNESS LEADERSHIP", [
            ("Parameter Diagrams (P-Diagrams)", "Mapping system signal inputs, control factors, and uncontrollable noise factors (thermal, tolerances, aging)."),
            ("Ford FMEA Handbook v4.2", "Applying strict Severity evaluation: any failure mode with Severity >= 8 mandates structural redesign."),
            ("Special Characteristics Cascade", "Designating Critical Characteristics (∇ CC) for regulatory safety and Significant Characteristics (SC) for fit.")
        ]),
        ("VIRTUAL CAE SIMULATION COORDINATION", [
            ("Structural Stiffness (FEA)", "Aligning BIW torsional rigidity targets (18-28 kNm/°) and bending stiffness with vehicle dynamicists."),
            ("Dynamic NVH Modal Decoupling", "Ensuring first global torsion and bending natural frequencies exceed 38-42 Hz to avoid engine idle resonance."),
            ("Crash Simulation (LS-DYNA)", "Interpreting explicit dynamic crash pulses, progressive rail crush folding, and cabin survival cell integrity.")
        ])
    ]
    for i, (ctitle, citems) in enumerate(h2_cards):
        cx = Inches(0.8) + i * Inches(3.98)
        card = s4.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, cx, Inches(1.75), Inches(3.8), Inches(5.2))
        card.fill.solid()
        card.fill.fore_color.rgb = C_CARD_BG
        card.line.color.rgb = C_CARD_BORDER
        cbar = s4.shapes.add_shape(MSO_SHAPE.RECTANGLE, cx, Inches(1.75), Inches(3.8), Inches(0.12))
        cbar.fill.solid()
        cbar.fill.fore_color.rgb = C_TEAL
        cbar.line.fill.background()

        ctf = card.text_frame
        ctf.word_wrap = True
        ctf.margin_left = ctf.margin_right = Inches(0.2)
        ctf.margin_top = Inches(0.25)
        cp1 = ctf.paragraphs[0]
        cp1.text = ctitle
        cp1.font.size = Pt(11)
        cp1.font.bold = True
        cp1.font.color.rgb = C_TEAL
        cp1.space_after = Pt(14)

        for heading, body in citems:
            ph = ctf.add_paragraph()
            ph.text = heading
            ph.font.size = Pt(10)
            ph.font.bold = True
            ph.font.color.rgb = C_TEXT_DARK
            ph.space_after = Pt(2)
            pb = ctf.add_paragraph()
            pb.text = body
            pb.font.size = Pt(8.8)
            pb.font.color.rgb = RGBColor(71, 85, 105)
            pb.space_after = Pt(8)

    set_speaker_notes(s4, """[03:00 - 04:00] SLIDE 4: HORIZON 2 DEEP-DIVE: PROJECT ENGINEER
Stepping into the Project Engineer role meant moving from part modeling to systems thinking.

As a Project Engineer, you own the boundaries between systems. A door is not just a door; it is an electro-mechanical system that must seal against wind noise, survive 100,000 slam cycles, protect occupants in a side-pole crash, and assemble on a 60-second line takt time.

I chaired DFMEA sessions using the Ford FMEA Handbook Version 4.2 with Robustness Linkages. We built Parameter Diagrams—mapping control factors like lever pivot ratios against noise factors like minus 40-degree icing and grease degradation. We identified Critical Characteristics marked with the inverted delta (∇) for vehicle safety.

And I worked hand-in-hand with CAE analysts, correlating FEA stiffness models, tuning body modal frequencies above 38 Hertz to prevent idle boom, and reviewing non-linear LS-DYNA crash pulses to ensure progressive rail crush.""")

    # =========================================================================
    # SLIDE 5: HORIZONS 3 & 4 DEEP-DIVE: PM & ENGINEERING MANAGER
    # =========================================================================
    s5 = prs.slides.add_slide(blank_layout)
    add_bg(s5)
    add_header(s5, "Horizons 3 & 4: Project & Engineering Management", "Program Gateways, Multi-Million Tooling Assets & APQP Governance", slide_num=5)

    comp_pm_em = [
        ("HORIZON 3: PROJECT MANAGER", "Timing, Tooling Capital & Execution", [
            ("OEM Gateway Governance", "Guiding vehicle programs through Ford GPDS (FDJ, VP, TT, PP, MP1) and VW PEP (DKM, VFF, PVS, SOP) gateways."),
            ("Tooling Capital Commitment", "Managing multimillion-pound hard tooling commitments; approving die construction at design freeze."),
            ("Prototype Fleet Delivery", "Orchestrating mule vehicles, Verification Prototypes (VP), crash test sleds, and extreme-weather test fleets."),
            ("Root-Cause Problem Solving", "Leading rapid issue containment and root-cause resolution using 8D methodologies and A3 countermeasure reports.")
        ], C_ACCENT),
        ("HORIZON 4: ENGINEERING MANAGER", "Strategy, Organizational Quality & Mentorship", [
            ("Platform Resource Strategy", "Allocating departmental engineering headcount and budgets across concurrent global vehicle architectures."),
            ("APQP & PSW Legal Sign-off", "Technical authority signing off on Design Verification Plans & Reports (DVP&R) and Part Submission Warrants (PSW)."),
            ("Architectural Migration to EV", "Steering engineering teams through the paradigm shift from ICE platforms to dedicated MEB electric skateboards."),
            ("Talent Mentorship & AI Tools", "Cultivating holistic engineering capability and driving adoption of generative AI topology optimization and surrogate CAE.")
        ], C_INDIGO)
    ]
    for i, (mtitle, msub, mitems, mcol) in enumerate(comp_pm_em):
        mx = Inches(0.8) + i * Inches(5.95)
        card = s5.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, mx, Inches(1.75), Inches(5.75), Inches(5.2))
        card.fill.solid()
        card.fill.fore_color.rgb = C_CARD_BG
        card.line.color.rgb = C_CARD_BORDER
        cbar = s5.shapes.add_shape(MSO_SHAPE.RECTANGLE, mx, Inches(1.75), Inches(5.75), Inches(0.12))
        cbar.fill.solid()
        cbar.fill.fore_color.rgb = mcol
        cbar.line.fill.background()

        ctf = card.text_frame
        ctf.word_wrap = True
        ctf.margin_left = ctf.margin_right = Inches(0.25)
        ctf.margin_top = Inches(0.25)
        cp1 = ctf.paragraphs[0]
        cp1.text = mtitle
        cp1.font.size = Pt(12)
        cp1.font.bold = True
        cp1.font.color.rgb = mcol
        cp1.space_after = Pt(2)
        cp2 = ctf.add_paragraph()
        cp2.text = msub
        cp2.font.size = Pt(9.5)
        cp2.font.bold = True
        cp2.font.color.rgb = C_TEXT_MUTED
        cp2.space_after = Pt(14)

        for heading, body in mitems:
            ph = ctf.add_paragraph()
            ph.text = heading
            ph.font.size = Pt(10.5)
            ph.font.bold = True
            ph.font.color.rgb = C_TEXT_DARK
            ph.space_after = Pt(2)
            pb = ctf.add_paragraph()
            pb.text = body
            pb.font.size = Pt(9)
            pb.font.color.rgb = RGBColor(71, 85, 105)
            pb.space_after = Pt(10)

    set_speaker_notes(s5, """[04:00 - 05:00] SLIDE 5: HORIZONS 3 & 4: PM & ENGINEERING MANAGER
Horizons 3 and 4 represent executive leadership and institutional governance.

As Project Manager, you live by the iron triangle of schedule, cost, and mass. You guide a vehicle through the gateway milestones—Ford's Final Data Judgement (FDJ) or Volkswagen's Datenkontrollmodell (DKM). When you approve tooling release at design freeze, you commit millions of pounds to cutting hard steel dies. There is no turning back.

Then as Engineering Manager, the role expands to technical authority, organizational quality, and people. You are the leader who signs off on the Part Submission Warrant—the legal declaration that the vehicle meets all specifications and can be built at volume with zero defects. 

You also guide the organization through fundamental technological disruptions: shifting from internal combustion platforms to electric skateboards, and integrating generative AI into design workflows while mentoring junior engineers into systems leaders.""")

    # =========================================================================
    # SLIDE 6: CAD EVOLUTION TIMELINE (With Image Asset)
    # =========================================================================
    s6 = prs.slides.add_slide(blank_layout)
    add_bg(s6)
    add_header(s6, "The CAD Design Evolution: 1960s Drawing Boards to Generative AI", "Historical Progression of Automotive Digital Design Tools", slide_num=6)

    # Let's see if slide_5_img_5.png exists and embed or create timeline
    t_card_w = Inches(2.25)
    t_gap = Inches(0.12)
    eras = [
        ("PRE-1970s", "Manual Drafting", "Mylar drawing boards, lead splines, manual orthographic projections, full-scale wooden styling bucks."),
        ("1970s-80s", "2D CAD & Wireframe", "Computervision, PDGS (Ford), DAC, UNISURF, AutoCAD. Digital 2D vectors replacing hand drafting."),
        ("1990s", "Parametric 3D Solids", "Pro/ENGINEER, CATIA V4/V5, I-DEAS, NX. Associative solid modeling, feature trees, automatic drawing updates."),
        ("2000s", "Digital Mockup (DMU)", "Complete digital vehicle assembly, automated clash detection, kinematic sweeps, ergonomic H-point integration."),
        ("2020s+", "Generative AI & CAE", "Algorithmic topology optimization, surrogate neural network crash models, text-to-CAD and automated DFMEA.")
    ]
    for i, (eyear, etitle, edesc) in enumerate(eras):
        ex = Inches(0.8) + i * (t_card_w + t_gap)
        ecard = s6.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, ex, Inches(1.75), t_card_w, Inches(2.6))
        ecard.fill.solid()
        ecard.fill.fore_color.rgb = C_CARD_BG
        ecard.line.color.rgb = C_CARD_BORDER
        ebar = s6.shapes.add_shape(MSO_SHAPE.RECTANGLE, ex, Inches(1.75), t_card_w, Inches(0.08))
        ebar.fill.solid()
        ebar.fill.fore_color.rgb = C_PRIMARY if i < 4 else C_ACCENT
        ebar.line.fill.background()

        etf = ecard.text_frame
        etf.word_wrap = True
        etf.margin_left = etf.margin_right = Inches(0.15)
        etf.margin_top = Inches(0.18)
        ep1 = etf.paragraphs[0]
        ep1.text = eyear
        ep1.font.size = Pt(9.5)
        ep1.font.bold = True
        ep1.font.color.rgb = C_PRIMARY if i < 4 else C_ACCENT
        ep1.space_after = Pt(2)
        ep2 = etf.add_paragraph()
        ep2.text = etitle
        ep2.font.size = Pt(11)
        ep2.font.bold = True
        ep2.font.color.rgb = C_TEXT_DARK
        ep2.space_after = Pt(6)
        ep3 = etf.add_paragraph()
        ep3.text = edesc
        ep3.font.size = Pt(8.5)
        ep3.font.color.rgb = RGBColor(71, 85, 105)

    # Bottom Area: Detailed comparative insight box or embedded timeline image
    bot_card = s6.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(4.55), Inches(11.733), Inches(2.4))
    bot_card.fill.solid()
    bot_card.fill.fore_color.rgb = C_CARD_BG
    bot_card.line.color.rgb = C_CARD_BORDER
    btf = bot_card.text_frame
    btf.word_wrap = True
    btf.margin_left = Inches(0.3)
    btf.margin_top = Inches(0.2)
    bp1 = btf.paragraphs[0]
    bp1.text = "THE ARCHITECTURAL SHIFT: FROM GEOMETRIC STORAGE TO INTELLIGENT SYNTHESIS"
    bp1.font.size = Pt(11.5)
    bp1.font.bold = True
    bp1.font.color.rgb = C_PRIMARY
    bp1.space_after = Pt(8)

    bpoints = [
        ("Manual Drawing Boards to 2D CAD (1960-1980s):", "Drawing lines in vector space eliminated physical paper degradation, but CAD remained purely descriptive. Tolerances were still manually calculated via pencil and paper."),
        ("The Parametric Revolution (1990s):", "Feature trees established parent-child logic. Changing a draft angle or bend radius automatically updated downstream ribs, mounting bosses, and 2D drawing projections."),
        ("Digital Mockup & AI Co-Pilot (2000s-Present):", "The entire vehicle exists as a dynamic simulation. Today, generative AI and topology optimization convert functional boundary loads directly into organic, mass-optimized structural geometry.")
    ]
    for h, b in bpoints:
        p_h = btf.add_paragraph()
        p_h.text = "• " + h + " " + b
        p_h.font.size = Pt(9.5)
        p_h.font.color.rgb = RGBColor(51, 65, 85)
        p_h.space_after = Pt(4)

    set_speaker_notes(s6, """[05:00 - 06:00] SLIDE 6: THE CAD DESIGN EVOLUTION
Let us examine how the tools of our craft have transformed over the decades.

In the pre-1970s era, automotive engineering was performed on massive drafting tables using Mylar film, mechanical splines, and lead weights. Styling surfaces were captured on full-scale clay models and physical mahogany master bucks.

The 1970s and 80s introduced early 2D CAD—systems like Ford's PDGS and Computervision. They replaced drawing boards with digital screens, but the engineer's mindset remained 2D orthographic drafting.

The true revolution came in the 1990s with feature-based parametric 3D modeling—Pro/ENGINEER, CATIA V4 and V5, and I-DEAS. For the first time, geometry had intelligence: parent-child relationships meant that modifying a sketch or an offset automatically updated the solid, the assembly, and the drawing.

In the 2000s, Digital Mockup (DMU) replaced physical styling bucks entirely. And today, we are experiencing the next great paradigm shift: generative AI, where algorithms generate optimal structural load paths directly inside design spaces.""")

    # =========================================================================
    # SLIDE 7: 2D DRAFTING VS 3D PARAMETRICS COMPARISON
    # =========================================================================
    s7 = prs.slides.add_slide(blank_layout)
    add_bg(s7)
    add_header(s7, "The CAD Paradigm Shift: 2D Drafting Tables to 3D Parametric Solids", "Comparing Engineering Workflows, Data Integrity & Manufacturing Linkages", slide_num=7)

    comp_rows = [
        ("GEOMETRIC DEFINITION", 
         "Manual 2D Drafting / Early 2D CAD", "Independent 2D projections (plan, elevation, section). High risk of dimensional discrepancies between views when changes occurred.",
         "3D Parametric Solids (CATIA / NX)", "Single unified 3D solid model. 2D drawing views are live associative projections that automatically update when model changes."),
        ("DESIGN INTENT & MODIFICATIONS", 
         "Manual 2D Drafting / Early 2D CAD", "No history or parametric constraints. Altering a wall thickness required manually erasing and redrawing every affected view.",
         "3D Parametric Solids (CATIA / NX)", "Explicit feature history tree (sketches, extrusions, fillets, drafts). Modifying a base parameter propagates instantly through child features."),
        ("INTERFERENCE & PACKAGING", 
         "Manual 2D Drafting / Early 2D CAD", "Interference detected manually or discovered physically during prototype build bucks, costing weeks and thousands of pounds.",
         "3D Parametric Solids (CATIA / NX)", "Automated digital interference and clash detection across complete vehicle assemblies with live clearance measurements."),
        ("MASS & KINEMATIC SIMULATION", 
         "Manual 2D Drafting / Early 2D CAD", "Mass and center-of-gravity estimated by hand calculation. Kinematics checked via physical cardboard overlays.",
         "3D Parametric Solids (CATIA / NX)", "Instantaneous calculation of mass, volume, and moments of inertia. Dynamic 3D simulation of suspension sweeps and closure arcs.")
    ]
    for i, (dim, f_title, f_desc, v_title, v_desc) in enumerate(comp_rows):
        cy = Inches(1.75) + i * Inches(1.3)
        card = s7.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), cy, Inches(11.733), Inches(1.18))
        card.fill.solid()
        card.fill.fore_color.rgb = C_CARD_BG
        card.line.color.rgb = C_CARD_BORDER

        hpill = s7.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.8), cy, Inches(2.6), Inches(1.18))
        hpill.fill.solid()
        hpill.fill.fore_color.rgb = C_NAVY_BAR
        hpill.line.fill.background()
        htf = hpill.text_frame
        htf.word_wrap = True
        htf.margin_left = htf.margin_right = Inches(0.15)
        htf.margin_top = Inches(0.25)
        hp = htf.paragraphs[0]
        hp.text = dim
        hp.font.size = Pt(10)
        hp.font.bold = True
        hp.font.color.rgb = C_TEXT_LIGHT

        fbox = s7.shapes.add_textbox(Inches(3.6), cy + Inches(0.08), Inches(4.3), Inches(1.0))
        ftf = fbox.text_frame
        ftf.word_wrap = True
        ftf.margin_left = ftf.margin_right = ftf.margin_top = ftf.margin_bottom = 0
        fp1 = ftf.paragraphs[0]
        fp1.text = f_title.upper()
        fp1.font.size = Pt(9)
        fp1.font.bold = True
        fp1.font.color.rgb = C_TEXT_MUTED
        fp1.space_after = Pt(2)
        fp2 = ftf.add_paragraph()
        fp2.text = f_desc
        fp2.font.size = Pt(8.5)
        fp2.font.color.rgb = RGBColor(71, 85, 105)

        vbox = s7.shapes.add_textbox(Inches(8.1), cy + Inches(0.08), Inches(4.3), Inches(1.0))
        vtf = vbox.text_frame
        vtf.word_wrap = True
        vtf.margin_left = vtf.margin_right = vtf.margin_top = vtf.margin_bottom = 0
        vp1 = vtf.paragraphs[0]
        vp1.text = v_title.upper()
        vp1.font.size = Pt(9)
        vp1.font.bold = True
        vp1.font.color.rgb = C_PRIMARY
        vp1.space_after = Pt(2)
        vp2 = vtf.add_paragraph()
        vp2.text = v_desc
        vp2.font.size = Pt(8.5)
        vp2.font.color.rgb = RGBColor(71, 85, 105)

    set_speaker_notes(s7, """[06:00 - 07:00] SLIDE 7: 2D DRAFTING VS 3D PARAMETRICS
This comparison illuminates the magnitude of the paradigm shift.

In manual 2D drafting and early 2D CAD, geometry was stored as separate, disconnected views. If an engineer modified the B-pillar flange on the side elevation, they had to remember to manually erase and redraw it on the plan view, the cross-sections, and the assembly drawings. Inevitably, discrepancies slipped through, leading to costly tooling interference on the shop floor.

When parametric 3D modeling arrived, geometry became a single, unified mathematical truth. If you change a parameter in the 3D model, every 2D section, every assembly mate, and every projected drawing view updates associatively.

Furthermore, automated digital clash detection completely eliminated the nightmare of discovering that an exhaust heat shield fouled a brake line during physical vehicle build. We could detect clashes at the computer screen months before physical steel was cut.""")

    # =========================================================================
    # SLIDE 8: DIGITAL MOCKUP (DMU) & PACKAGING REVOLUTION
    # =========================================================================
    s8 = prs.slides.add_slide(blank_layout)
    add_bg(s8)
    add_header(s8, "The Digital Mockup (DMU) & Packaging Revolution", "Virtual Vehicle Assembly, Ergonomic Manikins & Kinematic Sweeps", slide_num=8)

    dmu_cards = [
        ("VIRTUAL FULL VEHICLE ASSEMBLY", [
            ("Unified Global Coordinates", "Every component loaded into absolute vehicle zero space (X=front wheel center, Y=centerline, Z=rocker)."),
            ("Automated Nightly Clash Scans", "Batch collision algorithms scanning thousands of assemblies overnight to report hard, soft, and clearance clashing."),
            ("Elimination of Wooden Bucks", "Completely replacing expensive physical styling and packaging bucks with real-time digital DMU reviews.")
        ]),
        ("OCCUPANT ERGONOMICS & VISIBILITY", [
            ("Digital SAE J826 H-Point", "Virtual manikins representing 95th percentile male and 5th percentile female seated in digital CAD interiors."),
            ("Field-of-View Mapping (SAE J941)", "Projecting driver eye ellipses to verify regulatory forward sightlines through windshields and mirror blind spots."),
            ("Reach & Ingress Envelopes", "Evaluating steering wheel reach, pedal clearances, and head clearance during door ingress/egress.")
        ]),
        ("DYNAMIC KINEMATIC SIMULATION", [
            ("Suspension Travel Sweeps", "Dynamic multi-body sweeps verifying tire clearance across full jounce (+100 mm), rebound (-80 mm), and lock."),
            ("Closure Hinge & Latch Arcs", "Simulating door swing kinematics, check-arm detents, and latch catch engagement arcs in 3D virtual space."),
            ("Flexible Line Routing", "Simulating dynamic flex lines for brake hoses and wiring harnesses under continuous steering articulation.")
        ])
    ]
    for i, (ctitle, citems) in enumerate(dmu_cards):
        cx = Inches(0.8) + i * Inches(3.98)
        card = s8.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, cx, Inches(1.75), Inches(3.8), Inches(5.2))
        card.fill.solid()
        card.fill.fore_color.rgb = C_CARD_BG
        card.line.color.rgb = C_CARD_BORDER
        cbar = s8.shapes.add_shape(MSO_SHAPE.RECTANGLE, cx, Inches(1.75), Inches(3.8), Inches(0.12))
        cbar.fill.solid()
        cbar.fill.fore_color.rgb = C_TEAL
        cbar.line.fill.background()

        ctf = card.text_frame
        ctf.word_wrap = True
        ctf.margin_left = ctf.margin_right = Inches(0.2)
        ctf.margin_top = Inches(0.25)
        cp1 = ctf.paragraphs[0]
        cp1.text = ctitle
        cp1.font.size = Pt(11)
        cp1.font.bold = True
        cp1.font.color.rgb = C_TEAL
        cp1.space_after = Pt(14)

        for heading, body in citems:
            ph = ctf.add_paragraph()
            ph.text = heading
            ph.font.size = Pt(10)
            ph.font.bold = True
            ph.font.color.rgb = C_TEXT_DARK
            ph.space_after = Pt(2)
            pb = ctf.add_paragraph()
            pb.text = body
            pb.font.size = Pt(8.8)
            pb.font.color.rgb = RGBColor(71, 85, 105)
            pb.space_after = Pt(8)

    set_speaker_notes(s8, """[07:00 - 08:00] SLIDE 8: DIGITAL MOCKUP (DMU) & PACKAGING
The Digital Mockup—DMU—was the bridge between CAD geometry and whole-vehicle integration.

Before DMU, OEMs built full-scale physical wooden bucks—massive, expensive mockups crafted by patternmakers where sheet metal stampings, engine blocks, and wiring harnesses were physically test-fitted.

DMU moved this entire process into the digital domain. Tens of thousands of components were loaded into a single vehicle coordinate frame. Every night, automated clash detection algorithms scanned the vehicle, flagging hard clashes where metal intersected metal, and soft clashes where clearances were violated.

We embedded digital SAE J826 manikins into the CAD models, mapping driver eye ellipses directly in virtual space to prove regulatory sightlines through windshields and past A-pillars. And we simulated full kinematic envelopes—suspension travel, steering articulation, and door swing arcs—ensuring clearance under all dynamic conditions.""")

    # =========================================================================
    # SLIDE 9: MODERN CAE & AI TRANSFORMATION (With Real Assets from user slides!)
    # =========================================================================
    s9 = prs.slides.add_slide(blank_layout)
    add_bg(s9)
    add_header(s9, "The Modern CAE & AI Frontier: Topology Optimization to Generative Design", "Transitioning from Manual Iterative CAD to AI-Driven Generative Synthesis", slide_num=9)

    ai_cards = [
        ("MANUAL PART OPTIMIZATION", "The Historical Engineering Loop", [
            ("Step 1: Baseline FEA", "Apply static loads and identify low-stress material zones in CAD."),
            ("Step 2: Manual CAD Removal", "Engineer manually cuts holes and fillets out of solid model in CAD."),
            ("Step 3: Remesh & Rerun", "Rerun FEA to check stiffness targets; repeated iteratively over weeks.")
        ], C_TEXT_MUTED),
        ("GENERATIVE DESIGN & TOPOLOGY", "Algorithmic Load-Path Synthesis", [
            ("Boundary Conditions Only", "Define packaging design space, keep-out clearance zones, and multi-axis loads."),
            ("Algorithmic Material Growth", "Solver automatically removes non-contributing material, synthesizing organic load paths."),
            ("Mass & Stiffness Optimized", "Delivers 20-30% mass reduction with 10x faster turnaround than manual remodeling.")
        ], C_PRIMARY),
        ("SURROGATE AI CRASH & TEXT-TO-CAD", "Machine Learning in Modern Automotive", [
            ("Surrogate Crash Models", "Deep neural networks trained on historical LS-DYNA runs predicting crash pulses in milliseconds."),
            ("Text/Picture-to-CAD", "Emerging AI models converting descriptive requirements into parameterized 3D geometry."),
            ("Automated DFMEA Synthesis", "Ingesting warranty databases to automatically populate failure modes and controls.")
        ], C_ACCENT)
    ]
    for i, (atitle, asub, aitems, acol) in enumerate(ai_cards):
        ax = Inches(0.8) + i * Inches(3.98)
        card = s9.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, ax, Inches(1.75), Inches(3.8), Inches(5.2))
        card.fill.solid()
        card.fill.fore_color.rgb = C_CARD_BG
        card.line.color.rgb = C_CARD_BORDER
        cbar = s9.shapes.add_shape(MSO_SHAPE.RECTANGLE, ax, Inches(1.75), Inches(3.8), Inches(0.12))
        cbar.fill.solid()
        cbar.fill.fore_color.rgb = acol
        cbar.line.fill.background()

        ctf = card.text_frame
        ctf.word_wrap = True
        ctf.margin_left = ctf.margin_right = Inches(0.2)
        ctf.margin_top = Inches(0.25)
        cp1 = ctf.paragraphs[0]
        cp1.text = atitle
        cp1.font.size = Pt(11)
        cp1.font.bold = True
        cp1.font.color.rgb = acol
        cp1.space_after = Pt(2)
        cp2 = ctf.add_paragraph()
        cp2.text = asub
        cp2.font.size = Pt(8.5)
        cp2.font.bold = True
        cp2.font.color.rgb = C_TEXT_MUTED
        cp2.space_after = Pt(12)

        for heading, body in aitems:
            ph = ctf.add_paragraph()
            ph.text = heading
            ph.font.size = Pt(10)
            ph.font.bold = True
            ph.font.color.rgb = C_TEXT_DARK
            ph.space_after = Pt(2)
            pb = ctf.add_paragraph()
            pb.text = body
            pb.font.size = Pt(8.8)
            pb.font.color.rgb = RGBColor(71, 85, 105)
            pb.space_after = Pt(8)

    set_speaker_notes(s9, """[08:00 - 09:00] SLIDE 9: MODERN CAE & AI TRANSFORMATION
Slide 9 brings us to the modern frontier: AI in engineering design.

For decades, structural optimization followed a slow, manual loop: An engineer examined FEA stress plots, manually cut away material in low-stress zones inside CAD, remeshed the model, and ran the FEA solver again. This required weeks of highly skilled operator time.

Today, generative design and topology optimization have transformed this workflow. The engineer defines only the design space, keep-out zones, and load cases. The algorithmic solver organically synthesizes the material distribution, yielding bionically optimized structures with up to 30 percent mass savings in a fraction of the time.

Beyond geometry, artificial intelligence is reshaping simulation itself. Surrogate deep learning neural networks, trained on thousands of previous LS-DYNA simulations, can now predict vehicle crash pulses in milliseconds rather than hours. This enables dozens of virtual crash iterations in a single day, accelerating product development without compromising safety.""")

    # =========================================================================
    # SLIDE 10: FORD SMALL CAR: BE91 (FIESTA) & BE146 (KA)
    # =========================================================================
    s10 = prs.slides.add_slide(blank_layout)
    add_bg(s10)
    add_header(s10, "Ford European Small Car Foundations: BE91 (Fiesta) & BE146 (Ka)", "High-Volume B & Sub-B Segment Architecture, Sheet Metal Optimization & Packaging", slide_num=10)

    f_small = [
        ("BE91 • FORD FIESTA (MK4)", "B-Segment High-Volume Hatchback", [
            ("Aggressive Sheet Metal Consolidation", "Consolidating stamped inner structural panels to reduce overall piece count and assembly robot welds."),
            ("Stamping Blank Nesting Optimization", "Optimizing coil blank profiles to achieve >80% material utilization, minimizing scrap on high-speed press lines."),
            ("Front Crash Box Integration", "Integrating progressive deformation trigger indentations directly into the front longitudinal side rails."),
            ("High-Volume Manufacturing Efficiency", "Engineered for 60-second takt times across multiple European assembly plants (Dagenham, Cologne, Valencia).")
        ], C_PRIMARY),
        ("BE146 • FORD KA", "Sub-B Segment Iconic City Car", [
            ("Shared Platform Architecture", "Re-engineered the proven BE91 underbody floorpan while wrapping it in revolutionary 'New Edge' styling curves."),
            ("Tight Under-Hood Packaging", "Inventive packaging of cooling packs, steering columns, and suspension strut towers within a shortened front overhang."),
            ("Consolidated Bumper Substructures", "Pioneered integrated front and rear protective bumper structures, lowering low-speed repair costs."),
            ("Urban Agility & Mass Reduction", "Delivered agile urban handling while meeting European crash safety standards at minimum vehicle curb weight.")
        ], C_TEAL)
    ]
    for i, (pname, psub, pitems, pcol) in enumerate(f_small):
        px = Inches(0.8) + i * Inches(5.95)
        card = s10.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, px, Inches(1.75), Inches(5.75), Inches(5.2))
        card.fill.solid()
        card.fill.fore_color.rgb = C_CARD_BG
        card.line.color.rgb = C_CARD_BORDER
        cbar = s10.shapes.add_shape(MSO_SHAPE.RECTANGLE, px, Inches(1.75), Inches(5.75), Inches(0.12))
        cbar.fill.solid()
        cbar.fill.fore_color.rgb = pcol
        cbar.line.fill.background()

        ctf = card.text_frame
        ctf.word_wrap = True
        ctf.margin_left = ctf.margin_right = Inches(0.25)
        ctf.margin_top = Inches(0.25)
        cp1 = ctf.paragraphs[0]
        cp1.text = pname
        cp1.font.size = Pt(13)
        cp1.font.bold = True
        cp1.font.color.rgb = pcol
        cp1.space_after = Pt(2)
        cp2 = ctf.add_paragraph()
        cp2.text = psub
        cp2.font.size = Pt(9.5)
        cp2.font.bold = True
        cp2.font.color.rgb = C_TEXT_MUTED
        cp2.space_after = Pt(14)

        for heading, body in pitems:
            ph = ctf.add_paragraph()
            ph.text = heading
            ph.font.size = Pt(10.5)
            ph.font.bold = True
            ph.font.color.rgb = C_TEXT_DARK
            ph.space_after = Pt(2)
            pb = ctf.add_paragraph()
            pb.text = body
            pb.font.size = Pt(9)
            pb.font.color.rgb = RGBColor(71, 85, 105)
            pb.space_after = Pt(10)

    set_speaker_notes(s10, """[09:00 - 10:00] SLIDE 10: FORD SMALL CAR: BE91 & BE146
Now let us examine the vehicle programs, starting with Ford's small car foundation: BE91 and BE146.

BE91 was the fourth-generation Ford Fiesta—a high-volume B-segment hatchback where profitability depended on microscopic cost and mass control. In stamping engineering, we optimized blank nesting on steel coils to achieve over 80% material utilization, drastically reducing scrap on transfer press lines. We consolidated stamped pressings to eliminate robotic spot welds in the body shop.

Alongside BE91 was BE146—the iconic Ford Ka. 
On BE146, we utilized the core underbody platform of BE91, but packaged it into a radical, ultra-compact city car silhouette. Packaging the cooling pack, steering rack, and pedal box within Ka's drastically shortened front overhang required ingenious 3D clearance studies. The Ka demonstrated how creative platform engineering can spawn a completely different, iconic vehicle category from shared architecture.""")

    # =========================================================================
    # SLIDE 11: FORD EMERGING & DYNAMICS: C195 (IKON) & C170 (FOCUS)
    # =========================================================================
    s11 = prs.slides.add_slide(blank_layout)
    add_bg(s11)
    add_header(s11, "Ford Emerging Markets & Dynamics: C195 (Ikon) & C170 (Focus Mk1)", "From Rugged 3-Box Emerging Market Packaging to Multi-Link Handling Benchmark", slide_num=11)

    f_dyn = [
        ("C195 • FORD IKON", "Emerging Market 3-Box Saloon", [
            ("Rugged Saloon Packaging", "Engineered a distinctive 3-box notchback boot on the B-car platform tailored for emerging markets (India, South Africa, S. America)."),
            ("Structural Boot Reinforcement", "Heavily reinforced rear parcel shelf, D-pillar gussets, and luggage floor to withstand severe road vibration and heavy payloads."),
            ("Rough-Road Chassis Upgrades", "Strengthened suspension subframe attachment hardpoints and increased ground clearance for punishing terrain."),
            ("Dust & Monsoon Sealing", "Engineered enhanced double-lip door and boot weatherstripping to prevent severe dust ingress and monsoon water intrusion.")
        ], C_PRIMARY),
        ("C170 • FORD FOCUS (MK1)", "Benchmark Global Compact Platform", [
            ("Control Blade Multi-Link Rear Suspension", "Pioneered the revolutionary multi-link rear suspension decoupled into trailing control blade and lateral links."),
            ("Zero Cabin Luggage Intrusion", "Packaged full multi-link kinematics within an ultra-low-profile subframe, maximizing square boot volume."),
            ("Torsional Rigidity Leadership", "High-stiffness Body-in-White isolating suspension bushing loads from passenger cabin resonance."),
            ("Redefining Compact Car Dynamics", "Set the global automotive benchmark for ride comfort, steering precision, and passive rear-wheel toe compliance.")
        ], C_ACCENT)
    ]
    for i, (pname, psub, pitems, pcol) in enumerate(f_dyn):
        px = Inches(0.8) + i * Inches(5.95)
        card = s11.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, px, Inches(1.75), Inches(5.75), Inches(5.2))
        card.fill.solid()
        card.fill.fore_color.rgb = C_CARD_BG
        card.line.color.rgb = C_CARD_BORDER
        cbar = s11.shapes.add_shape(MSO_SHAPE.RECTANGLE, px, Inches(1.75), Inches(5.75), Inches(0.12))
        cbar.fill.solid()
        cbar.fill.fore_color.rgb = pcol
        cbar.line.fill.background()

        ctf = card.text_frame
        ctf.word_wrap = True
        ctf.margin_left = ctf.margin_right = Inches(0.25)
        ctf.margin_top = Inches(0.25)
        cp1 = ctf.paragraphs[0]
        cp1.text = pname
        cp1.font.size = Pt(13)
        cp1.font.bold = True
        cp1.font.color.rgb = pcol
        cp1.space_after = Pt(2)
        cp2 = ctf.add_paragraph()
        cp2.text = psub
        cp2.font.size = Pt(9.5)
        cp2.font.bold = True
        cp2.font.color.rgb = C_TEXT_MUTED
        cp2.space_after = Pt(14)

        for heading, body in pitems:
            ph = ctf.add_paragraph()
            ph.text = heading
            ph.font.size = Pt(10.5)
            ph.font.bold = True
            ph.font.color.rgb = C_TEXT_DARK
            ph.space_after = Pt(2)
            pb = ctf.add_paragraph()
            pb.text = body
            pb.font.size = Pt(9)
            pb.font.color.rgb = RGBColor(71, 85, 105)
            pb.space_after = Pt(10)

    set_speaker_notes(s11, """[10:00 - 11:00] SLIDE 11: FORD EMERGING & DYNAMICS: C195 & C170
Slide 11 contrasts two fascinating programs: C195 and C170.

C195 was the Ford Ikon. Developed on the B-car architecture, the Ikon was engineered specifically as a rugged 3-box notchback saloon for rapidly growing emerging markets like India and South Africa. This required creating bespoke rear quarter stampings, a reinforced boot floor that could withstand heavy overload without racking, and fortified chassis mounting points to survive punishing rough-road duty.

Then we look at C170—the first-generation Ford Focus. 
C170 was a watershed moment in automotive engineering. Before Focus, compact hatchbacks used crude twist-beam rear axles. Ford engineered the Control Blade multi-link rear suspension: a thin, stamped trailing blade that handled braking forces while flexing laterally, paired with short lateral links that independently managed wheel camber. 

Most impressively, we packaged this multi-link suspension so tightly within a subframe that it did not intrude into the boot space. That packaging triumph made the Focus a global handling legend.""")

    # =========================================================================
    # SLIDE 12: FORD D-SEGMENT: CD132 & EUCD
    # =========================================================================
    s12 = prs.slides.add_slide(blank_layout)
    add_bg(s12)
    add_header(s12, "Ford Global D-Segment: CD132 (Mondeo Mk3) & EUCD Joint Platform", "Boron Steel Nodes, Laser Brazing & Multi-Brand Cross-OEM Platform Architecture", slide_num=12)

    f_dseg = [
        ("CD132 • FORD MONDEO (MK3)", "D-Segment Executive Saloon & Estate", [
            ("Pioneering Boron Steel Nodes", "Early introduction of ultra-high-strength boron steel in structural B-pillars and rocker nodes for side impact safety."),
            ("Laser-Brazed Roof Seams", "Pioneered automated laser brazing on the roof ditch, replacing black rubber mouldings with an aerodynamic seamless joint."),
            ("Dual-Subframe NVH Isolation", "Engineered fully isolated front and rear chassis subframes with hydraulic bushings to eliminate road harshness."),
            ("Deep-Draw Side Aperture Stampings", "Overcoming extreme draw depths and thinning limits on single-piece side outer body stampings.")
        ], C_PRIMARY),
        ("EUCD • JOINT MULTI-BRAND ARCHITECTURE", "Shared Across Ford, Volvo & Land Rover", [
            ("Multi-OEM Architectural Harmonization", "Joint platform engineering uniting Mondeo Mk4, S-MAX, Galaxy, Volvo S80/V70/XC60, and Freelander 2."),
            ("World-Class Safety Cage Integration", "Harmonizing Volvo's legendary passenger cell crash standards with Ford's high-speed volume manufacturing lines."),
            ("Deformable Crash Subframe", "Engineered lower subframe deformation kinematics to absorb kinetic energy and meet strict pedestrian impact criteria."),
            ("Transverse Powertrain Flexibility", "Accommodated 4-, 5-, and 6-cylinder transverse engines, dual-clutch transmissions, and AWD drivelines.")
        ], C_TEAL)
    ]
    for i, (pname, psub, pitems, pcol) in enumerate(f_dseg):
        px = Inches(0.8) + i * Inches(5.95)
        card = s12.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, px, Inches(1.75), Inches(5.75), Inches(5.2))
        card.fill.solid()
        card.fill.fore_color.rgb = C_CARD_BG
        card.line.color.rgb = C_CARD_BORDER
        cbar = s12.shapes.add_shape(MSO_SHAPE.RECTANGLE, px, Inches(1.75), Inches(5.75), Inches(0.12))
        cbar.fill.solid()
        cbar.fill.fore_color.rgb = pcol
        cbar.line.fill.background()

        ctf = card.text_frame
        ctf.word_wrap = True
        ctf.margin_left = ctf.margin_right = Inches(0.25)
        ctf.margin_top = Inches(0.25)
        cp1 = ctf.paragraphs[0]
        cp1.text = pname
        cp1.font.size = Pt(13)
        cp1.font.bold = True
        cp1.font.color.rgb = pcol
        cp1.space_after = Pt(2)
        cp2 = ctf.add_paragraph()
        cp2.text = psub
        cp2.font.size = Pt(9.5)
        cp2.font.bold = True
        cp2.font.color.rgb = C_TEXT_MUTED
        cp2.space_after = Pt(14)

        for heading, body in pitems:
            ph = ctf.add_paragraph()
            ph.text = heading
            ph.font.size = Pt(10.5)
            ph.font.bold = True
            ph.font.color.rgb = C_TEXT_DARK
            ph.space_after = Pt(2)
            pb = ctf.add_paragraph()
            pb.text = body
            pb.font.size = Pt(9)
            pb.font.color.rgb = RGBColor(71, 85, 105)
            pb.space_after = Pt(10)

    set_speaker_notes(s12, """[11:00 - 12:00] SLIDE 12: FORD D-SEGMENT: CD132 & EUCD
In the D-segment, we scaled up structural complexity on CD132 and EUCD.

On CD132—the third-generation Mondeo—we pioneered the early adoption of ultra-high-strength boron steel in structural nodes. We also introduced automated laser brazing on the roof ditch: instead of pressing a wide gutter and covering it with a cheap plastic moulding, we joined the roof panel to the bodyside with a laser-brazed bronze seam, creating a flawless aesthetic line.

Then came EUCD—one of the industry's most ambitious joint platform programs. Ford, Volvo, and Land Rover shared this single architecture. We had to reconcile Volvo's safety culture with Ford's volume manufacturing speed. 

We engineered a modular front-end crash structure with deformable subframes that satisfied Euro NCAP pedestrian impact while managing high-speed frontal offset collisions across saloons, MPVs, and luxury SUVs like the Volvo XC60 and Freelander 2.""")

    # =========================================================================
    # SLIDE 13: FORD GLOBAL B-CAR & SUV: B2E & B2XX
    # =========================================================================
    s13 = prs.slides.add_slide(blank_layout)
    add_bg(s13)
    add_header(s13, "Ford Global B-Car & SUV: B2E (Fiesta Mk6) & B2XX (EcoSport)", "High-Volume Global Platform Flexibility, Raised SUV Packaging & Tailgate Engineering", slide_num=13)

    f_bcar = [
        ("B2E • GLOBAL FIESTA (MK6)", "Global High-Volume B-Segment", [
            ("Global Manufacturing Footprint", "Engineered for synchronized manufacturing across Europe, Asia, South America, and North America."),
            ("Hot-Stamped Boron Safety Cell", "Extensive hot-formed boron steel A-pillars, B-pillars, and rocker reinforcements achieving top safety ratings."),
            ("Hydroformed Front Subframe", "Hydroformed tubular front suspension subframe maximizing structural stiffness while cutting mass."),
            ("Electric Power Steering Packaging", "Pioneered early column-drive EPAS integration with optimized driver feedback.")
        ], C_PRIMARY),
        ("B2XX • FORD ECOSPORT", "Compact Crossover / SUV Architecture", [
            ("High Ground Clearance Packaging", "Raised ride height to >200 mm ground clearance, requiring revised suspension geometry and drive shaft angles."),
            ("Side-Hinged Tailgate Engineering", "Designed a unique side-hinged rear door carrying a full-size external spare wheel (>25 kg payload)."),
            ("Severe D-Pillar Structural Reinforcement", "Engineered heavy structural reinforcement brackets and forged hinges to eliminate door sag over rough terrain."),
            ("Dynamic Latch Fatigue & Sealing", "Multi-axis proving ground fatigue analysis to prevent latch rattle and water ingress under severe torsional racking.")
        ], C_ACCENT)
    ]
    for i, (pname, psub, pitems, pcol) in enumerate(f_bcar):
        px = Inches(0.8) + i * Inches(5.95)
        card = s13.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, px, Inches(1.75), Inches(5.75), Inches(5.2))
        card.fill.solid()
        card.fill.fore_color.rgb = C_CARD_BG
        card.line.color.rgb = C_CARD_BORDER
        cbar = s13.shapes.add_shape(MSO_SHAPE.RECTANGLE, px, Inches(1.75), Inches(5.75), Inches(0.12))
        cbar.fill.solid()
        cbar.fill.fore_color.rgb = pcol
        cbar.line.fill.background()

        ctf = card.text_frame
        ctf.word_wrap = True
        ctf.margin_left = ctf.margin_right = Inches(0.25)
        ctf.margin_top = Inches(0.25)
        cp1 = ctf.paragraphs[0]
        cp1.text = pname
        cp1.font.size = Pt(13)
        cp1.font.bold = True
        cp1.font.color.rgb = pcol
        cp1.space_after = Pt(2)
        cp2 = ctf.add_paragraph()
        cp2.text = psub
        cp2.font.size = Pt(9.5)
        cp2.font.bold = True
        cp2.font.color.rgb = C_TEXT_MUTED
        cp2.space_after = Pt(14)

        for heading, body in pitems:
            ph = ctf.add_paragraph()
            ph.text = heading
            ph.font.size = Pt(10.5)
            ph.font.bold = True
            ph.font.color.rgb = C_TEXT_DARK
            ph.space_after = Pt(2)
            pb = ctf.add_paragraph()
            pb.text = body
            pb.font.size = Pt(9)
            pb.font.color.rgb = RGBColor(71, 85, 105)
            pb.space_after = Pt(10)

    set_speaker_notes(s13, """[12:00 - 13:00] SLIDE 13: FORD GLOBAL B-CAR & SUV: B2E & B2XX
Slide 13 highlights Ford's global flexible platform engineering: B2E and B2XX.

B2E was the sixth-generation Fiesta—a truly global car manufactured across four continents. It incorporated extensive hot-stamped boron steel in the safety cell and a hydroformed tubular front subframe that delivered exceptional steering agility.

From B2E emerged B2XX—the Ford EcoSport compact SUV. 
Adapting a low-slung hatchback platform into a rugged SUV with over 200 mm of ground clearance required redesigning suspension articulation, drive axle plunge depths, and underbody stone protection.

The standout engineering challenge on B2XX was the rear tailgate. The styling called for a side-hinged rear door carrying a full-size external spare wheel. Hanging 25 kilograms on a cantilevered door subjected the D-pillar and hinges to immense dynamic cyclic twisting over rough roads. We designed heavy internal gusset reinforcements and forged hinge brackets, validating the assembly through rigorous proving ground fatigue testing to prevent door sag and latch rattle.""")

    # =========================================================================
    # SLIDE 14: VW MODULAR: MQB-27 & MQB-37
    # =========================================================================
    s14 = prs.slides.add_slide(blank_layout)
    add_bg(s14)
    add_header(s14, "Volkswagen Modular Transverse Matrix: MQB-27 (A0) & MQB-37 (A1/A2)", "The Baukasten Revolution: Standardized Hardpoints & Unprecedented Global Economies of Scale", slide_num=14)

    vw_mqb = [
        ("MQB-27 (MQB A0)", "Subcompact Modular Platform (Polo / T-Cross)", [
            ("Democratizing High-Tech Safety", "Integrated over 30% hot-formed boron steel into entry-level subcompacts, achieving 5-star Euro NCAP ratings."),
            ("RPS Datum System Standardization", "Full integration of Volkswagen's Referenzpunkt-System datum targets across multi-brand stamping plants."),
            ("Modular Cross-Car Beam", "Shared lightweight dashboard cross-car structure accommodating modular steering and HVAC units."),
            ("High Commonality Across Group", "Shared underbody components across VW Polo, T-Cross, SEAT Ibiza/Arona, and Škoda Fabia.")
        ], C_PRIMARY),
        ("MQB-37 (MQB A1/A2)", "Core Global Platform (Golf / Tiguan / Passat)", [
            ("The 'Fixed' Dimension", "Standardized uniform distance from pedal box to front wheel centerline across all vehicle lines."),
            ("Standardized 12° Engine Inclination", "Uniform engine tilt angles and exhaust routing allowed identical subframes across petrol, diesel, and hybrid."),
            ("Infinite Variable Dimensions", "Complete flexibility in wheelbase, track width, overhangs, and seating heights on identical framing bucks."),
            ("Industrial Efficiency Benchmark", "Reduced engineering hours by >30% while delivering unprecedented group manufacturing profitability.")
        ], C_TEAL)
    ]
    for i, (pname, psub, pitems, pcol) in enumerate(vw_mqb):
        px = Inches(0.8) + i * Inches(5.95)
        card = s14.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, px, Inches(1.75), Inches(5.75), Inches(5.2))
        card.fill.solid()
        card.fill.fore_color.rgb = C_CARD_BG
        card.line.color.rgb = C_CARD_BORDER
        cbar = s14.shapes.add_shape(MSO_SHAPE.RECTANGLE, px, Inches(1.75), Inches(5.75), Inches(0.12))
        cbar.fill.solid()
        cbar.fill.fore_color.rgb = pcol
        cbar.line.fill.background()

        ctf = card.text_frame
        ctf.word_wrap = True
        ctf.margin_left = ctf.margin_right = Inches(0.25)
        ctf.margin_top = Inches(0.25)
        cp1 = ctf.paragraphs[0]
        cp1.text = pname
        cp1.font.size = Pt(13)
        cp1.font.bold = True
        cp1.font.color.rgb = pcol
        cp1.space_after = Pt(2)
        cp2 = ctf.add_paragraph()
        cp2.text = psub
        cp2.font.size = Pt(9.5)
        cp2.font.bold = True
        cp2.font.color.rgb = C_TEXT_MUTED
        cp2.space_after = Pt(14)

        for heading, body in pitems:
            ph = ctf.add_paragraph()
            ph.text = heading
            ph.font.size = Pt(10.5)
            ph.font.bold = True
            ph.font.color.rgb = C_TEXT_DARK
            ph.space_after = Pt(2)
            pb = ctf.add_paragraph()
            pb.text = body
            pb.font.size = Pt(9)
            pb.font.color.rgb = RGBColor(71, 85, 105)
            pb.space_after = Pt(10)

    set_speaker_notes(s14, """[13:00 - 14:00] SLIDE 14: VOLKSWAGEN MODULAR: MQB-27 & MQB-37
Moving to Volkswagen marked my entry into the modular matrix revolution—the Modularer Querbaukasten, or MQB.

MQB-37 is widely considered the most successful platform strategy in automotive history. What made MQB brilliant was fixing a single critical manufacturing hardpoint: the distance from the pedal box to the front wheel centerline. By keeping that distance constant, Volkswagen standardized the engine mounting angle at 12 degrees rearward, standardized the exhaust tunnel, standardized the HVAC housing, and standardized the body shop welding framing bucks. 

Yet everything else—wheelbase, track width, ground clearance, and body style—remained flexible. A Golf hatchback, an estate, a Tiguan SUV, and a Passat saloon could all be welded on the exact same assembly lines.

On MQB-27, we brought that modular philosophy down to the subcompact A0 segment—Polo, T-Cross, Fabia—incorporating over 30% hot-formed boron steel into high-volume entry cars while maintaining aggressive cost targets.""")

    # =========================================================================
    # SLIDE 15: VW ELECTRIFICATION & COMMERCIAL: MEB & T7
    # =========================================================================
    s15 = prs.slides.add_slide(blank_layout)
    add_bg(s15)
    add_header(s15, "Volkswagen Electrification & Commercial: MEB Platform & T7 Multivan", "Dedicated EV Skateboard Architecture & Commercial Migration onto Modular Car Platforms", slide_num=15)

    vw_elec = [
        ("MEB • ELECTRIC SKATEBOARD PLATFORM", "Dedicated BEV Matrix (ID.3 / ID.4 / ID. Buzz)", [
            ("Structural Battery Pack Enclosure", "The high-voltage battery housing functions as an active underbody shear plate, increasing torsional stiffness past 30,000 Nm/°."),
            ("Multi-Cell Aluminium Crash Sills", "Massive extruded rocker sections engineered to absorb side pole impact before battery module intrusion."),
            ("Absence of Front ICE Load Path", "Front crumple zones redesigned with progressive rail accordion folding without reliance on engine block deceleration."),
            ("Flat Floor Interior Packaging", "Relocated HVAC unit forward into cowl area, creating D-segment interior cabin volume within a C-segment exterior footprint.")
        ], C_PRIMARY),
        ("T7 MULTIVAN • MODULAR MPV", "Commercial Vehicle Migration to MQB", [
            ("Migrating Van onto MQB Architecture", "Migrated Volkswagen's iconic commercial line onto passenger-car MQB foundations with car-like ride and handling."),
            ("Modular Floor Rail System", "Engineered flat floor rail tracks tested to extreme dynamic seatbelt pull loads (ECE R14) for sliding, removable seats."),
            ("Dual A-Pillar Structural Design", "Engineered dual A-pillar packaging with front quarter glass to maximize forward vision while ensuring roof crush strength."),
            ("Plug-In Hybrid Packaging", "Integrated high-voltage hybrid battery beneath the flat floor without encroaching on passenger cabin volume.")
        ], C_ACCENT)
    ]
    for i, (pname, psub, pitems, pcol) in enumerate(vw_elec):
        px = Inches(0.8) + i * Inches(5.95)
        card = s15.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, px, Inches(1.75), Inches(5.75), Inches(5.2))
        card.fill.solid()
        card.fill.fore_color.rgb = C_CARD_BG
        card.line.color.rgb = C_CARD_BORDER
        cbar = s15.shapes.add_shape(MSO_SHAPE.RECTANGLE, px, Inches(1.75), Inches(5.75), Inches(0.12))
        cbar.fill.solid()
        cbar.fill.fore_color.rgb = pcol
        cbar.line.fill.background()

        ctf = card.text_frame
        ctf.word_wrap = True
        ctf.margin_left = ctf.margin_right = Inches(0.25)
        ctf.margin_top = Inches(0.25)
        cp1 = ctf.paragraphs[0]
        cp1.text = pname
        cp1.font.size = Pt(13)
        cp1.font.bold = True
        cp1.font.color.rgb = pcol
        cp1.space_after = Pt(2)
        cp2 = ctf.add_paragraph()
        cp2.text = psub
        cp2.font.size = Pt(9.5)
        cp2.font.bold = True
        cp2.font.color.rgb = C_TEXT_MUTED
        cp2.space_after = Pt(14)

        for heading, body in pitems:
            ph = ctf.add_paragraph()
            ph.text = heading
            ph.font.size = Pt(10.5)
            ph.font.bold = True
            ph.font.color.rgb = C_TEXT_DARK
            ph.space_after = Pt(2)
            pb = ctf.add_paragraph()
            pb.text = body
            pb.font.size = Pt(9)
            pb.font.color.rgb = RGBColor(71, 85, 105)
            pb.space_after = Pt(10)

    set_speaker_notes(s15, """[14:00 - 15:00] SLIDE 15: VW ELECTRIFICATION & COMMERCIAL: MEB & T7
Slide 15 brings us to the electric revolution on MEB, and the commercial adaptation of MQB on the T7 Multivan.

MEB—the Modularer E-Antriebs-Baukasten—was a radical clean-sheet design that discarded 100 years of internal combustion assumptions. In an electric vehicle, the battery is not merely dead weight; the battery enclosure is an active structural shear plate bolted to the underbody, boosting vehicle torsional rigidity beyond 30,000 Nm per degree. 

Crash safety required reinventing side-impact architecture: because battery cells must not be deformed, we engineered massive multi-cell extruded aluminium side sills that arrest side pole impact cold before touching battery modules.

Meanwhile, on the T7 Multivan, we demonstrated the ultimate flexibility of MQB by moving Volkswagen's premium commercial MPV onto a car-based modular architecture. We engineered a flat floor with modular tracks that passed rigorous ECE R14 seatbelt pull tests, while packaging plug-in hybrid powertrains beneath the floor.""")

    # =========================================================================
    # SLIDE 16: MASTER DESIGN-TO-MANUFACTURE FLOWCHART (Complete Lifecycle)
    # =========================================================================
    s16 = prs.slides.add_slide(blank_layout)
    add_bg(s16)
    add_header(s16, "Master Design-to-Manufacture Flowchart: Complete Automotive Lifecycle", "End-to-End 12-Stage Industrialization Roadmap from Styling Concept to Serial SOP", slide_num=16)

    # 12 Process Flow blocks in 2 rows of 6
    flow_stages = [
        ("01. CONCEPT", "Voice of Customer, BOM targets, segment specs"),
        ("02. PACKAGING", "Hardpoints, H-point, ground clearance, eye ellipse"),
        ("03. 3D SURFACING", "Class-A scan offset to Class-B/C pressings & Master Sections"),
        ("04. DFM / DFA", "Stamping FLD, draft angles, rib sink ratios, gun access"),
        ("05. DFMEA", "P-Diagrams, Ford v4.2, Special Characteristics (∇ CC)"),
        ("06. 2D & GD&T", "ASME Y14.5, 3-2-1 datums, VW RPS targeting, Profile"),
        ("07. VIRTUAL CAE", "Torsional FEA, NVH modal decoupling, LS-DYNA crash"),
        ("08. HARD TOOLING", "Stamping dies, injection moulds, assembly bucks"),
        ("09. TOOLING TRYOUT", "First stamped parts (TT/VFF), 100% CMM balloon checks"),
        ("10. CAPABILITY", "PFMEA, Control Plans, Gage R&R (<10%), Cpk >= 1.67"),
        ("11. PPAP & PSW", "18 PPAP elements, DVP&R tests, signed Warrant (PSW)"),
        ("12. MASS SOP", "Job 1 launch, takt-time ramp, launch containment")
    ]

    card_w16 = Inches(1.85)
    gap16 = Inches(0.12)
    # Row 1 (Stages 1-6)
    for i in range(6):
        num_title, sdesc = flow_stages[i]
        fx = Inches(0.8) + i * (card_w16 + gap16)
        fcard = s16.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, fx, Inches(1.75), card_w16, Inches(2.3))
        fcard.fill.solid()
        fcard.fill.fore_color.rgb = C_CARD_BG
        fcard.line.color.rgb = C_CARD_BORDER
        fbar = s16.shapes.add_shape(MSO_SHAPE.RECTANGLE, fx, Inches(1.75), card_w16, Inches(0.08))
        fbar.fill.solid()
        fbar.fill.fore_color.rgb = C_PRIMARY
        fbar.line.fill.background()

        ftf = fcard.text_frame
        ftf.word_wrap = True
        ftf.margin_left = ftf.margin_right = Inches(0.12)
        ftf.margin_top = Inches(0.15)
        fp1 = ftf.paragraphs[0]
        fp1.text = num_title
        fp1.font.size = Pt(10)
        fp1.font.bold = True
        fp1.font.color.rgb = C_PRIMARY
        fp1.space_after = Pt(4)
        fp2 = ftf.add_paragraph()
        fp2.text = sdesc
        fp2.font.size = Pt(8.5)
        fp2.font.color.rgb = RGBColor(71, 85, 105)

    # Dividing Milestone Bar across middle
    mbar = s16.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(4.25), Inches(11.733), Inches(0.45))
    mbar.fill.solid()
    mbar.fill.fore_color.rgb = C_DARK_CARD
    mbar.line.color.rgb = C_ACCENT
    mtf = mbar.text_frame
    mtf.margin_left = Inches(0.2)
    mtf.margin_top = Inches(0.08)
    mp = mtf.paragraphs[0]
    mp.alignment = PP_ALIGN.CENTER
    mp.text = "★ MAJOR GATEWAY: DESIGN FREEZE / TOOLING KICK-OFF (FORD FDJ ↔ VW DKM) — CAPITAL RELEASE ★"
    mp.font.size = Pt(10)
    mp.font.bold = True
    mp.font.color.rgb = C_ACCENT

    # Row 2 (Stages 7-12)
    for i in range(6):
        num_title, sdesc = flow_stages[i+6]
        fx = Inches(0.8) + i * (card_w16 + gap16)
        fcard = s16.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, fx, Inches(4.85), card_w16, Inches(2.2))
        fcard.fill.solid()
        fcard.fill.fore_color.rgb = C_CARD_BG
        fcard.line.color.rgb = C_CARD_BORDER
        fbar = s16.shapes.add_shape(MSO_SHAPE.RECTANGLE, fx, Inches(4.85), card_w16, Inches(0.08))
        fbar.fill.solid()
        fbar.fill.fore_color.rgb = C_TEAL if i < 4 else C_INDIGO
        fbar.line.fill.background()

        ftf = fcard.text_frame
        ftf.word_wrap = True
        ftf.margin_left = ftf.margin_right = Inches(0.12)
        ftf.margin_top = Inches(0.15)
        fp1 = ftf.paragraphs[0]
        fp1.text = num_title
        fp1.font.size = Pt(10)
        fp1.font.bold = True
        fp1.font.color.rgb = C_TEAL if i < 4 else C_INDIGO
        fp1.space_after = Pt(4)
        fp2 = ftf.add_paragraph()
        fp2.text = sdesc
        fp2.font.size = Pt(8.5)
        fp2.font.color.rgb = RGBColor(71, 85, 105)

    set_speaker_notes(s16, """[15:00 - 16:30] SLIDE 16: MASTER DESIGN-TO-MANUFACTURE FLOWCHART
Slide 16 is the master roadmap of automotive vehicle delivery: The complete 12-stage Design-to-Manufacture Flowchart.

The top row represents Upstream Engineering—moving from Voice of Customer, through hardpoint packaging, Class-A to Class-B CAD surfacing, DFM feasibility, DFMEA risk mitigation, and GD&T detailing.

Right in the center sits the pivotal milestone: Design Freeze—Final Data Judgement (FDJ) in Ford, or Datenkontrollmodell (DKM) in Volkswagen. This is the financial Point of No Return, where multimillion-pound tooling purchase orders are released to cut hard steel.

The bottom row represents Downstream Industrialization—cutting stamping dies, executing Tooling Tryouts (TT/VFF), locking down PFMEAs and Control Plans, proving Measurement Systems capability with Gage R&R below 10%, achieving statistical Cpk of 1.67, and submitting the 18 elements of PPAP. Only when the Part Submission Warrant is signed can we celebrate Job 1 and Start of Production.""")

    # =========================================================================
    # SLIDE 17: FLOWCHART UPSTREAM: CONCEPT TO DESIGN FREEZE
    # =========================================================================
    s17 = prs.slides.add_slide(blank_layout)
    add_bg(s17)
    add_header(s17, "Design-to-Manufacture: Upstream Virtual Engineering", "Phase 1: Concept, Packaging, DFM, DFMEA & Virtual CAE to Design Freeze (FDJ / DKM)", slide_num=17)

    up_cards = [
        ("1. PACKAGING & HARDPOINTS", [
            ("Vehicle Coordinates", "Wheelbase, track, ground clearance, cowl point, and firewall plane."),
            ("Ergonomic H-Point", "SAE J826 manikin coordinates establishing seating reference point and eye ellipse."),
            ("Clearance Envelopes", "Kinematic wheel jounce sweeps and closure swing arcs.")
        ]),
        ("2. SURFACING & DFM/DFA", [
            ("Class-B Offsets", "Offsetting clay scan Class-A surfaces to structural inner pressings."),
            ("Stamping Feasibility", "Evaluating Formability Limit Diagrams (FLD), bend radii, and springback."),
            ("Assembly Ergonomics", "Ensuring robotic spot-weld flange width (>=16 mm) and poka-yoke features.")
        ]),
        ("3. DFMEA & SPECIAL CHARS", [
            ("Parameter Diagrams", "Mapping signal inputs, control factors, and noise factors (Ford v4.2)."),
            ("Severity Discipline", "Enforcing mandatory redesign for failure modes with Severity >= 8."),
            ("Special Chars (∇)", "Cascading Critical Characteristics (∇ CC) to 2D drawings and control plans.")
        ]),
        ("4. GD&T & VIRTUAL CAE", [
            ("ASME & RPS Schemes", "Establishing 3-2-1 / RPS datums and Profile of a Surface tolerances."),
            ("FEA Rigidity & NVH", "Targeting 18-28 kNm/° torsional stiffness and modal decoupling (>38 Hz)."),
            ("Crash (LS-DYNA)", "Simulating frontal progressive rail collapse and side boron intrusion.")
        ])
    ]
    u_w = Inches(2.7)
    u_gap = Inches(0.28)
    for i, (ctitle, citems) in enumerate(up_cards):
        ux = Inches(0.8) + i * (u_w + u_gap)
        card = s17.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, ux, Inches(1.75), u_w, Inches(4.3))
        card.fill.solid()
        card.fill.fore_color.rgb = C_CARD_BG
        card.line.color.rgb = C_CARD_BORDER
        cbar = s17.shapes.add_shape(MSO_SHAPE.RECTANGLE, ux, Inches(1.75), u_w, Inches(0.12))
        cbar.fill.solid()
        cbar.fill.fore_color.rgb = C_PRIMARY
        cbar.line.fill.background()

        ctf = card.text_frame
        ctf.word_wrap = True
        ctf.margin_left = ctf.margin_right = Inches(0.18)
        ctf.margin_top = Inches(0.22)
        cp1 = ctf.paragraphs[0]
        cp1.text = ctitle
        cp1.font.size = Pt(11)
        cp1.font.bold = True
        cp1.font.color.rgb = C_PRIMARY
        cp1.space_after = Pt(10)

        for heading, body in citems:
            ph = ctf.add_paragraph()
            ph.text = heading
            ph.font.size = Pt(9.5)
            ph.font.bold = True
            ph.font.color.rgb = C_TEXT_DARK
            ph.space_after = Pt(2)
            pb = ctf.add_paragraph()
            pb.text = body
            pb.font.size = Pt(8.5)
            pb.font.color.rgb = RGBColor(71, 85, 105)
            pb.space_after = Pt(8)

    # Freeze Gate callout at bottom
    gate_card = s17.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(6.15), Inches(11.733), Inches(0.85))
    gate_card.fill.solid()
    gate_card.fill.fore_color.rgb = C_DARK_CARD
    gate_card.line.color.rgb = C_PRIMARY
    gtf = gate_card.text_frame
    gtf.margin_left = Inches(0.25)
    gtf.margin_top = Inches(0.15)
    gp1 = gtf.paragraphs[0]
    gp1.text = "CRITICAL GATEWAY DELIVERABLES AT DESIGN FREEZE (FDJ / DKM):"
    gp1.font.size = Pt(10)
    gp1.font.bold = True
    gp1.font.color.rgb = C_ACCENT
    gp2 = gtf.add_paragraph()
    gp2.text = "✓ 100% CAD Surface Maturity  ✓ DFM Tooling Feasibility Sign-Off  ✓ DFMEA Signed with ∇ CC Identified  ✓ Virtual CAE Rigidity & Crash Confirmed"
    gp2.font.size = Pt(9.5)
    gp2.font.color.rgb = C_TEXT_LIGHT

    set_speaker_notes(s17, """[16:30 - 17:30] SLIDE 17: UPSTREAM VIRTUAL ENGINEERING
Let us drill down into the upstream virtual engineering phase.

This is where quality is won or lost. The 1-10-100 rule of quality dictates that an error caught here in CAD costs £1 to fix; in tooling it costs £10; on the assembly line it costs £100.

We progress through four rigorous gates: First, packaging and hardpoints, locking the occupant H-point and dynamic suspension envelopes. Second, surfacing and DFM, where we run stamping formability limit simulations to prove that sheet metal will not split or wrinkle. Third, DFMEA using Ford's Handbook v4.2, where we identify Critical Characteristics marked with the inverted delta (∇). And fourth, GD&T and virtual CAE simulation, where we confirm torsional rigidity, NVH modal decoupling, and crash pulse management.

Only when all four pillars are green do we approve Final Data Judgement (FDJ) and release hard tooling.""")

    # =========================================================================
    # SLIDE 18: FLOWCHART DOWNSTREAM: TOOLING TO SOP
    # =========================================================================
    s18 = prs.slides.add_slide(blank_layout)
    add_bg(s18)
    add_header(s18, "Design-to-Manufacture: Downstream Physical Industrialization", "Phase 2: Hard Tooling Build, Tooling Tryout (TT), Capability Studies & PPAP / PSW Sign-Off", slide_num=18)

    down_cards = [
        ("1. TOOLING PROCURE & BUILD", [
            ("Hard Tooling Machining", "CNC milling and EDM finishing of transfer stamping dies and injection moulds."),
            ("Welding Buck Fabrication", "Building robotic Body-in-White framing fixtures and geometric clamping nests."),
            ("Supplier Tooling Audits", "Conducting on-site progress reviews with Tier-1 die makers across Europe and Asia.")
        ]),
        ("2. TOOLING TRYOUT (TT / VFF)", [
            ("First Off-Tool Parts (FOTP)", "Pressing first physical stampings from production dies to detect metal springback."),
            ("100% CMM Balloon Inspection", "Probing every dimension against GD&T drawings on Coordinate Measuring Machines."),
            ("Die Recut & Compensation", "Recutting die surfaces in CAM to compensate for elastic recovery in boron steels.")
        ]),
        ("3. PROCESS CAPABILITY (CPK)", [
            ("Measurement Systems (MSA)", "Gage R&R studies proving measurement variance is <10% for critical characteristics."),
            ("Process Capability Cpk", "Mandated Cpk >= 1.67 (5-sigma quality) for all Critical Characteristics (∇ CC)."),
            ("PFMEA & Control Plans", "Synchronizing shop-floor operator instructions and poka-yoke inspection stations.")
        ]),
        ("4. PPAP & JOB 1 / SOP", [
            ("PPAP 18 Deliverables", "Compiling dimensional layouts, DVP&R test records, and material lab certs."),
            ("Part Submission Warrant", "Executive technical signature on PSW legally certifying production readiness."),
            ("Serial SOP Launch", "Line ramp-up at takt time with zero defects under launch containment protocols.")
        ])
    ]
    for i, (ctitle, citems) in enumerate(down_cards):
        dx = Inches(0.8) + i * (u_w + u_gap)
        card = s18.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, dx, Inches(1.75), u_w, Inches(4.3))
        card.fill.solid()
        card.fill.fore_color.rgb = C_CARD_BG
        card.line.color.rgb = C_CARD_BORDER
        cbar = s18.shapes.add_shape(MSO_SHAPE.RECTANGLE, dx, Inches(1.75), u_w, Inches(0.12))
        cbar.fill.solid()
        cbar.fill.fore_color.rgb = C_TEAL
        cbar.line.fill.background()

        ctf = card.text_frame
        ctf.word_wrap = True
        ctf.margin_left = ctf.margin_right = Inches(0.18)
        ctf.margin_top = Inches(0.22)
        cp1 = ctf.paragraphs[0]
        cp1.text = ctitle
        cp1.font.size = Pt(11)
        cp1.font.bold = True
        cp1.font.color.rgb = C_TEAL
        cp1.space_after = Pt(10)

        for heading, body in citems:
            ph = ctf.add_paragraph()
            ph.text = heading
            ph.font.size = Pt(9.5)
            ph.font.bold = True
            ph.font.color.rgb = C_TEXT_DARK
            ph.space_after = Pt(2)
            pb = ctf.add_paragraph()
            pb.text = body
            pb.font.size = Pt(8.5)
            pb.font.color.rgb = RGBColor(71, 85, 105)
            pb.space_after = Pt(8)

    # PSW Callout at bottom
    psw_card = s18.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(6.15), Inches(11.733), Inches(0.85))
    psw_card.fill.solid()
    psw_card.fill.fore_color.rgb = C_DARK_CARD
    psw_card.line.color.rgb = C_TEAL
    ptf = psw_card.text_frame
    ptf.margin_left = Inches(0.25)
    ptf.margin_top = Inches(0.15)
    pp1 = ptf.paragraphs[0]
    pp1.text = "THE LEGAL SUMMIT OF APQP: PART SUBMISSION WARRANT (PSW) SIGN-OFF:"
    pp1.font.size = Pt(10)
    pp1.font.bold = True
    pp1.font.color.rgb = C_ACCENT
    pp2 = ptf.add_paragraph()
    pp2.text = "✓ Full 18 PPAP Elements Verified  ✓ Cpk >= 1.67 Confirmed on ∇ CC  ✓ Gage R&R < 10%  ✓ Production Run-at-Rate Demonstrated at Full Line Speed"
    pp2.font.size = Pt(9.5)
    pp2.font.color.rgb = C_TEXT_LIGHT

    set_speaker_notes(s18, """[17:30 - 18:30] SLIDE 18: DOWNSTREAM INDUSTRIALIZATION
Now let us walk through downstream industrialization—the physical validation gauntlet.

First, hard tooling procurement and build: cutting hardened tool steel dies and building automated framing fixtures. 
Second, Tooling Tryout—TT in Ford, Vorserie in VW. We press the first parts off production dies and execute a 100% CMM balloon dimensional inspection. This is where we measure springback in advanced high-strength steels and recut the die surfaces to bring them to nominal.

Third, statistical process capability: We perform Measurement Systems Analysis (Gage R&R) to guarantee our gauges have less than 10% measurement error. We verify that all Critical Characteristics achieve a process capability Cpk of at least 1.67—fewer than 0.6 defects per million parts.

And fourth, the culmination of APQP: The 18 elements of PPAP. As an engineering manager, signing the Part Submission Warrant is your formal legal declaration that the parts conform to drawing, the DVP&R tests have passed, and the production line is ready for Job 1.""")

    # =========================================================================
    # SLIDE 19: PROCESS 1 - 3D DESIGN & PACKAGING
    # =========================================================================
    s19 = prs.slides.add_slide(blank_layout)
    add_bg(s19)
    add_header(s19, "Process 1: Initial 3D Design & Hardpoint Packaging", "Geometry Architecture, Ergonomics & Clearance Envelopes", slide_num=19)

    p1_cols = [
        ("HARDPOINTS & ARCHITECTURE", [
            ("Vehicle Coordinates", "Establishing absolute zero origins, front/rear wheel centers, cowl point, and ground clearance angles."),
            ("SAE J826 H-Point", "Positioning 95th percentile male / 5th percentile female manikins to define SgRP and heel point."),
            ("Vision & Glazing", "SAE J941 driver eye ellipse mapping ensuring regulatory vision through windshield and mirrors.")
        ]),
        ("SURFACE FEASIBILITY (CLASS A TO B/C)", [
            ("Offset Feasibility", "Translating styling clay scans into Class-B structural inners and Class-C non-visible brackets."),
            ("Flanging & Radii", "Modifying razor-sharp studio styling creases (<0.5 mm) to manufacturable stamping radii (>1.5 mm)."),
            ("Master Sections", "Cutting parametric cross-sections across pillars, sills, and headers to secure spot-weld flange access.")
        ]),
        ("KINEMATIC DYNAMIC ENVELOPES", [
            ("Suspension Sweeps", "Dynamic 3D swept volumes across full jounce (+100 mm), rebound (-80 mm), and steering lock."),
            ("Closure Kinematics", "Door and tailgate swing arcs with inclined hinge axes for natural gravity-assisted closure."),
            ("Weatherstrip Sealing", "Ensuring uniform 30-40% continuous seal compression around door apertures to stop wind noise.")
        ])
    ]
    for i, (col_title, items) in enumerate(p1_cols):
        cx = Inches(0.8) + i * Inches(3.98)
        card = s19.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, cx, Inches(1.75), Inches(3.8), Inches(5.2))
        card.fill.solid()
        card.fill.fore_color.rgb = C_CARD_BG
        card.line.color.rgb = C_CARD_BORDER
        cbar = s19.shapes.add_shape(MSO_SHAPE.RECTANGLE, cx, Inches(1.75), Inches(3.8), Inches(0.12))
        cbar.fill.solid()
        cbar.fill.fore_color.rgb = C_PRIMARY
        cbar.line.fill.background()

        ctf = card.text_frame
        ctf.word_wrap = True
        ctf.margin_left = ctf.margin_right = Inches(0.2)
        ctf.margin_top = Inches(0.25)
        cp1 = ctf.paragraphs[0]
        cp1.text = col_title
        cp1.font.size = Pt(11)
        cp1.font.bold = True
        cp1.font.color.rgb = C_PRIMARY
        cp1.space_after = Pt(14)

        for heading, body in items:
            ph = ctf.add_paragraph()
            ph.text = heading
            ph.font.size = Pt(10)
            ph.font.bold = True
            ph.font.color.rgb = C_TEXT_DARK
            ph.space_after = Pt(2)
            pb = ctf.add_paragraph()
            pb.text = body
            pb.font.size = Pt(8.8)
            pb.font.color.rgb = RGBColor(71, 85, 105)
            pb.space_after = Pt(8)

    set_speaker_notes(s19, """[18:30 - 19:30] SLIDE 19: PROCESS 1: INITIAL 3D DESIGN
Now, let us examine the 8 core engineering disciplines in detail. Process 1: Initial 3D Design and Hardpoint Packaging.

Everything starts with the hardpoints: wheel centerlines, cowl point, firewall plane, and ground clearance angles. 
From the SAE J826 manikin, we establish the Seating Reference Point—the H-point. That single point governs driver eye ellipses, pedal reach, headroom, knee clearance, and line-of-sight angles past the A-pillars.

Then comes Class-A to Class-B surfacing. Studio clay surfaces often feature razor-sharp styling creases with radii below 0.5 mm that would split sheet steel. We engineer the Class-B structural pressings, cutting parametric Master Sections through the A-pillar, rocker, and roof rail to verify spot-weld gun clearance and airbag deployment envelopes.

Finally, we run 3D kinematic sweeps: wheel jounce and rebound, steering lock sweeps, and door swing arcs to ensure weatherstrip seals compress uniformly by 30 to 40 percent.""")

    # =========================================================================
    # SLIDE 20: PROCESS 2 - DFM & DFA
    # =========================================================================
    s20 = prs.slides.add_slide(blank_layout)
    add_bg(s20)
    add_header(s20, "Process 2: Design for Manufacture (DFM) & Assembly (DFA)", "Sheet Metal Stamping, Injection Moulding & Assembly Ergonomics", slide_num=20)

    dfm_cards = [
        ("SHEET METAL STAMPING DFM", "Cold Stamping & Boron Pressing", [
            ("Formability Limit (FLD)", "Assessing major vs. minor principal strain to eliminate tearing and wrinkling in die draws."),
            ("Minimum Punch Radii", "Enforcing internal punch radii >= 1.5t for mild steel, and >= 2.5-3.0t for advanced high-strength steels."),
            ("Springback Compensation", "Reverse-compensating tooling surfaces in CAD/CAM to counteract severe elastic recovery in AHSS."),
            ("Draw Depth & Draft", "Maintaining minimum 3°-5° draft on vertical drawing walls to avoid die galling and panel split.")
        ], C_PRIMARY),
        ("INJECTION MOULDING DFM", "Polymers & Interior / Exterior Trim", [
            ("Nominal Wall Thickness", "Maintaining uniform 2.5-3.0 mm walls on trims to avoid differential shrinkage and warpage."),
            ("Rib-to-Wall Ratios", "Limiting rib base thickness to 50-60% of adjacent wall (trib <= 0.6t) to eliminate sink marks."),
            ("Draft Angle Standards", "0.5°-1.0° on polished tools; minimum 1.5° per 0.025 mm texture grain depth to prevent scuffing."),
            ("Tooling Pull & Parting Lines", "Aligning geometry to line of draw to eliminate costly hydraulic lifters and collapsing slides.")
        ], C_TEAL),
        ("DESIGN FOR ASSEMBLY (DFA)", "Plant Ergonomics & Robotic Accessibility", [
            ("Spot-Weld Flange Access", "Ensuring minimum 16-18 mm flange width for 16 mm robotic weld gun electrode tips."),
            ("Mistake-Proofing (Poka-Yoke)", "Asymmetrical mounting tabs preventing components from being installed inverted on the line."),
            ("Fastener Radial Clearance", "Minimum 35 mm clearance around bolt axes for multi-spindle automated nutrunners."),
            ("Modular Cockpit Marriage", "Designing cockpits and front-end modules for single-axis robotic insertion into the BIW.")
        ], C_ACCENT)
    ]
    for i, (ctitle, csub, citems, ccol) in enumerate(dfm_cards):
        cx = Inches(0.8) + i * Inches(3.98)
        card = s20.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, cx, Inches(1.75), Inches(3.8), Inches(5.2))
        card.fill.solid()
        card.fill.fore_color.rgb = C_CARD_BG
        card.line.color.rgb = C_CARD_BORDER
        cbar = s20.shapes.add_shape(MSO_SHAPE.RECTANGLE, cx, Inches(1.75), Inches(3.8), Inches(0.12))
        cbar.fill.solid()
        cbar.fill.fore_color.rgb = ccol
        cbar.line.fill.background()

        ctf = card.text_frame
        ctf.word_wrap = True
        ctf.margin_left = ctf.margin_right = Inches(0.2)
        ctf.margin_top = Inches(0.25)
        cp1 = ctf.paragraphs[0]
        cp1.text = ctitle
        cp1.font.size = Pt(11)
        cp1.font.bold = True
        cp1.font.color.rgb = ccol
        cp1.space_after = Pt(2)
        cp2 = ctf.add_paragraph()
        cp2.text = csub
        cp2.font.size = Pt(8.5)
        cp2.font.bold = True
        cp2.font.color.rgb = C_TEXT_MUTED
        cp2.space_after = Pt(12)

        for heading, body in citems:
            ph = ctf.add_paragraph()
            ph.text = heading
            ph.font.size = Pt(10)
            ph.font.bold = True
            ph.font.color.rgb = C_TEXT_DARK
            ph.space_after = Pt(2)
            pb = ctf.add_paragraph()
            pb.text = body
            pb.font.size = Pt(8.8)
            pb.font.color.rgb = RGBColor(71, 85, 105)
            pb.space_after = Pt(8)

    set_speaker_notes(s20, """[19:30 - 20:30] SLIDE 20: PROCESS 2: DFM & DFA
Process 2 is where CAD idealism meets manufacturing physics: DFM and DFA.

In sheet metal stamping, punch bend radii must be set to at least 1.5 times sheet thickness for mild steel, and 2.5 to 3.0 times thickness for advanced high-strength steels to avoid micro-cracks along bend lines. Furthermore, high-strength steels experience severe elastic springback upon die release, requiring CAM tooling surfaces to be reverse-compensated.

In injection moulding, the golden rule is wall thickness uniformity to prevent differential cooling warpage. Structural ribs must never exceed 50 to 60 percent of the adjacent wall thickness, or visible sink marks will ruin Class-A surfaces. 

In DFA, we design for assembly workers and robotic automation. A resistance spot-weld flange requires at least 16 millimetres of width to allow a standard 16 mm electrode tip full contact without edge burning. And asymmetrical Poka-Yoke locating pins guarantee mistake-proof one-way installation on the line.""")

    # =========================================================================
    # SLIDE 21: PROCESS 3 - DFMEA & ROBUSTNESS
    # =========================================================================
    s21 = prs.slides.add_slide(blank_layout)
    add_bg(s21)
    add_header(s21, "Process 3: DFMEA & Robustness Linkages", "Ford FMEA Handbook v4.2, P-Diagrams & Special Characteristics (∇)", slide_num=21)

    fmea_boxes = [
        ("PARAMETER DIAGRAM (P-DIAGRAM)", [
            ("Signal Input", "Driver command or system trigger (e.g., 40 N pull force on exterior door handle)."),
            ("Control Factors", "Design parameters: latch spring rate, cable stiffness, pivot mechanical advantage, alloy temper."),
            ("Noise Factors", "Uncontrollable disturbances: piece-to-piece tolerances, thermal extremes (-40°C to +85°C), seal icing, customer abuse."),
            ("Error States", "Failure modes: handle fails to return, high unlatching effort (>75 N), acoustic rattles on rough roads.")
        ]),
        ("RISK EVALUATION & FORD PHILOSOPHY", [
            ("Severity (S 1-10)", "Ratings 9-10 indicate regulatory safety non-compliance. S >= 8 mandates redesign regardless of RPN."),
            ("Occurrence (O 1-10)", "Assesses failure mechanism probability based on design maturity and historical warranty."),
            ("Detection (D 1-10)", "Evaluates capability of DVP&R virtual simulations and physical rig tests to catch defects prior to freeze."),
            ("The Severity Rule", "Never hide behind mathematical RPN. High severity items demand fail-safe containment.")
        ]),
        ("SPECIAL CHARACTERISTICS CASCADE", [
            ("Critical Characteristics (∇ CC)", "Features affecting vehicle safety or regulatory compliance. Mandates ∇ symbol on CAD, drawings, and Control Plans."),
            ("Significant Characteristics (SC)", "Key features driving customer satisfaction, fit, flush, and major assembly interfaces."),
            ("PFMEA & Control Plan Link", "Every ∇ CC cascades directly to Process FMEA, poka-yoke gauging, and Cpk >= 1.67 statistical controls."),
            ("DVP&R Verification", "Direct trace from failure mode to specific physical durability test protocol.")
        ])
    ]
    for i, (btitle, bitems) in enumerate(fmea_boxes):
        bx = Inches(0.8) + i * Inches(3.98)
        card = s21.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, bx, Inches(1.75), Inches(3.8), Inches(5.2))
        card.fill.solid()
        card.fill.fore_color.rgb = C_CARD_BG
        card.line.color.rgb = C_CARD_BORDER
        cbar = s21.shapes.add_shape(MSO_SHAPE.RECTANGLE, bx, Inches(1.75), Inches(3.8), Inches(0.12))
        cbar.fill.solid()
        cbar.fill.fore_color.rgb = C_ROSE if i == 1 else C_PRIMARY
        cbar.line.fill.background()

        ctf = card.text_frame
        ctf.word_wrap = True
        ctf.margin_left = ctf.margin_right = Inches(0.2)
        ctf.margin_top = Inches(0.25)
        cp1 = ctf.paragraphs[0]
        cp1.text = btitle
        cp1.font.size = Pt(11)
        cp1.font.bold = True
        cp1.font.color.rgb = C_ROSE if i == 1 else C_PRIMARY
        cp1.space_after = Pt(14)

        for heading, body in bitems:
            ph = ctf.add_paragraph()
            ph.text = heading
            ph.font.size = Pt(10)
            ph.font.bold = True
            ph.font.color.rgb = C_TEXT_DARK
            ph.space_after = Pt(2)
            pb = ctf.add_paragraph()
            pb.text = body
            pb.font.size = Pt(8.8)
            pb.font.color.rgb = RGBColor(71, 85, 105)
            pb.space_after = Pt(8)

    set_speaker_notes(s21, """[20:30 - 21:30] SLIDE 21: PROCESS 3: DFMEA & ROBUSTNESS
Process 3: Design Failure Mode and Effects Analysis.

My DFMEA methodology is grounded in Ford's FMEA Handbook Version 4.2 with Robustness Linkages. An FMEA is not paperwork filled out after design freeze; it is a living engineering design tool.

We start with the Parameter Diagram—the P-Diagram. We define the Signal Input, such as a 40 N pull force on a door handle. We map the Control Factors: lever pivot ratio, return spring rate, and cable stiffness. Then we bombard the system with Noise Factors: piece-to-piece tolerance stacks, temperature swings from -40°C in Sweden to +85°C in Arizona, ice ingress, grease aging, and customer abuse.

In evaluating risk, the Ford philosophy is definitive: Never hide behind the mathematical RPN score. If Severity is 8, 9, or 10—loss of vehicle function, fire, or regulatory non-compliance—it is an unacceptable condition. You cannot multiply it by low occurrence and ignore it. You must engineer out the root cause.

We identify Critical Characteristics marked with the inverted delta (∇) for safety and Significant Characteristics for customer fit, cascading them directly into the PFMEA and manufacturing Control Plans.""")

    # =========================================================================
    # SLIDE 22: PROCESS 4 - 2D DETAILING & GD&T
    # =========================================================================
    s22 = prs.slides.add_slide(blank_layout)
    add_bg(s22)
    add_header(s22, "Process 4: 2D Detailing & GD&T Architecture", "ASME Y14.5 / ISO 1101, Datum Schemes & Volkswagen RPS System", slide_num=22)

    gdt_cards = [
        ("THE 3-2-1 LOCATING PRINCIPLE", [
            ("Datum Reference Frame (DRF)", "Constraining all 6 spatial degrees of freedom (3 translations Tx, Ty, Tz and 3 rotations Rx, Ry, Rz)."),
            ("Primary Datum A (3 Points)", "Establishes the fundamental spatial plane; eliminates pitch, roll, and perpendicular translation."),
            ("Secondary Datum B (2 Points)", "Establishes a perpendicular vector line; constrains yaw and in-plane translation."),
            ("Tertiary Datum C (1 Point)", "Provides the final perpendicular stop point; locks the remaining translational axis.")
        ]),
        ("VOLKSWAGEN RPS SYSTEM", [
            ("Referenzpunkt-System", "VW's standardized coordinate datum targeting system applied across MQB, MEB, and commercial vehicles."),
            ("RPS Surface Pads (RPS-F)", "Precision-milled local pads on stamped panels functioning as repeatable CMM and jig contact targets."),
            ("RPS 2-Way & 4-Way Holes", "Standardized round and slotted tooling holes (RPS-H) locating sub-assemblies in robotic welding bucks."),
            ("End-to-End Traceability", "The same RPS datums defined in CAD are machined into stamping dies, checking fixtures, and CMM inspection nests.")
        ]),
        ("GEOMETRIC CONTROLS IN BIW", [
            ("Profile of a Surface (|∩|)", "The universal geometric control for complex 3D stamped sheet metal and aesthetic Class-A panels."),
            ("True Position (⨁)", "Locating fastener clearance holes, suspension subframe attachment points, and hinge pins."),
            ("Maximum Material Condition (MMC)", "Utilizing bonus tolerances on clearance holes as hole size departs from minimum MMC boundary."),
            ("Inspection Verification", "Defining automated Coordinate Measuring Machine (CMM) and inline optical laser scanning inspection vectors.")
        ])
    ]
    for i, (gtitle, gitems) in enumerate(gdt_cards):
        gx = Inches(0.8) + i * Inches(3.98)
        card = s22.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, gx, Inches(1.75), Inches(3.8), Inches(5.2))
        card.fill.solid()
        card.fill.fore_color.rgb = C_CARD_BG
        card.line.color.rgb = C_CARD_BORDER
        cbar = s22.shapes.add_shape(MSO_SHAPE.RECTANGLE, gx, Inches(1.75), Inches(3.8), Inches(0.12))
        cbar.fill.solid()
        cbar.fill.fore_color.rgb = C_TEAL
        cbar.line.fill.background()

        ctf = card.text_frame
        ctf.word_wrap = True
        ctf.margin_left = ctf.margin_right = Inches(0.2)
        ctf.margin_top = Inches(0.25)
        cp1 = ctf.paragraphs[0]
        cp1.text = gtitle
        cp1.font.size = Pt(11)
        cp1.font.bold = True
        cp1.font.color.rgb = C_TEAL
        cp1.space_after = Pt(14)

        for heading, body in gitems:
            ph = ctf.add_paragraph()
            ph.text = heading
            ph.font.size = Pt(10)
            ph.font.bold = True
            ph.font.color.rgb = C_TEXT_DARK
            ph.space_after = Pt(2)
            pb = ctf.add_paragraph()
            pb.text = body
            pb.font.size = Pt(8.8)
            pb.font.color.rgb = RGBColor(71, 85, 105)
            pb.space_after = Pt(8)

    set_speaker_notes(s22, """[21:30 - 22:30] SLIDE 22: PROCESS 4: 2D DETAILING & GD&T
Process 4: 2D Detailing and Geometric Dimensioning and Tolerancing.

A 2D engineering drawing is a legal and technical contract. Ambiguous plus-or-minus tolerances lead to assembly line failures. We enforce ASME Y14.5 and ISO 1101 standards.

Everything begins with the Datum Reference Frame and the 3-2-1 locating principle: Primary Datum A (3 points) locks 3 degrees of freedom; Secondary Datum B (2 points) locks 2 degrees; Tertiary Datum C (1 point) locks the final translation.

At Volkswagen, this principle is perfected through the Referenzpunkt-System—the RPS system. On MQB and MEB architectures, every stamping features dedicated RPS points: RPS-H locating holes and RPS-F surface contact pads. The beauty of RPS is total continuity: The exact coordinate datums created by the CAD designer are machined directly into the stamping dies, clamped by robotic framing bucks in the assembly plant, and measured on CMM tables.

For sheet metal surfaces, Profile of a Surface (|∩|) is our universal control. For clearance holes, True Position with Maximum Material Condition provides bonus tolerance, preventing scrap while guaranteeing bolt pass-through.""")

    # =========================================================================
    # SLIDE 23: PROCESS 5 - TOLERANCE STUDIES & 3D VSA
    # =========================================================================
    s23 = prs.slides.add_slide(blank_layout)
    add_bg(s23)
    add_header(s23, "Process 5: 1D Tolerance Stacks & 3D Variation Analysis", "Worst-Case, Statistical RSS & Monte Carlo Variation Simulation (VSA)", slide_num=23)

    vsa_cards = [
        ("1D TOLERANCE METHODS", "Worst-Case vs. Statistical RSS", [
            ("Worst-Case Arithmetic", "Twc = Σ |ti|. Assumes all parts simultaneously reach extreme dimensional limits. Overly conservative for mass production."),
            ("Root Sum of Squares (RSS)", "Trss = √(Σ ti²). Gaussian statistical model assuming independent normal distributions; ideal for high-volume lines (>200k/yr)."),
            ("Bender's Factor Correction", "Applying 1.3-1.5x multiplier to RSS to account for mean tooling wear and process drift over multi-year production runs.")
        ], C_PRIMARY),
        ("3D MONTE CARLO VSA", "Multi-Body Kinematic Variation", [
            ("Kinematic Simulation", "Running 5,000-10,000 virtual vehicle builds in VisVSA / 3DCS, modeling 6-DOF part variation and assembly sequences."),
            ("Exterior Gap & Flush", "Predicting hood-to-fender (3.5 ± 0.8 mm), door-to-door (4.0 ± 0.7 mm), and headlamp-to-bumper fitment."),
            ("Pareto Contribution Analysis", "Identifying the 'vital few' variables driving >70% of variation to target tooling investment precisely where it matters.")
        ], C_TEAL),
        ("THERMAL EXPANSION DYNAMICS", "Multi-Material Environmental Modeling", [
            ("Thermal Range (ΔT)", "Modeling structural expansion across -40°C arctic soak to +85°C high-ambient desert solar loading."),
            ("Material Mismatch (ΔL)", "Calculating expansion differentials between aluminium closures (α ≈ 23x10⁻⁶/K), steel BIW (α ≈ 12x10⁻⁶/K), and composites."),
            ("Weatherstrip Load Retention", "Verifying door seal compression remains within 30-40% across thermal extremes to prevent water leaks and wind hiss.")
        ], C_ACCENT)
    ]
    for i, (vtitle, vsub, vitems, vcol) in enumerate(vsa_cards):
        vx = Inches(0.8) + i * Inches(3.98)
        card = s23.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, vx, Inches(1.75), Inches(3.8), Inches(5.2))
        card.fill.solid()
        card.fill.fore_color.rgb = C_CARD_BG
        card.line.color.rgb = C_CARD_BORDER
        cbar = s23.shapes.add_shape(MSO_SHAPE.RECTANGLE, vx, Inches(1.75), Inches(3.8), Inches(0.12))
        cbar.fill.solid()
        cbar.fill.fore_color.rgb = vcol
        cbar.line.fill.background()

        ctf = card.text_frame
        ctf.word_wrap = True
        ctf.margin_left = ctf.margin_right = Inches(0.2)
        ctf.margin_top = Inches(0.25)
        cp1 = ctf.paragraphs[0]
        cp1.text = vtitle
        cp1.font.size = Pt(11)
        cp1.font.bold = True
        cp1.font.color.rgb = vcol
        cp1.space_after = Pt(2)
        cp2 = ctf.add_paragraph()
        cp2.text = vsub
        cp2.font.size = Pt(8.5)
        cp2.font.bold = True
        cp2.font.color.rgb = C_TEXT_MUTED
        cp2.space_after = Pt(12)

        for heading, body in vitems:
            ph = ctf.add_paragraph()
            ph.text = heading
            ph.font.size = Pt(10)
            ph.font.bold = True
            ph.font.color.rgb = C_TEXT_DARK
            ph.space_after = Pt(2)
            pb = ctf.add_paragraph()
            pb.text = body
            pb.font.size = Pt(8.8)
            pb.font.color.rgb = RGBColor(71, 85, 105)
            pb.space_after = Pt(8)

    set_speaker_notes(s23, """[22:30 - 23:30] SLIDE 23: PROCESS 5: TOLERANCE STUDIES & 3D VSA
Process 5: Dimensional Engineering and Tolerance Studies.

Exterior gap and flush consistency—hood-to-fender, door-to-quarter—is the primary visual cue by which customers judge build quality.

We approach this in two stages: First, 1D linear stacks. Worst-case analysis assumes every part in the chain hits its extreme boundary concurrently. In mass production, that is statistically unrealistic and drives excessive cost. We use Root Sum of Squares (RSS) corrected with Bender's factor of 1.3 to 1.5 to account for tool wear and process shifts.

Second, for complex 3D closures, parts rotate, twist, and sag in 3D space. We use 3D Variation Simulation Analysis (VSA) with Monte Carlo engines, simulating 10,000 virtual vehicle builds capturing clamping sequences and robotic spot-weld thermal distortion. 

VSA delivers a Pareto sensitivity chart showing that out of 25 dimensional variables, 3 contributors cause 75% of the gap variation. We can then focus tooling capital strictly on tightening those three critical tools.

Finally, we model thermal expansion differentials between steel bodies, aluminium closures, and composite tailgates across -40°C to +85°C.""")

    # =========================================================================
    # SLIDE 24: PROCESS 6 - FEA: RIGIDITY & NVH
    # =========================================================================
    s24 = prs.slides.add_slide(blank_layout)
    add_bg(s24)
    add_header(s24, "Process 6: Finite Element Analysis (FEA) — Rigidity & NVH", "Torsional Stiffness, Dynamic Modal Frequencies & Durability Fatigue", slide_num=24)

    fea_cards = [
        ("STATIC RIGIDITY TARGETS", "Handling, Ride & Door Racking", [
            ("Torsional Rigidity (kNm/°)", "Targeting 18-28 kNm/° on ICE platforms; >30 kNm/° on MEB skateboard EV architectures."),
            ("Bending Stiffness (N/mm)", "Vertical rocker deflection control ensuring door latch alignment and preventing body sag under load."),
            ("Local Mount Stiffness", "Ensuring >10,000 N/mm at strut towers and subframe mounting nodes to deliver crisp steering feedback.")
        ], C_PRIMARY),
        ("DYNAMIC NVH & MODAL FREQUENCIES", "Acoustic Decoupling Strategy", [
            ("First Torsion Mode (>38-42 Hz)", "Decoupling BIW resonant torsion from engine 4-cylinder idle firing excitation (25-30 Hz at 750-900 RPM)."),
            ("First Bending Mode (>42-46 Hz)", "Decoupling vehicle body bending modes from suspension wheel-hop inputs (12-15 Hz)."),
            ("Acoustic Boom Prevention", "Preventing low-frequency cabin resonance that causes passenger ear pressure and fatigue.")
        ], C_TEAL),
        ("FATIGUE & DURABILITY LIFE", "Proving Ground Load Simulation", [
            ("Road Load Data (WFT)", "Multi-axis load time histories from Belgian cobblestones, pothole strikes, and curb impacts."),
            ("Miner's Rule Cumulative Damage", "Σ (ni / Ni) <= 1.0. Stress-life (S-N) and strain-life (ε-N) durability analysis across 150,000+ miles."),
            ("Spot-Weld & Adhesive Fatigue", "Evaluating nugget shear stresses; implementing continuous weld-bonding adhesive to cut stress peaks by 40%.")
        ], C_ACCENT)
    ]
    for i, (ftitle, fsub, fitems, fcol) in enumerate(fea_cards):
        fx = Inches(0.8) + i * Inches(3.98)
        card = s24.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, fx, Inches(1.75), Inches(3.8), Inches(5.2))
        card.fill.solid()
        card.fill.fore_color.rgb = C_CARD_BG
        card.line.color.rgb = C_CARD_BORDER
        cbar = s24.shapes.add_shape(MSO_SHAPE.RECTANGLE, fx, Inches(1.75), Inches(3.8), Inches(0.12))
        cbar.fill.solid()
        cbar.fill.fore_color.rgb = fcol
        cbar.line.fill.background()

        ctf = card.text_frame
        ctf.word_wrap = True
        ctf.margin_left = ctf.margin_right = Inches(0.2)
        ctf.margin_top = Inches(0.25)
        cp1 = ctf.paragraphs[0]
        cp1.text = ftitle
        cp1.font.size = Pt(11)
        cp1.font.bold = True
        cp1.font.color.rgb = fcol
        cp1.space_after = Pt(2)
        cp2 = ctf.add_paragraph()
        cp2.text = fsub
        cp2.font.size = Pt(8.5)
        cp2.font.bold = True
        cp2.font.color.rgb = C_TEXT_MUTED
        cp2.space_after = Pt(12)

        for heading, body in fitems:
            ph = ctf.add_paragraph()
            ph.text = heading
            ph.font.size = Pt(10)
            ph.font.bold = True
            ph.font.color.rgb = C_TEXT_DARK
            ph.space_after = Pt(2)
            pb = ctf.add_paragraph()
            pb.text = body
            pb.font.size = Pt(8.8)
            pb.font.color.rgb = RGBColor(71, 85, 105)
            pb.space_after = Pt(8)

    set_speaker_notes(s24, """[23:30 - 24:30] SLIDE 24: PROCESS 6: FEA RIGIDITY & NVH
Process 6: Finite Element Analysis for Structural Rigidity, NVH, and Durability.

Static torsional rigidity, measured in kNm per degree, dictates handling responsiveness and squeak-and-rattle resistance. On C-segment cars like Focus and Golf, we targeted 18,000 to 24,000 Nm/degree. On the MEB electric skateboard, the structural battery tray propelled rigidity past 30,000 Nm/degree.

In dynamic NVH, modal analysis decouples natural body frequencies from excitation sources. A 4-cylinder engine idling at 800 RPM fires at 27 Hertz; suspension wheel-hop occurs at 12 to 15 Hertz. If the body's natural bending or torsional frequency coincides with 27 Hertz, the passenger cabin resonates like a drum, creating acoustic boom. We engineer BIW structural rings to push first global modes safely above 38 to 42 Hertz.

In durability, we feed multi-axis wheel force transducer data from proving ground cobblestones into fatigue solvers, applying Miner's rule across spot welds and introducing structural adhesives to cut cyclic stress peaks by 40%.""")

    # =========================================================================
    # SLIDE 25: PROCESS 7 - CRASH & EV SAFETY
    # =========================================================================
    s25 = prs.slides.add_slide(blank_layout)
    add_bg(s25)
    add_header(s25, "Process 7: Structural Crashworthiness & EV Safety", "Non-Linear Explicit Crash (LS-DYNA), Boron Steel & Battery Integrity", slide_num=25)

    crash_cards = [
        ("FRONTAL IMPACT LOAD PATHS", "Euro NCAP 40% Offset & Full Width", [
            ("Three Decoupled Paths", "Upper shotgun rail (25% energy), main longitudinal rail (55%), lower subframe extension (20%)."),
            ("Progressive Rail Collapse", "Hexagonal high-strength steel crash boxes with stamped trigger indentations creating uniform accordion crush."),
            ("Engine Block Kinematics", "Directing ICE block downward beneath passenger floorpan to prevent firewall penetration.")
        ], C_PRIMARY),
        ("SIDE IMPACT & BORON SAFETY CELL", "Severe Pole & Barrier Collisions", [
            ("Ultra-High-Strength Boron (22MnB5)", "Hot-stamped at 900°C and quenched to martensitic microstructure with Rm > 1500 MPa."),
            ("Tailored Tempering B-Pillar", "1500 MPa martensite at upper B-pillar prevents head strike; 600-800 MPa ductile base creates controlled plastic hinge."),
            ("Boron Cross-Car Beams", "High-strength floor cross-members transferring side barrier impact across the underbody tunnel.")
        ], C_ROSE),
        ("MEB EV BATTERY PROTECTION", "The Skateboard Safety Architecture", [
            ("Multi-Cell Aluminium Sills", "Massive extruded rocker sections engineered to absorb side pole impact before battery module intrusion."),
            ("Structural Battery Housing", "Heavy aluminium baseplate and internal web frame acting as an impenetrable survival cell."),
            ("High-Voltage Pyrofuse Detonation", "Automatic pyrotechnic disconnect isolating 400V/800V battery pack within 2 milliseconds of impact.")
        ], C_TEAL)
    ]
    for i, (ctitle, csub, citems, ccol) in enumerate(crash_cards):
        cx = Inches(0.8) + i * Inches(3.98)
        card = s25.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, cx, Inches(1.75), Inches(3.8), Inches(5.2))
        card.fill.solid()
        card.fill.fore_color.rgb = C_CARD_BG
        card.line.color.rgb = C_CARD_BORDER
        cbar = s25.shapes.add_shape(MSO_SHAPE.RECTANGLE, cx, Inches(1.75), Inches(3.8), Inches(0.12))
        cbar.fill.solid()
        cbar.fill.fore_color.rgb = ccol
        cbar.line.fill.background()

        ctf = card.text_frame
        ctf.word_wrap = True
        ctf.margin_left = ctf.margin_right = Inches(0.2)
        ctf.margin_top = Inches(0.25)
        cp1 = ctf.paragraphs[0]
        cp1.text = ctitle
        cp1.font.size = Pt(11)
        cp1.font.bold = True
        cp1.font.color.rgb = ccol
        cp1.space_after = Pt(2)
        cp2 = ctf.add_paragraph()
        cp2.text = csub
        cp2.font.size = Pt(8.5)
        cp2.font.bold = True
        cp2.font.color.rgb = C_TEXT_MUTED
        cp2.space_after = Pt(12)

        for heading, body in citems:
            ph = ctf.add_paragraph()
            ph.text = heading
            ph.font.size = Pt(10)
            ph.font.bold = True
            ph.font.color.rgb = C_TEXT_DARK
            ph.space_after = Pt(2)
            pb = ctf.add_paragraph()
            pb.text = body
            pb.font.size = Pt(8.8)
            pb.font.color.rgb = RGBColor(71, 85, 105)
            pb.space_after = Pt(8)

    set_speaker_notes(s25, """[24:30 - 25:30] SLIDE 25: PROCESS 7: CRASHWORTHINESS & EV SAFETY
Process 7: Structural Crashworthiness and Non-Linear Crash Simulation.

Crash simulation using LS-DYNA solves 80 to 120 milliseconds of violent deformation in microsecond increments.

In a 64 km/h frontal offset crash, the front structure absorbs megajoules of energy via three load paths: upper shotgun rails (25%), main longitudinal crash rails with stamped trigger indentations (55% via progressive accordion crush), and lower subframe rails (20%).

In side impact, where crush space is less than 200 mm, we rely on hot-stamped boron steel—22MnB5. Heated to 900°C and quenched in water-cooled dies, tensile strength leaps past 1,500 MPa. We employ tailored tempering on B-pillars: 1,500 MPa martensite at the upper pillar to resist intrusion, and a ductile 600 MPa base to create a controlled plastic hinge.

On MEB electric skateboards, crashworthiness had to be reinvented. An EV is 400 to 500 kg heavier, increasing crash kinetic energy by 40%. In side-pole impacts, battery intrusion can trigger thermal runaway. We engineered multi-cell extruded aluminium side sills that crush progressively, absorbing impact before touching battery modules, while pyrofuses isolate 400-volt circuits in 2 milliseconds.""")

    # =========================================================================
    # SLIDE 26: PROCESS 8 - APQP & PRODUCTION LAUNCH
    # =========================================================================
    s26 = prs.slides.add_slide(blank_layout)
    add_bg(s26)
    add_header(s26, "Process 8: APQP & Production Launch Governance", "From Gateway Milestones (GPDS / PEP) to Flawless Job 1 / SOP Launch", slide_num=26)

    apqp_cards = [
        ("APQP 5-PHASE LIFECYCLE", "Systematic Quality Framework", [
            ("Phase 1: Concept & Planning", "Translating Voice of Customer into target vehicle specifications and initial BOM."),
            ("Phase 2: Product Design", "CAD release, DFM/DFA, DFMEA, GD&T drawings, and DVP&R virtual verification."),
            ("Phase 3: Process Design", "Stamping die cutting, injection mould build, PFMEA, Control Plans, and packaging."),
            ("Phase 4: Product/Process Validation", "Run-at-Rate pilot production, Measurement Systems Analysis (Gage R&R), PPAP approval."),
            ("Phase 5: Feedback & Launch", "SOP launch containment, warranty tracking, ongoing SPC, and lessons-learned closed loop.")
        ], C_PRIMARY),
        ("OEM GATEWAY SYNCHRONIZATION", "Ford GPDS vs. Volkswagen PEP", [
            ("Concept Freeze", "Ford Concept Approval (CA) ↔ VW Projektvereinbarung / Konzeptfreigabe."),
            ("Design Freeze (Point of No Return)", "Ford Final Data Judgement (FDJ) ↔ VW Datenkontrollmodell (DKM). Hard tooling released."),
            ("Tooling Tryout (TT)", "First parts stamped from production dies ↔ VW Vorserie (VFF). Dimensional checks."),
            ("Pilot Production (PP / PVS)", "Full assembly line validation at takt time ↔ VW Nullserie (PVS)."),
            ("Start of Production (SOP / MP1)", "Mass Production 1 / Job 1 commercial launch.")
        ], C_TEAL),
        ("PPAP 18 ELEMENTS & CAPABILITY", "The Legal Manufacturing Contract", [
            ("Measurement Systems (MSA)", "Gage R&R < 10% mandatory for Critical Characteristics; 10-30% conditionally acceptable."),
            ("Process Capability (Cpk)", "Mandated Cpk >= 1.67 (5-sigma quality) for Critical Characteristics (∇ CC); Cpk >= 1.33 for standard."),
            ("Dimensional Layout", "100% full balloon inspection report on initial production sample parts from production tools."),
            ("Part Submission Warrant (PSW)", "The formal signed executive declaration certifying production readiness at rate with zero defects.")
        ], C_ACCENT)
    ]
    for i, (atitle, asub, aitems, acol) in enumerate(apqp_cards):
        ax = Inches(0.8) + i * Inches(3.98)
        card = s26.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, ax, Inches(1.75), Inches(3.8), Inches(5.2))
        card.fill.solid()
        card.fill.fore_color.rgb = C_CARD_BG
        card.line.color.rgb = C_CARD_BORDER
        cbar = s26.shapes.add_shape(MSO_SHAPE.RECTANGLE, ax, Inches(1.75), Inches(3.8), Inches(0.12))
        cbar.fill.solid()
        cbar.fill.fore_color.rgb = acol
        cbar.line.fill.background()

        ctf = card.text_frame
        ctf.word_wrap = True
        ctf.margin_left = ctf.margin_right = Inches(0.2)
        ctf.margin_top = Inches(0.25)
        cp1 = ctf.paragraphs[0]
        cp1.text = atitle
        cp1.font.size = Pt(11)
        cp1.font.bold = True
        cp1.font.color.rgb = acol
        cp1.space_after = Pt(2)
        cp2 = ctf.add_paragraph()
        cp2.text = asub
        cp2.font.size = Pt(8.5)
        cp2.font.bold = True
        cp2.font.color.rgb = C_TEXT_MUTED
        cp2.space_after = Pt(12)

        for heading, body in aitems:
            ph = ctf.add_paragraph()
            ph.text = heading
            ph.font.size = Pt(10)
            ph.font.bold = True
            ph.font.color.rgb = C_TEXT_DARK
            ph.space_after = Pt(2)
            pb = ctf.add_paragraph()
            pb.text = body
            pb.font.size = Pt(8.8)
            pb.font.color.rgb = RGBColor(71, 85, 105)
            pb.space_after = Pt(8)

    set_speaker_notes(s26, """[25:30 - 26:30] SLIDE 26: PROCESS 8: APQP & LAUNCH GOVERNANCE
Process 8: Advanced Product Quality Planning and Production Launch Governance.

APQP is the bridge that turns digital models into profitable serial manufacturing.

We synchronize APQP across the five classic phases, aligning them with OEM gateway milestones. In Ford GPDS, the critical milestone is FDJ—Final Data Judgement; in Volkswagen PEP, it is DKM—Datenkontrollmodell. This is the design freeze. Once you pass this gateway, millions of pounds in hard tooling are released. If a design error slips past FDJ, fixing it in hardened tool steel during Tooling Tryout (TT) costs ten times more, and fixing it at Pilot Production costs a hundred times more.

In Phase 4, we enforce rigorous statistical controls. We conduct Measurement Systems Analysis—Gage R&R. If your measuring fixture or CMM has more than 10 percent measurement variation, you cannot trust your quality data. For all Critical Characteristics marked with the inverted delta, we mandate a process capability Cpk of at least 1.67—ensuring fewer than 0.6 defects per million parts produced.

The culmination of APQP is the Production Part Approval Process—PPAP, covering 18 stringent deliverables. As an engineering manager, signing the Part Submission Warrant (PSW) is your formal declaration that the components meet every drawing requirement, the DVP&R is complete, and the supplier can manufacture at full production rate.""")

    # =========================================================================
    # SLIDE 27: CASE STUDY 1 - FORD C170 FOCUS MULTI-LINK
    # =========================================================================
    s27 = prs.slides.add_slide(blank_layout)
    add_bg(s27)
    add_header(s27, "Technical Case Study 1: The Multi-Link Packaging Triumph of Ford C170 Focus", "Decoupled Longitudinal & Lateral Kinematics Delivering Handling Benchmarks & Maximum Boot Space", slide_num=27)

    c1_cards = [
        ("THE HISTORICAL CONUNDRUM", [
            ("Twist-Beam Compromise", "Compact C-segment cars universally used cheap twist-beam rear axles, compromising ride quality and lateral cornering stability."),
            ("The Multi-Link Barrier", "Traditional multi-link independent rear suspensions were considered too costly and intruded severely into boot luggage space."),
            ("The Ford Dynamic Challenge", "Ford leadership demanded class-leading vehicle dynamics ('fun-to-drive') without compromising family luggage utility.")
        ]),
        ("THE CONTROL BLADE PACKAGING SOLUTION", [
            ("Decoupled Kinematics", "Longitudinal trailing arm (the flat stamped 'Control Blade') decoupled from short lateral camber/toe links."),
            ("Braking & Harshness Compliance", "The thin vertical blade absorbed road longitudinal impact and braking torque while flexing laterally without binding."),
            ("Passive Rear-Wheel Steer", "Under lateral cornering forces, the elastomeric bushings induced passive toe-in, stabilizing the rear axle at speed."),
            ("Zero Boot Intrusion", "Packaged entire multi-link assembly within a compact subframe beneath the floor, preserving an immense square boot.")
        ]),
        ("ARCHITECTURAL & MARKET IMPACT", [
            ("Handling Leadership", "The C170 Focus swept global automotive awards, beating premium German saloons in ride and handling evaluations."),
            ("Class Benchmark for Two Decades", "The Control Blade architecture set the industry standard, copied by competitors across Europe and Asia."),
            ("Proof of Packaging Mastery", "Demonstrated that innovative geometric packaging delivers premium dynamics within high-volume cost constraints.")
        ])
    ]
    for i, (ctitle, citems) in enumerate(c1_cards):
        cx = Inches(0.8) + i * Inches(3.98)
        card = s27.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, cx, Inches(1.75), Inches(3.8), Inches(5.2))
        card.fill.solid()
        card.fill.fore_color.rgb = C_CARD_BG
        card.line.color.rgb = C_CARD_BORDER
        cbar = s27.shapes.add_shape(MSO_SHAPE.RECTANGLE, cx, Inches(1.75), Inches(3.8), Inches(0.12))
        cbar.fill.solid()
        cbar.fill.fore_color.rgb = C_PRIMARY
        cbar.line.fill.background()

        ctf = card.text_frame
        ctf.word_wrap = True
        ctf.margin_left = ctf.margin_right = Inches(0.2)
        ctf.margin_top = Inches(0.25)
        cp1 = ctf.paragraphs[0]
        cp1.text = ctitle
        cp1.font.size = Pt(11)
        cp1.font.bold = True
        cp1.font.color.rgb = C_PRIMARY
        cp1.space_after = Pt(14)

        for heading, body in citems:
            ph = ctf.add_paragraph()
            ph.text = heading
            ph.font.size = Pt(10)
            ph.font.bold = True
            ph.font.color.rgb = C_TEXT_DARK
            ph.space_after = Pt(2)
            pb = ctf.add_paragraph()
            pb.text = body
            pb.font.size = Pt(8.8)
            pb.font.color.rgb = RGBColor(71, 85, 105)
            pb.space_after = Pt(8)

    set_speaker_notes(s27, """[26:30 - 27:15] SLIDE 27: CASE STUDY 1: FORD C170 FOCUS
Let us examine our first technical case study: The Ford C170 Focus multi-link packaging triumph.

Before the Focus, compact family cars used twist-beam rear suspensions because multi-link setups consumed boot space and were deemed too expensive. 
Ford's team broke this paradigm with the Control Blade suspension. By separating the longitudinal trailing arm from the lateral links, the thin, stamped Control Blade absorbed braking torque and road harshness while flexing laterally. Short lateral links controlled wheel camber and toe independently.

Under cornering load, the elastomeric bushings induced passive toe-in, making the car feel agile yet rock-solid at high speeds. 
And because we packaged the entire system below the luggage floor within a compact subframe, boot volume was untouched. The C170 redefined compact car dynamics for twenty years.""")

    # =========================================================================
    # SLIDE 28: CASE STUDY 2 - FORD EUCD SAFETY HARMONIZATION
    # =========================================================================
    s28 = prs.slides.add_slide(blank_layout)
    add_bg(s28)
    add_header(s28, "Technical Case Study 2: Structural Safety Harmonization of Ford EUCD", "Uniting Ford Volume Assembly with Volvo Safety Cage Rigor Across Shared Platforms", slide_num=28)

    c2_cards = [
        ("THE MULTI-OEM CHALLENGE", [
            ("Three Distinct Brands", "Developing a single shared platform for Ford (Mondeo/S-MAX), Volvo (S80/V70/XC60), and Land Rover (Freelander 2)."),
            ("Conflicting Brand Philosophies", "Reconciling Volvo's unyielding passenger cell safety expectations with Ford's high-speed assembly line takt times."),
            ("Diverse Body Styles & Weights", "Accommodating saloons, estates, 7-seat MPVs, and all-wheel-drive SUVs across divergent curb weights.")
        ]),
        ("THE STRUCTURAL SOLUTION", [
            ("Multi-Tier Front Crash Rails", "Three decoupled front load paths absorbing energy at 64 km/h offset impacts while controlling deceleration pulses."),
            ("Deformable Crash Subframe", "Lower front subframe engineered to shear away and tilt the engine downward beneath the floor in severe impacts."),
            ("Hot-Stamped Boron Safety Cell", "Extensive hot-formed boron steel B-pillars and floor cross-members linking left and right rocker sills."),
            ("Pedestrian Impact Sub-Structure", "Optimized cowl and fender brackets absorbing pedestrian head impacts to achieve Euro NCAP compliance.")
        ]),
        ("MANUFACTURING & MARKET SUCCESS", [
            ("5-Star Euro NCAP Across All Lines", "Every derivative vehicle on EUCD achieved 5-star Euro NCAP ratings, setting new executive segment safety benchmarks."),
            (">60% Underbody Commonality", "Shared over 60% of structural underbody pressings, unlocking massive global tooling and purchasing economies."),
            ("Proof of Cross-OEM Synergy", "Demonstrated that divergent engineering cultures can unite to produce world-class architectures.")
        ])
    ]
    for i, (ctitle, citems) in enumerate(c2_cards):
        cx = Inches(0.8) + i * Inches(3.98)
        card = s28.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, cx, Inches(1.75), Inches(3.8), Inches(5.2))
        card.fill.solid()
        card.fill.fore_color.rgb = C_CARD_BG
        card.line.color.rgb = C_CARD_BORDER
        cbar = s28.shapes.add_shape(MSO_SHAPE.RECTANGLE, cx, Inches(1.75), Inches(3.8), Inches(0.12))
        cbar.fill.solid()
        cbar.fill.fore_color.rgb = C_TEAL
        cbar.line.fill.background()

        ctf = card.text_frame
        ctf.word_wrap = True
        ctf.margin_left = ctf.margin_right = Inches(0.2)
        ctf.margin_top = Inches(0.25)
        cp1 = ctf.paragraphs[0]
        cp1.text = ctitle
        cp1.font.size = Pt(11)
        cp1.font.bold = True
        cp1.font.color.rgb = C_TEAL
        cp1.space_after = Pt(14)

        for heading, body in citems:
            ph = ctf.add_paragraph()
            ph.text = heading
            ph.font.size = Pt(10)
            ph.font.bold = True
            ph.font.color.rgb = C_TEXT_DARK
            ph.space_after = Pt(2)
            pb = ctf.add_paragraph()
            pb.text = body
            pb.font.size = Pt(8.8)
            pb.font.color.rgb = RGBColor(71, 85, 105)
            pb.space_after = Pt(8)

    set_speaker_notes(s28, """[27:15 - 28:00] SLIDE 28: CASE STUDY 2: FORD EUCD SAFETY
Case Study 2 examines the structural harmonization of the EUCD platform.

Joint multi-brand platforms often fail because divergent brand priorities create gridlock. On EUCD, Ford, Volvo, and Land Rover shared the architecture. Volvo demanded extreme safety cage survivability; Ford required high-speed stamping and assembly efficiency for Mondeo and S-MAX; Land Rover needed off-road ground clearance for Freelander 2.

We harmonized these demands by engineering a three-tier front crash load path with a deformable subframe that sheared downward in high-speed crashes, directing engine mass under the passenger cell. We utilized hot-stamped boron steel across all B-pillars and floor cross-members. 

The result was five-star Euro NCAP ratings across every single model, while sharing more than 60 percent of underbody structural stampings across three global brands.""")

    # =========================================================================
    # SLIDE 29: CASE STUDY 3 - MQB ICE VS MEB EV SKATEBOARD
    # =========================================================================
    s29 = prs.slides.add_slide(blank_layout)
    add_bg(s29)
    add_header(s29, "Technical Case Study 3: The Skateboard Revolution — MQB ICE vs. MEB EV", "Architectural Deconstruction: Internal Combustion Cradle vs. Structural Battery Skateboard", slide_num=29)

    comp_mqb_meb = [
        ("CRASH ENERGY MANAGEMENT", 
         "Conventional ICE Architecture (MQB-37)", "Heavy engine block acts as rigid mass in frontal crash; front rails fold around engine while directing it downward beneath passenger floorpan.",
         "Dedicated EV Skateboard (MEB Platform)", "No rigid engine block allows longer progressive front rail crush; but high-voltage battery demands zero side-pole intrusion via extruded aluminium sills."),
        ("TORSIONAL RIGIDITY CONTRIBUTION", 
         "Conventional ICE Architecture (MQB-37)", "Rigidity achieved via central floor exhaust tunnel, boxed rocker sills, and rear parcel shelf structure (typical: 20,000 - 24,000 Nm/°).",
         "Dedicated EV Skateboard (MEB Platform)", "Aluminium battery housing acts as massive underbody structural shear plate, increasing torsional rigidity past 30,000 Nm/° (+25% over ICE)."),
        ("CABIN SPACE & PACKAGING", 
         "Conventional ICE Architecture (MQB-37)", "High dash cowl and central floor tunnel dividing passenger footwells; engine and cooling pack dictate front axle position.",
         "Dedicated EV Skateboard (MEB Platform)", "Completely flat cabin floor with zero exhaust tunnel; HVAC relocated forward into bulkhead; D-segment interior space in C-segment footprint.")
    ]
    for i, (dim, m_title, m_desc, e_title, e_desc) in enumerate(comp_mqb_meb):
        cy = Inches(1.75) + i * Inches(1.7)
        card = s29.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), cy, Inches(11.733), Inches(1.52))
        card.fill.solid()
        card.fill.fore_color.rgb = C_CARD_BG
        card.line.color.rgb = C_CARD_BORDER

        hpill = s29.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.8), cy, Inches(2.8), Inches(1.52))
        hpill.fill.solid()
        hpill.fill.fore_color.rgb = C_NAVY_BAR
        hpill.line.fill.background()
        htf = hpill.text_frame
        htf.word_wrap = True
        htf.margin_left = htf.margin_right = Inches(0.15)
        htf.margin_top = Inches(0.4)
        hp = htf.paragraphs[0]
        hp.text = dim
        hp.font.size = Pt(11)
        hp.font.bold = True
        hp.font.color.rgb = C_TEXT_LIGHT

        fbox = s29.shapes.add_textbox(Inches(3.8), cy + Inches(0.1), Inches(4.3), Inches(1.3))
        ftf = fbox.text_frame
        ftf.word_wrap = True
        ftf.margin_left = ftf.margin_right = ftf.margin_top = ftf.margin_bottom = 0
        fp1 = ftf.paragraphs[0]
        fp1.text = m_title.upper()
        fp1.font.size = Pt(9.5)
        fp1.font.bold = True
        fp1.font.color.rgb = C_PRIMARY
        fp1.space_after = Pt(2)
        fp2 = ftf.add_paragraph()
        fp2.text = m_desc
        fp2.font.size = Pt(8.8)
        fp2.font.color.rgb = RGBColor(71, 85, 105)

        vbox = s29.shapes.add_textbox(Inches(8.3), cy + Inches(0.1), Inches(4.1), Inches(1.3))
        vtf = vbox.text_frame
        vtf.word_wrap = True
        vtf.margin_left = vtf.margin_right = vtf.margin_top = vtf.margin_bottom = 0
        vp1 = vtf.paragraphs[0]
        vp1.text = e_title.upper()
        vp1.font.size = Pt(9.5)
        vp1.font.bold = True
        vp1.font.color.rgb = C_TEAL
        vp1.space_after = Pt(2)
        vp2 = vtf.add_paragraph()
        vp2.text = e_desc
        vp2.font.size = Pt(8.8)
        vp2.font.color.rgb = RGBColor(71, 85, 105)

    set_speaker_notes(s29, """[28:00 - 28:45] SLIDE 29: CASE STUDY 3: MQB ICE VS MEB EV
Case Study 3 deconstructs the profound paradigm shift between MQB and MEB.

On MQB, frontal crash energy management revolves around the engine block: the rails must accordion-crush while pushing the heavy cast engine downward beneath the floorpan. On MEB, with no engine in the front, the crash rails have a longer uninterrupted crumple zone, but they must absorb 40% higher kinetic energy due to the 500 kg battery pack.

In side impact, MQB relies on B-pillar deflection and floor cross-members. On MEB, deforming the battery pack risks thermal runaway. We engineered multi-cell aluminium side sill extrusions that arrest pole intrusion before touching battery modules.

Finally, in structural rigidity, MQB achieves 20,000 to 24,000 Nm/degree using a central tunnel. On MEB, the battery housing acts as an active underbody shear plate, propelling torsional rigidity past 30,000 Nm/degree.""")

    # =========================================================================
    # SLIDE 30: ENGINEERING MANAGEMENT & CAPITAL ASSETS
    # =========================================================================
    s30 = prs.slides.add_slide(blank_layout)
    add_bg(s30)
    add_header(s30, "Engineering Leadership & Capital Asset Governance", "Multi-Million Tooling Commitments, Point of No Return & Team Capability", slide_num=30)

    mgmt_cards = [
        ("TOOLING ASSET GOVERNANCE", [
            ("Managing 'Point of No Return'", "Rigorous technical reviews prior to Tooling Kick-Off (FDJ/DKM) preventing catastrophic late tooling rework."),
            ("High-Stakes Stamping Dies", "A single transfer die set for a side aperture outer costs $4M-$6M; requires zero tolerance for geometric errors."),
            ("Supplier Run-at-Rate Audits", "Leading on-site audits at supplier press shops to verify cycle takt time and dimensional stability.")
        ], C_PRIMARY),
        ("PEOPLE & TEAM LEADERSHIP", [
            ("Cross-Functional Harmony", "Uniting styling designers, body engineers, CAE simulation specialists, and assembly plant directors."),
            ("Mentoring Future Leaders", "Transforming junior CAD operators into holistic systems engineers who understand cost, tooling, and physics."),
            ("Codifying Lessons Learned", "Ensuring manufacturing launch defects and warranty feedback are written into future platform design guidelines.")
        ], C_TEAL),
        ("STRATEGIC PLATFORM SCALABILITY", [
            ("Cross-Brand Architecture", "Leveraging modular toolkits to maximize commonality across volume, commercial, and premium brands."),
            ("Bridging CAD to Serial SOP", "Maintaining relentless technical rigor from initial 3D sketch all the way to legal PSW signature."),
            ("Embracing Digital Disruption", "Leading engineering organizations into the future of electrified skateboards and generative AI CAE.")
        ], C_ACCENT)
    ]
    for i, (mtitle, mitems, mcol) in enumerate(mgmt_cards):
        mx = Inches(0.8) + i * Inches(3.98)
        card = s30.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, mx, Inches(1.75), Inches(3.8), Inches(5.2))
        card.fill.solid()
        card.fill.fore_color.rgb = C_CARD_BG
        card.line.color.rgb = C_CARD_BORDER
        cbar = s30.shapes.add_shape(MSO_SHAPE.RECTANGLE, mx, Inches(1.75), Inches(3.8), Inches(0.12))
        cbar.fill.solid()
        cbar.fill.fore_color.rgb = mcol
        cbar.line.fill.background()

        ctf = card.text_frame
        ctf.word_wrap = True
        ctf.margin_left = ctf.margin_right = Inches(0.2)
        ctf.margin_top = Inches(0.25)
        cp1 = ctf.paragraphs[0]
        cp1.text = mtitle
        cp1.font.size = Pt(11)
        cp1.font.bold = True
        cp1.font.color.rgb = mcol
        cp1.space_after = Pt(14)

        for heading, body in mitems:
            ph = ctf.add_paragraph()
            ph.text = heading
            ph.font.size = Pt(10)
            ph.font.bold = True
            ph.font.color.rgb = C_TEXT_DARK
            ph.space_after = Pt(2)
            pb = ctf.add_paragraph()
            pb.text = body
            pb.font.size = Pt(8.8)
            pb.font.color.rgb = RGBColor(71, 85, 105)
            pb.space_after = Pt(8)

    set_speaker_notes(s30, """[28:45 - 29:15] SLIDE 30: ENGINEERING MANAGEMENT & CAPITAL
As an Engineering Manager, your output shifts from CAD surfaces to capital governance and organizational capability.

Consider the financial weight of tooling capital: A single transfer stamping die set for a bodyside aperture outer costs between four and six million pounds. If an engineering manager approves tooling kick-off before CAD models, DFM simulations, and tolerance stackups are verified, that capital is placed at grave risk. Managing the Point of No Return requires uncompromising technical integrity.

Equally vital is cultivating people. The best engineering teams are those where designers understand press line limits, where project engineers know how to interrogate an FEA mesh, and where every engineer takes personal pride in zero-defect quality.""")

    # =========================================================================
    # SLIDE 31: CORE TAKEAWAYS & SYNTHESIS
    # =========================================================================
    s31 = prs.slides.add_slide(blank_layout)
    add_bg(s31)
    add_header(s31, "Core Takeaways: Four Tenets of World-Class Automotive Engineering", "Synthesis of 25+ Years Across 12 Landmark Programs & 8 Core Disciplines", slide_num=31)

    takeaways = [
        ("1. MASTER THE MICRO TO DELIVER THE MACRO", 
         "Vehicle platform success is decided at the micrometer level. Datum schemes (GD&T / RPS), punch bend radii, and 1D/3D tolerance stackups dictate whether a multi-billion-pound architecture launches smoothly or suffers costly factory rework.", C_PRIMARY),
        ("2. UPSTREAM PREVENTION BEATS DOWNSTREAM CRISIS", 
         "Robust DFMEAs, Parameter Diagrams, and early DFM/DFA eliminate failures at the CAD cursor. Catching an error in virtual CAD costs 1x; fixing it in hard tooling costs 10x; fixing it at pilot production costs 100x.", C_TEAL),
        ("3. MODULAR SCALABILITY DEFINES OEM SURVIVAL", 
         "The evolution from dedicated platforms (C170) to modular matrix ecosystems (MQB) and dedicated electric skateboards (MEB) proves the power of standardizing hidden manufacturing interfaces while preserving brand distinctiveness.", C_ACCENT),
        ("4. AUTHENTIC LEADERSHIP IS GROUNDED IN FIRST PRINCIPLES", 
         "The most effective engineering leaders are those who have personally held the CAD pencil, calculated tolerance stacks, chaired DFMEA reviews, and signed off on crash test sleds. Technical empathy drives organizational excellence.", C_INDIGO)
    ]
    for i, (ttitle, tdesc, tcol) in enumerate(takeaways):
        ty = Inches(1.75) + i * Inches(1.3)
        card = s31.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), ty, Inches(11.733), Inches(1.18))
        card.fill.solid()
        card.fill.fore_color.rgb = C_CARD_BG
        card.line.color.rgb = C_CARD_BORDER
        lbar = s31.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.8), ty, Inches(0.12), Inches(1.18))
        lbar.fill.solid()
        lbar.fill.fore_color.rgb = tcol
        lbar.line.fill.background()

        ttf = card.text_frame
        ttf.word_wrap = True
        ttf.margin_left = Inches(0.3)
        ttf.margin_top = Inches(0.18)
        ttf.margin_right = Inches(0.25)
        tp1 = ttf.paragraphs[0]
        tp1.text = ttitle
        tp1.font.size = Pt(11.5)
        tp1.font.bold = True
        tp1.font.color.rgb = tcol
        tp1.space_after = Pt(2)
        tp2 = ttf.add_paragraph()
        tp2.text = tdesc
        tp2.font.size = Pt(9.5)
        tp2.font.color.rgb = RGBColor(51, 65, 85)

    set_speaker_notes(s31, """[29:15 - 29:45] SLIDE 31: CORE TAKEAWAYS
To conclude our journey, I leave you with four core tenets:

First: Master the micro to deliver the macro. A two-millimetre mismatch on a body opening will shut down an assembly plant producing 1,000 cars a day. 
Second: Upstream prevention beats downstream crisis. Every hour invested in a thorough P-Diagram and DFMEA saves fifty hours of late redesign. The 1-10-100 rule is absolute.
Third: Modular scalability defines OEM survival. Standardizing hidden manufacturing interfaces is the secret to platform profitability.
And fourth: Authentic leadership is grounded in technical first principles. Credibility stems from having sat in the CAD chair, calculated the tolerance stacks, reviewed the crash pulses, and verified the APQP control plans yourself.""")

    # =========================================================================
    # SLIDE 32: CONCLUSION & TECHNICAL Q&A (Dark Obsidian)
    # =========================================================================
    s32 = prs.slides.add_slide(blank_layout)
    add_bg(s32, dark=True)

    tbox32 = s32.shapes.add_textbox(Inches(1.2), Inches(1.2), Inches(11.0), Inches(2.2))
    tf32 = tbox32.text_frame
    tf32.word_wrap = True
    p0 = tf32.paragraphs[0]
    p0.text = "COLLABORATIVE EXCHANGE & DISCUSSION"
    p0.font.size = Pt(12)
    p0.font.bold = True
    p0.font.color.rgb = C_ACCENT
    p0.space_after = Pt(8)
    p1 = tf32.add_paragraph()
    p1.text = "Questions & Technical Discussion"
    p1.font.size = Pt(36)
    p1.font.bold = True
    p1.font.color.rgb = C_TEXT_LIGHT
    p1.space_after = Pt(10)
    p2 = tf32.add_paragraph()
    p2.text = "Deep-dive exploration of vehicle architectures, process execution, and engineering leadership."
    p2.font.size = Pt(15)
    p2.font.color.rgb = RGBColor(148, 163, 184)

    prompts = [
        ("CRASH & EV INTEGRATION", "Transitioning structural crash teams from traditional ICE front rails to high-voltage MEB skateboard battery protection."),
        ("DIMENSIONAL QUALITY", "Overcoming real-world challenges when migrating from 1D tolerance stacks to 3D Monte Carlo variation simulation (VSA)."),
        ("APQP & GATEWAY SPEED", "Accelerating automotive development timing without compromising Cpk >= 1.67 capability and PSW sign-off.")
    ]
    card32_w = Inches(3.6)
    gap32 = Inches(0.35)
    for i, (ptitle, ptext) in enumerate(prompts):
        px = Inches(1.2) + i * (card32_w + gap32)
        pcard = s32.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, px, Inches(3.8), card32_w, Inches(2.5))
        pcard.fill.solid()
        pcard.fill.fore_color.rgb = C_DARK_CARD
        pcard.line.color.rgb = RGBColor(30, 58, 102)

        ptf = pcard.text_frame
        ptf.word_wrap = True
        ptf.margin_left = ptf.margin_right = Inches(0.25)
        ptf.margin_top = Inches(0.25)
        pp1 = ptf.paragraphs[0]
        pp1.text = "DISCUSSION TOPIC " + str(i+1)
        pp1.font.size = Pt(9.5)
        pp1.font.bold = True
        pp1.font.color.rgb = C_ACCENT
        pp1.space_after = Pt(4)
        pp2 = ptf.add_paragraph()
        pp2.text = ptitle
        pp2.font.size = Pt(12)
        pp2.font.bold = True
        pp2.font.color.rgb = C_TEXT_LIGHT
        pp2.space_after = Pt(10)
        pp3 = ptf.add_paragraph()
        pp3.text = ptext
        pp3.font.size = Pt(9.5)
        pp3.font.color.rgb = RGBColor(203, 213, 225)

    set_speaker_notes(s32, """[29:45 - 30:00+] SLIDE 32: CONCLUSION & OPEN DISCUSSION
Thank you very much for your time and engagement. 

We now open the floor for technical questions and discussion across any of the twelve vehicle platforms, the CAD evolution, the Design-to-Manufacture flowchart, or the eight core engineering disciplines.

Thank you.""")

    clean_path = r"C:\tmp\00-Mycat\Engineering\Automotive_Engineering_32Slides_Clean.pptx"
    prs.save(clean_path)
    print(f"Successfully generated clean 32-slide presentation (no pictures): {clean_path}")

    # Also try to update other paths if unlocked
    for alt_path in [
        r"C:\tmp\00-Mycat\Engineering\Automotive_Engineering_Master_Presentation_32Slides.pptx",
        r"C:\tmp\00-Mycat\Engineering\Automotive_Engineering_30Min_Master_Presentation.pptx"
    ]:
        try:
            prs.save(alt_path)
            print(f"Also updated: {alt_path}")
        except PermissionError:
            print(f"Note: {alt_path} is currently locked by PowerPoint; skipping.")

if __name__ == "__main__":
    build_expanded_32_slide_presentation()
