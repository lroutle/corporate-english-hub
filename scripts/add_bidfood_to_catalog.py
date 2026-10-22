import sys
from pathlib import Path

CATALOG_PATH = Path("scripts/curriculum_catalog.py")

bidfood_code = '''

def get_bidfood_purchasing_curriculum():
    curriculum = []
    # A2 Foundation (001-020)
    a2_topics = [
        ("001", "Food Product Catalog & Packaging Units: Present Simple & Plurals", "Supplier Sourcing & Vendor Relationship Management", "Countable vs Uncountable Nouns & Plurals"),
        ("002", "Daily Purchase Orders & Supplier Confirmation: Present Simple 3rd Person", "Inventory Management, Lead Times & EDI Purchase Orders", "Present Simple 3rd person singular -s"),
        ("003", "Delivery Notes & Missing Quantities: Past Simple Regular & Irregular", "Quality Specifications, Food Safety & Non-Conformance Claims", "Past Simple regular & irregular verbs"),
        ("004", "Cold Warehouse Staging & Pallet Storage: Prepositions of Place", "Cold-Chain Logistics & Temperature-Controlled Transport", "Prepositions of Place (in, on, next to, between)"),
        ("005", "Receiving Chilled Goods & Temperature Checks: Modal Verbs (Must, Can, Should)", "Quality Specifications, Food Safety & Non-Conformance Claims", "Modal verbs (must, can, should)"),
        ("006", "Basic Supplier Inquiries by Email: Polite Requests (Could you, Would you)", "Supplier Sourcing & Vendor Relationship Management", "Polite Requests & Question Formation"),
        ("007", "Pricing Units, Weight Discrepancies & Kilogram Calculations: Numbers & Decimals", "Contract Terms, Incoterms & Payment Negotiation", "Numbers, units, weights & decimals"),
        ("008", "Morning Delivery Status Handover: Past Simple vs Present Simple", "Cold-Chain Logistics & Temperature-Controlled Transport", "Past Simple vs Present Simple"),
        ("009", "Comparing Supplier Prices & Minimum Order Quantities: Comparatives & Superlatives", "Supplier Sourcing & Vendor Relationship Management", "Comparatives & Superlatives (cheaper, lowest)"),
        ("010", "Navigating the Distribution Depot: Prepositions of Motion (Into, Onto, Across)", "Cold-Chain Logistics & Temperature-Controlled Transport", "Prepositions of Motion (into, onto, across)"),
        ("011", "Shelf Life & Best-Before Date Verification: Quantifiers (Some, Any, Enough, Much)", "Quality Specifications, Food Safety & Non-Conformance Claims", "Quantifiers (some, any, enough, too much)"),
        ("012", "Receiving Damaged Goods: Imperatives & Rejection Phrasing", "Quality Specifications, Food Safety & Non-Conformance Claims", "Imperatives for Directives & Checklists"),
        ("013", "Fish & Seafood Sourcing Inquiries: Modal Verbs (Can we, May I, Have to)", "Supplier Sourcing & Vendor Relationship Management", "Obligation & Permission (have to, may)"),
        ("014", "Tracking Inbound Refrigerated Trucks: Present Continuous for Active Shipments", "Cold-Chain Logistics & Temperature-Controlled Transport", "Present Continuous for in-transit tracking"),
        ("015", "Supplier Delivery Punctuality: Adverbs of Frequency (Always, Usually, Rarely)", "Supplier Sourcing & Vendor Relationship Management", "Adverbs of Frequency (always, usually, rarely)"),
        ("016", "Payment Terms & Invoice Verification: Rules & Obligations (Have to, Must not)", "Contract Terms, Incoterms & Payment Negotiation", "Rules & Obligations (have to, must not)"),
        ("017", "Warehouse Receiving Routine: Sequence Connectors (First, Next, Then, Finally)", "Cold-Chain Logistics & Temperature-Controlled Transport", "Sequence Markers (first, next, then, finally)"),
        ("018", "Reporting Quality Complaints to Suppliers: Past Simple Negatives & Questions", "Quality Specifications, Food Safety & Non-Conformance Claims", "Past Simple Negatives & Question Forms"),
        ("019", "Emergency Reorders for Depleted Stock: There is / There are & Quantifiers", "Inventory Management, Lead Times & EDI Purchase Orders", "There is / There are & Quantifiers"),
        ("020", "End-of-Month Stocktaking & Discrepancy Reporting: Checklist Phrasing", "Inventory Management, Lead Times & EDI Purchase Orders", "Compound Imperatives & Inventory Checklists")
    ]
    for num, title, track, grammar in a2_topics:
        curriculum.append({
            "test_id": f"BID-PUR-A2-{num}", "title": title, "level": "A2", "category": "core",
            "workplace_track": track, "grammar_focus": grammar, "estimated_time_minutes": 10,
            "description": f"Foundational wholesale purchasing English module covering {title.lower()}."
        })

    # B1 Operational (001-020)
    b1_topics = [
        ("001", "Cold-Chain Logistics & Data Logger Readings: Past Simple vs Past Perfect", "Cold-Chain Logistics & Temperature-Controlled Transport", "Past Simple vs Past Perfect"),
        ("002", "Master Purchasing Agreements & Volume Rebates: Passive Voice in Commercial SOPs", "Contract Terms, Incoterms & Payment Negotiation", "Passive Voice in Commercial SOPs"),
        ("003", "Daily Supplier Escalations & Backorder Updates: Present Simple vs Continuous", "Supplier Sourcing & Vendor Relationship Management", "Present Simple vs Present Continuous"),
        ("004", "Importing Frozen Meat & Poultry: First & Second Conditionals (If/When)", "Quality Specifications, Food Safety & Non-Conformance Claims", "First & Second Conditionals (If/When)"),
        ("005", "Managing Perishable Goods Claims: Prepositions of Cause & Manner", "Quality Specifications, Food Safety & Non-Conformance Claims", "Prepositions of Cause & Manner"),
        ("006", "Supplier Quality Specifications & Certificates of Analysis (CoA): Relative Clauses", "Quality Specifications, Food Safety & Non-Conformance Claims", "Relative Clauses (which, that, whose)"),
        ("007", "Commodity Price Fluctuation & Fuel Surcharges: Modal Verbs of Probability", "Contract Terms, Incoterms & Payment Negotiation", "Modal Verbs of Probability (must be, can't be)"),
        ("008", "Auditing Supplier Processing Facilities: Past Continuous vs Past Simple", "Supplier Sourcing & Vendor Relationship Management", "Past Continuous vs Past Simple"),
        ("009", "Customs Clearance & Single Administrative Document (SAD): Present Perfect with Yet, Already, Just", "Cold-Chain Logistics & Temperature-Controlled Transport", "Present Perfect with yet, already, just"),
        ("010", "Evaluating Alternative Packaging Materials: Degrees of Comparison & Tolerances", "Quality Specifications, Food Safety & Non-Conformance Claims", "Degrees of Comparison & Tolerances"),
        ("011", "Consolidating Less-Than-Truckload (LTL) Shipments: Purpose Clauses (In order to, So that)", "Cold-Chain Logistics & Temperature-Controlled Transport", "Purpose Clauses (in order to, so that)"),
        ("012", "Third-Party Logistics (3PL) Service Level Agreements: Passive Voice Reporting Forms", "Cold-Chain Logistics & Temperature-Controlled Transport", "Passive Voice Reporting Forms"),
        ("013", "Short-Dated Product Clearance & Markdown Strategies: Conditionals in Inventory Management", "Inventory Management, Lead Times & EDI Purchase Orders", "Conditionals in Inventory Management"),
        ("014", "EDI Purchase Order Exchange & ASN Synchronization: Temporal Conjunctions (Until, As soon as)", "Inventory Management, Lead Times & EDI Purchase Orders", "Temporal Conjunctions (until, as soon as, while)"),
        ("015", "Supplier Contract Renegotiation & Price Defense: Phrasal Verbs in Commercial Purchasing", "Contract Terms, Incoterms & Payment Negotiation", "Phrasal Verbs in Commercial Purchasing"),
        ("016", "Incoterms 2020 in Food Import (FCA, CIF, DPU, DAP): Passive Voice with Modals", "Contract Terms, Incoterms & Payment Negotiation", "Passive Voice with Modals"),
        ("017", "Supplier Quality Non-Conformance & CAPA Tracking: Present Perfect Continuous", "Quality Specifications, Food Safety & Non-Conformance Claims", "Present Perfect Continuous (duration)"),
        ("018", "Supplier Sourcing Audits & IFS/BRC Certification: Reported Speech in Quality Audits", "Supplier Sourcing & Vendor Relationship Management", "Reported Speech in Quality Audits"),
        ("019", "Cross-Docking Perishable Produce at Distribution Centers: Prepositions of Motion & Logistics Flow", "Cold-Chain Logistics & Temperature-Controlled Transport", "Prepositions of Motion & Logistics Flow"),
        ("020", "Post-Delivery Damage Claims & Carrier Subrogation: Cause & Effect Connectors", "Quality Specifications, Food Safety & Non-Conformance Claims", "Cause & Effect Connectors (due to, owing to)")
    ]
    for num, title, track, grammar in b1_topics:
        curriculum.append({
            "test_id": f"BID-PUR-B1-{num}", "title": title, "level": "B1", "category": "core",
            "workplace_track": track, "grammar_focus": grammar, "estimated_time_minutes": 15,
            "description": f"Intermediate professional purchasing English module analyzing {title.lower()}."
        })

    # B2 Advanced (001-020)
    b2_topics = [
        ("001", "Long-Term Supply Contracts & Force Majeure Invocation: Inverted Third Conditionals", "Contract Terms, Incoterms & Payment Negotiation", "Inverted Conditionals (Had we known...)"),
        ("002", "Annual Vendor Rebate & Payment Term Negotiations: Negative Inversion for Professional Rigor", "Contract Terms, Incoterms & Payment Negotiation", "Negative Inversion (Rarely does, Under no circumstances)"),
        ("003", "Hedge Accounting & Currency Risk in Food Commodities: Mixed Conditionals", "Contract Terms, Incoterms & Payment Negotiation", "Mixed Conditionals (past cause, present result)"),
        ("004", "Supplier Code of Conduct & ESG Carbon Footprint Audits: Mandative Subjunctive in Corporate Procurement", "Supplier Sourcing & Vendor Relationship Management", "Mandative Subjunctive (mandate that X furnish)"),
        ("005", "Private Label Manufacturing Agreements & Recipe Exclusivity: Complex Relative Clauses & Restrictive Covenants", "Supplier Sourcing & Vendor Relationship Management", "Preposition + Relative Pronoun (in which, under whose)"),
        ("006", "Product Recall Crisis Management & Supply Chain Traceability: Participle Clauses in Incident Inquests", "Quality Specifications, Food Safety & Non-Conformance Claims", "Participle Clauses (Having identified, Being informed)"),
        ("007", "Exclusive Wholesale Distribution Rights & Territorial Restrictions: Advanced Conditionals & Concession Clauses", "Contract Terms, Incoterms & Payment Negotiation", "Concession Clauses (Even though, Whereas, Albeit)"),
        ("008", "Supply Shortages & Allocation Quota Negotiations: Advanced Modal Deduction & Epistemic Stance", "Supplier Sourcing & Vendor Relationship Management", "Advanced Modals (cannot have been, must have realized)"),
        ("009", "Container Shipping Demurrage & Detention Disputes: Discourse Markers in Commercial Dispute Escalation", "Cold-Chain Logistics & Temperature-Controlled Transport", "Formal Discourse Markers (notwithstanding, conversely)"),
        ("010", "Global Seafood Sourcing: Sustainable Fisheries & Tariff Classifications: Advanced Passive Constructions", "Supplier Sourcing & Vendor Relationship Management", "Advanced Passive Reporting (is understood to have been)"),
        ("011", "Supplier Insolvency & Contingency Dual-Sourcing Strategies: Hypothetical & Unreal Structures", "Supplier Sourcing & Vendor Relationship Management", "Hypothetical Inversion (Were a supplier to enter...)"),
        ("012", "Cold-Chain Fleet Logistics Outsourcing Tender: Evaluative Language & RFP Defense", "Cold-Chain Logistics & Temperature-Controlled Transport", "Evaluative Language in RFP Scoring"),
        ("013", "Anti-Corruption & Fair Trade Compliance in Agricultural Sourcing: Fronting & Inversion for Emphasis", "Supplier Sourcing & Vendor Relationship Management", "Fronting & Inversion (On no account may...)"),
        ("014", "Multi-Million Euro Annual Purchasing Budgeting: Advanced Forecasting & Quantitative Hedging", "Contract Terms, Incoterms & Payment Negotiation", "Epistemic Hedging & Future Projections"),
        ("015", "Supplier Contract Breach & Liquidated Damages Claims: Legalistic Phrasing in Procurement Disputes", "Contract Terms, Incoterms & Payment Negotiation", "Legalistic Phrasing & Contractual Formulas"),
        ("016", "Biosecurity Quarantines & Veterinary Border Inspection Post (BIP) Holds: Formal Epistemic Modals", "Quality Specifications, Food Safety & Non-Conformance Claims", "Epistemic Modals (may well, might conceivably)"),
        ("017", "Warehouse Automation & Automated Storage and Retrieval System (ASRS) Procurement: High-Register Engineering RFQs", "Inventory Management, Lead Times & EDI Purchase Orders", "Formulaic Subjunctive in Technical Specifications"),
        ("018", "Packaging Sustainability Directive (EU PPWR) Purchasing Compliance: Regulatory Deontic Modals", "Quality Specifications, Food Safety & Non-Conformance Claims", "Regulatory Deontic Modals (shall comply, is obliged to)"),
        ("019", "Vendor Performance Scorecards & Supplier KPI Reviews: Diplomatic Hedging & Constructive Criticism", "Supplier Sourcing & Vendor Relationship Management", "Diplomatic Hedging & Stance"),
        ("020", "Joint Business Planning (JBP) with Multinationals: Executive Negotiation Rhetoric", "Supplier Sourcing & Vendor Relationship Management", "High-Register Executive Negotiation Rhetoric")
    ]
    for num, title, track, grammar in b2_topics:
        curriculum.append({
            "test_id": f"BID-PUR-B2-{num}", "title": title, "level": "B2", "category": "core",
            "workplace_track": track, "grammar_focus": grammar, "estimated_time_minutes": 15,
            "description": f"Advanced commercial purchasing module evaluating {title.lower()}."
        })

    # C1 Advanced (001-020)
    c1_topics = [
        ("001", "International Commodity Futures Hedging & Derivative Supply Contracts", "Contract Terms, Incoterms & Payment Negotiation", "Mandative Subjunctive & Financial Jurisprudence"),
        ("002", "Multinational Food Consortium Merger & European Commission Anti-Trust Inquest", "Supplier Sourcing & Vendor Relationship Management", "High-Register Anti-Trust Competition Law"),
        ("003", "Cross-Border Food Fraud & Adulteration Forensic Arbitration", "Quality Specifications, Food Safety & Non-Conformance Claims", "Forensic Trade Arbitration & Evidence Standards"),
        ("004", "Transcontinental Reefer Container Fleet Default & Force Majeure Maritime Litigation", "Cold-Chain Logistics & Temperature-Controlled Transport", "Maritime Law & Hague-Visby Cargo Rules"),
        ("005", "Global Food Safety Initiative (GFSI) Systemic Failure Arbitration Under Swiss Law", "Quality Specifications, Food Safety & Non-Conformance Claims", "Commercial Arbitration Formulas & Indemnification"),
        ("006", "International Trade Sanctions & Geopolitical Agricultural Embargo Inquests", "Contract Terms, Incoterms & Payment Negotiation", "Deontic Inversion & WTO Agricultural Treaty Law"),
        ("007", "Corporate Sustainability Due Diligence Directive (CSDDD) Global Supply Chain Governance", "Supplier Sourcing & Vendor Relationship Management", "High-Register Corporate Governance & ESG Liability"),
        ("008", "Catastrophic Cold-Storage Ammonia Catastrophe: Third-Party Warehouse Tort Claims", "Cold-Chain Logistics & Temperature-Controlled Transport", "Forensic Civil Liability & Multi-Party Tort Law"),
        ("009", "Bilateral Agricultural Quota Dispute Before the WTO Dispute Settlement Body", "Contract Terms, Incoterms & Payment Negotiation", "Diplomatic Trade Treaty Phrasing & Retaliation"),
        ("010", "Forensic Supplier Deposition: Cartel Price-Fixing in Wholesale Frozen Foods", "Supplier Sourcing & Vendor Relationship Management", "Legal Cross-Examination & Forensic Testimony"),
        ("011", "Master Franchise Distribution & Brand Licensing Sovereign Jurisdiction Disputes", "Contract Terms, Incoterms & Payment Negotiation", "Complex Jurisdictional Clauses & Choice of Law"),
        ("012", "International Currency Collapse & Hyperinflationary Agricultural Indexation", "Contract Terms, Incoterms & Payment Negotiation", "Contractual Price Adjustment Formulas"),
        ("013", "Biotechnology & Genetically Modified Food Regulatory Interdiction Inquests", "Quality Specifications, Food Safety & Non-Conformance Claims", "Biosafety Protocols & Precautionary Principle Jurisprudence"),
        ("014", "Black Sea Grain & Edible Oil Corridor Maritime Blockade Force Majeure", "Cold-Chain Logistics & Temperature-Controlled Transport", "Admiralty Law & War Risk Repudiation"),
        ("015", "Class Action Shareholder Inquest: Supply Chain Deforestation Disclosures", "Supplier Sourcing & Vendor Relationship Management", "Corporate Securities Disclosure Litigation"),
        ("016", "High-Volume Private Label Intellectual Property & Trademark Infringement Disputes", "Supplier Sourcing & Vendor Relationship Management", "FMCG Trademark Litigation & Packaging Claims"),
        ("017", "Multi-National Cold Chain Transshipment Hub Catastrophic Power Grid Failure Arbitration", "Cold-Chain Logistics & Temperature-Controlled Transport", "Arbitral Award Enforcement & Liability Allocation"),
        ("018", "Export Credit Agency (ECA) Sovereign Guarantee Default in Food Aid Procurement", "Contract Terms, Incoterms & Payment Negotiation", "Sovereign Debt Restructuring & ECA Credit Agreements"),
        ("019", "Administrative Regulatory Penal Defense: EU Deforestation Regulation (EUDR)", "Quality Specifications, Food Safety & Non-Conformance Claims", "Regulatory Compliance Verification & Due Diligence Defenses"),
        ("020", "Chief Procurement Officer Keynote: Global Food Security & Resilient Supply Networks", "Supplier Sourcing & Vendor Relationship Management", "High-Register Executive Keynote Rhetoric")
    ]
    for num, title, track, grammar in c1_topics:
        curriculum.append({
            "test_id": f"BID-PUR-C1-{num}", "title": title, "level": "C1", "category": "core",
            "workplace_track": track, "grammar_focus": grammar, "estimated_time_minutes": 20,
            "description": f"Mastery-tier corporate procurement leadership module examining {title.lower()}."
        })

    return curriculum


def get_bidfood_engineering_curriculum():
    curriculum = []
    # A2 Foundation (001-020)
    a2_topics = [
        ("001", "Processing Plant Tools, Gaskets & PPE: Present Simple & Imperatives", "Preventative Maintenance, PLC Automation & Breakdown Diagnostics", "Imperatives & Present Simple"),
        ("002", "Daily Maintenance Routines & Conveyor Lubrication: Present Simple", "Processing Plant Conveyors & Automated Packaging Lines", "Present Simple 3rd person singular -s"),
        ("003", "Yesterday's Equipment Stoppages & Broken Belts: Past Simple Regular & Irregular", "Preventative Maintenance, PLC Automation & Breakdown Diagnostics", "Past Simple regular & irregular verbs"),
        ("004", "Factory Layout & Ammonia Valve Locations: Prepositions of Place", "Industrial Refrigeration & Ammonia Cascade Systems", "Prepositions of Place (above, behind, under)"),
        ("005", "Ammonia Refrigeration Room Safety & Gas Detectors: Can & Must", "Industrial Refrigeration & Ammonia Cascade Systems", "Modal verbs (must, can, must not)"),
        ("006", "Selecting Sanitary Fittings: Tri-Clamps, Butterfly Valves & O-Rings", "CIP (Clean-in-Place) Sanitation & Food Hygiene Engineering", "Demonstratives & Countable Equipment Nouns"),
        ("007", "Operating Parameters: Bar, Celsius & Flow Rates (L/min): Numbers & Decimals", "Steam Boilers, Compressed Air & Plant Utilities", "Numbers, units, pressures & temperatures"),
        ("008", "Shift Handover Log: Reporting Compressor Operating Hours: Past Simple vs Present Simple", "Industrial Refrigeration & Ammonia Cascade Systems", "Past Simple vs Present Simple"),
        ("009", "Freezer Tunnel Core Temperatures & Fan Speeds: Comparatives & Superlatives", "Industrial Refrigeration & Ammonia Cascade Systems", "Comparatives & Superlatives (colder, fastest)"),
        ("010", "Sanitary Pipeline Cleaning Routing: Prepositions of Motion (Through, Into, Along)", "CIP (Clean-in-Place) Sanitation & Food Hygiene Engineering", "Prepositions of Motion (through, into, along)"),
        ("011", "Boiler Water Treatment & Chemical Dosing: Quantifiers (Some, Any, Enough, Too much)", "Steam Boilers, Compressed Air & Plant Utilities", "Quantifiers (some, any, enough, too much)"),
        ("012", "Emergency Stop Buttons & Interlock Gates: Imperatives for Directives", "Processing Plant Conveyors & Automated Packaging Lines", "Imperatives for Emergency Directives"),
        ("013", "Working at Heights on Cold Storage Racks: Modal Verbs (Should, Must not, Have to)", "Preventative Maintenance, PLC Automation & Breakdown Diagnostics", "Modal verbs (should, must not, have to)"),
        ("014", "Pneumatic Valve Actuator Troubleshooting: Present Continuous for Active Faults", "Processing Plant Conveyors & Automated Packaging Lines", "Present Continuous for Active Faults"),
        ("015", "Sanitation Cycle Frequency & Swab Tests: Adverbs of Frequency", "CIP (Clean-in-Place) Sanitation & Food Hygiene Engineering", "Adverbs of Frequency (always, never, rarely)"),
        ("016", "Chemical Cleaning PPE & Acid Storage: Rules & Obligations (Have to, Must not)", "CIP (Clean-in-Place) Sanitation & Food Hygiene Engineering", "Rules & Obligations (have to, must not)"),
        ("017", "Pump Impeller Disassembly & Seal Inspection: Sequence Markers (First, Then, Next, Finally)", "Preventative Maintenance, PLC Automation & Breakdown Diagnostics", "Sequence Markers (first, then, next, finally)"),
        ("018", "Reporting Damaged Conveyor Modular Belts: Past Simple Negatives & Questions", "Processing Plant Conveyors & Automated Packaging Lines", "Past Simple Negatives & Question Forms"),
        ("019", "Spare Motor Ordering & Bearing Inventory: There is / There are & Quantifiers", "Preventative Maintenance, PLC Automation & Breakdown Diagnostics", "There is / There are & Quantifiers"),
        ("020", "Lockout-Tagout (LOTO) Procedures & Energy Isolation: Checklist Phrasing", "Preventative Maintenance, PLC Automation & Breakdown Diagnostics", "Compound Imperatives & Safety Checklists")
    ]
    for num, title, track, grammar in a2_topics:
        curriculum.append({
            "test_id": f"BID-ENG-A2-{num}", "title": title, "level": "A2", "category": "core",
            "workplace_track": track, "grammar_focus": grammar, "estimated_time_minutes": 10,
            "description": f"Foundational food process engineering English module covering {title.lower()}."
        })

    # B1 Operational (001-020)
    b1_topics = [
        ("001", "Ammonia Refrigeration Compressor Overhaul: Past Simple vs Past Perfect", "Industrial Refrigeration & Ammonia Cascade Systems", "Past Simple vs Past Perfect"),
        ("002", "Automated Spiral Freezer Belt Tension & Defrost Cycles: Passive Voice in Maintenance SOPs", "Industrial Refrigeration & Ammonia Cascade Systems", "Passive Voice in Maintenance SOPs"),
        ("003", "Shift Handover & Daily Utility Consumption: Present Simple vs Continuous", "Steam Boilers, Compressed Air & Plant Utilities", "Present Simple vs Present Continuous"),
        ("004", "Pasteurizer Flow Divert Valve Troubleshooting: First & Second Conditionals", "CIP (Clean-in-Place) Sanitation & Food Hygiene Engineering", "First & Second Conditionals (If/When)"),
        ("005", "Clean-in-Place (CIP) Caustic & Acid Cycles: Prepositions of Cause & Manner", "CIP (Clean-in-Place) Sanitation & Food Hygiene Engineering", "Prepositions of Cause & Manner"),
        ("006", "Plate Heat Exchanger Gasket Replacement & Leak Testing: Relative Clauses", "Industrial Refrigeration & Ammonia Cascade Systems", "Relative Clauses (which, that, whose)"),
        ("007", "Compressed Air Desiccant Dryer Dewpoint Calibration: Modal Verbs of Probability", "Steam Boilers, Compressed Air & Plant Utilities", "Modal Verbs of Probability (must be, can't be)"),
        ("008", "Steam Boiler Water Level Controller Diagnostics: Past Continuous vs Past Simple", "Steam Boilers, Compressed Air & Plant Utilities", "Past Continuous vs Past Simple"),
        ("009", "High-Speed Slicing & Portioning Machine Calibration: Present Perfect with Yet, Already, Just", "Processing Plant Conveyors & Automated Packaging Lines", "Present Perfect with yet, already, just"),
        ("010", "Modified Atmosphere Packaging (MAP) Gas Mixing Accuracy: Degrees of Comparison & Tolerances", "Processing Plant Conveyors & Automated Packaging Lines", "Degrees of Comparison & Tolerances"),
        ("011", "Centrifugal Product Pump Mechanical Seal Installation: Purpose Clauses (In order to, So that)", "CIP (Clean-in-Place) Sanitation & Food Hygiene Engineering", "Purpose Clauses (in order to, so that)"),
        ("012", "Food Safety Equipment Audits (IFS/HACCP): Passive Voice Reporting Forms", "CIP (Clean-in-Place) Sanitation & Food Hygiene Engineering", "Passive Voice Reporting Forms"),
        ("013", "Refrigeration Evaporator Fan VFD Fault Codes: Conditionals in Diagnostics", "Industrial Refrigeration & Ammonia Cascade Systems", "Conditionals in Diagnostic Troubleshooting"),
        ("014", "Automated Palletizer Stacking Pattern & Sensor Tuning: Temporal Conjunctions (Until, As soon as)", "Processing Plant Conveyors & Automated Packaging Lines", "Temporal Conjunctions (until, as soon as, while)"),
        ("015", "Plant Wastewater Treatment & DAF System Diagnostics: Phrasal Verbs in Plant Maintenance", "Steam Boilers, Compressed Air & Plant Utilities", "Phrasal Verbs in Plant Maintenance"),
        ("016", "Hygienic Pipe Welding & Orbital TIG Weld Inspection: Passive Voice with Modals", "CIP (Clean-in-Place) Sanitation & Food Hygiene Engineering", "Passive Voice with Modals"),
        ("017", "Predictive Vibration Analysis on Ammonia Screw Compressors: Present Perfect Continuous", "Industrial Refrigeration & Ammonia Cascade Systems", "Present Perfect Continuous (duration)"),
        ("018", "Supplier Factory Acceptance Testing (FAT) for New Packaging Lines: Reported Speech in Equipment Handovers", "Processing Plant Conveyors & Automated Packaging Lines", "Reported Speech in Equipment Handovers"),
        ("019", "Electrical Control Cabinet Wiring & 24V DC Circuit Routing: Prepositions of Motion & Spatial Arrangement", "Preventative Maintenance, PLC Automation & Breakdown Diagnostics", "Prepositions of Motion & Spatial Arrangement"),
        ("020", "Post-Breakdown Root Cause Analysis (RCA) on Blending Line: Cause & Effect Connectors", "Preventative Maintenance, PLC Automation & Breakdown Diagnostics", "Cause & Effect Connectors (due to, owing to)")
    ]
    for num, title, track, grammar in b1_topics:
        curriculum.append({
            "test_id": f"BID-ENG-B1-{num}", "title": title, "level": "B1", "category": "core",
            "workplace_track": track, "grammar_focus": grammar, "estimated_time_minutes": 15,
            "description": f"Intermediate process engineering English module analyzing {title.lower()}."
        })

    # B2 Advanced (001-020)
    b2_topics = [
        ("001", "Industrial Refrigeration Charge Leakage & Emergency Ventilation: Inverted Third Conditionals", "Industrial Refrigeration & Ammonia Cascade Systems", "Inverted Conditionals (Had the sensor detected...)"),
        ("002", "PLC Safety Interlocks & Cat 4 Emergency Stop Verification: Negative Inversion for Rigor", "Preventative Maintenance, PLC Automation & Breakdown Diagnostics", "Negative Inversion (Under no circumstances should...)"),
        ("003", "Combined Heat and Power (CHP) Gas Turbine Tripping: Mixed Conditionals", "Steam Boilers, Compressed Air & Plant Utilities", "Mixed Conditionals (past cause, present consequence)"),
        ("004", "CIP Cross-Contamination Prevention & Double-Seat Valve Blocks: Mandative Subjunctive in Sanitary Design", "CIP (Clean-in-Place) Sanitation & Food Hygiene Engineering", "Mandative Subjunctive (mandate that valves provide)"),
        ("005", "SCADA Network Segmentation & Industrial Firewall Architecture: Complex Relative Clauses & Network Topologies", "Preventative Maintenance, PLC Automation & Breakdown Diagnostics", "Preposition + Relative Pronoun (routing of which)"),
        ("006", "Catastrophic Ammonia Compressor Crankshaft Shear Failure: Participle Clauses in Forensic Inquests", "Industrial Refrigeration & Ammonia Cascade Systems", "Participle Clauses (Having analyzed, Having sustained)"),
        ("007", "Energy Efficiency Optimization & Heat Recovery from Condensers: Advanced Conditionals & Concession Clauses", "Industrial Refrigeration & Ammonia Cascade Systems", "Concession Clauses (Although, Whereas, In spite of)"),
        ("008", "Steam Pressure Reduction Station & Safety Relief Valve Sizing: Advanced Modal Deduction & Epistemic Stance", "Steam Boilers, Compressed Air & Plant Utilities", "Advanced Modals (cannot possibly have lifted)"),
        ("009", "Automated Guided Vehicle (AGV) Fleet Dispatch & Fleet Bottlenecks: Discourse Markers in Engineering Reviews", "Processing Plant Conveyors & Automated Packaging Lines", "Formal Discourse Markers (notwithstanding, conversely)"),
        ("010", "Blast Freezing Thermodynamics & Airflow Distribution Modeling: Advanced Passive Constructions", "Industrial Refrigeration & Ammonia Cascade Systems", "Advanced Passive Reporting (are modeled to calculate)"),
        ("011", "Biological Wastewater Digester Biogas Generation Disruptions: Hypothetical & Unreal Structures", "Steam Boilers, Compressed Air & Plant Utilities", "Hypothetical Inversion (Were the digester pH to drop...)"),
        ("012", "OEM Capital Equipment Procurement & FAT Defect Punch-Lists: Evaluative Language & Dispute Escalation", "Processing Plant Conveyors & Automated Packaging Lines", "Evaluative Language in FAT Punch-Lists"),
        ("013", "Hazardous Work Authorization: Confined Space Entry into Mixing Silos: Fronting & Inversion for Emphasis", "Preventative Maintenance, PLC Automation & Breakdown Diagnostics", "Fronting & Inversion (Only after atmosphere testing...)"),
        ("014", "Total Productive Maintenance (TPM) & Overall Equipment Effectiveness (OEE): Advanced Statistical Reporting", "Preventative Maintenance, PLC Automation & Breakdown Diagnostics", "Epistemic Hedging & Statistical Reporting"),
        ("015", "Process Chiller Refrigerant Phase-Out (F-Gas Regulations): High-Register Regulatory Compliance", "Industrial Refrigeration & Ammonia Cascade Systems", "Regulatory Deontic Modals (shall comply, is mandated to)"),
        ("016", "Automated Sorter Optical Sensor Vision Inspection Failure: Epistemic Hedging in Root Cause Analysis", "Processing Plant Conveyors & Automated Packaging Lines", "Epistemic Hedging (might conceivably have misread)"),
        ("017", "High-Pressure Hydraulic Power Pack Failure & Fluid Analysis: Advanced Technical Causal Chains", "Processing Plant Conveyors & Automated Packaging Lines", "Advanced Causal Chains (resulted from, stemmed from)"),
        ("018", "Dust Explosion Protection (ATEX Directive) in Flour & Sugar Silos: Regulatory Deontic Modals", "Preventative Maintenance, PLC Automation & Breakdown Diagnostics", "ATEX Regulatory Modals (must undergo, shall verify)"),
        ("019", "Preventative Maintenance Vibration Spectrum & Demodulation Analysis: Precision Diagnostic Lexicon", "Preventative Maintenance, PLC Automation & Breakdown Diagnostics", "Diagnostic Frequency Jargon & Complex Post-Modifiers"),
        ("020", "Engineering Management Review: Decarbonization & Net-Zero Factory Targets: Executive Persuasion Rhetoric", "Steam Boilers, Compressed Air & Plant Utilities", "High-Register Executive Persuasion Rhetoric")
    ]
    for num, title, track, grammar in b2_topics:
        curriculum.append({
            "test_id": f"BID-ENG-B2-{num}", "title": title, "level": "B2", "category": "core",
            "workplace_track": track, "grammar_focus": grammar, "estimated_time_minutes": 15,
            "description": f"Advanced food processing plant engineering module evaluating {title.lower()}."
        })

    # C1 Advanced (001-020)
    c1_topics = [
        ("001", "Catastrophic Ammonia Gas Release Inquest: Industrial Safety & Environmental Court Inquest", "Industrial Refrigeration & Ammonia Cascade Systems", "Forensic Inquest Rhetoric & Environmental Court Discourse"),
        ("002", "Multi-Million Euro Automated High-Bay Cold Store EPC Contract Default Arbitration", "Industrial Refrigeration & Ammonia Cascade Systems", "FIDIC Engineering Contract Default Arbitration"),
        ("003", "European Union Industrial Emissions Directive (IED) Regulatory Non-Compliance Inquest", "Steam Boilers, Compressed Air & Plant Utilities", "Environmental Administrative Law & Penal Appeals"),
        ("004", "Critical Machinery Patent Infringement Litigation: Cryogenic Spiral Freezer Airflow Design", "Industrial Refrigeration & Ammonia Cascade Systems", "Mechanical Patent Claim Construction & Cross-Examination"),
        ("005", "Catastrophic Dust Explosion & Fire Litigation: ATEX Equipment Liability Arbitration", "Preventative Maintenance, PLC Automation & Breakdown Diagnostics", "ATEX Causation Analysis & Product Liability Litigation"),
        ("006", "Food Plant Pathogen Contamination (Listeria monocytogenes) Civil Liability Inquest", "CIP (Clean-in-Place) Sanitation & Food Hygiene Engineering", "Microbiological Forensic Tracing & Tort Defense"),
        ("007", "Industrial Steam Boiler Explosion: Independent Forensic Engineering Inquiry", "Steam Boilers, Compressed Air & Plant Utilities", "Pressure Vessel Failure Analysis & Statutory Inquiry"),
        ("008", "Major Utility Grid Blackout & Multi-Facility Ammonia Dump Arbitration Under English Law", "Industrial Refrigeration & Ammonia Cascade Systems", "Commercial Arbitration Formulas & Grid Loss Indemnification"),
        ("009", "International OEM Machinery Supply Contract Breach: Performance Guarantee Litigation", "Processing Plant Conveyors & Automated Packaging Lines", "Contractual Performance Warranties & Jurisdictional Claims"),
        ("010", "Forensic Expert Witness Deposition: Sanitary Welding Failure & Product Contamination", "CIP (Clean-in-Place) Sanitation & Food Hygiene Engineering", "Cross-Examination Deposition & NDT Metallurgical Testimony"),
        ("011", "National Carbon Border Adjustment Mechanism (CBAM) Industrial Decarbonization Audits", "Steam Boilers, Compressed Air & Plant Utilities", "High-Register Energy Governance & Carbon Auditing"),
        ("012", "Corporate Manslaughter & Industrial Accident Defense: Confined Space Asphyxiation", "Preventative Maintenance, PLC Automation & Breakdown Diagnostics", "Occupational Health & Safety Criminal Defense"),
        ("013", "Global Industrial Automation Supply Chain Embargo & Microprocessor Force Majeure", "Preventative Maintenance, PLC Automation & Breakdown Diagnostics", "International Sanctions & Semiconductor Force Majeure"),
        ("014", "Multi-Site Industrial Refrigeration Energy Performance Contracting (EPC) Disputes", "Industrial Refrigeration & Ammonia Cascade Systems", "Energy Service Performance Measurement Disputes"),
        ("015", "Board-Level Capital Expenditure Defense: Multi-Facility Green Hydrogen Boiler Conversion", "Steam Boilers, Compressed Air & Plant Utilities", "Executive Capital Allocation Justification & Board Rhetoric"),
        ("016", "Supercritical CO2 Industrial Extraction Plant High-Pressure Pipe Rupture Inquest", "Industrial Refrigeration & Ammonia Cascade Systems", "High-Pressure Thermodynamics & Material Fatigue Inquests"),
        ("017", "Corporate Cybersecurity Inquest: SCADA Operational Technology (OT) Stuxnet-Style Infiltration", "Preventative Maintenance, PLC Automation & Breakdown Diagnostics", "OT Cybersecurity Governance & Forensic Inquests"),
        ("018", "Automated Cold Store Structural Collapse Inquest: Seismic Design & Dynamic Load Modeling", "Industrial Refrigeration & Ammonia Cascade Systems", "Civil & Structural Engineering Forensic Analysis"),
        ("019", "Industrial Effluent Discharge Environmental Sanctions Defense: Chemical Oxygen Demand Violations", "Steam Boilers, Compressed Air & Plant Utilities", "Water Quality Jurisprudence & Municipal Discharge Appeals"),
        ("020", "Vice President of Engineering Keynote: Autonomous Lights-Out Food Manufacturing Plants", "Preventative Maintenance, PLC Automation & Breakdown Diagnostics", "High-Register Executive Visionary Industrial Leadership")
    ]
    for num, title, track, grammar in c1_topics:
        curriculum.append({
            "test_id": f"BID-ENG-C1-{num}", "title": title, "level": "C1", "category": "core",
            "workplace_track": track, "grammar_focus": grammar, "estimated_time_minutes": 20,
            "description": f"Mastery-tier food processing engineering leadership module examining {title.lower()}."
        })

    return curriculum
'''

content = CATALOG_PATH.read_text(encoding="utf-8")

# Check if already added
if "get_bidfood_purchasing_curriculum" not in content:
    # Find the end of functions before ALL_CURRICULA
    idx = content.find("ALL_CURRICULA = {")
    if idx != -1:
        new_content = content[:idx] + bidfood_code + "\n" + content[idx:]
        # Update ALL_CURRICULA dictionary
        new_content = new_content.replace(
            '"teva-it": get_tapi_it_curriculum\n}',
            '"teva-it": get_tapi_it_curriculum,\n    "bidfood-purchasing": get_bidfood_purchasing_curriculum,\n    "bidfood-engineering": get_bidfood_engineering_curriculum\n}'
        )
        CATALOG_PATH.write_text(new_content, encoding="utf-8")
        print("Successfully added Bidfood Purchasing and Engineering curricula to curriculum_catalog.py!")
    else:
        print("Error: Could not locate ALL_CURRICULA in curriculum_catalog.py")
else:
    print("Bidfood curricula already present in curriculum_catalog.py")
