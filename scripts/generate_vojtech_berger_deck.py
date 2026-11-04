import sys
from pathlib import Path
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE

def build_pptx_deck(output_pptx_path):
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5) # 16:9 widescreen layout
    blank_layout = prs.slide_layouts[6]

    # Executive Palette: Aluminium Packaging + Football
    C_BG_DARK = RGBColor(11, 19, 43)        # Deep Aluminium Navy / Obsidian
    C_BG_LIGHT = RGBColor(248, 250, 252)    # Slate 50
    C_CARD_BG = RGBColor(255, 255, 255)     # Pure White
    C_CARD_BORDER = RGBColor(226, 232, 240) # Slate 200
    C_DARK_CARD = RGBColor(20, 32, 60)      # Navy 850
    C_PRIMARY = RGBColor(2, 132, 199)       # Sky / Steel Blue
    C_PRIMARY_LIGHT = RGBColor(56, 189, 248)# Bright Sky
    C_STEEL = RGBColor(71, 85, 105)         # Metallic Steel Slate
    C_EMERALD = RGBColor(16, 185, 129)      # Football Pitch Emerald
    C_GREEN_DARK = RGBColor(5, 150, 105)    # Deep Green
    C_GOLD = RGBColor(245, 158, 11)         # Referee Gold / Warning
    C_ROSE = RGBColor(225, 29, 72)          # Disciplinary Red / Defect
    C_TEXT_DARK = RGBColor(15, 23, 42)      # Slate 900
    C_TEXT_MUTED = RGBColor(100, 116, 139)  # Slate 500
    C_TEXT_LIGHT = RGBColor(241, 245, 249)  # Slate 100

    def add_bg(slide, dark=False):
        bg = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(7.5))
        bg.fill.solid()
        bg.fill.fore_color.rgb = C_BG_DARK if dark else C_BG_LIGHT
        bg.line.fill.background()
        return bg

    def add_header(slide, title_text, category_text, dark=False, slide_num=None, total_slides=19):
        # Category Pill
        cat_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.35), Inches(9.5), Inches(0.32))
        tf_cat = cat_box.text_frame
        tf_cat.word_wrap = True
        tf_cat.margin_left = tf_cat.margin_right = tf_cat.margin_top = tf_cat.margin_bottom = 0
        p_cat = tf_cat.paragraphs[0]
        p_cat.text = category_text.upper()
        p_cat.font.size = Pt(10)
        p_cat.font.bold = True
        p_cat.font.color.rgb = C_EMERALD if dark else C_PRIMARY

        # Slide Number Badge
        if slide_num:
            num_box = slide.shapes.add_textbox(Inches(10.5), Inches(0.35), Inches(2.0), Inches(0.32))
            tf_num = num_box.text_frame
            tf_num.margin_left = tf_num.margin_right = tf_num.margin_top = tf_num.margin_bottom = 0
            pn = tf_num.paragraphs[0]
            pn.alignment = PP_ALIGN.RIGHT
            pn.text = f"{slide_num:02d} / {total_slides:02d}"
            pn.font.size = Pt(10)
            pn.font.bold = True
            pn.font.color.rgb = RGBColor(148, 163, 184)

        # Title
        title_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.68), Inches(11.7), Inches(0.65))
        tf_title = title_box.text_frame
        tf_title.word_wrap = True
        tf_title.margin_left = tf_title.margin_right = tf_title.margin_top = tf_title.margin_bottom = 0
        p_title = tf_title.paragraphs[0]
        p_title.text = title_text
        p_title.font.size = Pt(20)
        p_title.font.bold = True
        p_title.font.color.rgb = C_TEXT_LIGHT if dark else C_TEXT_DARK

        # Accent Bar
        line = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.8), Inches(1.38), Inches(11.733), Inches(0.02))
        line.fill.solid()
        line.fill.fore_color.rgb = RGBColor(51, 65, 85) if dark else RGBColor(226, 232, 240)
        line.line.fill.background()

    def add_card(slide, left, top, width, height, bg_color=C_CARD_BG, border_color=C_CARD_BORDER):
        card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
        card.fill.solid()
        card.fill.fore_color.rgb = bg_color
        if border_color:
            card.line.color.rgb = border_color
            card.line.width = Pt(1)
        else:
            card.line.fill.background()
        return card

    # ==========================================
    # SLIDE 1: Title Slide (Dark)
    # ==========================================
    s1 = prs.slides.add_slide(blank_layout)
    add_bg(s1, dark=True)

    # Accent top border
    bar = s1.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(0.12))
    bar.fill.solid()
    bar.fill.fore_color.rgb = C_EMERALD
    bar.line.fill.background()

    # Category Pill
    pill = add_card(s1, Inches(0.9), Inches(1.0), Inches(5.8), Inches(0.42), bg_color=RGBColor(16, 40, 70), border_color=C_PRIMARY_LIGHT)
    tf_pill = pill.text_frame
    tf_pill.vertical_anchor = MSO_ANCHOR.MIDDLE
    p = tf_pill.paragraphs[0]
    p.text = "AL INVEST BŘIDLIČNÁ • DIVIZE OBALY • QUALITY ENGINEERING"
    p.font.size = Pt(10)
    p.font.bold = True
    p.font.color.rgb = C_PRIMARY_LIGHT
    p.alignment = PP_ALIGN.CENTER

    # Main Title
    tb_title = s1.shapes.add_textbox(Inches(0.9), Inches(1.65), Inches(11.5), Inches(1.6))
    tf_t = tb_title.text_frame
    tf_t.word_wrap = True
    p1 = tf_t.paragraphs[0]
    p1.text = "Technical English & Grammar Diagnostic Deck"
    p1.font.size = Pt(36)
    p1.font.bold = True
    p1.font.color.rgb = RGBColor(255, 255, 255)

    p2 = tf_t.add_paragraph()
    p2.text = "Aluminium Food Packaging Quality Engineering & World Sports (Football Analytics)"
    p2.font.size = Pt(20)
    p2.font.color.rgb = C_PRIMARY_LIGHT
    p2.space_before = Pt(10)

    # Info Cards in Grid
    card1 = add_card(s1, Inches(0.9), Inches(3.6), Inches(3.65), Inches(2.8), bg_color=C_DARK_CARD, border_color=RGBColor(30, 58, 95))
    tf1 = card1.text_frame
    tf1.margin_left = tf1.margin_right = tf1.margin_top = tf1.margin_bottom = Inches(0.25)
    p = tf1.paragraphs[0]
    p.text = "👤 ASSESSED PROFESSIONAL"
    p.font.size = Pt(11)
    p.font.bold = True
    p.font.color.rgb = C_EMERALD
    p = tf1.add_paragraph()
    p.text = "Vojtěch Berger"
    p.font.size = Pt(18)
    p.font.bold = True
    p.font.color.rgb = C_TEXT_LIGHT
    p.space_before = Pt(8)
    p = tf1.add_paragraph()
    p.text = "Specialista kvality – divize Obaly\nQuality Engineer – Packaging Division\nAL INVEST Břidličná, a.s.\nVojtech.Berger@alinvest.cz"
    p.font.size = Pt(11)
    p.font.color.rgb = RGBColor(203, 213, 225)
    p.space_before = Pt(8)

    card2 = add_card(s1, Inches(4.85), Inches(3.6), Inches(3.65), Inches(2.8), bg_color=C_DARK_CARD, border_color=RGBColor(30, 58, 95))
    tf2 = card2.text_frame
    tf2.margin_left = tf2.margin_right = tf2.margin_top = tf2.margin_bottom = Inches(0.25)
    p = tf2.paragraphs[0]
    p.text = "🏭 TECHNICAL CORE"
    p.font.size = Pt(11)
    p.font.bold = True
    p.font.color.rgb = C_PRIMARY_LIGHT
    p = tf2.add_paragraph()
    p.text = "Alu Packaging & Food Safety"
    p.font.size = Pt(16)
    p.font.bold = True
    p.font.color.rgb = C_TEXT_LIGHT
    p.space_before = Pt(8)
    p = tf2.add_paragraph()
    p.text = "• Foil rolling & gauge tolerances\n• Pinholes, surface tension & dyne\n• Heat-seal integrity & lamination\n• BRCGS, FSSC 22000 & 8D reports\n• Customer claims & CAPA"
    p.font.size = Pt(11)
    p.font.color.rgb = RGBColor(203, 213, 225)
    p.space_before = Pt(8)

    card3 = add_card(s1, Inches(8.8), Inches(3.6), Inches(3.65), Inches(2.8), bg_color=C_DARK_CARD, border_color=RGBColor(30, 58, 95))
    tf3 = card3.text_frame
    tf3.margin_left = tf3.margin_right = tf3.margin_top = tf3.margin_bottom = Inches(0.25)
    p = tf3.paragraphs[0]
    p.text = "⚽ SPECIALIZED PASSION"
    p.font.size = Pt(11)
    p.font.bold = True
    p.font.color.rgb = C_GOLD
    p = tf3.add_paragraph()
    p.text = "World Sports & Football"
    p.font.size = Pt(16)
    p.font.bold = True
    p.font.color.rgb = C_TEXT_LIGHT
    p.space_before = Pt(8)
    p = tf3.add_paragraph()
    p.text = "• Tactical pressing & low blocks\n• Champions League & Premier League\n• VAR & semi-automated offside\n• Transfer analytics & squad depth\n• High-stakes post-match debate"
    p.font.size = Pt(11)
    p.font.color.rgb = RGBColor(203, 213, 225)
    p.space_before = Pt(8)

    # Footer note
    tb_foot = s1.shapes.add_textbox(Inches(0.9), Inches(6.8), Inches(11.5), Inches(0.4))
    tf_f = tb_foot.text_frame
    p = tf_f.paragraphs[0]
    p.text = "Instructor: Lee Routledge | Bespoke Corporate Language Architecture & Technical Diagnostics"
    p.font.size = Pt(10)
    p.font.color.rgb = RGBColor(148, 163, 184)

    # ==========================================
    # SLIDE 2: Agenda (50/50 Dual-Domain Framework)
    # ==========================================
    s2 = prs.slides.add_slide(blank_layout)
    add_bg(s2, dark=False)
    add_header(s2, "Session Roadmap: The 50/50 Executive Framework", "Diagnostic & Assessment Strategy", slide_num=2)

    c1 = add_card(s2, Inches(0.8), Inches(1.7), Inches(5.65), Inches(5.1), bg_color=C_CARD_BG)
    tf1 = c1.text_frame
    tf1.margin_left = tf1.margin_right = tf1.margin_top = tf1.margin_bottom = Inches(0.3)
    p = tf1.paragraphs[0]
    p.text = "PART 1: SPOKEN AUDIT & RAPPORT (30 MIN)"
    p.font.size = Pt(12)
    p.font.bold = True
    p.font.color.rgb = C_PRIMARY

    items_p1 = [
        ("00–05m: Introduction & Professional Context", "Establishing baseline fluency, greeting protocol, and professional scope at AL INVEST Břidličná."),
        ("05–15m: Packaging Operations & Quality Assurance", "Walking through foil converting lines, gauge checking, pinhole scanning, and BRCGS food safety compliance."),
        ("15–25m: Football Passions & Strategic Debate", "Discussing favored football clubs, European tournaments, tactical systems, and the impact of VAR technology."),
        ("25–30m: High-Stakes Dilemma Exploration", "Spontaneous resolution of an urgent customer complaint vs a refereeing controversy under pressure.")
    ]
    for title, desc in items_p1:
        p = tf1.add_paragraph()
        p.text = title
        p.font.size = Pt(12)
        p.font.bold = True
        p.font.color.rgb = C_TEXT_DARK
        p.space_before = Pt(10)
        p = tf1.add_paragraph()
        p.text = desc
        p.font.size = Pt(10.5)
        p.font.color.rgb = C_TEXT_MUTED

    c2 = add_card(s2, Inches(6.85), Inches(1.7), Inches(5.65), Inches(5.1), bg_color=C_CARD_BG)
    tf2 = c2.text_frame
    tf2.margin_left = tf2.margin_right = tf2.margin_top = tf2.margin_bottom = Inches(0.3)
    p = tf2.paragraphs[0]
    p.text = "PART 2: DIAGNOSTIC & APPLIED GRAMMAR (30 MIN)"
    p.font.size = Pt(12)
    p.font.bold = True
    p.font.color.rgb = C_GREEN_DARK

    items_p2 = [
        ("30–45m: The 18-Point Diagnostic Screening", "Targeted sentences blending aluminium packaging quality with football match analysis to pinpoint grammatical accuracy."),
        ("45–52m: Top 6 'Czenglish' Traps Screening", "Immediate error-spotting covering control vs inspect, reklamace vs complaint, since/for, and conditional 'will' errors."),
        ("52–56m: High-Impact Deep Dives", "Rapid drills on Passive Voice in 8D reports and Conditionals in quality tolerances and tactical formations."),
        ("56–60m: Strength Profile & Personalized Syllabus", "Synthesizing observed linguistic strengths and setting a clear roadmap for subsequent sessions.")
    ]
    for title, desc in items_p2:
        p = tf2.add_paragraph()
        p.text = title
        p.font.size = Pt(12)
        p.font.bold = True
        p.font.color.rgb = C_TEXT_DARK
        p.space_before = Pt(10)
        p = tf2.add_paragraph()
        p.text = desc
        p.font.size = Pt(10.5)
        p.font.color.rgb = C_TEXT_MUTED

    # ==========================================
    # SLIDE 3: Spoken Audit 1 - Packaging Quality
    # ==========================================
    s3 = prs.slides.add_slide(blank_layout)
    add_bg(s3, dark=False)
    add_header(s3, "Spoken Audit 1: Daily Quality Operations at AL INVEST", "Part 1 • Spoken Diagnostic", slide_num=3)

    c1 = add_card(s3, Inches(0.8), Inches(1.7), Inches(5.65), Inches(5.1), bg_color=C_CARD_BG)
    tf = c1.text_frame
    tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = Inches(0.3)
    p = tf.paragraphs[0]
    p.text = "PROMPT 1: ROLE, PRODUCTION & FOIL CONVERTING"
    p.font.size = Pt(11)
    p.font.bold = True
    p.font.color.rgb = C_PRIMARY

    p = tf.add_paragraph()
    p.text = "\"Could you introduce your responsibilities as Quality Engineer in the Packaging Division? What types of aluminium packaging does AL INVEST produce, and what are your daily inspection routines?\""
    p.font.size = Pt(13)
    p.font.bold = True
    p.font.color.rgb = C_TEXT_DARK
    p.space_before = Pt(8)

    p = tf.add_paragraph()
    p.text = "🎯 Target Structures & Vocabulary:"
    p.font.size = Pt(11)
    p.font.bold = True
    p.font.color.rgb = C_STEEL
    p.space_before = Pt(14)

    bullets = [
        "Present Simple for habitual procedures & SOPs",
        "Third-person singular inflection ('the line runs', 'it measures')",
        "Domain terms: bare foil, converted foil, lamination, lacquering",
        "Parameters: thickness/gauge (µm), tensile strength, elongation"
    ]
    for b in bullets:
        p = tf.add_paragraph()
        p.text = "• " + b
        p.font.size = Pt(10.5)
        p.font.color.rgb = C_TEXT_MUTED

    c2 = add_card(s3, Inches(6.85), Inches(1.7), Inches(5.65), Inches(5.1), bg_color=C_CARD_BG)
    tf = c2.text_frame
    tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = Inches(0.3)
    p = tf.paragraphs[0]
    p.text = "PROMPT 2: CAREER EVOLUTION & DIVISION DEVELOPMENTS"
    p.font.size = Pt(11)
    p.font.bold = True
    p.font.color.rgb = C_GREEN_DARK

    p = tf.add_paragraph()
    p.text = "\"How long have you been working in quality engineering at AL INVEST, and how has the packaging division evolved in terms of customer standards and food safety requirements?\""
    p.font.size = Pt(13)
    p.font.bold = True
    p.font.color.rgb = C_TEXT_DARK
    p.space_before = Pt(8)

    p = tf.add_paragraph()
    p.text = "🎯 Target Structures & Vocabulary:"
    p.font.size = Pt(11)
    p.font.bold = True
    p.font.color.rgb = C_STEEL
    p.space_before = Pt(14)

    bullets = [
        "Present Perfect (since / for) vs Past Simple (past career steps)",
        "Eliminating: *'I work here since 3 years'* -> *'I have worked here for...'*",
        "Evolution vocabulary: automated inspection, stringent migration limits",
        "Standards: BRCGS Packaging Materials, ISO 9001, FSSC 22000"
    ]
    for b in bullets:
        p = tf.add_paragraph()
        p.text = "• " + b
        p.font.size = Pt(10.5)
        p.font.color.rgb = C_TEXT_MUTED

    # ==========================================
    # SLIDE 4: Spoken Audit 2 - World Football Passion
    # ==========================================
    s4 = prs.slides.add_slide(blank_layout)
    add_bg(s4, dark=False)
    add_header(s4, "Spoken Audit 2: World Football Passion & Tactical Philosophy", "Part 1 • Spoken Diagnostic", slide_num=4)

    c1 = add_card(s4, Inches(0.8), Inches(1.7), Inches(5.65), Inches(5.1), bg_color=C_CARD_BG)
    tf = c1.text_frame
    tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = Inches(0.3)
    p = tf.paragraphs[0]
    p.text = "PROMPT 3: FAVORITE CLUBS & COMPETITIVE PASSION"
    p.font.size = Pt(11)
    p.font.bold = True
    p.font.color.rgb = C_GOLD

    p = tf.add_paragraph()
    p.text = "\"Which domestic or international football teams do you support or follow with passion? What makes following them compelling, and how do you track their matches?\""
    p.font.size = Pt(13)
    p.font.bold = True
    p.font.color.rgb = C_TEXT_DARK
    p.space_before = Pt(8)

    p = tf.add_paragraph()
    p.text = "🎯 Target Structures & Vocabulary:"
    p.font.size = Pt(11)
    p.font.bold = True
    p.font.color.rgb = C_STEEL
    p.space_before = Pt(14)

    bullets = [
        "Expressing passion, preference, and emotional engagement",
        "Comparative & superlative structures (*'far more dynamic than...', 'the most consistent squad'*);",
        "Adverbs of frequency (*regularly, occasionally, whenever they play*)",
        "Sports terms: fixture list, table standings, derbies, European nights"
    ]
    for b in bullets:
        p = tf.add_paragraph()
        p.text = "• " + b
        p.font.size = Pt(10.5)
        p.font.color.rgb = C_TEXT_MUTED

    c2 = add_card(s4, Inches(6.85), Inches(1.7), Inches(5.65), Inches(5.1), bg_color=C_CARD_BG)
    tf = c2.text_frame
    tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = Inches(0.3)
    p = tf.paragraphs[0]
    p.text = "PROMPT 4: TACTICAL FORMATIONS & MODERN COACHING"
    p.font.size = Pt(11)
    p.font.bold = True
    p.font.color.rgb = C_GREEN_DARK

    p = tf.add_paragraph()
    p.text = "\"In modern top-tier football, do you prefer high-intensity pressing (like Klopp or Guardiola) or structured, disciplined counter-attacking? What makes a tactical system work?\""
    p.font.size = Pt(13)
    p.font.bold = True
    p.font.color.rgb = C_TEXT_DARK
    p.space_before = Pt(8)

    p = tf.add_paragraph()
    p.text = "🎯 Target Structures & Vocabulary:"
    p.font.size = Pt(11)
    p.font.bold = True
    p.font.color.rgb = C_STEEL
    p.space_before = Pt(14)

    bullets = [
        "Nuanced opinion phrases (*'In my opinion...', 'From a tactical perspective...'*)",
        "First & Second Conditionals (*'If a team presses high, they risk...'*)",
        "Tactical concepts: inverted wingers, low block, transitional phase",
        "Analytical metrics: Expected Goals (xG), pressing triggers, possession"
    ]
    for b in bullets:
        p = tf.add_paragraph()
        p.text = "• " + b
        p.font.size = Pt(10.5)
        p.font.color.rgb = C_TEXT_MUTED

    # ==========================================
    # SLIDE 5: Spoken Audit 3 - 8D & Defect Investigation
    # ==========================================
    s5 = prs.slides.add_slide(blank_layout)
    add_bg(s5, dark=False)
    add_header(s5, "Spoken Audit 3: Non-Conformance & Root Cause Analysis", "Part 1 • Spoken Diagnostic", slide_num=5)

    c1 = add_card(s5, Inches(0.8), Inches(1.7), Inches(5.65), Inches(5.1), bg_color=C_CARD_BG)
    tf = c1.text_frame
    tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = Inches(0.3)
    p = tf.paragraphs[0]
    p.text = "PROMPT 5: NARRATIVE OF A DEFECT INCIDENT"
    p.font.size = Pt(11)
    p.font.bold = True
    p.font.color.rgb = C_ROSE

    p = tf.add_paragraph()
    p.text = "\"Can you describe a significant packaging defect, customer complaint, or line stoppage you had to investigate? What happened on the converting line, and how did you discover it?\""
    p.font.size = Pt(13)
    p.font.bold = True
    p.font.color.rgb = C_TEXT_DARK
    p.space_before = Pt(8)

    p = tf.add_paragraph()
    p.text = "🎯 Target Structures & Vocabulary:"
    p.font.size = Pt(11)
    p.font.bold = True
    p.font.color.rgb = C_STEEL
    p.space_before = Pt(14)

    bullets = [
        "Narrative Past Tenses: Past Simple & Past Continuous",
        "Interrupted actions: *'While the slitter was operating, the web tore...'*,",
        "Defect types: pinholes, oil spots, delamination, lacquer wrinkles",
        "Time sequence connectors: *initially, subsequent to, immediately after*"
    ]
    for b in bullets:
        p = tf.add_paragraph()
        p.text = "• " + b
        p.font.size = Pt(10.5)
        p.font.color.rgb = C_TEXT_MUTED

    c2 = add_card(s5, Inches(6.85), Inches(1.7), Inches(5.65), Inches(5.1), bg_color=C_CARD_BG)
    tf = c2.text_frame
    tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = Inches(0.3)
    p = tf.paragraphs[0]
    p.text = "PROMPT 6: THE 8D METHODOLOGY & CUSTOMER COMMUNICATION"
    p.font.size = Pt(11)
    p.font.bold = True
    p.font.color.rgb = C_PRIMARY

    p = tf.add_paragraph()
    p.text = "\"When handling an 8D report for a major food brand (e.g. Nestlé or Danone), how do you explain the containment actions and permanent corrective measures in English?\""
    p.font.size = Pt(13)
    p.font.bold = True
    p.font.color.rgb = C_TEXT_DARK
    p.space_before = Pt(8)

    p = tf.add_paragraph()
    p.text = "🎯 Target Structures & Vocabulary:"
    p.font.size = Pt(11)
    p.font.bold = True
    p.font.color.rgb = C_STEEL
    p.space_before = Pt(14)

    bullets = [
        "Impersonal Passive Voice (*'The batch was quarantined immediately'*)",
        "Present Perfect for status (*'We have already implemented a new sensor'*)",
        "8D phases: D3 Containment, D4 Root Cause (5 Whys), D5 Corrective Action",
        "Diplomatic & reassuring tone with international audit representatives"
    ]
    for b in bullets:
        p = tf.add_paragraph()
        p.text = "• " + b
        p.font.size = Pt(10.5)
        p.font.color.rgb = C_TEXT_MUTED

    # ==========================================
    # SLIDE 6: Spoken Audit 4 - VAR & Technological Controversies
    # ==========================================
    s6 = prs.slides.add_slide(blank_layout)
    add_bg(s6, dark=False)
    add_header(s6, "Spoken Audit 4: Technology & High-Stakes Officiating (VAR)", "Part 1 • Spoken Diagnostic", slide_num=6)

    c1 = add_card(s6, Inches(0.8), Inches(1.7), Inches(5.65), Inches(5.1), bg_color=C_CARD_BG)
    tf = c1.text_frame
    tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = Inches(0.3)
    p = tf.paragraphs[0]
    p.text = "PROMPT 7: VAR, GOAL-LINE TECH & OFFSIDE CONTROVERSIES"
    p.font.size = Pt(11)
    p.font.bold = True
    p.font.color.rgb = C_GREEN_DARK

    p = tf.add_paragraph()
    p.text = "\"Do you believe VAR and semi-automated offside technology have made football fairer, or have they damaged the spontaneous emotion of celebrating a goal?\""
    p.font.size = Pt(13)
    p.font.bold = True
    p.font.color.rgb = C_TEXT_DARK
    p.space_before = Pt(8)

    p = tf.add_paragraph()
    p.text = "🎯 Target Structures & Vocabulary:"
    p.font.size = Pt(11)
    p.font.bold = True
    p.font.color.rgb = C_STEEL
    p.space_before = Pt(14)

    bullets = [
        "Balancing pros and cons (*'On the one hand... whereas on the other...'*)",
        "Hypothetical reasoning (*'Without VAR, referees would make...'*)",
        "Officiating terms: clear and obvious error, pitchside monitor, handball law",
        "Contrastive connectors: *despite, nevertheless, on the contrary*"
    ]
    for b in bullets:
        p = tf.add_paragraph()
        p.text = "• " + b
        p.font.size = Pt(10.5)
        p.font.color.rgb = C_TEXT_MUTED

    c2 = add_card(s6, Inches(6.85), Inches(1.7), Inches(5.65), Inches(5.1), bg_color=C_CARD_BG)
    tf = c2.text_frame
    tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = Inches(0.3)
    p = tf.paragraphs[0]
    p.text = "PROMPT 8: HYPOTHETICAL RULE REFORMS & INNOVATIONS"
    p.font.size = Pt(11)
    p.font.bold = True
    p.font.color.rgb = C_GOLD

    p = tf.add_paragraph()
    p.text = "\"If IFAB (the International Football Association Board) invited you to change or modify one single rule in world football, which rule would you reform and why?\""
    p.font.size = Pt(13)
    p.font.bold = True
    p.font.color.rgb = C_TEXT_DARK
    p.space_before = Pt(8)

    p = tf.add_paragraph()
    p.text = "🎯 Target Structures & Vocabulary:"
    p.font.size = Pt(11)
    p.font.bold = True
    p.font.color.rgb = C_STEEL
    p.space_before = Pt(14)

    bullets = [
        "Second Conditional: *'If I had the authority, I would abolish...'*,",
        "Subjunctive & modal hedging (*'It would be preferable to implement...'*)",
        "Reform concepts: sin bins (orange cards), effective playing time clock",
        "Articulating long-term impact on player safety and fair play"
    ]
    for b in bullets:
        p = tf.add_paragraph()
        p.text = "• " + b
        p.font.size = Pt(10.5)
        p.font.color.rgb = C_TEXT_MUTED

    # ==========================================
    # SLIDE 7: Diagnostic Grammar 1 - Tenses
    # ==========================================
    s7 = prs.slides.add_slide(blank_layout)
    add_bg(s7, dark=False)
    add_header(s7, "Diagnostic Grammar 1: Tense Differentiation (Quality & Sports)", "Part 2 • Grammar Screening (Items 1–3)", slide_num=7)

    items = [
        ("1. Routine Procedure vs Ongoing Investigation (Present Simple / Cont.)",
         "Right now our quality team _______ (investigate) a customer complaint regarding pinholes in a coffee foil laminate, but normally we _______ (conduct) standard sampling every two hours.\n\n"
         "A) investigates / are conducting\nB) is investigating / conduct  ✓\nC) investigates / conduct",
         "Rule: Present Continuous for temporary ongoing actions; Present Simple for permanent SOP routines."),

        ("2. Incident Interruption during Slitting (Past Cont. + Past Simple)",
         "While the operator _______ (monitor) the web tension at 350 m/min, the optical pinhole detector suddenly _______ (trigger) an emergency audio alarm.\n\n"
         "A) was monitoring / triggered  ✓\nB) monitored / was triggering\nC) was monitoring / was triggering",
         "Rule: Past Continuous sets the ongoing background activity; Past Simple describes the sharp interruption."),

        ("3. Professional Tenure & League Match History (Pres. Perf. vs Past)",
         "Vojtěch _______ (work) as a quality specialist in packaging for four years now, but before joining AL INVEST he _______ (manage) automotive testing.\n\n"
         "A) worked / has managed\nB) has worked / managed  ✓\nC) is working / managed",
         "Rule: Present Perfect connects unfinished duration to the present (with for/since); Past Simple marks finished past roles.")
    ]

    for idx, (head, body, tip) in enumerate(items):
        top_pos = Inches(1.7 + idx * 1.7)
        card = add_card(s7, Inches(0.8), top_pos, Inches(11.7), Inches(1.5), bg_color=C_CARD_BG)
        tf = card.text_frame
        tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = Inches(0.18)
        p = tf.paragraphs[0]
        p.text = head
        p.font.size = Pt(11)
        p.font.bold = True
        p.font.color.rgb = C_PRIMARY
        p = tf.add_paragraph()
        p.text = body
        p.font.size = Pt(9.5)
        p.font.color.rgb = C_TEXT_DARK
        p = tf.add_paragraph()
        p.text = "💡 " + tip
        p.font.size = Pt(8.5)
        p.font.italic = True
        p.font.color.rgb = C_EMERALD

    # ==========================================
    # SLIDE 8: Diagnostic Grammar 2 - Passive Voice
    # ==========================================
    s8 = prs.slides.add_slide(blank_layout)
    add_bg(s8, dark=False)
    add_header(s8, "Diagnostic Grammar 2: Passive Voice in Quality Audits & Sports", "Part 2 • Grammar Screening (Items 4–6)", slide_num=8)

    items = [
        ("4. Laboratory Foil Inspection & Standard Annealing (Present Passive)",
         "Before the bare aluminium coil is converted into food packaging, its tensile strength and elongation _______ (test) and its surface _______ (degrease) to ensure proper lacquer adhesion.\n\n"
         "A) are tested / is degreased  ✓\nB) test / degreases\nC) are testing / is degreasing",
         "Rule: Passive Voice is mandatory in technical SOPs where the action and material matter more than the agent."),

        ("5. Football Match Disciplinary Action (Past Passive)",
         "Following an on-field VAR review in the 74th minute, the opposing defender _______ (dismiss) with a red card and three penalty points _______ (deduct) from the club.\n\n"
         "A) was dismissed / were deducted  ✓\nB) dismissed / deducted\nC) was dismissing / was deducted",
         "Rule: Past Passive (was/were + past participle) for official match sanctions and referee decisions."),

        ("6. Batch Quarantine & 8D Containment (Present Perfect Passive)",
         "All suspicious reels from batch #2026-B _______ (quarantine) in the warehouse until the micro-leakage report _______ (complete) by the external lab.\n\n"
         "A) have quarantined / will complete\nB) have been quarantined / has been completed  ✓\nC) are quarantined / completed",
         "Rule: Present Perfect Passive (have been + V3) describes completed containment whose protective result holds right now.")
    ]

    for idx, (head, body, tip) in enumerate(items):
        top_pos = Inches(1.7 + idx * 1.7)
        card = add_card(s8, Inches(0.8), top_pos, Inches(11.7), Inches(1.5), bg_color=C_CARD_BG)
        tf = card.text_frame
        tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = Inches(0.18)
        p = tf.paragraphs[0]
        p.text = head
        p.font.size = Pt(11)
        p.font.bold = True
        p.font.color.rgb = C_GREEN_DARK
        p = tf.add_paragraph()
        p.text = body
        p.font.size = Pt(9.5)
        p.font.color.rgb = C_TEXT_DARK
        p = tf.add_paragraph()
        p.text = "💡 " + tip
        p.font.size = Pt(8.5)
        p.font.italic = True
        p.font.color.rgb = C_PRIMARY

    # ==========================================
    # SLIDE 9: Diagnostic Grammar 3 - Conditionals
    # ==========================================
    s9 = prs.slides.add_slide(blank_layout)
    add_bg(s9, dark=False)
    add_header(s9, "Diagnostic Grammar 3: Conditionals in Quality Specs & Tactics", "Part 2 • Grammar Screening (Items 7–9)", slide_num=9)

    items = [
        ("7. Zero Conditional: Scientific Laws of Foil Permeability",
         "If the thickness of the barrier aluminium layer _______ (fall) below 6.35 microns, the pinhole density _______ (rise) according to international packaging standards.\n\n"
         "A) falls / will rise\nB) falls / rises  ✓\nC) will fall / rises",
         "Rule: Zero Conditional (If + Present Simple, Present Simple) states constant physical or metallurgical facts."),

        ("8. First Conditional: Production Consequence & Tactical Counter",
         "If the customer's incoming inspection _______ (detect) delamination between the foil and the PE film, our plant _______ (dispatch) a replacement batch within 48 hours.\n\n"
         "A) detects / will dispatch  ✓\nB) will detect / dispatches\nC) detects / dispatches",
         "Rule: First Conditional (If + Present Simple, will + base verb) describes real, probable future contractual contingencies."),

        ("9. Second Conditional: Hypothetical Quality Investment & Scouting",
         "If AL INVEST _______ (install) 100% optical camera inspection on all slitting lines, we _______ (prevent) virtually all surface defect claims.\n\n"
         "A) installs / would prevent\nB) installed / would prevent  ✓\nC) installed / will prevent",
         "Rule: Second Conditional (If + Past Simple, would + base verb) explores hypothetical or unreal operational upgrades.")
    ]

    for idx, (head, body, tip) in enumerate(items):
        top_pos = Inches(1.7 + idx * 1.7)
        card = add_card(s9, Inches(0.8), top_pos, Inches(11.7), Inches(1.5), bg_color=C_CARD_BG)
        tf = card.text_frame
        tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = Inches(0.18)
        p = tf.paragraphs[0]
        p.text = head
        p.font.size = Pt(11)
        p.font.bold = True
        p.font.color.rgb = C_GOLD
        p = tf.add_paragraph()
        p.text = body
        p.font.size = Pt(9.5)
        p.font.color.rgb = C_TEXT_DARK
        p = tf.add_paragraph()
        p.text = "💡 " + tip
        p.font.size = Pt(8.5)
        p.font.italic = True
        p.font.color.rgb = C_PRIMARY

    # ==========================================
    # SLIDE 10: Diagnostic Grammar 4 - 3rd Conditional & Past Modals
    # ==========================================
    s10 = prs.slides.add_slide(blank_layout)
    add_bg(s10, dark=False)
    add_header(s10, "Diagnostic Grammar 4: 8D Root Cause & Post-Match Retrospectives", "Part 2 • Grammar Screening (Items 10–12)", slide_num=10)

    items = [
        ("10. Third Conditional: Root Cause Prevention in Packaging",
         "If the slitter operator _______ (replace) the dull cutting knives at the scheduled interval, the aluminium web _______ (not / tear) on the customer's pouch-packing line.\n\n"
         "A) replaced / wouldn't tear\nB) had replaced / wouldn't have torn  ✓\nC) had replaced / wouldn't tear",
         "Rule: Third Conditional (If + had + V3, would have + V3) evaluates unchangeable past events in 8D audits."),

        ("11. Third Conditional: Missed Champions League Decider",
         "If the striker _______ (convert) the penalty in stoppage time, the club _______ (qualify) directly for the knockout phase.\n\n"
         "A) had converted / would have qualified  ✓\nB) converted / would qualify\nC) had converted / qualified",
         "Rule: Expressing retrospective regret and alternative sporting outcomes in tournament history."),

        ("12. Past Modals of Deduction: Investigating Defect Causes",
         "The heat-seal lacquer failed the peel test; the drying tunnel temperature _______ (must / drop) below the specified curing threshold during the shift.\n\n"
         "A) must drop\nB) must have dropped  ✓\nC) should drop",
         "Rule: *Must have + V3* expresses high certainty regarding a past cause based on physical evidence.")
    ]

    for idx, (head, body, tip) in enumerate(items):
        top_pos = Inches(1.7 + idx * 1.7)
        card = add_card(s10, Inches(0.8), top_pos, Inches(11.7), Inches(1.5), bg_color=C_CARD_BG)
        tf = card.text_frame
        tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = Inches(0.18)
        p = tf.paragraphs[0]
        p.text = head
        p.font.size = Pt(11)
        p.font.bold = True
        p.font.color.rgb = C_ROSE
        p = tf.add_paragraph()
        p.text = body
        p.font.size = Pt(9.5)
        p.font.color.rgb = C_TEXT_DARK
        p = tf.add_paragraph()
        p.text = "💡 " + tip
        p.font.size = Pt(8.5)
        p.font.italic = True
        p.font.color.rgb = C_GREEN_DARK

    # ==========================================
    # SLIDE 11: Diagnostic Grammar 5 - Modals & Regulations
    # ==========================================
    s11 = prs.slides.add_slide(blank_layout)
    add_bg(s11, dark=False)
    add_header(s11, "Diagnostic Grammar 5: Modals of Obligation & Food Safety Rules", "Part 2 • Grammar Screening (Items 13–15)", slide_num=11)

    items = [
        ("13. Regulatory Compliance: EU Food Contact Law (Must / Have to)",
         "Under EU Framework Regulation (EC) 1935/2004, all aluminium packaging intended for food contact _______ not release constituents into foodstuffs in quantities that endanger human health.\n\n"
         "A) must / shall  ✓\nB) can\nC) should",
         "Rule: *Must* and legal *shall* indicate strict statutory obligations in food contact materials."),

        ("14. Sporting Laws: Rules of the Pitch (Prohibition vs Absence of Obligation)",
         "A football referee _______ use the pitchside VAR monitor for every single foul, but they _______ review any possible red card or penalty award.\n\n"
         "A) mustn't / should\nB) doesn't have to / must  ✓\nC) can't / have to",
         "Rule: *Doesn't have to* = no obligation; *Must* = mandatory protocol."),

        ("15. BRCGS Packaging Audit Preparation (Should vs Must Not)",
         "Quality inspectors _______ store chemical solvents near open food-contact packaging reels under any circumstances.\n\n"
         "A) don't have to\nB) must not  ✓\nC) shouldn't",
         "Rule: *Must not* indicates complete prohibition and immediate audit non-conformance.")
    ]

    for idx, (head, body, tip) in enumerate(items):
        top_pos = Inches(1.7 + idx * 1.7)
        card = add_card(s11, Inches(0.8), top_pos, Inches(11.7), Inches(1.5), bg_color=C_CARD_BG)
        tf = card.text_frame
        tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = Inches(0.18)
        p = tf.paragraphs[0]
        p.text = head
        p.font.size = Pt(11)
        p.font.bold = True
        p.font.color.rgb = C_PRIMARY
        p = tf.add_paragraph()
        p.text = body
        p.font.size = Pt(9.5)
        p.font.color.rgb = C_TEXT_DARK
        p = tf.add_paragraph()
        p.text = "💡 " + tip
        p.font.size = Pt(8.5)
        p.font.italic = True
        p.font.color.rgb = C_GREEN_DARK

    # ==========================================
    # SLIDE 12: Diagnostic Grammar 6 - Prepositions & Collocations
    # ==========================================
    s12 = prs.slides.add_slide(blank_layout)
    add_bg(s12, dark=False)
    add_header(s12, "Diagnostic Grammar 6: Prepositions & Technical Collocations", "Part 2 • Grammar Screening (Items 16–18)", slide_num=12)

    items = [
        ("16. Quality Engineering Responsibilities & Compliance",
         "As a quality specialist, Vojtěch is responsible _______ ensuring full compliance _______ BRCGS Packaging standards across all converting lines.\n\n"
         "A) for / with  ✓\nB) of / to\nC) about / in",
         "Rule: *Responsible FOR* + -ing / noun; *Compliant WITH* / *Compliance WITH*."),

        ("17. Football Match Transition & Tactical Positioning",
         "The counter-attack originated _______ a turnover _______ midfield, catching the backline completely out of position.\n\n"
         "A) in / on\nB) from / in  ✓\nC) with / at",
         "Rule: *Originate FROM*; *IN midfield / ON the pitch / ON the wing*."),

        ("18. Customer Claim Management & Root Cause Settlement",
         "Our technical team apologized _______ the customer _______ the delayed CoAs and agreed _______ an on-site audit next Tuesday.\n\n"
         "A) to / for / on (or to)  ✓\nB) with / about / with\nC) at / of / for",
         "Rule: *Apologize TO someone FOR something*; *Agree ON a date / TO a proposal*.")
    ]

    for idx, (head, body, tip) in enumerate(items):
        top_pos = Inches(1.7 + idx * 1.7)
        card = add_card(s12, Inches(0.8), top_pos, Inches(11.7), Inches(1.5), bg_color=C_CARD_BG)
        tf = card.text_frame
        tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = Inches(0.18)
        p = tf.paragraphs[0]
        p.text = head
        p.font.size = Pt(11)
        p.font.bold = True
        p.font.color.rgb = C_GREEN_DARK
        p = tf.add_paragraph()
        p.text = body
        p.font.size = Pt(9.5)
        p.font.color.rgb = C_TEXT_DARK
        p = tf.add_paragraph()
        p.text = "💡 " + tip
        p.font.size = Pt(8.5)
        p.font.italic = True
        p.font.color.rgb = C_PRIMARY

    # ==========================================
    # SLIDE 13: Error Spotting (Czenglish Traps)
    # ==========================================
    s13 = prs.slides.add_slide(blank_layout)
    add_bg(s13, dark=False)
    add_header(s13, "Error-Spotting: Top 6 'Czenglish' Traps in Packaging & Sports", "Part 2 • Diagnostic Accuracy", slide_num=13)

    traps = [
        ("1. The 'Work Here Since' Trap",
         "❌ \"I work as a quality engineer in AL INVEST since three years.\"\n"
         "✓ \"I have been working as a quality engineer at AL INVEST for three years.\"",
         "Czech 'pracuji od/už 3 roky' requires Present Perfect Continuous + FOR (duration) or SINCE (starting date)."),

        ("2. The False Friend: 'Control' vs 'Inspect / Check'",
         "❌ \"We must control each slit coil for surface defects.\"\n"
         "✓ \"We must inspect / check / examine each slit coil for surface defects.\"",
         "'Control' in English means to govern or regulate; testing quality is 'inspect, check, audit, or monitor'."),

        ("3. The 'Reclamation' Trap",
         "❌ \"The packaging client sent an urgent reclamation about pinholes.\"\n"
         "✓ \"The packaging client submitted an urgent complaint / claim regarding pinholes.\"",
         "Czech 'reklamace' translates to customer complaint, quality claim, or non-conformance notice."),

        ("4. Modal + Infinitive with 'To'",
         "❌ \"The referee should to review the penalty incident on the monitor.\"\n"
         "✓ \"The referee should review the penalty incident on the monitor.\"",
         "Modal verbs (should, must, can, could, would) are followed directly by the bare infinitive (no 'to')."),

        ("5. The 'Discuss About' Preposition Trap",
         "❌ \"Our engineering team will discuss about the heat-seal delamination tomorrow.\"\n"
         "✓ \"Our engineering team will discuss the heat-seal delamination tomorrow.\"",
         "'Discuss' is transitive in English — never use 'about' after discuss (compare: 'talk about' vs 'discuss')."),

        ("6. The Conditional 'If + Will' Trap",
         "❌ \"If the manager will change the tactical formation, they will score.\"\n"
         "✓ \"If the manager changes the tactical formation, they will score.\"",
         "In 1st conditionals, the 'if' condition clause takes Present Simple, NEVER 'will'.")
    ]

    for idx, (title, examples, note) in enumerate(traps):
        col = idx % 2
        row = idx // 2
        left_pos = Inches(0.8 + col * 6.05)
        top_pos = Inches(1.7 + row * 1.7)
        card = add_card(s13, left_pos, top_pos, Inches(5.65), Inches(1.5), bg_color=C_CARD_BG)
        tf = card.text_frame
        tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = Inches(0.18)
        p = tf.paragraphs[0]
        p.text = title
        p.font.size = Pt(11)
        p.font.bold = True
        p.font.color.rgb = C_ROSE
        p = tf.add_paragraph()
        p.text = examples
        p.font.size = Pt(9.5)
        p.font.color.rgb = C_TEXT_DARK
        p = tf.add_paragraph()
        p.text = "💡 " + note
        p.font.size = Pt(8.5)
        p.font.italic = True
        p.font.color.rgb = C_TEXT_MUTED

    # ==========================================
    # SLIDE 14: Deep Dive - Present Perfect vs Past Simple
    # ==========================================
    s14 = prs.slides.add_slide(blank_layout)
    add_bg(s14, dark=False)
    add_header(s14, "Grammar Deep Dive: Present Perfect vs Past Simple", "Part 2 • Targeted Technical Review", slide_num=14)

    c1 = add_card(s14, Inches(0.8), Inches(1.7), Inches(5.65), Inches(5.1), bg_color=C_CARD_BG)
    tf1 = c1.text_frame
    tf1.margin_left = tf1.margin_right = tf1.margin_top = tf1.margin_bottom = Inches(0.3)
    p = tf1.paragraphs[0]
    p.text = "PAST SIMPLE: FINISHED TIME & SPECIFIC DATES"
    p.font.size = Pt(12)
    p.font.bold = True
    p.font.color.rgb = C_GOLD

    p = tf1.add_paragraph()
    p.text = "Use when the time period is over or tied to an exact past moment."
    p.font.size = Pt(10.5)
    p.font.color.rgb = C_TEXT_MUTED
    p.space_before = Pt(6)

    p = tf1.add_paragraph()
    p.text = "🔑 Trigger Words: yesterday, in 2024, last week, three shifts ago, during the morning audit."
    p.font.size = Pt(10)
    p.font.bold = True
    p.font.color.rgb = C_STEEL
    p.space_before = Pt(8)

    p = tf1.add_paragraph()
    p.text = "Industrial Packaging Examples:"
    p.font.size = Pt(11)
    p.font.bold = True
    p.font.color.rgb = C_TEXT_DARK
    p.space_before = Pt(10)

    p = tf1.add_paragraph()
    p.text = "• \"We recalibrated the optical pinhole sensors on line 3 yesterday morning.\"\n• \"The customer submitted their audit report on May 14th.\"\n• \"The slitter operator stopped the web immediately when tension dropped.\""
    p.font.size = Pt(10)
    p.font.color.rgb = C_TEXT_DARK

    p = tf1.add_paragraph()
    p.text = "Football History Examples:"
    p.font.size = Pt(11)
    p.font.bold = True
    p.font.color.rgb = C_TEXT_DARK
    p.space_before = Pt(10)

    p = tf1.add_paragraph()
    p.text = "• \"Spain won the European Championship in July 2024.\"\n• \"The referee gave a yellow card in the 22nd minute of the derby.\""
    p.font.size = Pt(10)
    p.font.color.rgb = C_TEXT_DARK

    c2 = add_card(s14, Inches(6.85), Inches(1.7), Inches(5.65), Inches(5.1), bg_color=C_CARD_BG)
    tf2 = c2.text_frame
    tf2.margin_left = tf2.margin_right = tf2.margin_top = tf2.margin_bottom = Inches(0.3)
    p = tf2.paragraphs[0]
    p.text = "PRESENT PERFECT: STATUS UP TO NOW & RELEVANT RESULT"
    p.font.size = Pt(12)
    p.font.bold = True
    p.font.color.rgb = C_GREEN_DARK

    p = tf2.add_paragraph()
    p.text = "Use when the time is open or the past action has immediate current impact."
    p.font.size = Pt(10.5)
    p.font.color.rgb = C_TEXT_MUTED
    p.space_before = Pt(6)

    p = tf2.add_paragraph()
    p.text = "🔑 Trigger Words: so far, already, recently, since, this week, yet, up to now."
    p.font.size = Pt(10)
    p.font.bold = True
    p.font.color.rgb = C_STEEL
    p.space_before = Pt(8)

    p = tf2.add_paragraph()
    p.text = "Industrial Packaging Examples:"
    p.font.size = Pt(11)
    p.font.bold = True
    p.font.color.rgb = C_TEXT_DARK
    p.space_before = Pt(10)

    p = tf2.add_paragraph()
    p.text = "• \"We have already inspected 14 master coils this morning.\"\n• \"Have you received the laboratory CoA for the lacquering lot yet?\"\n• \"AL INVEST has maintained BRCGS Packaging certification for years.\""
    p.font.size = Pt(10)
    p.font.color.rgb = C_TEXT_DARK

    p = tf2.add_paragraph()
    p.text = "Football Analytics Examples:"
    p.font.size = Pt(11)
    p.font.bold = True
    p.font.color.rgb = C_TEXT_DARK
    p.space_before = Pt(10)

    p = tf2.add_paragraph()
    p.text = "• \"The striker has scored 12 goals so far this season.\"\n• \"Have the VAR officials verified the offside line yet?\""
    p.font.size = Pt(10)
    p.font.color.rgb = C_TEXT_DARK

    # ==========================================
    # SLIDE 15: Deep Dive - Active vs Passive in 8D Reports
    # ==========================================
    s15 = prs.slides.add_slide(blank_layout)
    add_bg(s15, dark=False)
    add_header(s15, "Grammar Deep Dive: The Passive Voice in 8D Reports", "Part 2 • Targeted Technical Review", slide_num=15)

    c1 = add_card(s15, Inches(0.8), Inches(1.7), Inches(5.65), Inches(5.1), bg_color=C_CARD_BG)
    tf1 = c1.text_frame
    tf1.margin_left = tf1.margin_right = tf1.margin_top = tf1.margin_bottom = Inches(0.3)
    p = tf1.paragraphs[0]
    p.text = "❌ SUBJECTIVE / INFORMAL ACTIVE (AVOID IN AUDITS)"
    p.font.size = Pt(11)
    p.font.bold = True
    p.font.color.rgb = C_ROSE

    items_act = [
        ("\"The forklift driver dropped the master coil.\"", "Focuses personal blame on the operator rather than packaging integrity."),
        ("\"We tested the peel strength at 180°C.\"", "Sounds conversational rather than standard laboratory documentation."),
        ("\"Somebody forgot to clean the lacquering roller.\"", "Unprofessional tone in formal customer-facing 8D non-conformance reports."),
        ("\"The referee made a catastrophic mistake.\"", "Emotional commentary rather than objective post-match review.")
    ]
    for act, reason in items_act:
        p = tf1.add_paragraph()
        p.text = act
        p.font.size = Pt(11)
        p.font.bold = True
        p.font.color.rgb = C_TEXT_DARK
        p.space_before = Pt(10)
        p = tf1.add_paragraph()
        p.text = "⚠️ " + reason
        p.font.size = Pt(9.5)
        p.font.color.rgb = C_TEXT_MUTED

    c2 = add_card(s15, Inches(6.85), Inches(1.7), Inches(5.65), Inches(5.1), bg_color=C_CARD_BG)
    tf2 = c2.text_frame
    tf2.margin_left = tf2.margin_right = tf2.margin_top = tf2.margin_bottom = Inches(0.3)
    p = tf2.paragraphs[0]
    p.text = "✓ OBJECTIVE AUDIT PASSIVE (RECOMMENDED)"
    p.font.size = Pt(11)
    p.font.bold = True
    p.font.color.rgb = C_GREEN_DARK

    items_pass = [
        ("\"The master coil was damaged during internal transport.\"", "Focuses objectively on the material status and containment requirement."),
        ("\"Heat-seal peel strength was evaluated at 180°C (DIN 55529).\"", "Establishes institutional rigor, standard test methods, and precision."),
        ("\"Inadequate roller cleaning was identified as the direct root cause.\"", "Clean 8D D4 phrasing appropriate for multinational food brand auditors."),
        ("\"An on-field error was corrected following VAR intervention.\"", "Calm, standardized sports governance language.")
    ]
    for pas, benefit in items_pass:
        p = tf2.add_paragraph()
        p.text = pas
        p.font.size = Pt(11)
        p.font.bold = True
        p.font.color.rgb = C_TEXT_DARK
        p.space_before = Pt(10)
        p = tf2.add_paragraph()
        p.text = "✓ " + benefit
        p.font.size = Pt(9.5)
        p.font.color.rgb = C_GREEN_DARK

    # ==========================================
    # SLIDE 16: Live Case Study 1 - Snack Foil Delamination
    # ==========================================
    s16 = prs.slides.add_slide(blank_layout)
    add_bg(s16, dark=False)
    add_header(s16, "Live Case Study 1: The Laminated Snack Foil Delamination Crisis", "Extension Bank • Spoken Fluency Drill", slide_num=16)

    c_top = add_card(s16, Inches(0.8), Inches(1.7), Inches(11.7), Inches(1.5), bg_color=RGBColor(241, 245, 249), border_color=C_PRIMARY)
    tf_top = c_top.text_frame
    tf_top.margin_left = tf_top.margin_right = tf_top.margin_top = tf_top.margin_bottom = Inches(0.2)
    p = tf_top.paragraphs[0]
    p.text = "THE SCENARIO (CUSTOMER COMPLAINT FROM MULTINATIONAL FOOD PACKER):"
    p.font.size = Pt(11)
    p.font.bold = True
    p.font.color.rgb = C_PRIMARY
    p = tf_top.add_paragraph()
    p.text = "A tier-one potato chip manufacturer in Poland urgently contacts AL INVEST. During high-speed vertical form-fill-seal (VFFS) packing at 120 bags/minute, the outer PET film is peeling away from the 7 µm aluminium barrier foil, causing seal failures and nitrogen flush leakage. They threaten to shut down two lines and claim €45,000 in downtime losses."
    p.font.size = Pt(10.5)
    p.font.color.rgb = C_TEXT_DARK
    p.space_before = Pt(4)

    # 3 Strategy Cards below
    steps = [
        ("Step 1: Immediate Containment (D3)",
         "What language and actions must Vojtěch deploy immediately?\n\n"
         "• \"All reels currently in transit are being put on hold.\"\n"
         "• \"Retain samples from batch #308 are being tested in our lab right now.\"\n"
         "• Structure: Present Continuous Passive + Modals of urgency.",
         C_PRIMARY),
        ("Step 2: Root Cause Investigation (D4)",
         "How do we explain the 5 Whys without admitting liability prematurely?\n\n"
         "• \"If corona treatment had dropped, surface dyne would have fallen below 38.\"\n"
         "• \"The solvent mixture might have caused adhesive curing issues.\"\n"
         "• Structure: 3rd Conditionals & Past Modals of Deduction.",
         C_GOLD),
        ("Step 3: Corrective Actions & Resolution (D5)",
         "How do we assure the auditor that the fix is permanent?\n\n"
         "• \"Adhesion monitoring has been integrated into hourly inspection sheets.\"\n"
         "• \"We will dispatch fully validated reels by express courier tomorrow.\"\n"
         "• Structure: Present Perfect Passive + 1st Conditional guarantees.",
         C_GREEN_DARK)
    ]

    for idx, (head, body, col) in enumerate(steps):
        left_pos = Inches(0.8 + idx * 4.0)
        c = add_card(s16, left_pos, Inches(3.4), Inches(3.7), Inches(3.4), bg_color=C_CARD_BG)
        tf = c.text_frame
        tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = Inches(0.22)
        p = tf.paragraphs[0]
        p.text = head
        p.font.size = Pt(11)
        p.font.bold = True
        p.font.color.rgb = col
        p = tf.add_paragraph()
        p.text = body
        p.font.size = Pt(9.5)
        p.font.color.rgb = C_TEXT_DARK
        p.space_before = Pt(8)

    # ==========================================
    # SLIDE 17: Live Case Study 2 - Champions League Final VAR
    # ==========================================
    s17 = prs.slides.add_slide(blank_layout)
    add_bg(s17, dark=False)
    add_header(s17, "Live Case Study 2: The 89th-Minute Champions League Final VAR", "Extension Bank • Spoken Fluency Drill", slide_num=17)

    c_top = add_card(s17, Inches(0.8), Inches(1.7), Inches(11.7), Inches(1.5), bg_color=RGBColor(241, 245, 249), border_color=C_GREEN_DARK)
    tf_top = c_top.text_frame
    tf_top.margin_left = tf_top.margin_right = tf_top.margin_top = tf_top.margin_bottom = Inches(0.2)
    p = tf_top.paragraphs[0]
    p.text = "THE SCENARIO (HIGH-STAKES FOOTBALL CONTROVERSY):"
    p.font.size = Pt(11)
    p.font.bold = True
    p.font.color.rgb = C_GREEN_DARK
    p = tf_top.add_paragraph()
    p.text = "In the 89th minute of the UEFA Champions League Final, tied 1-1, a powerful strike deflects off a defender's thigh and strikes their outstretched arm while they are sliding to block the cross. The referee does not whistle, but the VAR calls him to the pitchside monitor. If awarded, the resulting penalty will decide the European champion."
    p.font.size = Pt(10.5)
    p.font.color.rgb = C_TEXT_DARK
    p.space_before = Pt(4)

    steps_fb = [
        ("Analysis 1: Law 12 Interpretation",
         "Was the arm in an unnatural silhouette?\n\n"
         "• \"The arm was extended, but it was supporting the player's fall.\"\n"
         "• \"Because the ball deflected off his own thigh first, it wasn't deliberate.\"\n"
         "• Structure: Explaining nuances with past contrastive linkers.",
         C_PRIMARY),
        ("Analysis 2: VAR Threshold (Clear & Obvious)",
         "Should the video referee have intervened?\n\n"
         "• \"If the on-field decision wasn't a clear error, VAR shouldn't have intervened.\"\n"
         "• \"The referee must retain final authority over subjective interpretations.\"\n"
         "• Structure: 3rd Conditional + Modal obligations (should have).",
         C_GOLD),
        ("Analysis 3: Post-Match Tactical Fallout",
         "How does the losing coach articulate their frustration diplomatically?\n\n"
         "• \"Had the penalty not been awarded, we would have forced extra time.\"\n"
         "• \"We must accept the ruling, but technology needs clearer boundaries.\"\n"
         "• Structure: Inverted conditionals (*Had we...*) + diplomatic hedging.",
         C_ROSE)
    ]

    for idx, (head, body, col) in enumerate(steps_fb):
        left_pos = Inches(0.8 + idx * 4.0)
        c = add_card(s17, left_pos, Inches(3.4), Inches(3.7), Inches(3.4), bg_color=C_CARD_BG)
        tf = c.text_frame
        tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = Inches(0.22)
        p = tf.paragraphs[0]
        p.text = head
        p.font.size = Pt(11)
        p.font.bold = True
        p.font.color.rgb = col
        p = tf.add_paragraph()
        p.text = body
        p.font.size = Pt(9.5)
        p.font.color.rgb = C_TEXT_DARK
        p.space_before = Pt(8)

    # ==========================================
    # SLIDE 18: Technical & Sports Glossary
    # ==========================================
    s18 = prs.slides.add_slide(blank_layout)
    add_bg(s18, dark=False)
    add_header(s18, "Bilingual Domain Reference: Packaging & Football Terminology", "Curriculum Reference & Vocabulary", slide_num=18)

    c1 = add_card(s18, Inches(0.8), Inches(1.7), Inches(5.65), Inches(5.1), bg_color=C_CARD_BG)
    tf1 = c1.text_frame
    tf1.margin_left = tf1.margin_right = tf1.margin_top = tf1.margin_bottom = Inches(0.25)
    p = tf1.paragraphs[0]
    p.text = "🏭 ALUMINIUM PACKAGING QUALITY (CZECH - ENGLISH)"
    p.font.size = Pt(11)
    p.font.bold = True
    p.font.color.rgb = C_PRIMARY

    pack_terms = [
        ("Foliová válcovna / Převíjení", "Aluminium rolling mill / Slitting & Rewinding"),
        ("Tloušťka fólie / Tolerance", "Foil gauge / Thickness tolerance (µm)"),
        ("Poréznost / Mikrodírky", "Pinhole detection / Micro-porosity"),
        ("Pevnost v tahu / Tažnost", "Tensile strength (Rm) / Elongation at break (A50)"),
        ("Svarová pevnost / Těsnost", "Heat-seal strength / Seal integrity & peel test"),
        ("Povrchové napětí (Dyne)", "Surface wetting tension (Dyne level / test inks)"),
        ("Laminace / Lakování", "Lamination (Alu/PE/PET) / Lacquer coating"),
        ("Reklamace zákazníka", "Customer complaint / Quality claim (NCR)"),
        ("Nápravná a preventivní opatření", "CAPA (Corrective and Preventive Actions)"),
        ("Protokol o neshodě (8D)", "8D Problem Solving Report (Containment/Root Cause)")
    ]
    for cz, en in pack_terms:
        p = tf1.add_paragraph()
        p.text = f"• {cz} → {en}"
        p.font.size = Pt(9.5)
        p.font.color.rgb = C_TEXT_DARK

    c2 = add_card(s18, Inches(6.85), Inches(1.7), Inches(5.65), Inches(5.1), bg_color=C_CARD_BG)
    tf2 = c2.text_frame
    tf2.margin_left = tf2.margin_right = tf2.margin_top = tf2.margin_bottom = Inches(0.25)
    p = tf2.paragraphs[0]
    p.text = "⚽ WORLD SPORTS & FOOTBALL ANALYTICS"
    p.font.size = Pt(11)
    p.font.bold = True
    p.font.color.rgb = C_GREEN_DARK

    sport_terms = [
        ("Vysoký presink / Nízký blok", "High pressing / Compact low defensive block"),
        ("Přechodová fáze do útoku", "Attacking transition / Counter-attacking turnover"),
        ("Obranná linie / Ofsajdová past", "Backline defensive line / Offside trap"),
        ("Očekávané góly (xG)", "Expected Goals (xG) / Shot conversion rate"),
        ("Přezkum videa (VAR)", "VAR review / Clear and obvious error protocol"),
        ("Otočení skóre / Vyrovnání", "Comeback victory / Equalizing goal in stoppage time"),
        ("Finanční fair play (FFP)", "UEFA Financial Fair Play / Squad cost ratio"),
        ("Čisté konto / Herní vytížení", "Clean sheet / Squad rotation & match fitness"),
        ("Obrácená křídla / Krajní beci", "Inverted wingers / Overlapping full-backs"),
        ("Zákaz přestupů / Výkupní klauzule", "Transfer ban / Release buyout clause")
    ]
    for cz, en in sport_terms:
        p = tf2.add_paragraph()
        p.text = f"• {cz} → {en}"
        p.font.size = Pt(9.5)
        p.font.color.rgb = C_TEXT_DARK

    # ==========================================
    # SLIDE 19: Action Plan & Next Steps (Dark)
    # ==========================================
    s19 = prs.slides.add_slide(blank_layout)
    add_bg(s19, dark=True)
    add_header(s19, "Action Plan: Tailored Syllabus for Vojtěch Berger", "Executive Pathway", dark=True, slide_num=19)

    c1 = add_card(s19, Inches(0.8), Inches(1.7), Inches(5.65), Inches(4.5), bg_color=C_DARK_CARD, border_color=RGBColor(30, 58, 95))
    tf1 = c1.text_frame
    tf1.margin_left = tf1.margin_right = tf1.margin_top = tf1.margin_bottom = Inches(0.25)
    p = tf1.paragraphs[0]
    p.text = "🎯 TARGET COMPETENCIES"
    p.font.size = Pt(12)
    p.font.bold = True
    p.font.color.rgb = C_PRIMARY_LIGHT

    milestones = [
        ("Flawless 8D Technical Reporting", "Mastering the passive voice and formal connectors to write audit-ready non-conformance reports for multinational food brand owners."),
        ("Conditionals for Tolerances & Negotiations", "Using 1st, 2nd, and 3rd conditionals effortlessly when explaining physical foil tolerances and debating quality claim settlements."),
        ("Spontaneous Spoken Agility", "Gaining rapid fluency during unexpected online supplier audits and customer visits without hesitating over verb tenses."),
        ("Sports Debate & Rapport Mastery", "Using high-level idiomatic football English to build effortless social rapport with international commercial partners.")
    ]
    for title, desc in milestones:
        p = tf1.add_paragraph()
        p.text = "✓ " + title
        p.font.size = Pt(11)
        p.font.bold = True
        p.font.color.rgb = C_TEXT_LIGHT
        p.space_before = Pt(8)
        p = tf1.add_paragraph()
        p.text = desc
        p.font.size = Pt(9.5)
        p.font.color.rgb = RGBColor(203, 213, 225)

    c2 = add_card(s19, Inches(6.85), Inches(1.7), Inches(5.65), Inches(4.5), bg_color=C_DARK_CARD, border_color=RGBColor(30, 58, 95))
    tf2 = c2.text_frame
    tf2.margin_left = tf2.margin_right = tf2.margin_top = tf2.margin_bottom = Inches(0.25)
    p = tf2.paragraphs[0]
    p.text = "📦 RECOMMENDED LEARNING TOOLS"
    p.font.size = Pt(12)
    p.font.bold = True
    p.font.color.rgb = C_EMERALD

    tools = [
        ("Interactive Grammar Deck (HTML5)", "The companion single-file browser deck with instant interactive answer checking, explanation popups, and keyboard shortcuts."),
        ("Dedicated Quality Simulation Modules", "Practicing realistic BRCGS audit scenarios, pinhole complaints, and lacquering defect disputes."),
        ("Weekly Football Tactical Briefings", "Using real Premier League and Champions League analytical articles for reading and oral summarization."),
        ("Czenglish Error Elimination Drills", "Targeted 5-minute warm-ups each session to eradicate false friends (*control/reclamation*) permanently.")
    ]
    for title, desc in tools:
        p = tf2.add_paragraph()
        p.text = "• " + title
        p.font.size = Pt(11)
        p.font.bold = True
        p.font.color.rgb = C_TEXT_LIGHT
        p.space_before = Pt(8)
        p = tf2.add_paragraph()
        p.text = desc
        p.font.size = Pt(9.5)
        p.font.color.rgb = RGBColor(203, 213, 225)

    # Bottom Contact Bar
    bar_bot = add_card(s19, Inches(0.8), Inches(6.4), Inches(11.7), Inches(0.65), bg_color=RGBColor(16, 28, 52), border_color=C_PRIMARY)
    tf_b = bar_bot.text_frame
    tf_b.margin_left = tf_b.margin_right = tf_b.margin_top = tf_b.margin_bottom = Inches(0.12)
    p = tf_b.paragraphs[0]
    p.text = "Client: Vojtěch Berger | AL INVEST Břidličná, a.s. | Packaging Division | Vojtech.Berger@alinvest.cz"
    p.font.size = Pt(10)
    p.font.bold = True
    p.font.color.rgb = C_PRIMARY_LIGHT
    p = tf_b.add_paragraph()
    p.text = "Course Instructor: Lee Routledge | Corporate English Hub | Bespoke Diagnostic Assessment"
    p.font.size = Pt(9.5)
    p.font.color.rgb = RGBColor(148, 163, 184)

    prs.save(output_pptx_path)
    print(f"[OK] Generated PPTX Deck: {output_pptx_path}")

if __name__ == "__main__":
    out_path = Path("Vojtech_Berger_Packaging_Quality_Football_Grammar_Deck.pptx")
    build_pptx_deck(out_path)
