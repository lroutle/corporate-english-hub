import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
catalog_path = ROOT / "scripts" / "curriculum_catalog.py"
content = catalog_path.read_text(encoding="utf-8")

alinvest_code = '''
def get_alinvest_packaging_curriculum():
    curriculum = []
    # A2 Foundation (001-020)
    a2_topics = [
        ("001", "Aluminium Foil Gauges, Alloy Types & Cleanroom PPE: Present Simple & Imperatives", "Foil Converting, Slitting & Cleanroom Operations", "Imperatives & Present Simple"),
        ("002", "Daily Slitting Routines & Web Tension Monitoring: Present Simple 3rd Person", "Foil Converting, Slitting & Cleanroom Operations", "Present Simple 3rd person singular -s"),
        ("003", "Yesterday's Coil Edge Trimming & Web Break Stoppages: Past Simple", "Quality Assurance, Pinhole Detection & Gauge Tolerances", "Past Simple regular & irregular verbs"),
        ("004", "Converting Hall Layout & Slitter Blade Locations: Prepositions of Place", "Foil Converting, Slitting & Cleanroom Operations", "Prepositions of Place (above, behind, next to)"),
        ("005", "Cleanroom Hygiene Rules & Food Contact Restrictions: Can & Must", "Lamination, Lacquering & Barrier Testing (BRCGS/ISO)", "Modal verbs (must, can, must not)"),
        ("006", "Selecting Quality Tools: Micrometers, Dyne Pens & Calipers", "Quality Assurance, Pinhole Detection & Gauge Tolerances", "Demonstratives & Countable Nouns"),
        ("007", "Foil Thickness Tolerances: Microns, Grammage & Tensile Units", "Quality Assurance, Pinhole Detection & Gauge Tolerances", "Numbers, units & decimals"),
        ("008", "Shift Handover Log: Reporting Converted Tonnage & Waste Percentage", "Foil Converting, Slitting & Cleanroom Operations", "Past Simple vs Present Simple"),
        ("009", "Coil Annealing Temperatures & Surface Hardness: Comparatives & Superlatives", "Foil Converting, Slitting & Cleanroom Operations", "Comparatives & Superlatives (thinner, highest)"),
        ("010", "Moving Master Coils: Prepositions of Motion (Into, Onto, Across)", "Foil Converting, Slitting & Cleanroom Operations", "Prepositions of Motion (into, onto, across)"),
        ("011", "Dyne Test Pen Chemicals & Solvent Stock: Quantifiers (Some, Any, Enough)", "Quality Assurance, Pinhole Detection & Gauge Tolerances", "Quantifiers (some, any, enough, too much)"),
        ("012", "Emergency Rewinder Stop & Safety Interlocks: Imperatives for Directives", "Foil Converting, Slitting & Cleanroom Operations", "Imperatives for Emergency Directives"),
        ("013", "Handling Solvent Lacquers & Retort Adhesives: Modal Verbs (Should, Must not)", "Lamination, Lacquering & Barrier Testing (BRCGS/ISO)", "Modal verbs (should, must not, have to)"),
        ("014", "Inline Pinhole Detector Faults: Present Continuous for Active Issues", "Quality Assurance, Pinhole Detection & Gauge Tolerances", "Present Continuous for Active Faults"),
        ("015", "Surface Dyne Level Checks & Wetting Frequency: Adverbs of Frequency", "Quality Assurance, Pinhole Detection & Gauge Tolerances", "Adverbs of Frequency (always, never, rarely)"),
        ("016", "Solvent Storage & ATEX Cleanroom Safety: Rules & Obligations", "Lamination, Lacquering & Barrier Testing (BRCGS/ISO)", "Rules & Obligations (have to, must not)"),
        ("017", "Replacing Slitting Circular Knives: Sequence Markers (First, Next, Then, Finally)", "Foil Converting, Slitting & Cleanroom Operations", "Sequence Markers (first, next, then, finally)"),
        ("018", "Logging Pinhole Counts & Surface Scratches: Past Simple Negatives & Questions", "Quality Assurance, Pinhole Detection & Gauge Tolerances", "Past Simple Negatives & Questions"),
        ("019", "Ordering Packaging Cores & Wooden End-Plugs: There is / There are", "Foil Converting, Slitting & Cleanroom Operations", "There is / There are & Quantifiers"),
        ("020", "Pre-Shipment Inspection & Pallet Wrapping: Compound Imperatives", "Quality Assurance, Pinhole Detection & Gauge Tolerances", "Compound Imperatives & Checklist Phrasing")
    ]
    for num, title, track, grammar in a2_topics:
        curriculum.append({
            "test_id": f"AL-PKG-A2-{num}", "title": title, "level": "A2", "category": "core",
            "workplace_track": track, "grammar_focus": grammar, "estimated_time_minutes": 10,
            "description": f"Foundational aluminium packaging quality module covering {title.lower()}."
        })

    # B1 Operational (001-020)
    b1_topics = [
        ("001", "Aluminium Foil Annealing Cycles: Past Simple vs Present Perfect", "Foil Converting, Slitting & Cleanroom Operations", "Past Simple vs Present Perfect"),
        ("002", "Standard Operating Procedures for Gravure Lacquer Coating: Passive Voice", "Lamination, Lacquering & Barrier Testing (BRCGS/ISO)", "Passive Voice in Process SOPs"),
        ("003", "Monitoring Web Tension Fluctuations: Present Simple vs Present Continuous", "Foil Converting, Slitting & Cleanroom Operations", "Present Simple vs Present Continuous"),
        ("004", "Preventing Pinhole Formation During High-Speed Cold Rolling: First & Second Conditionals", "Quality Assurance, Pinhole Detection & Gauge Tolerances", "First & Second Conditionals (If/When)"),
        ("005", "Investigating Delamination in Polyethylene-Aluminium Triplex Laminates: Modals of Deduction", "8D Root-Cause Problem Solving & Customer Claims", "Modal Verbs of Deduction (must be, can\\'t be)"),
        ("006", "Calibrating Optical Surface Inspection Cameras: Relative Clauses", "Quality Assurance, Pinhole Detection & Gauge Tolerances", "Relative Clauses (which, that, whose)"),
        ("007", "Heat-Seal Threshold & Dwell Time Testing: Time Clauses", "Lamination, Lacquering & Barrier Testing (BRCGS/ISO)", "Time Clauses (as soon as, until, once)"),
        ("008", "Reporting Raw Ingot Purity Discrepancies to Rolling Mill Suppliers: Reported Speech", "8D Root-Cause Problem Solving & Customer Claims", "Reported Speech & Reporting Verbs"),
        ("009", "Slitting Knife Wear & Burr Formation: Cause and Effect Connectors", "Foil Converting, Slitting & Cleanroom Operations", "Cause & Effect Connectors (due to, therefore)"),
        ("010", "Customer Complaint Investigation: Snack Pouch Oxygen Permeation: Past Continuous vs Past Simple", "8D Root-Cause Problem Solving & Customer Claims", "Past Continuous vs Past Simple"),
        ("011", "Evaluating Dyne Wetting Tension with Test Pens: Prepositions of Specification", "Quality Assurance, Pinhole Detection & Gauge Tolerances", "Prepositions of Specification (within, below, across)"),
        ("012", "Troubleshooting Solvent Retention in Lacquered Foil: Second Conditional", "Lamination, Lacquering & Barrier Testing (BRCGS/ISO)", "Second Conditional for Technical Troubleshooting"),
        ("013", "Cold-Form Blister Foil Deep-Drawing Performance: Phrasal Verbs", "Foil Converting, Slitting & Cleanroom Operations", "Technical Phrasal Verbs (carry out, set up, back off)"),
        ("014", "BRCGS Packaging Materials Internal Audit Findings: Passive Voice vs Active Voice", "Lamination, Lacquering & Barrier Testing (BRCGS/ISO)", "Passive vs Active in Quality Audits"),
        ("015", "Foil Gauge Profile Variations Across Web Width: Comparatives & Quantifiers", "Quality Assurance, Pinhole Detection & Gauge Tolerances", "Comparative Modifiers (substantially, slightly)"),
        ("016", "Responding to Client Non-Conformance Claims: Polite Business Correspondence", "8D Root-Cause Problem Solving & Customer Claims", "Polite Register & Professional Correspondence"),
        ("017", "Corona Treatment & Surface Oxidation Decay: Modal Verbs of Obligation", "Foil Converting, Slitting & Cleanroom Operations", "Modals of Obligation (shall, must, ought to)"),
        ("018", "Tensile Peel Strength Testing on Autoclave Retort Pouches: Sequence & Process Flow", "Lamination, Lacquering & Barrier Testing (BRCGS/ISO)", "Sequence & Process Connectors"),
        ("019", "Investigating Coil Telescoping During Rewind: Third Conditional", "Foil Converting, Slitting & Cleanroom Operations", "Third Conditional for Root-Cause Failures"),
        ("020", "End-of-Month Scrap Rate Analysis & Yield Optimization: Discourse Markers", "Quality Assurance, Pinhole Detection & Gauge Tolerances", "Discourse Markers & Trend Descriptions")
    ]
    for num, title, track, grammar in b1_topics:
        curriculum.append({
            "test_id": f"AL-PKG-B1-{num}", "title": title, "level": "B1", "category": "core",
            "workplace_track": track, "grammar_focus": grammar, "estimated_time_minutes": 15,
            "description": f"Intermediate packaging quality module covering {title.lower()}."
        })

    # B2 Upper-Intermediate (001-020)
    b2_topics = [
        ("001", "8D CAPA Methodology: Root Cause Identification for Micro-Perforations: Past Modals of Deduction", "8D Root-Cause Problem Solving & Customer Claims", "Past Modals of Deduction (must have been, could not have)"),
        ("002", "BRCGS Food Contact Migration Compliance: EU Regulation 10/2011: Passive Reporting Verbs", "Lamination, Lacquering & Barrier Testing (BRCGS/ISO)", "Passive Reporting Verbs (it is asserted, was demonstrated)"),
        ("003", "Multi-Layer Barrier Integrity Under Extreme Retort Sterilization: Mixed Conditionals", "Lamination, Lacquering & Barrier Testing (BRCGS/ISO)", "Mixed Conditionals (Unreal Past & Present Result)"),
        ("004", "Audit Non-Conformity Justification to Multinational Confectionery Clients: Subjunctive Mood", "8D Root-Cause Problem Solving & Customer Claims", "Subjunctive Mood in Quality Directives"),
        ("005", "Ultrasonic & Thermal Heat-Seal Integrity Under Hydrostatic Pressure: Complex Participle Clauses", "Quality Assurance, Pinhole Detection & Gauge Tolerances", "Participle Clauses (Having observed, Being exposed)"),
        ("006", "Surface Energy Decay & Storage Aging in Corona-Treated Aluminium: Inversion After Negative Adverbials", "Foil Converting, Slitting & Cleanroom Operations", "Inversion After Negative Adverbials (Seldom, Rarely)"),
        ("007", "Defending Gauge Tolerances in Pharmaceutical Push-Through Blister Foil: Concession & Contrast", "Quality Assurance, Pinhole Detection & Gauge Tolerances", "Concession Clauses (Notwithstanding, Whereas)"),
        ("008", "Resolving Interlaminar Delamination Under Dynamic Flex-Crack Stress: Cleft Sentences", "8D Root-Cause Problem Solving & Customer Claims", "Cleft Sentences for Emphasis (It was the lacquer thickness that...)"),
        ("009", "High-Speed Laser Pinhole Scanner Sensitivity & Optical Scatter Calibration: Nominalization", "Quality Assurance, Pinhole Detection & Gauge Tolerances", "Technical Nominalization & Complex Noun Phrases"),
        ("010", "ISO 9001:2015 Risk-Based Quality Management in Cleanroom Slitting: Deontic vs Epistemic Modals", "Lamination, Lacquering & Barrier Testing (BRCGS/ISO)", "Deontic vs Epistemic Modality"),
        ("011", "Residual Solvent Chromatography in Food-Grade Printed Foil: Advanced Relative Clauses", "Lamination, Lacquering & Barrier Testing (BRCGS/ISO)", "Advanced Relative Clauses (in which case, whereby)"),
        ("012", "Evaluating High-Barrier Aluminium Blister Moisture Permeation (WVTR): Conditional Inversion", "Quality Assurance, Pinhole Detection & Gauge Tolerances", "Inverted Conditionals (Had the seal exceeded, Should the foil fail)"),
        ("013", "Customer Quality SLA Negotiation for Coffee Capsule Aluminium Lids: Diplomatic Language", "8D Root-Cause Problem Solving & Customer Claims", "Diplomatic Persuasion & Conditional Concessions"),
        ("014", "Alloy Grain Size & Intergranular Corrosion in Acidic Food Packaging: Adjective-Noun Collocations", "Quality Assurance, Pinhole Detection & Gauge Tolerances", "Dense Technical Collocations & Register"),
        ("015", "Inline Viscosity Control in Solvent-Based Vinyl Lacquering: Complex Prepositional Phrases", "Lamination, Lacquering & Barrier Testing (BRCGS/ISO)", "Compound Prepositions (in accordance with, with respect to)"),
        ("016", "Root-Cause Failure Analysis of Slitter Edge Burr Induced Tearing: Rhetorical Framing", "8D Root-Cause Problem Solving & Customer Claims", "Rhetorical Framing & Logical Deduction"),
        ("017", "Comparing Water-Based vs Solvent-Based Primer Emissions (VOC): Advanced Comparative Structures", "Lamination, Lacquering & Barrier Testing (BRCGS/ISO)", "Proportional Comparatives (the more volatile, the greater)"),
        ("018", "Coil Winding Tension Profiling to Prevent Centre Sag & Wrinkling: Participial Adjectives", "Foil Converting, Slitting & Cleanroom Operations", "Participial Adjectives & Compound Modifiers"),
        ("019", "Audit Defense Against Allergen Cross-Contamination in Shared Converting Halls: Evidential Stance", "Lamination, Lacquering & Barrier Testing (BRCGS/ISO)", "Evidential Markers & Authorial Stance"),
        ("020", "Statistical Process Control (SPC) Capability Indices (Cp, Cpk) in Rolling Mills: Quantifying Precision", "Quality Assurance, Pinhole Detection & Gauge Tolerances", "Statistical Precision & Modifiers of Degree")
    ]
    for num, title, track, grammar in b2_topics:
        curriculum.append({
            "test_id": f"AL-PKG-B2-{num}", "title": title, "level": "B2", "category": "core",
            "workplace_track": track, "grammar_focus": grammar, "estimated_time_minutes": 15,
            "description": f"Upper-intermediate aluminium packaging engineering module investigating {title.lower()}."
        })

    # C1 Advanced (001-020)
    c1_topics = [
        ("001", "Forensic Delamination Inquest: Triplex Barrier Foil in Retort Pouch Sterilization: Negative Inversion", "8D Root-Cause Problem Solving & Customer Claims", "Negative Inversion & Forensic Causality"),
        ("002", "BRCGS Issue 6 Global Standard Certification Audit Defense: Deontic Modality & Regulatory Mandates", "Lamination, Lacquering & Barrier Testing (BRCGS/ISO)", "Deontic Modals & Regulatory Shall"),
        ("003", "Catastrophic Seal Rupture Under Autoclave Back-Pressure: Multi-Physics Failure Report", "8D Root-Cause Problem Solving & Customer Claims", "Epistemic Hedging in Liability Disputes"),
        ("004", "Patent Arbitration: Cold-Formable Barrier Foil Alloy Composition (EN AW-8021B): Legal Syntax", "Quality Assurance, Pinhole Detection & Gauge Tolerances", "Litigation Syntax & Counter-Argumentation"),
        ("005", "Non-Intentionally Added Substances (NIAS) Toxicological Risk Assessment: High-Register Scientific Discourse", "Lamination, Lacquering & Barrier Testing (BRCGS/ISO)", "Toxicological Register & Dense Nominalization"),
        ("006", "Multinational Supplier Quality Agreement (SQA) Warranty & Indemnity Clauses: Contractual Subjunctive", "8D Root-Cause Problem Solving & Customer Claims", "Contractual Subjunctive & Risk Mitigation"),
        ("007", "Stochastic Finite Element Modeling of Foil Micro-Necking Under High-Speed Deep Draw", "Quality Assurance, Pinhole Detection & Gauge Tolerances", "Advanced Participle Density & Syntactic Embedding"),
        ("008", "Global Extended Producer Responsibility (EPR) & Aluminium Recyclability Mandates (PPWR)", "Lamination, Lacquering & Barrier Testing (BRCGS/ISO)", "Policy Argumentation & Environmental Directives"),
        ("009", "Autonomous Inline Hyperspectral Defect Classification & Sensor Redundancy", "Quality Assurance, Pinhole Detection & Gauge Tolerances", "Techno-Scientific Qualification of System Limits"),
        ("010", "Aero-Thermal Thermodynamics in Continuous Coil Annealing Furnaces", "Foil Converting, Slitting & Cleanroom Operations", "Stylistic Fronting & Structural Inversion"),
        ("011", "Expert Witness Deposition: Food Recall Induced by Pinholes in Aseptic Beverage Cartons", "8D Root-Cause Problem Solving & Customer Claims", "Forensic Deposition & Cross-Examination Syntax"),
        ("012", "Cleanroom HVAC Micro-Particulate Certification Under ISO 14644-1: Normative Standards", "Foil Converting, Slitting & Cleanroom Operations", "Normative Directives & Compliance Phrasing"),
        ("013", "Interfacial Adhesion Chemistry: Silane Primers vs Polyurethane Adhesives: High Register", "Lamination, Lacquering & Barrier Testing (BRCGS/ISO)", "Nuanced Stance & Authorial Confidence Markers"),
        ("014", "Carbon Footprint Life Cycle Assessment (LCA) for Primary Smelted vs Recycled Aluminium", "Foil Converting, Slitting & Cleanroom Operations", "Life Cycle Carbon Accounting Register"),
        ("015", "Supply Chain Force Majeure Invocation Following Global Bauxite Export Restrictions", "8D Root-Cause Problem Solving & Customer Claims", "Contractual Liability & Exemption Formulas"),
        ("016", "Nanoscale Surface Roughness Profilometry & Contact Angle Goniometry in Foil Wettability", "Quality Assurance, Pinhole Detection & Gauge Tolerances", "Academic Laboratory Register & Passive Density"),
        ("017", "Executive Board Defense of Capital Investment in High-Speed Converting Slitters", "Foil Converting, Slitting & Cleanroom Operations", "Executive Persuasion & Strategic Hedging"),
        ("018", "Cross-Border Commercial Quality Dispute Arbitration Under UNCITRAL Rules", "8D Root-Cause Problem Solving & Customer Claims", "Legalistic Conditionals & Arbitration Terminology"),
        ("019", "Predictive Maintenance Algorithms for Dynamic Vibration Monitoring on Rolling Mills", "Foil Converting, Slitting & Cleanroom Operations", "Algorithmic Precision & Computational Phrasing"),
        ("020", "Bilateral Technical Quality Protocol for Pharmaceutical Blister Packaging Supply to Tier-1 Clients", "Quality Assurance, Pinhole Detection & Gauge Tolerances", "Bilateral Treaty & Quality Protocol Formulation")
    ]
    for num, title, track, grammar in c1_topics:
        curriculum.append({
            "test_id": f"AL-PKG-C1-{num}", "title": title, "level": "C1", "category": "core",
            "workplace_track": track, "grammar_focus": grammar, "estimated_time_minutes": 20,
            "description": f"Mastery-tier packaging quality leadership module examining {title.lower()}."
        })

    return curriculum
'''

# Update ALL_CURRICULA dictionary
old_all = '''ALL_CURRICULA = {
    "tatra-engineering": get_tatra_eng_curriculum,
    "tatra-sales-engineering": get_tatra_sales_curriculum,
    "tapi-engineering": get_tapi_eng_curriculum,
    "teva-engineering": get_tapi_eng_curriculum,
    "tapi-chemistry": get_tapi_chem_curriculum,
    "tapi-it": get_tapi_it_curriculum,
    "teva-it": get_tapi_it_curriculum,
    "bidfood-purchasing": get_bidfood_purchasing_curriculum,
    "bidfood-engineering": get_bidfood_engineering_curriculum
}'''

new_all = '''ALL_CURRICULA = {
    "tatra-engineering": get_tatra_eng_curriculum,
    "tatra-sales-engineering": get_tatra_sales_curriculum,
    "tapi-engineering": get_tapi_eng_curriculum,
    "teva-engineering": get_tapi_eng_curriculum,
    "tapi-chemistry": get_tapi_chem_curriculum,
    "tapi-it": get_tapi_it_curriculum,
    "teva-it": get_tapi_it_curriculum,
    "bidfood-purchasing": get_bidfood_purchasing_curriculum,
    "bidfood-engineering": get_bidfood_engineering_curriculum,
    "alinvest-packaging": get_alinvest_packaging_curriculum
}'''

if "def get_alinvest_packaging_curriculum" not in content:
    idx = content.find("ALL_CURRICULA = {")
    content = content[:idx] + alinvest_code + "\n" + content[idx:]
    content = content.replace(old_all, new_all)
    catalog_path.write_text(content, encoding="utf-8")
    print("Successfully added get_alinvest_packaging_curriculum to curriculum_catalog.py")
else:
    print("get_alinvest_packaging_curriculum already exists in curriculum_catalog.py")
