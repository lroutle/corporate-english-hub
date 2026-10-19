"""
Comprehensive 400-Module Curriculum Catalog for 5 Independent Corporate Testing Suites.
80 Modules per suite: 20 A2 Foundation, 20 B1 Operational, 20 B2 Advanced, 20 C2 Mastery.
"""

def get_tatra_eng_curriculum():
    curriculum = []
    # A2 (001-020)
    a2_topics = [
        ("001", "Workshop Tools, Fasteners & PPE: Present Simple & Imperatives", "Workshop Assembly & Line Tooling", "Imperatives & Present Simple"),
        ("002", "Daily Shift Routines & Machine Operation: Present Simple", "Workshop Assembly & Line Tooling", "Present Simple 3rd person -s"),
        ("003", "Yesterday's Workshop Faults & Defective Parts: Past Simple", "Quality Assurance, Inspection & Torque Verification", "Past Simple regular & irregular"),
        ("004", "Chassis Geometry & Tool Locations: Prepositions of Place", "Central Backbone Tube & Chassis R&D", "Prepositions of Place (under, between, on)"),
        ("005", "Plant Warning Signs & Crane Safety: Can & Must", "Workshop Assembly & Line Tooling", "Modal verbs (must, can, must not)"),
        ("006", "Hand Tool Selection: Wrenches, Sockets & Screwdrivers", "Workshop Assembly & Line Tooling", "Demonstratives & Countable Nouns"),
        ("007", "Workplace Measurements: Millimeters, Bar & Kilograms", "Quality Assurance, Inspection & Torque Verification", "Numbers, units & decimals"),
        ("008", "Shift Handover Notes: Reporting Daily Output", "Workshop Assembly & Line Tooling", "Past Simple vs Present Simple"),
        ("009", "Vehicle Tyre Pressures & Wheel Nut Torques", "Suspension, Half-Axles & CTIS Diagnostics", "Adjectives & Comparatives (higher, tighter)"),
        ("010", "Assembly Line Parts Staging & Storage Bins", "Workshop Assembly & Line Tooling", "Prepositions of Direction (into, onto, across)"),
        ("011", "Engine Fluid Checks: Coolant, Oil & Brake Fluid", "Powertrain & Engine Systems (Air-cooled V8 & Cummins)", "Quantifiers (some, any, enough, too much)"),
        ("012", "Workshop Emergency Procedures & Fire Extinguishers", "Workshop Assembly & Line Tooling", "Imperatives for Emergency Directives"),
        ("013", "Battery Handling, Charging & High-Voltage Warnings", "Powertrain & Engine Systems (Air-cooled V8 & Cummins)", "Modal verbs (should, must not, have to)"),
        ("014", "Pneumatic Hose Routing & Air Leak Inspections", "Suspension, Half-Axles & CTIS Diagnostics", "Present Continuous for Active Faults"),
        ("015", "Welding Shop Safety & Protective Gear", "Workshop Assembly & Line Tooling", "Adverbs of Frequency (always, never, rarely)"),
        ("016", "Cleaning Solvent Storage & Ventilation Guidelines", "Workshop Assembly & Line Tooling", "Rules & Obligations (have to, don't have to)"),
        ("017", "Chassis Painting & Surface Degreasing Steps", "Workshop Assembly & Line Tooling", "Sequence Markers (first, then, next, finally)"),
        ("018", "Reporting Broken Drills & Damaged Cutting Inserts", "Quality Assurance, Inspection & Torque Verification", "Past Simple Negatives & Questions"),
        ("019", "Spare Bolt Ordering: Part Numbers & Quantities", "Workshop Assembly & Line Tooling", "There is / There are & Quantifiers"),
        ("020", "End-of-Shift Cleaning & Lockout Procedures", "Workshop Assembly & Line Tooling", "Compound Imperatives & Checklist Phrasing")
    ]
    for num, title, track, grammar in a2_topics:
        curriculum.append({
            "test_id": f"TTR-ENG-A2-{num}", "title": title, "level": "A2", "category": "core",
            "workplace_track": track, "grammar_focus": grammar, "estimated_time_minutes": 10,
            "description": f"Foundational workplace English module covering {title.lower()}."
        })

    # B1 (001-020)
    b1_topics = [
        ("001", "Chassis Assembly & Torque Verification: Past Simple vs Past Perfect", "Central Backbone Tube & Chassis R&D", "Past Simple vs Past Perfect"),
        ("002", "Swinging Half-Axles Alignment & Differential Gear Setup", "Suspension, Half-Axles & CTIS Diagnostics", "Passive Voice in Assembly SOPs"),
        ("003", "Shift Handover & Daily Line Routines: Present Simple vs Continuous", "Workshop Assembly & Line Tooling", "Present Simple vs Present Continuous"),
        ("004", "Central Tire Inflation System (CTIS) Leak Diagnostics", "Suspension, Half-Axles & CTIS Diagnostics", "First & Second Conditionals (If/When)"),
        ("005", "Air Suspension Bellows Replacement: Sequence & Safety", "Suspension, Half-Axles & CTIS Diagnostics", "Prepositions of Cause & Manner"),
        ("006", "Powertrain Mounting & Vibration Damper Calibration", "Powertrain & Engine Systems (Air-cooled V8 & Cummins)", "Relative Clauses (which, that, whose)"),
        ("007", "Hydraulic Steering Circuit Pressure Testing & Troubleshooting", "Suspension, Half-Axles & CTIS Diagnostics", "Modal Verbs of Probability (must be, can't be)"),
        ("008", "Air-Cooled V8 Engine Overhaul & Cylinder Head Torquing", "Powertrain & Engine Systems (Air-cooled V8 & Cummins)", "Past Continuous vs Past Simple"),
        ("009", "Transmission Gearbox Flange Sealing & O-Ring Selection", "Powertrain & Engine Systems (Air-cooled V8 & Cummins)", "Present Perfect with yet, already, just"),
        ("010", "Driveline Propeller Shaft Balancing & Runout Tolerances", "Central Backbone Tube & Chassis R&D", "Degrees of Comparison & Tolerances"),
        ("011", "Pneumatic Dual-Circuit Brake Actuator Adjustment", "Suspension, Half-Axles & CTIS Diagnostics", "Purpose Clauses (in order to, so that)"),
        ("012", "Chassis Weld Inspection: Ultrasonic Testing & NDT Reporting", "Quality Assurance, Inspection & Torque Verification", "Passive Voice Reporting Forms"),
        ("013", "Cold Weather Pre-Heating Systems (Webasto) Diagnostics", "Powertrain & Engine Systems (Air-cooled V8 & Cummins)", "Conditionals in Diagnostic Troubleshooting"),
        ("014", "Differential Lock Pneumatic Actuator Synchronization", "Suspension, Half-Axles & CTIS Diagnostics", "Temporal Conjunctions (until, as soon as, while)"),
        ("015", "Cooling Fan Hydrostatic Drive Leak Troubleshooting", "Powertrain & Engine Systems (Air-cooled V8 & Cummins)", "Phrasal Verbs in Mechanical Repair"),
        ("016", "Prototype Test Track Rig Setup & Accelerometer Sensor Calibration", "Vehicle Homologation & NATO STANAG Mobility", "Passive Voice with Modals"),
        ("017", "Leaf Spring Shackle Bushing Wear & Replacement Guidelines", "Suspension, Half-Axles & CTIS Diagnostics", "Present Perfect Continuous (duration)"),
        ("018", "Supplier Quality Audits: Fastener Tensile Strength Non-Conformance", "Quality Assurance, Inspection & Torque Verification", "Reported Speech in Quality Audits"),
        ("019", "Electrical Wiring Harness Routing Across the Backbone Tube", "Central Backbone Tube & Chassis R&D", "Prepositions of Motion & Spatial Arrangement"),
        ("020", "Pre-Delivery Road Test Inspection: Defect Punch-List Reporting", "Quality Assurance, Inspection & Torque Verification", "Cause & Effect Connectors (due to, owing to)")
    ]
    for num, title, track, grammar in b1_topics:
        curriculum.append({
            "test_id": f"TTR-ENG-B1-{num}", "title": title, "level": "B1", "category": "core",
            "workplace_track": track, "grammar_focus": grammar, "estimated_time_minutes": 15,
            "description": f"Intermediate technical English module analyzing {title.lower()}."
        })

    # B2 (001-020)
    b2_topics = [
        ("001", "Torsional Stiffness & Finite Element Analysis: Mixed Conditionals", "Central Backbone Tube & Chassis R&D", "Mixed Conditionals in Structural Analysis"),
        ("002", "NATO STANAG 4380 Mobility Trials & Trench Crossing Validation", "Vehicle Homologation & NATO STANAG Mobility", "Negative Inversion for Professional Rigor"),
        ("003", "CAN-Bus Heavy Vehicle Telemetry & J1939 Protocol Diagnostics", "Powertrain & Engine Systems (Air-cooled V8 & Cummins)", "Complex Passive Structures & Participles"),
        ("004", "Hydrostatic Fan Drive Efficiency vs Parasitic Engine Load Modeling", "Powertrain & Engine Systems (Air-cooled V8 & Cummins)", "Hedging & Modality in Technical Papers"),
        ("005", "Independent Swinging Half-Axle Camber Angles Under Dynamic Load", "Suspension, Half-Axles & CTIS Diagnostics", "Third Conditional in Failure Analyses"),
        ("006", "Extreme Desert & Arctic Thermal Performance Validation Testing", "Vehicle Homologation & NATO STANAG Mobility", "Subjunctive in Environmental Test Standards"),
        ("007", "Drivetrain Gear Tooth Pitting & Metallurgical Fatigue Inquests", "Forensic Failure Analysis & Structural Metallurgy", "Inverted Conditionals (Had the gear been...)"),
        ("008", "Chassis Frame Anti-Corrosion Cataphoretic Coating Specifications", "Workshop Assembly & Line Tooling", "Nominalization in Engineering Specs"),
        ("009", "Multi-Axle Steering Geometry (8x8 and 10x10) Dynamic Simulation", "Suspension, Half-Axles & CTIS Diagnostics", "Participial Clauses for Concise Descriptions"),
        ("010", "Modular Armor Cabin Ballistic Protection (STANAG 4569 Level 3)", "Vehicle Homologation & NATO STANAG Mobility", "Deontic vs Epistemic Modals in Defense"),
        ("011", "Exhaust After-Treatment System (SCR / AdBlue) Emission Compliance", "Powertrain & Engine Systems (Air-cooled V8 & Cummins)", "Complex Relative Clauses & Concessives"),
        ("012", "Propshaft Universal Joint Angularity & Driveline Torsional Vibration", "Central Backbone Tube & Chassis R&D", "Gerund vs Infinitive Nuances"),
        ("013", "Hydraulic Retarder Braking Curves Under Full GVM Descent", "Suspension, Half-Axles & CTIS Diagnostics", "Adverbial Clauses of Contrast & Condition"),
        ("014", "Winch Recovery Cable Tensile Failure: Forensic Metallurgical Inquest", "Forensic Failure Analysis & Structural Metallurgy", "Causative Verbs & Passive Reporting"),
        ("015", "All-Wheel Drive Inter-Axle Differential Lock Automated Logic", "Suspension, Half-Axles & CTIS Diagnostics", "Subjunctive Mood in Software System Specs"),
        ("016", "Air-Cooled Engine Thermal Gradient Finite Element Verification", "Powertrain & Engine Systems (Air-cooled V8 & Cummins)", "Complex Linking Words in R&D Papers"),
        ("017", "Titanium-Alloy Suspension Spring Prototype Weight Reduction Audit", "Central Backbone Tube & Chassis R&D", "Hypothetical Conditional Structures"),
        ("018", "Tire Footprint Deformation Analysis Under CTIS Low-Pressure Sand Mode", "Suspension, Half-Axles & CTIS Diagnostics", "Nuanced Comparative Phrasing in Research"),
        ("019", "Chassis Resonance Frequency & Cab Shake Isolator Damper Tuning", "Vehicle Homologation & NATO STANAG Mobility", "Participial Modifiers & Complex Nominal Groups"),
        ("020", "ECE R29 Cabin Crash-Worthiness & Impact Energy Absorption Inquest", "Vehicle Homologation & NATO STANAG Mobility", "Inversion After Negative & Restrictive Phrases")
    ]
    for num, title, track, grammar in b2_topics:
        curriculum.append({
            "test_id": f"TTR-ENG-B2-{num}", "title": title, "level": "B2", "category": "core",
            "workplace_track": track, "grammar_focus": grammar, "estimated_time_minutes": 15,
            "description": f"Upper-intermediate engineering module investigating {title.lower()}."
        })

    # C2 (001-020)
    c2_topics = [
        ("001", "Forensic Failure Analysis, Structural Metallurgy & NATO Offsets", "Forensic Failure Analysis & Structural Metallurgy", "Negative Inversion & Nuanced Hedging"),
        ("002", "Intergovernmental Military Vehicle Procurement & Defense Treaty Compliance", "Vehicle Homologation & NATO STANAG Mobility", "Diplomatic Subjunctive & Treaty Nomenclature"),
        ("003", "Catastrophic Drivetrain Shear Fracture: Multi-Physics Forensic Inquest", "Forensic Failure Analysis & Structural Metallurgy", "Epistemic Hedging in Legal Inquests"),
        ("004", "Patent Infringement Arbitration: Central Backbone Tube Tubular Backbone Concept", "Central Backbone Tube & Chassis R&D", "Litigation Syntax & Counter-Argumentation"),
        ("005", "Hydrogen Embrittlement in High-Tensile Axle Flange Fasteners", "Forensic Failure Analysis & Structural Metallurgy", "High-Register Scientific Discourse"),
        ("006", "Multi-National Joint Venture Technology Transfer & IP Protection Clauses", "Vehicle Homologation & NATO STANAG Mobility", "Contractual Subjunctive & Risk Mitigation"),
        ("007", "Stochastic Dynamic Load Life Prediction Under Severe Off-Road Torture Rigs", "Central Backbone Tube & Chassis R&D", "Advanced Participle Clauses & Density"),
        ("008", "Ballistic & Mine-Blast Shock Wave Propagation Through Modular Armor Cabins", "Vehicle Homologation & NATO STANAG Mobility", "Complex Cause-Effect Nominal Constructions"),
        ("009", "Autonomous Military Convoy Platooning Protocol Functional Safety (ISO 26262)", "Vehicle Homologation & NATO STANAG Mobility", "Regulatory Imperatives & Deontic Modality"),
        ("010", "Aero-Thermal Engine Bay Fluid Dynamics in 55°C Ambient Desert Operations", "Powertrain & Engine Systems (Air-cooled V8 & Cummins)", "Stylistic Fronting & Structural Inversion"),
        ("011", "Expert Witness Deposition: Multi-Axle Roll-Over Dynamic Stability Inquest", "Vehicle Homologation & NATO STANAG Mobility", "Forensic Deposition & Cross-Examination Syntax"),
        ("012", "Electro-Hydraulic Steer-by-Wire Redundancy Architecture Legal Certification", "Suspension, Half-Axles & CTIS Diagnostics", "Normative Directives & Mandatory Shall"),
        ("013", "Composite Material Delamination in Lightweight Heavy-Duty Drivelines", "Forensic Failure Analysis & Structural Metallurgy", "Nuanced Stance & Authorial Confidence Markers"),
        ("014", "Lifecycle Environmental Sustainability & EU Heavy-Duty Fleet CO2 Mandates", "Powertrain & Engine Systems (Air-cooled V8 & Cummins)", "Policy Argumentation & Counter-Claims"),
        ("015", "Supply Chain Force Majeure Invocations & Geopolitical Embargo Compliance", "Vehicle Homologation & NATO STANAG Mobility", "Contractual Liability & Exemption Clauses"),
        ("016", "Advanced Fatigue Crack Tip Plasticity Modeling in Forged Half-Axles", "Forensic Failure Analysis & Structural Metallurgy", "Academic Research Register & Passive Density"),
        ("017", "High-Register Executive Board Defense of Capital R&D Platform Investment", "Central Backbone Tube & Chassis R&D", "Executive Persuasion & Strategic Hedging"),
        ("018", "Cross-Border Warranty Dispute Arbitration Under UNCITRAL Model Law", "Quality Assurance, Inspection & Torque Verification", "Legalistic Conditionals & Arbitration Formulas"),
        ("019", "Autonomous Off-Road Vehicle Lidar Sensor Degradation Under Heavy Mud Splash", "Vehicle Homologation & NATO STANAG Mobility", "Techno-Scientific Qualification of Limits"),
        ("020", "Sovereign Defense Ministry Counter-Trade & Offset Fulfillment Inquest", "Vehicle Homologation & NATO STANAG Mobility", "Bilateral Intergovernmental Treaty Syntax")
    ]
    for num, title, track, grammar in c2_topics:
        curriculum.append({
            "test_id": f"TTR-ENG-C2-{num}", "title": title, "level": "C2", "category": "core",
            "workplace_track": track, "grammar_focus": grammar, "estimated_time_minutes": 20,
            "description": f"Mastery-tier forensic and executive engineering module examining {title.lower()}."
        })

    return curriculum

def get_tatra_sales_curriculum():
    curriculum = []
    # A2 (001-020)
    a2_topics = [
        ("001", "Customer Inquiries, Vehicle Pricing & Stock: Present Simple", "Customer Inquiries, Quotations & Specifications", "Present Simple for Vehicle Catalogs"),
        ("002", "Polite Email Requests to Foreign Dealers: Can, Could & Please", "Polite Business Communication & Dealership Correspondence", "Polite modals (could you, please, would)"),
        ("003", "Trade Fairs & Client Negotiations: Past Simple", "Commercial Negotiation & Payment Milestones", "Past Simple for Meetings & Visits"),
        ("004", "Truck Quantities, Weights & Prices: Numbers & Quantifiers", "Customer Inquiries, Quotations & Specifications", "Numbers, Prices, Currencies & Quantifiers"),
        ("005", "Delivery Deadlines & Shipping Schedules: Prepositions of Time", "Export Logistics & Incoterms 2020 (EXW, FCA, CPT, CIP, DAP, DDP)", "Prepositions of Time (at, on, in, by)"),
        ("006", "Booking Hotel & Airport Transfers for Foreign Delegations", "Polite Business Communication & Dealership Correspondence", "Future with going to & Present Continuous"),
        ("007", "Product Catalog Inquiries: Chassis Configurations & Axle Ratios", "Customer Inquiries, Quotations & Specifications", "Question Formation with Wh- Words"),
        ("008", "Writing Quotation Follow-Up Emails to Prospective Buyers", "Customer Inquiries, Quotations & Specifications", "Present Perfect with just & already"),
        ("009", "Confirming Spare Parts Orders & Invoice Totals", "Letters of Credit, Customs & Freight Documentation", "Verbs of Confirmation & Simple Modals"),
        ("010", "Dealing with Simple Delivery Delay Inquiries", "Export Logistics & Incoterms 2020 (EXW, FCA, CPT, CIP, DAP, DDP)", "Apologetic Phrasing & Present Continuous"),
        ("011", "Client Registration at the International Defense Expo", "Polite Business Communication & Dealership Correspondence", "Articles (a, an, the) & Demonstratives"),
        ("012", "Basic Payment Terms: Wire Transfers & Proforma Invoices", "Commercial Negotiation & Payment Milestones", "Imperatives & Polite Requests in Invoicing"),
        ("013", "Explaining Warranty Duration & Standard Coverage Limits", "Customer Inquiries, Quotations & Specifications", "Comparative Adjectives & Coverage Rules"),
        ("014", "Scheduling Online Video Demonstrations Across Time Zones", "Polite Business Communication & Dealership Correspondence", "Time Expressions & Availability Formulas"),
        ("015", "Foreign Dealership Contact Details & Directory Updates", "Polite Business Communication & Dealership Correspondence", "Personal Pronouns & Possessive Forms"),
        ("016", "Truck Color, Cabin Options & Custom Paint Requests", "Customer Inquiries, Quotations & Specifications", "Adjectives of Specification & Options"),
        ("017", "Inquiring About Sea Freight Container Availability", "Export Logistics & Incoterms 2020 (EXW, FCA, CPT, CIP, DAP, DDP)", "Polite Inquiries (Is there, Are there)"),
        ("018", "Handling Simple Pricing Objections on Base Chassis Models", "Commercial Negotiation & Payment Milestones", "Concessive Connectors (but, although)"),
        ("019", "Thank-You Notes Following Successful Factory Visits", "Polite Business Communication & Dealership Correspondence", "Formal Appreciation Formulas"),
        ("020", "Export Packaging Instructions for Humid Tropical Climates", "Export Logistics & Incoterms 2020 (EXW, FCA, CPT, CIP, DAP, DDP)", "Imperatives for Packing Guidelines")
    ]
    for num, title, track, grammar in a2_topics:
        curriculum.append({
            "test_id": f"TTR-SALES-A2-{num}", "title": title, "level": "A2", "category": "core",
            "workplace_track": track, "grammar_focus": grammar, "estimated_time_minutes": 10,
            "description": f"Foundational sales English module covering {title.lower()}."
        })

    # B1 (001-020)
    b1_topics = [
        ("001", "Spare Parts Dispatch & Export Clearance: Present Perfect vs Past Simple", "Export Logistics & Incoterms 2020 (EXW, FCA, CPT, CIP, DAP, DDP)", "Present Perfect vs Past Simple"),
        ("002", "Incoterms 2020 Obligations: EXW vs FCA vs DAP Risk Transfer", "Export Logistics & Incoterms 2020 (EXW, FCA, CPT, CIP, DAP, DDP)", "Passive Voice & Responsibility Clauses"),
        ("003", "Letter of Credit (L/C) Discrepancy Rectification with Issuing Banks", "Letters of Credit, Customs & Freight Documentation", "First Conditional & Temporal Clauses"),
        ("004", "Dealership Margin & Annual Sales Target Negotiations", "Commercial Negotiation & Payment Milestones", "Modals of Negotiation & Softening"),
        ("005", "Bill of Lading Amendments & Sea Freight Consignment Tracking", "Letters of Credit, Customs & Freight Documentation", "Present Perfect Continuous (tracking duration)"),
        ("006", "Government Fleet Tender Submission Checklist & Compliance Sheets", "Defense & Government Tenders (NATO STANAG Bids)", "Relative Clauses in Tender Criteria"),
        ("007", "Customs Bonded Warehouse Entry & Import Tariff Classification", "Letters of Credit, Customs & Freight Documentation", "Prepositions of Origin & Transit"),
        ("008", "Explaining Tatra Chassis Superiority in Mining & Off-Road Tenders", "Customer Inquiries, Quotations & Specifications", "Comparative & Superlative Structures"),
        ("009", "Contractual Liquidated Damages for Late Shipment: Avoiding Penalties", "Commercial Negotiation & Payment Milestones", "Second Conditional in Risk Assessment"),
        ("010", "End-User Certificate (EUC) Verification for Defense Export Control", "Defense & Government Tenders (NATO STANAG Bids)", "Passive Reporting Verbs"),
        ("011", "After-Sales Service Level Agreements (SLA) & Technician Dispatch", "Commercial Negotiation & Payment Milestones", "Future Continuous & Future Perfect"),
        ("012", "Foreign Currency Exchange Fluctuation Clauses in Long-Term Bids", "Commercial Negotiation & Payment Milestones", "Connectors of Cause, Purpose & Condition"),
        ("013", "Freight Forwarder Carrier Liability for Sea-Transit Salt Corrosion", "Export Logistics & Incoterms 2020 (EXW, FCA, CPT, CIP, DAP, DDP)", "Past Perfect for Sequence of Damage"),
        ("014", "Dealership Warranty Reimbursement Claim Verification & Auditing", "Polite Business Communication & Dealership Correspondence", "Modal Verbs of Deduction"),
        ("015", "Technical Deviation Requests from Tender Minimum Specifications", "Defense & Government Tenders (NATO STANAG Bids)", "Polite Assertiveness & Hedging"),
        ("016", "Roll-on/Roll-off (Ro-Ro) Vessel Stevedore Loading Coordination", "Export Logistics & Incoterms 2020 (EXW, FCA, CPT, CIP, DAP, DDP)", "Phrasal Verbs in Maritime Logistics"),
        ("017", "Counter-Trade Offsets: Local Assembly Kit (CKD) Proposals", "Defense & Government Tenders (NATO STANAG Bids)", "Reported Speech in Government Meetings"),
        ("018", "Distributor Termination Warnings Due to Contractual Non-Performance", "Polite Business Communication & Dealership Correspondence", "Conditional Structures & Legal Directives"),
        ("019", "Tender Performance Bond Bank Guarantees & Escrow Accounts", "Commercial Negotiation & Payment Milestones", "Obligation Verbs (shall, must, undertake)"),
        ("020", "Post-Sale Customer Satisfaction Audits & Fleet Utilization Reviews", "Customer Inquiries, Quotations & Specifications", "Evaluative Adjectives & Feedback Syntax")
    ]
    for num, title, track, grammar in b1_topics:
        curriculum.append({
            "test_id": f"TTR-SALES-B1-{num}", "title": title, "level": "B1", "category": "core",
            "workplace_track": track, "grammar_focus": grammar, "estimated_time_minutes": 15,
            "description": f"Intermediate sales and logistics module analyzing {title.lower()}."
        })

    # B2 (001-020)
    b2_topics = [
        ("001", "High-Stakes Defense Tender Bargaining: Inversion for Emphasis", "Defense & Government Tenders (NATO STANAG Bids)", "Inversion for Diplomatic Emphasis"),
        ("002", "NATO STANAG Homologation Defense Bid Deviations & Exceptions", "Defense & Government Tenders (NATO STANAG Bids)", "Subjunctive in Contractual Deviations"),
        ("003", "Commercial Contract Risk Mitigation: Force Majeure & Hardship Clauses", "International Defense Tender Arbitration & ICC Contracts", "Third Conditional in Contract Breach"),
        ("004", "Exclusive Master Dealership Territory Rights & Non-Compete Clauses", "Commercial Negotiation & Payment Milestones", "Restrictive & Non-Restrictive Relative Clauses"),
        ("005", "Multi-Million Euro Tender Financing: Export Credit Agency (EGAP) Guarantees", "Commercial Negotiation & Payment Milestones", "Passive Causative & Financial Modals"),
        ("006", "Sovereign Debt Repayment Default Safeguards in UN Mining Concessions", "Commercial Negotiation & Payment Milestones", "Mixed Conditionals in Sovereign Risk"),
        ("007", "Competitive Defense Tender Inquests Against Western European Truck OEMs", "Defense & Government Tenders (NATO STANAG Bids)", "Counter-Argumentative Discourse Markers"),
        ("008", "Multilateral Consortium Joint Bidding Governance & Liability Allocation", "Defense & Government Tenders (NATO STANAG Bids)", "Complex Nominalizations in Contracts"),
        ("009", "Liquidated Damages Dispute Escalation & Mediation Protocols", "International Defense Tender Arbitration & ICC Contracts", "Formal Diplomatic Hedging"),
        ("010", "Anti-Bribery & FCPA Compliance Certification in International Sales", "Defense & Government Tenders (NATO STANAG Bids)", "Mandative Subjunctive & Legal Directives"),
        ("011", "Defense Offset Industrial Participation Agreements: Technology Transfer", "Defense & Government Tenders (NATO STANAG Bids)", "Participle Clauses in Trade Agreements"),
        ("012", "Sanctions Screening & Dual-Use Export Control Compliance Verification", "Export Logistics & Incoterms 2020 (EXW, FCA, CPT, CIP, DAP, DDP)", "Negative Restrictive Adverbials"),
        ("013", "Customs Valuation Audits on Intercompany Transfer Pricing", "Letters of Credit, Customs & Freight Documentation", "Complex Prepositional Phrases"),
        ("014", "Heavy Mining Fleet Full-Life Maintenance & Repair Contract (MARC) Bids", "Commercial Negotiation & Payment Milestones", "Conditional Concessives (even if, provided that)"),
        ("015", "Dealer Network De-Stocking Strategies During Global Supply Chain Shocks", "Polite Business Communication & Dealership Correspondence", "Hypothetical Inversion in Financial Forecasting"),
        ("016", "Bid Bond Forfeiture Risk Management During Political Upheaval", "Defense & Government Tenders (NATO STANAG Bids)", "Unreal Past Conditionals with Modals"),
        ("017", "Maritime General Average Declarations & Cargo Insurance Litigation", "Export Logistics & Incoterms 2020 (EXW, FCA, CPT, CIP, DAP, DDP)", "Passive Constructions in Marine Law"),
        ("018", "Tender Protests & Legal Appeals Against Biased Procurement Specifications", "Defense & Government Tenders (NATO STANAG Bids)", "Adversative Conjunctions & Legal Stance"),
        ("019", "Tripartite Trade Financing via Irrevocable Confirmed Letters of Credit", "Letters of Credit, Customs & Freight Documentation", "Verbs of Binding Legal Undertaking"),
        ("020", "Key Account Executive Presentations to General Staff Military Procurement", "Defense & Government Tenders (NATO STANAG Bids)", "Rhetorical Fronting & Nuanced Persuasion")
    ]
    for num, title, track, grammar in b2_topics:
        curriculum.append({
            "test_id": f"TTR-SALES-B2-{num}", "title": title, "level": "B2", "category": "core",
            "workplace_track": track, "grammar_focus": grammar, "estimated_time_minutes": 15,
            "description": f"Upper-intermediate commercial and defense sales module analyzing {title.lower()}."
        })

    # C2 (001-020)
    c2_topics = [
        ("001", "International Defense Tender Arbitration, ICC Jurisdiction & Force Majeure", "International Defense Tender Arbitration & ICC Contracts", "Contractual Subjunctive & Risk Hedging"),
        ("002", "Sovereign Debt Default & Paris Club Intergovernmental Rescheduling", "Commercial Negotiation & Payment Milestones", "Intergovernmental Treaty Syntax"),
        ("003", "Cross-Border Patent Invalidation Defense in Military All-Wheel Drive", "International Defense Tender Arbitration & ICC Contracts", "Litigation Counter-Plea Formulas"),
        ("004", "Geopolitical Embargo Repudiation & Bilateral Defense Supply Arbitration", "International Defense Tender Arbitration & ICC Contracts", "Deontic Inversion & Diplomatic Reserve"),
        ("005", "Multi-Billion Dollar NATO Framework Agreement Defense Consortium Inquest", "Defense & Government Tenders (NATO STANAG Bids)", "High-Register Executive Governance"),
        ("006", "Foreign Corrupt Practices Act (FCPA) Multi-Jurisdictional Forensic Audit", "Defense & Government Tenders (NATO STANAG Bids)", "Forensic Interrogative Syntax & Caveats"),
        ("007", "Bilateral Defense Offset Technology Co-Production Treaty Drafting", "Defense & Government Tenders (NATO STANAG Bids)", "Diplomatic Treaty Drafting Terminology"),
        ("008", "WTO Subsidies & Countervailing Measures Appellate Body Defense", "Commercial Negotiation & Payment Milestones", "International Trade Dispute Syntax"),
        ("009", "International Chamber of Commerce (ICC) Emergency Arbitrator Injunctions", "International Defense Tender Arbitration & ICC Contracts", "Judicial Injunctive Imperatives"),
        ("010", "Sovereign Immunity Waiver Clauses in Military Vehicle Supply Pacts", "International Defense Tender Arbitration & ICC Contracts", "Legalistic Exemption & Waiver Formulas"),
        ("011", "Transnational Joint Venture Shareholder Deadlock Dissolution Inquest", "International Defense Tender Arbitration & ICC Contracts", "Corporate Governance Litigation Discourse"),
        ("012", "Strategic Dual-Use Export License Revocation Judicial Review", "Export Logistics & Incoterms 2020 (EXW, FCA, CPT, CIP, DAP, DDP)", "Administrative Law Adjudication Syntax"),
        ("013", "Catastrophic Maritime Cargo Loss: Hague-Visby Rules Carrier Liability", "Export Logistics & Incoterms 2020 (EXW, FCA, CPT, CIP, DAP, DDP)", "Maritime Admiralty Law Inquest Register"),
        ("014", "UN Sanctions Implementation & Third-Country Transshipment Inquests", "Export Logistics & Incoterms 2020 (EXW, FCA, CPT, CIP, DAP, DDP)", "Regulatory Compliance Investigation Syntax"),
        ("015", "Hostile Takeover Defense & Defense Asset Golden Share Protection", "Commercial Negotiation & Payment Milestones", "Corporate Legal Stance & Hedging"),
        ("016", "Sovereign Buyer Repudiation of Defense Contracts in Post-War Transition", "International Defense Tender Arbitration & ICC Contracts", "Repudiation & Compensation Discourse"),
        ("017", "Multi-Tiered Alternative Dispute Resolution (ADR) Escalation Clauses", "International Defense Tender Arbitration & ICC Contracts", "Contractual Escalation Mechanics"),
        ("018", "Public Procurement Integrity Inquests & Whistleblower Defense Protocols", "Defense & Government Tenders (NATO STANAG Bids)", "Ethical Governance & Investigative Register"),
        ("019", "Cross-Border Technology Licensing Royalty Withholding Tax Litigation", "Commercial Negotiation & Payment Milestones", "Fiscal Jurisdictional Argumentation"),
        ("020", "Ministerial Bilateral Defense Agreement Ratification Press Briefing", "Defense & Government Tenders (NATO STANAG Bids)", "High-Level Diplomatic Spokesperson Register")
    ]
    for num, title, track, grammar in c2_topics:
        curriculum.append({
            "test_id": f"TTR-SALES-C2-{num}", "title": title, "level": "C2", "category": "core",
            "workplace_track": track, "grammar_focus": grammar, "estimated_time_minutes": 20,
            "description": f"Mastery-tier international commercial and defense sales module examining {title.lower()}."
        })

    return curriculum

print("Curriculum helper module created.")


def get_teva_eng_curriculum():
    curriculum = []
    # A2 (001-020)
    a2_topics = [
        ("001", "Cleanroom Gowning, Airlocks & PPE: Imperatives & Must", "Cleanroom Gowning, Airlocks & Facility PPE", "Imperatives & Must"),
        ("002", "Sterile Line Sensor Readings & Status: Present Simple", "SCADA, PLC & Industrial Automation", "Present Simple 3rd person -s"),
        ("003", "Yesterday's Machine Stoppages & Maintenance: Past Simple", "Sterile Compounding & Filling Line Automation", "Past Simple regular & irregular"),
        ("004", "Cleanroom Airflow & Sensor Positions: Prepositions of Place", "Cleanroom HVAC Cascades & Differential Pressure", "Prepositions of Place"),
        ("005", "Autoclave Cycles & Temperatures: Numbers & Measurements", "Tablet Compression & Lyophilization Equipment", "Numbers & Measurements"),
        ("006", "HEPA Filter Differential Pressure Readings: Pascal Ranges", "Cleanroom HVAC Cascades & Differential Pressure", "Comparative Adjectives (higher, lower)"),
        ("007", "Daily Line Sanitization: Disinfectant Spraying & Wiping SOPs", "Cleanroom Gowning, Airlocks & Facility PPE", "Sequence Markers (first, next, then)"),
        ("008", "Tablet Press Tooling & Punch Inspection: Simple Present", "Tablet Compression & Lyophilization Equipment", "Present Simple Question Forms"),
        ("009", "Compressed Air Valve Operation & Pressure Gauge Readings", "SCADA, PLC & Industrial Automation", "Imperatives & Can"),
        ("010", "Reporting Broken Glass Vials on the Packaging Belt", "Sterile Compounding & Filling Line Automation", "Past Simple Negatives & Modals"),
        ("011", "Cleanroom Waste Bin Segregation: General vs Biohazard", "Cleanroom Gowning, Airlocks & Facility PPE", "Countable vs Uncountable Nouns"),
        ("012", "Peristaltic Pump Tubing Installation & Flow Direction", "Sterile Compounding & Filling Line Automation", "Prepositions of Motion (through, along, into)"),
        ("013", "Water for Injection (WFI) Sampling Point Locations", "Cleanroom HVAC Cascades & Differential Pressure", "Demonstratives (this, that, these, those)"),
        ("014", "Emergency Eye-Wash Station Testing: Weekly Checklists", "Cleanroom Gowning, Airlocks & Facility PPE", "Adverbs of Frequency"),
        ("015", "Lyophilizer Door Seal Inspection & Cleaning Routine", "Tablet Compression & Lyophilization Equipment", "Present Continuous for Active Maintenance"),
        ("016", "Label Printer Ribbon Replacement & Batch Code Checks", "SCADA, PLC & Industrial Automation", "Action Verbs & Direct Objects"),
        ("017", "Sterilization Indicator Strip Color Verification", "Tablet Compression & Lyophilization Equipment", "Adjectives of State & Condition"),
        ("018", "Shift Handover Logbook Entries for Sterile Line 2", "Sterile Compounding & Filling Line Automation", "Past Simple vs Present Simple"),
        ("019", "Electrical Panel Lockout/Tagout (LOTO) Warning Signs", "SCADA, PLC & Industrial Automation", "Prohibitive Modals (must not, do not)"),
        ("020", "Cleanroom Interlock Airlock Buzzer Alarms: Dos and Don'ts", "Cleanroom Gowning, Airlocks & Facility PPE", "Obligations & Permissions (can, cannot, have to)")
    ]
    for num, title, track, grammar in a2_topics:
        curriculum.append({
            "test_id": f"TEV-ENG-A2-{num}", "title": title, "level": "A2", "category": "core",
            "workplace_track": track, "grammar_focus": grammar, "estimated_time_minutes": 10,
            "description": f"Foundational pharmaceutical engineering module covering {title.lower()}."
        })

    # B1 (001-020)
    b1_topics = [
        ("001", "Cleanroom HVAC Pressure Alarms: Past Simple vs Past Perfect", "Cleanroom HVAC Cascades & Differential Pressure", "Past Simple vs Past Perfect"),
        ("002", "HEPA Filter Integrity DOP Testing & Smoke Pattern Studies", "Cleanroom HVAC Cascades & Differential Pressure", "Passive Voice in Testing Protocols"),
        ("003", "SCADA Automated Alarm Response & Line Stoppage Escalation", "SCADA, PLC & Industrial Automation", "First & Second Conditionals"),
        ("004", "Sterile Filling Needle Dosing Accuracy & Peristaltic Pump Drifts", "Sterile Compounding & Filling Line Automation", "Present Perfect with since & for"),
        ("005", "Tablet Compression Rotary Press Weight Variation Investigations", "Tablet Compression & Lyophilization Equipment", "Relative Clauses in Equipment Faults"),
        ("006", "Steam-in-Place (SIP) Temperature Thermocouple Mapping", "Sterile Compounding & Filling Line Automation", "Passive Voice with Modal Verbs"),
        ("007", "Water for Injection (WFI) Loop Conductivity & Ozone Sanitization", "Cleanroom HVAC Cascades & Differential Pressure", "Purpose Clauses (in order that, so that)"),
        ("008", "Lyophilization Condenser Ice Cake Thickness & Vacuum Leaks", "Tablet Compression & Lyophilization Equipment", "Modal Verbs of Probability (might, must have)"),
        ("009", "Isolator Glovebox Pressure Decay Leak Testing & Port Replacement", "Cleanroom Gowning, Airlocks & Facility PPE", "Temporal Clauses (as soon as, until)"),
        ("010", "Blister Packaging Machine Heat-Sealing Foil Fault Reporting", "Tablet Compression & Lyophilization Equipment", "Reported Speech in Deviation Logs"),
        ("011", "Clean-in-Place (CIP) Caustic Rinse Flow Rate Verification", "Sterile Compounding & Filling Line Automation", "Cause & Effect Connectors (due to, as a result)"),
        ("012", "Preventive Maintenance Scheduling & Calibration Tagging SOPs", "SCADA, PLC & Industrial Automation", "Future Forms in Engineering Planning"),
        ("013", "Differential Pressure Sensor Zero-Span Electronic Calibration", "Cleanroom HVAC Cascades & Differential Pressure", "Conditionals in Instrument Tuning"),
        ("014", "Automated Visual Inspection (AVI) Reject Rate Spikes on Vials", "Sterile Compounding & Filling Line Automation", "Passive Reporting of Statistics"),
        ("015", "Fluid Bed Dryer Granulation Humidity Sensor Maintenance", "Tablet Compression & Lyophilization Equipment", "Phrasal Verbs in Equipment Repair"),
        ("016", "Emergency Nitrogen Blanketing Valve Actuation Failure Inquests", "Sterile Compounding & Filling Line Automation", "Past Continuous in Event Timelines"),
        ("017", "Sterile Room Airflow Velocity Anemometer Traverse Testing", "Cleanroom HVAC Cascades & Differential Pressure", "Tolerances & Comparative Structures"),
        ("018", "Equipment Change Control Initiation: Servo Motor Retrofits", "Computerized System Validation (CSV & GAMP 5)", "Formal Justification Connectors"),
        ("019", "Cleanroom Decontamination via Vaporized Hydrogen Peroxide (VHP)", "Cleanroom Gowning, Airlocks & Facility PPE", "Passive Imperatives & Process Chains"),
        ("020", "Packaging Line Serialization Camera Misalignment Troubleshooting", "SCADA, PLC & Industrial Automation", "Past Unreal Scenarios (could have been)")
    ]
    for num, title, track, grammar in b1_topics:
        curriculum.append({
            "test_id": f"TEV-ENG-B1-{num}", "title": title, "level": "B1", "category": "core",
            "workplace_track": track, "grammar_focus": grammar, "estimated_time_minutes": 15,
            "description": f"Intermediate pharmaceutical engineering module investigating {title.lower()}."
        })

    # B2 (001-020)
    b2_topics = [
        ("001", "21 CFR Part 11 Electronic Records & CSV: Subjunctive & Directives", "21 CFR Part 11 Electronic Records & Data Integrity", "Mandative Subjunctive & Regulatory Directives"),
        ("002", "GAMP 5 Category 4 Configured Software Qualification Protocols", "Computerized System Validation (CSV & GAMP 5)", "Complex Passive Structures"),
        ("003", "Cleanroom Differential Pressure Cascade Loss Root Cause Analysis", "Cleanroom HVAC Cascades & Differential Pressure", "Third Conditional in GxP Deviations"),
        ("004", "Robotic Aseptic Vial Filling Machine Qualification (OQ/PQ)", "Sterile Compounding & Filling Line Automation", "Participial Clauses in Validation Protocols"),
        ("005", "Automated Autoclave F0 Lethality Calculation Verification Inquests", "Tablet Compression & Lyophilization Equipment", "Inverted Conditionals (Had the cycle...)"),
        ("006", "SCADA PLC Ladder Logic Change Control & Version Management", "SCADA, PLC & Industrial Automation", "Subjunctive in Engineering Directives"),
        ("007", "Lyophilizer Vacuum Leak Rate Inquests & Helium Mass Spectrometry", "Tablet Compression & Lyophilization Equipment", "Hedging in Deviation Technical Reports"),
        ("008", "Continuous Environmental Monitoring System (EMS) Sensor Drifts", "Cleanroom HVAC Cascades & Differential Pressure", "Nominalization in Validation Docs"),
        ("009", "Centrifugal WFI Pump Mechanical Seal Failure Forensic Inquest", "Cleanroom HVAC Cascades & Differential Pressure", "Passive Causative (have something verified)"),
        ("010", "Aseptic Media Fill Failure: Microbiological Contamination CAPA", "FDA/EMA Regulatory Inspection Defense & Audit Management", "Modal Verbs of Deduction & Retrospective Inquest"),
        ("011", "Cleanroom ISO 14644-1 Airborne Particle Count Statistical Analysis", "Cleanroom HVAC Cascades & Differential Pressure", "Complex Relative Clauses & Quantifiers"),
        ("012", "Critical Process Parameter (CPP) Excursions During Tablet Coating", "Tablet Compression & Lyophilization Equipment", "Adverbial Clauses of Concession & Contrast"),
        ("013", "Bioreactor Clean-in-Place (CIP) Spray Ball Shadow Area Validation", "Sterile Compounding & Filling Line Automation", "Negative Inversion for Safety Emphasis"),
        ("014", "GAMP 5 Category 5 Custom Script Traceability Matrix Audits", "Computerized System Validation (CSV & GAMP 5)", "Subjunctive in Traceability Requirements"),
        ("015", "Automated Visual Inspection AI Algorithm Re-Validation Protocols", "Sterile Compounding & Filling Line Automation", "Participial Modifiers & Technical Jargon"),
        ("016", "Emergency Power Transfer Switch Failure During Lyophilization Cycle", "Tablet Compression & Lyophilization Equipment", "Mixed Conditionals in Equipment Crashes"),
        ("017", "Sterile Filter Membrane Bacterial Retention Validation Challenge", "Sterile Compounding & Filling Line Automation", "Scientific Passive & Argumentation"),
        ("018", "Pure Steam Generator Condensate Quality Non-Conformance Inquests", "Cleanroom HVAC Cascades & Differential Pressure", "Causative Verbs & Risk Evaluation"),
        ("019", "Cleanroom De-Gowning Area Air Turbulence Aerodynamic CFD Studies", "Cleanroom Gowning, Airlocks & Facility PPE", "Complex Comparative Phrasing in Research"),
        ("020", "Unannounced Regulatory Audit Defense: Equipment Maintenance Records", "FDA/EMA Regulatory Inspection Defense & Audit Management", "Professional Diplomatic Assertiveness")
    ]
    for num, title, track, grammar in b2_topics:
        curriculum.append({
            "test_id": f"TEV-ENG-B2-{num}", "title": title, "level": "B2", "category": "core",
            "workplace_track": track, "grammar_focus": grammar, "estimated_time_minutes": 15,
            "description": f"Upper-intermediate pharmaceutical engineering module analyzing {title.lower()}."
        })

    # C2 (001-020)
    c2_topics = [
        ("001", "Unannounced FDA/EMA Regulatory Inspection Defense & GAMP 5 Disputes", "FDA/EMA Regulatory Inspection Defense & Audit Management", "Diplomatic Counter-Argumentation & Hedging"),
        ("002", "FDA Warning Letter Official Response: Data Integrity Remediation", "21 CFR Part 11 Electronic Records & Data Integrity", "High-Register Regulatory Legal Defense"),
        ("003", "Catastrophic Cleanroom Bio-Containment Breach Inquest & Liability", "FDA/EMA Regulatory Inspection Defense & Audit Management", "Forensic Investigation Syntax"),
        ("004", "EU GMP Annex 1 Revised Barrier Separation (RABS/Isolators) Litigation", "Cleanroom Gowning, Airlocks & Facility PPE", "Deontic Inversion & Legal Directives"),
        ("005", "Global Multi-Site CSV Framework Harmonization Inquests", "Computerized System Validation (CSV & GAMP 5)", "Administrative Governance Syntax"),
        ("006", "Lyophilizer Collapse During Multi-Million Dollar Biologic Batch Inquest", "Tablet Compression & Lyophilization Equipment", "Epistemic Hedging in Liability Disputes"),
        ("007", "Pharmaceutical Continuous Manufacturing PAT Validation Disputes", "SCADA, PLC & Industrial Automation", "Advanced Scientific Discourse"),
        ("008", "Cross-Border Active Substance Contamination Forensic Toxicology Inquest", "Sterile Compounding & Filling Line Automation", "Causative & Concessive Complex Syntax"),
        ("009", "GAMP 5 Electronic Audit Trail Tampering Forensic Expert Testimony", "21 CFR Part 11 Electronic Records & Data Integrity", "Forensic Cross-Examination Deposition"),
        ("010", "WFI Pyrogen Contamination Root Cause Inquest: Biofilm Kinetics", "Cleanroom HVAC Cascades & Differential Pressure", "High-Register Scientific Stance"),
        ("011", "Robotic Sterile Filling Cell Micro-Vibration & Particle Shedding Review", "Sterile Compounding & Filling Line Automation", "Participial Density & Nominal Groups"),
        ("012", "Contract Engineering EPCMV Contractor Gross Negligence Litigation", "FDA/EMA Regulatory Inspection Defense & Audit Management", "Contractual Breach & Indemnification"),
        ("013", "Consent Decree Remediation Governance Before the US Department of Justice", "FDA/EMA Regulatory Inspection Defense & Audit Management", "Judicial Decree & Compliance Discourse"),
        ("014", "Autonomous Mobile Robot (AMR) Cleanroom Logistics Safety Inquest", "Cleanroom Gowning, Airlocks & Facility PPE", "Normative Safety Jurisprudence"),
        ("015", "High-Potency Active Pharmaceutical Ingredient (HPAPI) Containment Inquest", "Sterile Compounding & Filling Line Automation", "Toxicological Risk Qualification"),
        ("016", "Pharmaceutical Cold Chain Global Distribution Breach Litigation", "FDA/EMA Regulatory Inspection Defense & Audit Management", "Multi-Jurisdictional Tort Liability"),
        ("017", "Sterile Facility Aging Infrastructure Re-Licensing Strategy Defense", "Cleanroom HVAC Cascades & Differential Pressure", "Executive Strategic Defense Phrasing"),
        ("018", "Automated Visual Inspection False Rejection Rate Machine Learning Disputes", "SCADA, PLC & Industrial Automation", "Algorithmic Validation Law Syntax"),
        ("019", "Regulatory Recertification of Terminal Sterilization Cycles Post-Overhaul", "Tablet Compression & Lyophilization Equipment", "Administrative Adjudication Formulations"),
        ("020", "Board-Level Capital Expenditure Justification for Next-Gen Biologics Plant", "FDA/EMA Regulatory Inspection Defense & Audit Management", "Corporate Executive Persuasion & Rhetoric")
    ]
    for num, title, track, grammar in c2_topics:
        curriculum.append({
            "test_id": f"TEV-ENG-C2-{num}", "title": title, "level": "C2", "category": "core",
            "workplace_track": track, "grammar_focus": grammar, "estimated_time_minutes": 20,
            "description": f"Mastery-tier pharmaceutical engineering governance module examining {title.lower()}."
        })

    return curriculum

def get_tapi_chem_curriculum():
    curriculum = []
    # A2 (001-020)
    a2_topics = [
        ("001", "Laboratory Glassware, Reagents & Fume Hoods: Imperatives & Must", "Laboratory Glassware, Reagents & Fume Hoods", "Imperatives & Must"),
        ("002", "Daily QC Testing & Analytical Weighing: Present Simple", "Analytical Chemistry (HPLC, GC, Spectroscopy)", "Present Simple 3rd person -s"),
        ("003", "Yesterday's Chemical Synthesis & Titration: Past Simple", "Organic Chemical Synthesis & Batch Reactors", "Past Simple regular & irregular"),
        ("004", "Chemical Storage & Reagent Cabinets: Prepositions of Place", "Hazardous Reagents, Solvent Recovery & Lab Safety", "Prepositions of Place"),
        ("005", "Temperatures, Milligrams & Liquid Volumes: Units & Numbers", "In-Process Control (IPC) & Out-of-Specification (OOS)", "Units, numbers & decimals"),
        ("006", "Analytical Balance Calibration: Certified Weights & Tare Buttons", "Analytical Chemistry (HPLC, GC, Spectroscopy)", "Imperatives in SOP Instructions"),
        ("007", "Solvent Bottle Labeling: Chemical Names, Lot Numbers & Dates", "Hazardous Reagents, Solvent Recovery & Lab Safety", "Countable vs Uncountable Nouns"),
        ("008", "Heating Mantles & Magnetic Stirrers: Speed & Heat Controls", "Organic Chemical Synthesis & Batch Reactors", "Comparatives & Adjustments"),
        ("009", "Vacuum Desiccator Maintenance & Silica Gel Color Checks", "Laboratory Glassware, Reagents & Fume Hoods", "Adjectives of Condition"),
        ("010", "Reporting Broken Volumetric Flasks & Pipette Tips", "Laboratory Glassware, Reagents & Fume Hoods", "Past Simple Negatives & Questions"),
        ("011", "Rotary Evaporator Water Bath Temperature Monitoring", "Organic Chemical Synthesis & Batch Reactors", "Present Continuous for Active Runs"),
        ("012", "Chemical Waste Carboy Disposal: Halogenated vs Non-Halogenated", "Hazardous Reagents, Solvent Recovery & Lab Safety", "Modal Verbs (must, must not, can)"),
        ("013", "pH Meter Buffer Solution Calibration: pH 4.0, 7.0 & 10.0", "Analytical Chemistry (HPLC, GC, Spectroscopy)", "Prepositions of Measurement"),
        ("014", "Emergency Eyewash & Body Shower Station Weekly Checks", "Hazardous Reagents, Solvent Recovery & Lab Safety", "Adverbs of Frequency"),
        ("015", "Melting Point Capillary Tube Filling & Visual Inspection", "Analytical Chemistry (HPLC, GC, Spectroscopy)", "Step-by-Step Sequence Markers"),
        ("016", "Karl Fischer Titration Reagent Replacement & Drift Checks", "Analytical Chemistry (HPLC, GC, Spectroscopy)", "Present Perfect with just/already"),
        ("017", "Fume Hood Airflow Velocity Alarms: Red Light Warning Actions", "Hazardous Reagents, Solvent Recovery & Lab Safety", "Conditionals with If and When"),
        ("018", "TLC Chromatography Chamber Solvent Level & Cover Glass", "Analytical Chemistry (HPLC, GC, Spectroscopy)", "Spatial Prepositions (above, below, on)"),
        ("019", "Synthesis Glassware Washing & Drying Oven Temperature Rules", "Laboratory Glassware, Reagents & Fume Hoods", "Rules & Obligations (have to, must)"),
        ("020", "End-of-Shift Lab Bench Cleanup & Gas Tap Shutoff Rules", "Hazardous Reagents, Solvent Recovery & Lab Safety", "Checklists & Final Imperatives")
    ]
    for num, title, track, grammar in a2_topics:
        curriculum.append({
            "test_id": f"TAPI-CHEM-A2-{num}", "title": title, "level": "A2", "category": "core",
            "workplace_track": track, "grammar_focus": grammar, "estimated_time_minutes": 10,
            "description": f"Foundational chemical laboratory module covering {title.lower()}."
        })

    # B1 (001-020)
    b1_topics = [
        ("001", "API Reactor Yield & Solvent Recovery: Present Perfect vs Past Simple", "Organic Chemical Synthesis & Batch Reactors", "Present Perfect vs Past Simple"),
        ("002", "Karl Fischer Water Determination: Drift Rates & Titrant Factorization", "Analytical Chemistry (HPLC, GC, Spectroscopy)", "Passive Voice in Analytical SOPs"),
        ("003", "HPLC Chromatography Mobile Phase Degassing & Baseline Drift", "Analytical Chemistry (HPLC, GC, Spectroscopy)", "First & Second Conditionals"),
        ("004", "Rotary Evaporator Vacuum Distillation & Solvent Condenser Drops", "Organic Chemical Synthesis & Batch Reactors", "Present Perfect Continuous (duration)"),
        ("005", "Batch Reactor Crystallization Temperature Ramps & Seed Crystal Dosing", "Organic Chemical Synthesis & Batch Reactors", "Relative Clauses in Reaction Parameters"),
        ("006", "Recrystallization Purification: Activated Charcoal Decoloration Steps", "Organic Chemical Synthesis & Batch Reactors", "Passive Voice with Modals"),
        ("007", "Buchner Funnel Vacuum Filtration Cake Washing & Solvent Pull-Through", "Organic Chemical Synthesis & Batch Reactors", "Prepositions of Motion & Direction"),
        ("008", "In-Process Control (IPC) Reaction Completion Testing via TLC Plates", "In-Process Control (IPC) & Out-of-Specification (OOS)", "Temporal Conjunctions (until, as soon as)"),
        ("009", "Gas Chromatography Carrier Gas Helium Cylinder Pressure Switches", "Analytical Chemistry (HPLC, GC, Spectroscopy)", "Modals of Deduction & Probability"),
        ("010", "pH Electrode Slope Drift & Calibration Buffer Solution Deviations", "Analytical Chemistry (HPLC, GC, Spectroscopy)", "Reported Speech in QC Logs"),
        ("011", "API Vacuum Tray Dryer Drying Loss Curve Verification", "Organic Chemical Synthesis & Batch Reactors", "Cause & Effect Connectors"),
        ("012", "Hazardous Organic Solvent Segregation: Chlorinated vs Ethers", "Hazardous Reagents, Solvent Recovery & Lab Safety", "Categorization Structures & Quantifiers"),
        ("013", "Mass Spectrometry Electrospray Ionization (ESI) Source Cleaning", "Analytical Chemistry (HPLC, GC, Spectroscopy)", "Phrasal Verbs in Lab Maintenance"),
        ("014", "Exothermic Grignard Reaction Temperature Spike Troubleshooting", "Organic Chemical Synthesis & Batch Reactors", "Past Continuous in Event Timelines"),
        ("015", "HPLC Guard Column Backpressure Increase & Replacement Trigger", "Analytical Chemistry (HPLC, GC, Spectroscopy)", "Tolerances & Comparative Adjectives"),
        ("016", "Centrifuge Solid-Liquid Separation Cake Cracking Inquests", "Organic Chemical Synthesis & Batch Reactors", "Passive Voice Reporting Forms"),
        ("017", "UV-Vis Spectrophotometer Quartz Cuvette Scratch Inspection", "Analytical Chemistry (HPLC, GC, Spectroscopy)", "Adverbial Clauses of Contrast"),
        ("018", "Synthesis Reagent Certificate of Analysis (CoA) Verification", "Pharmacopeial Compliance (Ph. Eur., USP, JP)", "Obligation Verbs (shall, must, verify)"),
        ("019", "Fractional Distillation Column Reflux Ratio Adjustment", "Organic Chemical Synthesis & Batch Reactors", "Purpose Clauses (so that, in order to)"),
        ("020", "Analytical Balance Annual Recertification Deviation Logging", "Analytical Chemistry (HPLC, GC, Spectroscopy)", "Past Unreal Scenarios (could have occurred)")
    ]
    for num, title, track, grammar in b1_topics:
        curriculum.append({
            "test_id": f"TAPI-CHEM-B1-{num}", "title": title, "level": "B1", "category": "core",
            "workplace_track": track, "grammar_focus": grammar, "estimated_time_minutes": 15,
            "description": f"Intermediate chemical synthesis and analytical module analyzing {title.lower()}."
        })

    # B2 (001-020)
    b2_topics = [
        ("001", "HPLC Chromatography Out-of-Specification (OOS): Third Conditional", "Analytical Chemistry (HPLC, GC, Spectroscopy)", "Third Conditional in OOS Investigations"),
        ("002", "Chiral Chromatography Enantiomeric Purity (% ee) Determination", "Analytical Chemistry (HPLC, GC, Spectroscopy)", "Subjunctive in Pharmacopeial Limits"),
        ("003", "Exothermic Runaway Reaction Kinetics in Jacketed Pilot Reactors", "Organic Chemical Synthesis & Batch Reactors", "Mixed Conditionals in Chemical Safety"),
        ("004", "Nitrosamine Genotoxic Trace Contaminant GC-MS/MS Quantification", "Nitrosamine Impurity Profiling & ICH Guidelines", "Negative Inversion for Analytical Rigor"),
        ("005", "API Polymorph Screening via X-Ray Powder Diffraction (XRPD)", "Analytical Chemistry (HPLC, GC, Spectroscopy)", "Participial Clauses in Research Papers"),
        ("006", "Forced Degradation Studies: Acid, Base, Peroxide & Thermal Pathways", "Pharmacopeial Compliance (Ph. Eur., USP, JP)", "Hedging & Stance in Stability Reports"),
        ("007", "HPLC Column Peak Tailing & Asymmetry Factor Exceedance Inquests", "Analytical Chemistry (HPLC, GC, Spectroscopy)", "Inverted Conditionals (Had the column...)"),
        ("008", "Homogeneous Catalyst Ligand Poisoning & Recovery Metallurgy", "Organic Chemical Synthesis & Batch Reactors", "Nominalization in Process Chemistry"),
        ("009", "Headspace GC Residual Solvent Testing According to ICH Q3C", "Pharmacopeial Compliance (Ph. Eur., USP, JP)", "Mandative Subjunctive & Directives"),
        ("010", "Pilot Plant Scale-Up Mass Transfer & Impeller Shear Stress Modeling", "Organic Chemical Synthesis & Batch Reactors", "Complex Passive Constructions"),
        ("011", "Differential Scanning Calorimetry (DSC) Thermal Stability Audits", "Hazardous Reagents, Solvent Recovery & Lab Safety", "Complex Relative Clauses & Modals"),
        ("012", "LC-MS High-Resolution Accurate Mass Unknown Impurity Identification", "Analytical Chemistry (HPLC, GC, Spectroscopy)", "Passive Causative & Analytical Verbs"),
        ("013", "Process Analytical Technology (PAT) Real-Time Reaction Near-IR Monitoring", "In-Process Control (IPC) & Out-of-Specification (OOS)", "Adverbial Clauses of Condition & Concession"),
        ("014", "Continuous Flow Micro-Reactor Synthesis Route Optimization", "Organic Chemical Synthesis & Batch Reactors", "Participial Modifiers & Technical Jargon"),
        ("015", "OOS Phase II Laboratory Investigation: Re-Testing vs Root Cause", "In-Process Control (IPC) & Out-of-Specification (OOS)", "Subjunctive Mood in SOP Governance"),
        ("016", "Solid-State Nuclear Magnetic Resonance (ssNMR) Tautomer Elucidation", "Analytical Chemistry (HPLC, GC, Spectroscopy)", "Academic Scientific Discourse Register"),
        ("017", "Heavy Metal Scavenger Resin Depletion Kinetics in Crude API Slurry", "Organic Chemical Synthesis & Batch Reactors", "Causative Verbs & Risk Mitigation"),
        ("018", "Validation of Analytical Methods According to ICH Q2(R2) Guidelines", "Pharmacopeial Compliance (Ph. Eur., USP, JP)", "Normative Directives & Compliance Forms"),
        ("019", "Solvent Extraction Partition Coefficient Non-Linearity Inquests", "Organic Chemical Synthesis & Batch Reactors", "Hypothetical Inversion in Chemical Modeling"),
        ("020", "Unannounced Health Authority Audit of Laboratory Data Integrity (ALCOA+)", "In-Process Control (IPC) & Out-of-Specification (OOS)", "Professional Diplomatic Assertiveness")
    ]
    for num, title, track, grammar in b2_topics:
        curriculum.append({
            "test_id": f"TAPI-CHEM-B2-{num}", "title": title, "level": "B2", "category": "core",
            "workplace_track": track, "grammar_focus": grammar, "estimated_time_minutes": 15,
            "description": f"Upper-intermediate chemical API synthesis module analyzing {title.lower()}."
        })

    # C2 (001-020)
    c2_topics = [
        ("001", "Pharmacopeial Monograph Harmonization, Nitrosamines & ICH Q2(R2)", "Forensic Patent Litigation & Monograph Harmonization", "Diplomatic Counter-Argumentation & Hedging"),
        ("002", "Patent Invalidation Litigation: Novel Polymorphic Salt Crystal Forms", "Forensic Patent Litigation & Monograph Harmonization", "High-Register Patent Jurisprudence"),
        ("003", "Nitrosamine Mutagenic Risk Toxicological Assessment (ICH M7) Defense", "Nitrosamine Impurity Profiling & ICH Guidelines", "Forensic Toxicological Deposition"),
        ("004", "Cross-Border API Supply Contract Quality Agreement Breach Litigation", "Forensic Patent Litigation & Monograph Harmonization", "Contractual Breach & Indemnification"),
        ("005", "Genotoxic Impurity Threshold of Toxicological Concern (TTC) Inquests", "Nitrosamine Impurity Profiling & ICH Guidelines", "Epistemic Hedging in Regulatory Filings"),
        ("006", "European Directorate (EDQM) Certificate of Suitability (CEP) Suspension Appeals", "Pharmacopeial Compliance (Ph. Eur., USP, JP)", "Administrative Law Appeals Syntax"),
        ("007", "Catastrophic Chemical Plant Toxic Runaway Effluent Discharge Inquest", "Hazardous Reagents, Solvent Recovery & Lab Safety", "Environmental Tort Liability Inquest"),
        ("008", "Supercritical Fluid Chromatography Commercial Technology Transfer Disputes", "Analytical Chemistry (HPLC, GC, Spectroscopy)", "Complex Multi-Clause Scientific Argumentation"),
        ("009", "Chiral Inversion in Vivo Pharmacokinetic Patent Defense Inquests", "Forensic Patent Litigation & Monograph Harmonization", "Biochemical Patent Defense Syntax"),
        ("010", "Continuous Synthesis Micro-Reactor Reactor Blockage Explosive Inquest", "Organic Chemical Synthesis & Batch Reactors", "Forensic Incident Inquest Discourse"),
        ("011", "Expert Witness Deposition: Analytical Method Cross-Validation Failures", "In-Process Control (IPC) & Out-of-Specification (OOS)", "Forensic Cross-Examination Deposition"),
        ("012", "Harmonization of Pharmacopeial Dissolution Testing Protocols (Ph. Eur. vs USP)", "Pharmacopeial Compliance (Ph. Eur., USP, JP)", "Treaty & Monograph Harmonization Syntax"),
        ("013", "Industrial Solvent Recovery Distillation Column Dioxin Formation Inquest", "Hazardous Reagents, Solvent Recovery & Lab Safety", "Toxicological Environmental Discourse"),
        ("014", "Catalytic Asymmetric Hydrogenation Intellectual Property Counter-Claims", "Organic Chemical Synthesis & Batch Reactors", "Patent Claim Construction Terminology"),
        ("015", "OOS False Negative Release Fraud Inquest: Regulatory Whistleblower Defense", "In-Process Control (IPC) & Out-of-Specification (OOS)", "Regulatory Fraud Investigation Register"),
        ("016", "Solid-State Degradation Kinetics in High-Temperature Tropical Storage", "Pharmacopeial Compliance (Ph. Eur., USP, JP)", "High-Register Physical Chemistry Discourse"),
        ("017", "International Arbitration of Raw Material Contamination Damage Claims", "Forensic Patent Litigation & Monograph Harmonization", "Commercial Arbitration Formulas"),
        ("018", "Executive Board Defense of Green Chemistry API Capital Re-Tooling", "Organic Chemical Synthesis & Batch Reactors", "Corporate Strategic Persuasion Syntax"),
        ("019", "Regulatory Warning Letter Response: Impurity Analytical Method Deficiencies", "In-Process Control (IPC) & Out-of-Specification (OOS)", "High-Stakes Regulatory Response Phrasing"),
        ("020", "Scientific Advisory Board Dispute: Synthetic Route Freedom to Operate", "Forensic Patent Litigation & Monograph Harmonization", "High-Register Scientific Counsel Dialogue")
    ]
    for num, title, track, grammar in c2_topics:
        curriculum.append({
            "test_id": f"TAPI-CHEM-C2-{num}", "title": title, "level": "C2", "category": "core",
            "workplace_track": track, "grammar_focus": grammar, "estimated_time_minutes": 20,
            "description": f"Mastery-tier chemical research and regulatory governance module examining {title.lower()}."
        })

    return curriculum

def get_teva_it_curriculum():
    curriculum = []
    # A2 (001-020)
    a2_topics = [
        ("001", "Hardware Setup, Peripherals & Cables: Imperatives & Can", "Hardware Setup, Peripherals & Datacenter Cabling", "Imperatives & Can"),
        ("002", "Daily Service Desk Support & User Tickets: Present Simple", "ITIL Global Service Desk & Incident Escalation", "Present Simple 3rd person -s"),
        ("003", "Yesterday's Network Outage & Server Restarts: Past Simple", "IT Infrastructure, Networking & Cloud Operations (Azure/AWS)", "Past Simple regular & irregular"),
        ("004", "Server Rack Connections & Ports: Prepositions of Place", "Hardware Setup, Peripherals & Datacenter Cabling", "Prepositions of Place"),
        ("005", "Cybersecurity Warnings & Password Rules: Must & Must Not", "Cybersecurity, Endpoint Protection & Zero Trust Architecture", "Modal verbs (must, must not, have to)"),
        ("006", "Laptop Docking Station Setup: USB-C & Dual Monitors", "Hardware Setup, Peripherals & Datacenter Cabling", "Imperatives in Hardware Guides"),
        ("007", "Password Reset Requests & MFA Authenticator App Setup", "Identity & Access Management (IAM, Active Directory, MFA)", "Polite Requests & Wh- Questions"),
        ("008", "Wi-Fi Connectivity Troubleshooting & Airplane Mode Checks", "IT Infrastructure, Networking & Cloud Operations (Azure/AWS)", "Present Continuous for Active Faults"),
        ("009", "Network Printer Mapping & Paper Jam Error Messages", "Hardware Setup, Peripherals & Datacenter Cabling", "Countable vs Uncountable Nouns"),
        ("010", "Reporting Phishing Emails & Suspicious Links to IT Security", "Cybersecurity, Endpoint Protection & Zero Trust Architecture", "Past Simple Negatives & Modals"),
        ("011", "Software Installation Requests: Approved Corporate Catalogs", "ITIL Global Service Desk & Incident Escalation", "Modal Verbs (can, may, should)"),
        ("012", "Clearing Browser Cache & Cookies on Enterprise Chrome", "IT Infrastructure, Networking & Cloud Operations (Azure/AWS)", "Sequence Markers (first, then, next)"),
        ("013", "Keyboard Shortcuts: Screen Locking (Win+L) & Task Manager", "Hardware Setup, Peripherals & Datacenter Cabling", "Imperatives & Direct Objects"),
        ("014", "Antivirus Definition Update Status & Scheduled Scans", "Cybersecurity, Endpoint Protection & Zero Trust Architecture", "Present Perfect with just & already"),
        ("015", "VPN Client Connection Failures & Remote Work Access", "IT Infrastructure, Networking & Cloud Operations (Azure/AWS)", "Conditionals with If & When"),
        ("016", "Outlook Mailbox Quota Full Warnings & Archiving Basics", "ITIL Global Service Desk & Incident Escalation", "Comparatives (larger, smaller, older)"),
        ("017", "Service Desk Ticket Severity Levels: Low, Medium, High", "ITIL Global Service Desk & Incident Escalation", "Adjectives of Priority & Urgency"),
        ("018", "Ethernet Patch Cable Routing in Desk Cable Trays", "Hardware Setup, Peripherals & Datacenter Cabling", "Prepositions of Motion (through, along, under)"),
        ("019", "External USB Flash Drive Prohibitions on GxP Laptops", "Cybersecurity, Endpoint Protection & Zero Trust Architecture", "Strict Prohibitions (must not, are not allowed)"),
        ("020", "End-of-Day Workstation Shutdown & Screen Sleep Policies", "Hardware Setup, Peripherals & Datacenter Cabling", "Obligations & Checklists")
    ]
    for num, title, track, grammar in a2_topics:
        curriculum.append({
            "test_id": f"TEV-IT-A2-{num}", "title": title, "level": "A2", "category": "core",
            "workplace_track": track, "grammar_focus": grammar, "estimated_time_minutes": 10,
            "description": f"Foundational IT workplace English module covering {title.lower()}."
        })

    # B1 (001-020)
    b1_topics = [
        ("001", "Cloud Server Outage Post-Mortems: Past Simple vs Past Perfect", "IT Infrastructure, Networking & Cloud Operations (Azure/AWS)", "Past Simple vs Past Perfect"),
        ("002", "Active Directory Group Policy Object (GPO) Deployment Failures", "Identity & Access Management (IAM, Active Directory, MFA)", "Passive Voice in Sysadmin SOPs"),
        ("003", "Firewall Port Blocking & Rule Configuration Troubleshooting", "Cybersecurity, Endpoint Protection & Zero Trust Architecture", "First & Second Conditionals"),
        ("004", "Virtual Machine Snapshot Rollbacks After Corrupted Kernel Patches", "IT Infrastructure, Networking & Cloud Operations (Azure/AWS)", "Present Perfect with since & for"),
        ("005", "DNS Resolution Timeouts & DHCP Lease Exhaustion Incidents", "IT Infrastructure, Networking & Cloud Operations (Azure/AWS)", "Relative Clauses in Network Topology"),
        ("006", "Database SQL Query Latency Spikes & Index Optimization", "DevOps, CI/CD Pipelines & Microservices Architecture", "Passive Voice with Modal Verbs"),
        ("007", "Microsoft 365 Exchange Hybrid Mailflow Delivery Delays", "IT Infrastructure, Networking & Cloud Operations (Azure/AWS)", "Purpose Clauses (in order to, so that)"),
        ("008", "Data Center Uninterruptible Power Supply (UPS) Battery Health Logs", "Hardware Setup, Peripherals & Datacenter Cabling", "Modal Verbs of Probability"),
        ("009", "ITIL Incident Severity 1 Major Escalation Bridge Coordination", "ITIL Global Service Desk & Incident Escalation", "Temporal Clauses (while, until, as soon as)"),
        ("010", "Endpoint Encryption (BitLocker) Recovery Key Retrieval Protocols", "Cybersecurity, Endpoint Protection & Zero Trust Architecture", "Reported Speech in Security Tickets"),
        ("011", "Cloud Storage Blob Lifecycle Management & Cold Archive Tiers", "IT Infrastructure, Networking & Cloud Operations (Azure/AWS)", "Cause & Effect Connectors"),
        ("012", "Disaster Recovery Off-Site Tape Backup Synchronization Logs", "21 CFR Part 11 GxP Cloud Compliance & Disaster Recovery", "Future Continuous & Future Perfect"),
        ("013", "VLAN Tagging & Trunk Port Misconfiguration on Edge Switches", "IT Infrastructure, Networking & Cloud Operations (Azure/AWS)", "Conditionals in Network Diagnostics"),
        ("014", "Service Desk SLA Breach Warnings & Resolution Milestone Updates", "ITIL Global Service Desk & Incident Escalation", "Passive Reporting of Metrics"),
        ("015", "Linux SSH Key Pair Generation & Bastion Host Configuration", "IT Infrastructure, Networking & Cloud Operations (Azure/AWS)", "Phrasal Verbs in Cloud Operations"),
        ("016", "Ransomware Isolated Host Quarantine & Forensic Memory Dump Logs", "Cybersecurity, Endpoint Protection & Zero Trust Architecture", "Past Continuous in Incident Chronology"),
        ("017", "Software License Compliance Audits: Server Core CAL Counts", "ITIL Global Service Desk & Incident Escalation", "Comparative Structures & Tolerances"),
        ("018", "Automated CI/CD Pipeline Build Break Alerts on GitHub Actions", "DevOps, CI/CD Pipelines & Microservices Architecture", "Formal Root Cause Connectors"),
        ("019", "Mobile Device Management (MDM) Intune Remote Wipe Procedures", "Cybersecurity, Endpoint Protection & Zero Trust Architecture", "Passive Imperatives & Policies"),
        ("020", "Post-Incident Retrospective Action Items: Preventing Recurrence", "ITIL Global Service Desk & Incident Escalation", "Past Unreal Scenarios (should have done)")
    ]
    for num, title, track, grammar in b1_topics:
        curriculum.append({
            "test_id": f"TEV-IT-B1-{num}", "title": title, "level": "B1", "category": "core",
            "workplace_track": track, "grammar_focus": grammar, "estimated_time_minutes": 15,
            "description": f"Intermediate IT infrastructure and operations module analyzing {title.lower()}."
        })

    # B2 (001-020)
    b2_topics = [
        ("001", "Zero Trust Security Architecture: Inversion for Emphasis", "Cybersecurity, Endpoint Protection & Zero Trust Architecture", "Negative Inversion for Security Directives"),
        ("002", "Kubernetes Pod CrashLoopBackOff Container Orchestration Inquests", "DevOps, CI/CD Pipelines & Microservices Architecture", "Complex Passive Structures"),
        ("003", "Multi-Factor Authentication (MFA) Fatigue & Prompt Bombing Attacks", "Identity & Access Management (IAM, Active Directory, MFA)", "Third Conditional in Security Breaches"),
        ("004", "AWS/Azure Multi-Region Cloud Redundancy Failover Simulations", "IT Infrastructure, Networking & Cloud Operations (Azure/AWS)", "Participial Clauses in Architecture Specs"),
        ("005", "SIEM Log Correlation & Advanced Threat Hunting Query Formulations", "Cybersecurity, Endpoint Protection & Zero Trust Architecture", "Inverted Conditionals (Had the threat...)"),
        ("006", "Infrastructure as Code (Terraform) Drift Detection & State Locking", "DevOps, CI/CD Pipelines & Microservices Architecture", "Subjunctive in Configuration Standards"),
        ("007", "Database Read Replica Replication Lag Under Heavy Transaction Load", "IT Infrastructure, Networking & Cloud Operations (Azure/AWS)", "Hedging in Performance Diagnostics"),
        ("008", "SOC 2 Type II Security Compliance & Trust Service Criteria Audits", "21 CFR Part 11 GxP Cloud Compliance & Disaster Recovery", "Nominalization in Audit Reports"),
        ("009", "API Gateway Rate Limiting & OAuth2 Token Validation Inquests", "DevOps, CI/CD Pipelines & Microservices Architecture", "Passive Causative & Microservice Specs"),
        ("010", "Privileged Access Management (PAM) Vault Session Recording Rules", "Identity & Access Management (IAM, Active Directory, MFA)", "Modal Verbs of Deduction & Governance"),
        ("011", "Global SD-WAN Packet Loss & Multipath Border Gateway BGP Inquests", "IT Infrastructure, Networking & Cloud Operations (Azure/AWS)", "Complex Relative Clauses & Concessives"),
        ("012", "Hardware Security Module (HSM) Cryptographic Key Rotation Policies", "Cybersecurity, Endpoint Protection & Zero Trust Architecture", "Adverbial Clauses of Contrast & Condition"),
        ("013", "Ransomware Lateral Movement Containment via Network Microsegmentation", "Cybersecurity, Endpoint Protection & Zero Trust Architecture", "Negative Inversion for Perimeter Defense"),
        ("014", "21 CFR Part 11 Electronic Signature Validation in GxP Cloud SaaS", "21 CFR Part 11 GxP Cloud Compliance & Disaster Recovery", "Subjunctive in Regulatory IT Directives"),
        ("015", "Penetration Testing Exploitation Reports: Cross-Site Scripting (XSS)", "Cybersecurity, Endpoint Protection & Zero Trust Architecture", "Participial Modifiers & Vulnerability Jargon"),
        ("016", "Cloud Disaster Recovery RTO/RPO SLA Breach Impact Analyses", "21 CFR Part 11 GxP Cloud Compliance & Disaster Recovery", "Mixed Conditionals in Recovery Disasters"),
        ("017", "Data Loss Prevention (DLP) Endpoint USB Exfiltration Interceptions", "Cybersecurity, Endpoint Protection & Zero Trust Architecture", "Scientific Passive & Security Policies"),
        ("018", "Zero-Day Vulnerability Patching Mandates Under Emergency Change Control", "Cybersecurity, Endpoint Protection & Zero Trust Architecture", "Normative Directives & Mandatory Shall"),
        ("019", "Microservices Distributed Tracing & OpenTelemetry Latency Spikes", "DevOps, CI/CD Pipelines & Microservices Architecture", "Hypothetical Inversion in Cloud Metrics"),
        ("020", "Executive CISO Briefing: External Red Team Attack Surface Findings", "Cybersecurity, Endpoint Protection & Zero Trust Architecture", "Professional Diplomatic Assertiveness")
    ]
    for num, title, track, grammar in b2_topics:
        curriculum.append({
            "test_id": f"TEV-IT-B2-{num}", "title": title, "level": "B2", "category": "core",
            "workplace_track": track, "grammar_focus": grammar, "estimated_time_minutes": 15,
            "description": f"Upper-intermediate enterprise IT and cybersecurity module analyzing {title.lower()}."
        })

    # C2 (001-020)
    c2_topics = [
        ("001", "Enterprise Zero Trust Breach Disclosure, Cloud SLA Litigation & Governance", "Enterprise Cyber Breach Governance & SLA Litigation", "Diplomatic Counter-Argumentation & Hedging"),
        ("002", "Board-Level Cyber Catastrophe Inquest: Nation-State APT Intrusion", "Enterprise Cyber Breach Governance & SLA Litigation", "High-Register Cybersecurity Governance"),
        ("003", "Transatlantic Cloud Data Residency Litigation: EU-US Data Privacy Framework", "Enterprise Cyber Breach Governance & SLA Litigation", "Forensic Data Privacy Jurisprudence"),
        ("004", "Multi-Million Dollar Global Cloud Hyperscaler SLA Default Litigation", "Enterprise Cyber Breach Governance & SLA Litigation", "Contractual Breach & Indemnification"),
        ("005", "Cyber Insurance Carrier Claim Repudiation Arbitration Under English Law", "Enterprise Cyber Breach Governance & SLA Litigation", "Arbitration Formulas & Exemption Clauses"),
        ("006", "Enterprise Ransomware Extortion Inquest: Sanctions Compliance (OFAC)", "Cybersecurity, Endpoint Protection & Zero Trust Architecture", "Deontic Inversion & Sanctions Law"),
        ("007", "Critical Infrastructure Cybersecurity Directive (EU NIS2) Board Governance", "Enterprise Cyber Breach Governance & SLA Litigation", "Administrative Governance Syntax"),
        ("008", "Zero-Day Exploit Supply Chain Breach Inquest: Third-Party Vendor Liability", "Cybersecurity, Endpoint Protection & Zero Trust Architecture", "Epistemic Hedging in Liability Disputes"),
        ("009", "GAMP 5 Multi-Tenant Cloud SaaS Validation Audits in Pharmaceutical IT", "21 CFR Part 11 GxP Cloud Compliance & Disaster Recovery", "Regulatory Administrative Law Syntax"),
        ("010", "Forensic Expert Deposition: Insider Threat Data Exfiltration Inquest", "Enterprise Cyber Breach Governance & SLA Litigation", "Forensic Deposition & Cross-Examination"),
        ("011", "Global Identity Federation Kerberos/OAuth Protocol Vulnerability Analysis", "Identity & Access Management (IAM, Active Directory, MFA)", "Participial Density & Cryptographic Jargon"),
        ("012", "Dark Web Credential Spill Forensic Response: Corporate Reputational Defense", "Cybersecurity, Endpoint Protection & Zero Trust Architecture", "Executive Strategic Defense Phrasing"),
        ("013", "Enterprise AI Large Language Model Data Leakage & Confidentiality Breach", "DevOps, CI/CD Pipelines & Microservices Architecture", "Techno-Legal Stance & Intellectual Property"),
        ("014", "Submarine Fiber Optic Cable Severance: International Cloud Force Majeure", "IT Infrastructure, Networking & Cloud Operations (Azure/AWS)", "Maritime International Law & Force Majeure"),
        ("015", "Class Action Shareholder Litigation Post-Cybersecurity Breach Disclosure", "Enterprise Cyber Breach Governance & SLA Litigation", "Corporate Securities Litigation Discourse"),
        ("016", "Post-Quantum Cryptography Migration Strategy Before Executive Committee", "Cybersecurity, Endpoint Protection & Zero Trust Architecture", "High-Register Executive Persuasion Syntax"),
        ("017", "Global Data Center Catastrophic Power Failure Emergency Arbitration", "IT Infrastructure, Networking & Cloud Operations (Azure/AWS)", "Commercial Arbitration Formulas"),
        ("018", "Software Bill of Materials (SBOM) Open-Source License Invalidation Claims", "DevOps, CI/CD Pipelines & Microservices Architecture", "Intellectual Property Claim Construction"),
        ("019", "Regulatory Fine Defense: GDPR Article 32 Technical Measures Violation", "Enterprise Cyber Breach Governance & SLA Litigation", "Administrative Regulatory Penal Defense"),
        ("020", "CISO Keynote Defense: Enterprise Digital Sovereignty in Hostile Geopolitics", "Enterprise Cyber Breach Governance & SLA Litigation", "High-Register Geopolitical Rhetoric")
    ]
    for num, title, track, grammar in c2_topics:
        curriculum.append({
            "test_id": f"TEV-IT-C2-{num}", "title": title, "level": "C2", "category": "core",
            "workplace_track": track, "grammar_focus": grammar, "estimated_time_minutes": 20,
            "description": f"Mastery-tier global IT leadership and cybersecurity governance module examining {title.lower()}."
        })

    return curriculum

ALL_CURRICULA = {
    "tatra-engineering": get_tatra_eng_curriculum,
    "tatra-sales-engineering": get_tatra_sales_curriculum,
    "teva-engineering": get_teva_eng_curriculum,
    "tapi-chemistry": get_tapi_chem_curriculum,
    "teva-it": get_teva_it_curriculum
}
