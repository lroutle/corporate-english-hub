#!/usr/bin/env python3
"""
Build the Master Curriculum Manifest for the 120 Tatra Trucks Interactive English Modules.
"""

import json
from pathlib import Path

curriculum = [
    # =========================================================================
    # CEFR B1: CORE MODULES (001 - 050)
    # =========================================================================
    {
        "test_id": "TTR-B1-001",
        "title": "Chassis Assembly & Final Inspection: Past Simple vs Past Perfect",
        "level": "B1",
        "category": "core",
        "workplace_track": "Quality Assurance & Assembly",
        "estimated_time_minutes": 15,
        "description": "Master narrative past tenses and sequence of events during pre-delivery inspection and defect detection.",
        "grammar_focus": "Past Simple vs Past Perfect Passive"
    },
    {
        "test_id": "TTR-B1-002",
        "title": "International Spare Parts Dispatch: Present Perfect vs Past Simple",
        "level": "B1",
        "category": "core",
        "workplace_track": "International Sales & Tenders",
        "estimated_time_minutes": 15,
        "description": "Differentiate finished time reference from status up to the present when updating foreign dealerships on consignments.",
        "grammar_focus": "Present Perfect vs Past Simple with Time Adverbials"
    },
    {
        "test_id": "TTR-B1-003",
        "title": "Shift Handover & Daily Line Routines: Present Simple vs Continuous",
        "level": "B1",
        "category": "core",
        "workplace_track": "Quality Assurance & Assembly",
        "estimated_time_minutes": 12,
        "description": "Distinguish permanent shop floor standard procedures from temporary deviations and ongoing maintenance tasks.",
        "grammar_focus": "Present Simple vs Present Continuous"
    },
    {
        "test_id": "TTR-B1-004",
        "title": "Production Bottlenecks & Assembly Delays: Present Perfect Continuous",
        "level": "B1",
        "category": "core",
        "workplace_track": "Procurement & Supply Chain",
        "estimated_time_minutes": 15,
        "description": "Communicate ongoing actions and duration leading up to the present regarding supplier backlogs.",
        "grammar_focus": "Present Perfect Continuous (for / since / how long)"
    },
    {
        "test_id": "TTR-B1-005",
        "title": "Factory Safety Directives & ISO Standards: Modals of Obligation",
        "level": "B1",
        "category": "core",
        "workplace_track": "Quality Assurance & Assembly",
        "estimated_time_minutes": 12,
        "description": "Apply must, have to, must not, and don't have to accurately in workshop PPE and hazardous chemical regulations.",
        "grammar_focus": "Modals of Obligation & Prohibition"
    },
    {
        "test_id": "TTR-B1-006",
        "title": "Cab Mounting & Surface Coating: Passive Voice (Present Simple)",
        "level": "B1",
        "category": "core",
        "workplace_track": "General Automotive Manufacturing",
        "estimated_time_minutes": 14,
        "description": "Describe automated cataphoresis dipping, primer application, and cab welding in standard manufacturing manuals.",
        "grammar_focus": "Present Simple Passive"
    },
    {
        "test_id": "TTR-B1-007",
        "title": "Hydraulic Pressure & Dyno Testing: First Conditional & Troubleshooting",
        "level": "B1",
        "category": "core",
        "workplace_track": "Powertrain & R&D Engineering",
        "estimated_time_minutes": 15,
        "description": "Formulate real condition-consequence clauses during engine dyno runs and hydraulic circuit checks.",
        "grammar_focus": "First Conditional (if / unless / as soon as)"
    },
    {
        "test_id": "TTR-B1-008",
        "title": "Heavy Duty Axle Comparison: Comparatives & Superlatives",
        "level": "B1",
        "category": "core",
        "workplace_track": "Powertrain & R&D Engineering",
        "estimated_time_minutes": 12,
        "description": "Compare vehicle gross weight ratings, ground clearance, and turning radius across Tatra 4x4, 6x6, and 8x8 chassis.",
        "grammar_focus": "Comparative and Superlative Adjectives & Adverbs"
    },
    {
        "test_id": "TTR-B1-009",
        "title": "Customer Inquiries & Technical Clarifications: Indirect Questions",
        "level": "B1",
        "category": "core",
        "workplace_track": "International Sales & Tenders",
        "estimated_time_minutes": 14,
        "description": "Formulate polite, non-inverted inquiries when corresponding with overseas distributors and municipal fleet buyers.",
        "grammar_focus": "Indirect Questions & Embedded Inquiries"
    },
    {
        "test_id": "TTR-B1-010",
        "title": "Spare Parts Warehouse Inventory: Countable vs Uncountable Nouns",
        "level": "B1",
        "category": "core",
        "workplace_track": "Procurement & Supply Chain",
        "estimated_time_minutes": 12,
        "description": "Eliminate Czenglish quantifiers on machinery, equipment, information, scrap, and damage.",
        "grammar_focus": "Countable vs Uncountable Nouns & Quantifiers"
    },
    {
        "test_id": "TTR-B1-011",
        "title": "Suspension Air Leak Diagnostics: Past Simple vs Continuous",
        "level": "B1",
        "category": "core",
        "workplace_track": "Homologation, Testing & Field Operations",
        "estimated_time_minutes": 14,
        "description": "Document sudden component failures occurring while high-speed off-road test driving was underway.",
        "grammar_focus": "Past Continuous interrupted by Past Simple"
    },
    {
        "test_id": "TTR-B1-012",
        "title": "Tatra Assembly Line Tooling: Relative Clauses (Defining)",
        "level": "B1",
        "category": "core",
        "workplace_track": "Quality Assurance & Assembly",
        "estimated_time_minutes": 12,
        "description": "Identify specialized tools, pneumatic wrenches, and jigs with which, that, who, and where.",
        "grammar_focus": "Defining Relative Clauses"
    },
    {
        "test_id": "TTR-B1-013",
        "title": "Export Delivery Commitments: Future Forms (Will vs Going To)",
        "level": "B1",
        "category": "core",
        "workplace_track": "International Sales & Tenders",
        "estimated_time_minutes": 14,
        "description": "Differentiate spontaneous commercial concessions from scheduled factory dispatch dates.",
        "grammar_focus": "Future: will vs be going to vs Present Continuous"
    },
    {
        "test_id": "TTR-B1-014",
        "title": "Component Defect Root-Cause: Dependent Prepositions",
        "level": "B1",
        "category": "core",
        "workplace_track": "Quality Assurance & Assembly",
        "estimated_time_minutes": 14,
        "description": "Apply correct prepositions: depend on, responsible for, comply with, result in, and account for.",
        "grammar_focus": "Dependent Prepositions in Technical Contexts"
    },
    {
        "test_id": "TTR-B1-015",
        "title": "Preventative Workshop Maintenance: Modals of Advice",
        "level": "B1",
        "category": "core",
        "workplace_track": "After-Sales, Service & Training",
        "estimated_time_minutes": 12,
        "description": "Issue actionable recommendations using should, shouldn't, ought to, and had better.",
        "grammar_focus": "Modals of Advice & Recommendation"
    },
    {
        "test_id": "TTR-B1-016",
        "title": "Transmission Assembly Protocols: Verb Patterns (Gerund vs Infinitive 1)",
        "level": "B1",
        "category": "core",
        "workplace_track": "Quality Assurance & Assembly",
        "estimated_time_minutes": 14,
        "description": "Master verbs followed by gerund or infinitive (avoid, consider, remember, stop, forget).",
        "grammar_focus": "Gerund vs Infinitive after Common Engineering Verbs"
    },
    {
        "test_id": "TTR-B1-017",
        "title": "Technical Component Replacement: Phrasal Verbs on the Line",
        "level": "B1",
        "category": "core",
        "workplace_track": "Quality Assurance & Assembly",
        "estimated_time_minutes": 14,
        "description": "Use automotive workshop phrasal verbs: strip down, put back, tighten up, wear out, set up.",
        "grammar_focus": "Separable and Inseparable Phrasal Verbs"
    },
    {
        "test_id": "TTR-B1-018",
        "title": "Incoterms & Export Contracts: Zero & First Conditionals",
        "level": "B1",
        "category": "core",
        "workplace_track": "International Sales & Tenders",
        "estimated_time_minutes": 14,
        "description": "Determine insurance liability, FOB vs CIF terms, and shipping risk transitions.",
        "grammar_focus": "Zero and First Conditionals in Commercial Agreements"
    },
    {
        "test_id": "TTR-B1-019",
        "title": "Engine Dynamometer Torque Curves: Describing Graphs & Trends",
        "level": "B1",
        "category": "core",
        "workplace_track": "Powertrain & R&D Engineering",
        "estimated_time_minutes": 14,
        "description": "Describe rpm, peak torque, fuel consumption spikes, and steady drops across power bands.",
        "grammar_focus": "Trend Verbs, Adverbs, and Prepositions (rise by, peak at)"
    },
    {
        "test_id": "TTR-B1-020",
        "title": "Subcontractor Steel Deliveries: Articles (A, An, The, Zero Article)",
        "level": "B1",
        "category": "core",
        "workplace_track": "Procurement & Supply Chain",
        "estimated_time_minutes": 12,
        "description": "Overcome Czech mother-tongue article omissions in technical purchase specifications.",
        "grammar_focus": "Definite, Indefinite, and Zero Articles in Technical Writing"
    },
    {
        "test_id": "TTR-B1-021",
        "title": "Off-Road Prototype Modifications: Second Conditional",
        "level": "B1",
        "category": "core",
        "workplace_track": "Powertrain & R&D Engineering",
        "estimated_time_minutes": 15,
        "description": "Discuss hypothetical engineering redesigns and chassis weight reductions.",
        "grammar_focus": "Second Conditional (If + Past Simple, would + base form)"
    },
    {
        "test_id": "TTR-B1-022",
        "title": "Tatra Backbone Tube Assembly: Past Simple Passive",
        "level": "B1",
        "category": "core",
        "workplace_track": "Quality Assurance & Assembly",
        "estimated_time_minutes": 14,
        "description": "Audit historical production logs: how the central tube and flanges were cast, welded, and inspected.",
        "grammar_focus": "Past Simple Passive"
    },
    {
        "test_id": "TTR-B1-023",
        "title": "Quality Audit Incident Reports: Linking Words of Contrast",
        "level": "B1",
        "category": "core",
        "workplace_track": "Quality Assurance & Assembly",
        "estimated_time_minutes": 14,
        "description": "Balance positive audit findings with non-conformities using however, although, in spite of.",
        "grammar_focus": "Connectors of Contrast & Concession"
    },
    {
        "test_id": "TTR-B1-024",
        "title": "Supplier Delivery Schedules: Prepositions of Time",
        "level": "B1",
        "category": "core",
        "workplace_track": "Procurement & Supply Chain",
        "estimated_time_minutes": 12,
        "description": "Precisely specify deadlines using in, on, at, by, within, and until in vendor purchase orders.",
        "grammar_focus": "Prepositions of Time & Deadlines"
    },
    {
        "test_id": "TTR-B1-025",
        "title": "Dealer Network Communications: Reported Speech (Statements)",
        "level": "B1",
        "category": "core",
        "workplace_track": "International Sales & Tenders",
        "estimated_time_minutes": 15,
        "description": "Relay distributor feedback and headquarters decisions with proper backshift of tenses.",
        "grammar_focus": "Reported Speech: Tense Backshift & Reporting Verbs"
    },
    {
        "test_id": "TTR-B1-026",
        "title": "Dakar Rally Support Logistics: Phrasal Verbs in Field Ops",
        "level": "B1",
        "category": "core",
        "workplace_track": "Homologation, Testing & Field Operations",
        "estimated_time_minutes": 14,
        "description": "Coordinate race truck servicing under tight schedules: break down, hold up, call in, catch up.",
        "grammar_focus": "Logistics & Operational Phrasal Verbs"
    },
    {
        "test_id": "TTR-B1-027",
        "title": "Cab Ergonomics & Controls: Non-Defining Relative Clauses",
        "level": "B1",
        "category": "core",
        "workplace_track": "Powertrain & R&D Engineering",
        "estimated_time_minutes": 14,
        "description": "Supply extra descriptive facts about driver comfort features using which, whose, and where.",
        "grammar_focus": "Non-Defining Relative Clauses with Commas"
    },
    {
        "test_id": "TTR-B1-028",
        "title": "Assembly Robotics Migration: Used to vs Be Used To",
        "level": "B1",
        "category": "core",
        "workplace_track": "General Automotive Manufacturing",
        "estimated_time_minutes": 14,
        "description": "Contrast former manual fabrication with current acclimation to automated CNC laser welding.",
        "grammar_focus": "Used to + base form vs Be/Get used to + -ing"
    },
    {
        "test_id": "TTR-B1-029",
        "title": "Service Bulletin Dispatches: Passive Voice with Modals",
        "level": "B1",
        "category": "core",
        "workplace_track": "After-Sales, Service & Training",
        "estimated_time_minutes": 14,
        "description": "Instruct field mechanics on procedures that must be executed or should be lubricated.",
        "grammar_focus": "Modal Passives (must be inspected, can be adjusted)"
    },
    {
        "test_id": "TTR-B1-030",
        "title": "Overseas Procurement Bids: Quantifiers & Partitives",
        "level": "B1",
        "category": "core",
        "workplace_track": "Procurement & Supply Chain",
        "estimated_time_minutes": 12,
        "description": "Specify raw material quantities: a great deal of, a batch of, numerous, several, few vs a few.",
        "grammar_focus": "Quantifiers & Expressions of Quantity"
    },
    {
        "test_id": "TTR-B1-031",
        "title": "Air Brake Pressure Drop: Cause & Effect Connectors",
        "level": "B1",
        "category": "core",
        "workplace_track": "Quality Assurance & Assembly",
        "estimated_time_minutes": 14,
        "description": "Link mechanical seal failures to air leaks using due to, owing to, as a result of, therefore.",
        "grammar_focus": "Conjunctions and Prepositions of Cause and Effect"
    },
    {
        "test_id": "TTR-B1-032",
        "title": "Technical Warranty Inquiries: Reported Questions",
        "level": "B1",
        "category": "core",
        "workplace_track": "After-Sales, Service & Training",
        "estimated_time_minutes": 14,
        "description": "Report dealer queries regarding warranty coverage without inverted question order.",
        "grammar_focus": "Reported Questions (if/whether and Wh- words)"
    },
    {
        "test_id": "TTR-B1-033",
        "title": "International Customer Tenders: Making Polite Requests",
        "level": "B1",
        "category": "core",
        "workplace_track": "International Sales & Tenders",
        "estimated_time_minutes": 12,
        "description": "Formulate diplomatic requests with could you please, would you mind + ing, would it be possible.",
        "grammar_focus": "Polite Formulaic Requests & Inquiries"
    },
    {
        "test_id": "TTR-B1-034",
        "title": "Engine Oil & Lubrication Specs: Verb Patterns (Gerund vs Infinitive 2)",
        "level": "B1",
        "category": "core",
        "workplace_track": "After-Sales, Service & Training",
        "estimated_time_minutes": 14,
        "description": "Detail requirements: allow to drain, require adding, recommend changing, fail to operate.",
        "grammar_focus": "Verb Patterns: Verb + Object + Infinitive vs Gerund"
    },
    {
        "test_id": "TTR-B1-035",
        "title": "Factory Spatial Layout & Transport: Prepositions of Place",
        "level": "B1",
        "category": "core",
        "workplace_track": "General Automotive Manufacturing",
        "estimated_time_minutes": 12,
        "description": "Guide visitors and forklifts between paint shop, stamping hall, and test track.",
        "grammar_focus": "Prepositions of Place and Direction (across, through, alongside)"
    },
    {
        "test_id": "TTR-B1-036",
        "title": "Technical Workshop Instructions: Imperatives & Sequencing",
        "level": "B1",
        "category": "core",
        "workplace_track": "Quality Assurance & Assembly",
        "estimated_time_minutes": 12,
        "description": "Draft clear Standard Operating Procedures (SOP): first loosen, next align, ensure that.",
        "grammar_focus": "Imperatives and Sequential Adverbs"
    },
    {
        "test_id": "TTR-B1-037",
        "title": "Chassis Geometrical Tolerances: Numbers & Measurements",
        "level": "B1",
        "category": "core",
        "workplace_track": "Quality Assurance & Assembly",
        "estimated_time_minutes": 14,
        "description": "Communicate millimeters, angular degrees, torque in Nm, and tolerance margins accurately.",
        "grammar_focus": "Technical Dimensions, Tolerances & Units of Measurement"
    },
    {
        "test_id": "TTR-B1-038",
        "title": "Sales Email Register: Semi-Formal vs Formal Expressions",
        "level": "B1",
        "category": "core",
        "workplace_track": "International Sales & Tenders",
        "estimated_time_minutes": 14,
        "description": "Select appropriate register when answering inquiries from foreign defense ministries vs dealers.",
        "grammar_focus": "Email Register, Openers, and Sign-offs"
    },
    {
        "test_id": "TTR-B1-039",
        "title": "Extreme Off-Road Mobility: Modals of Ability & Capacity",
        "level": "B1",
        "category": "core",
        "workplace_track": "Powertrain & R&D Engineering",
        "estimated_time_minutes": 12,
        "description": "Express vehicle capabilities: can ford water up to 1.5m, is able to conquer 45-degree gradients.",
        "grammar_focus": "Modals of Ability: Can, Could, Be able to, Capable of"
    },
    {
        "test_id": "TTR-B1-040",
        "title": "Assembly Line Problem Symptoms: Adjectives & Participles",
        "level": "B1",
        "category": "core",
        "workplace_track": "Quality Assurance & Assembly",
        "estimated_time_minutes": 14,
        "description": "Identify defective states: seized bearings, misaligned shafts, frayed wiring, cracked housings.",
        "grammar_focus": "Participle Adjectives (-ed vs -ing) in Mechanical Diagnostics"
    },
    {
        "test_id": "TTR-B1-041",
        "title": "Supplier Quality Claims: So vs Such, Too vs Enough",
        "level": "B1",
        "category": "core",
        "workplace_track": "Procurement & Supply Chain",
        "estimated_time_minutes": 12,
        "description": "Express defects: so brittle that it broke, such high porosity, not elastic enough.",
        "grammar_focus": "So/Such and Too/Enough with Adjectives and Nouns"
    },
    {
        "test_id": "TTR-B1-042",
        "title": "Production Milestones & Deadlines: Future Time Clauses",
        "level": "B1",
        "category": "core",
        "workplace_track": "Quality Assurance & Assembly",
        "estimated_time_minutes": 14,
        "description": "Ensure Present Simple is used after time conjunctions: when the truck clears inspection, as soon as.",
        "grammar_focus": "Time Clauses with When, As Soon As, Before, After + Present Simple"
    },
    {
        "test_id": "TTR-B1-043",
        "title": "International Trade Fair Follow-ups: Phrasal Verbs in Sales",
        "level": "B1",
        "category": "core",
        "workplace_track": "International Sales & Tenders",
        "estimated_time_minutes": 14,
        "description": "Manage leads from IDET and Eurosatory: follow up on, reach out to, close down, look into.",
        "grammar_focus": "Commercial Phrasal Verbs"
    },
    {
        "test_id": "TTR-B1-044",
        "title": "Factory Noise & Air Emission Checks: Adverbs of Frequency & Degree",
        "level": "B1",
        "category": "core",
        "workplace_track": "General Automotive Manufacturing",
        "estimated_time_minutes": 12,
        "description": "Report emissions monitoring results using scarcely, frequently, rarely, substantially.",
        "grammar_focus": "Adverbs of Frequency, Position, and Degree"
    },
    {
        "test_id": "TTR-B1-045",
        "title": "Customer Fleet Handover: Giving Oral Instructions & Demonstrations",
        "level": "B1",
        "category": "core",
        "workplace_track": "After-Sales, Service & Training",
        "estimated_time_minutes": 14,
        "description": "Walk the client through differential lock engagement and tire inflation system operation.",
        "grammar_focus": "Instructional Discourse Markers & Modal Auxiliary Review"
    },
    {
        "test_id": "TTR-B1-046",
        "title": "Pneumatic Circuit Troubleshooting: Question Tags & Confirmation",
        "level": "B1",
        "category": "core",
        "workplace_track": "Homologation, Testing & Field Operations",
        "estimated_time_minutes": 12,
        "description": "Verify test readings with workshop technicians using accurate question tags.",
        "grammar_focus": "Question Tags in Spoken Professional Dialogue"
    },
    {
        "test_id": "TTR-B1-047",
        "title": "Technical Datasheet Specifications: Compounds & Modifiers",
        "level": "B1",
        "category": "core",
        "workplace_track": "Powertrain & R&D Engineering",
        "estimated_time_minutes": 14,
        "description": "Form compound adjectives: heavy-duty, air-cooled, all-wheel-drive, corrosion-resistant.",
        "grammar_focus": "Compound Adjectives & Hyphenation in Engineering"
    },
    {
        "test_id": "TTR-B1-048",
        "title": "Commercial Pricing Revisions: Expressing Reasons & Purposes",
        "level": "B1",
        "category": "core",
        "workplace_track": "International Sales & Tenders",
        "estimated_time_minutes": 14,
        "description": "Explain price adjustments using in order to, so that, so as to avoid, because.",
        "grammar_focus": "Clauses of Purpose (in order to / so that)"
    },
    {
        "test_id": "TTR-B1-049",
        "title": "Engine Oil Contamination Incident: Past Perfect Continuous",
        "level": "B1",
        "category": "core",
        "workplace_track": "Quality Assurance & Assembly",
        "estimated_time_minutes": 15,
        "description": "Describe continuous past processes preceding an engine breakdown on the test circuit.",
        "grammar_focus": "Past Perfect Continuous (had been leaking for hours)"
    },
    {
        "test_id": "TTR-B1-050",
        "title": "Plant Tour for Foreign Delegations: Politeness & Small Talk",
        "level": "B1",
        "category": "core",
        "workplace_track": "International Sales & Tenders",
        "estimated_time_minutes": 14,
        "description": "Welcome overseas partners to the Kopřivnice plant with polished conversational phrases.",
        "grammar_focus": "Social Business English & Modal Conversational Strategies"
    },

    # =========================================================================
    # CEFR B2: CORE MODULES (051 - 100)
    # =========================================================================
    {
        "test_id": "TTR-B2-001",
        "title": "Chassis Stress Analysis & Simulation: Mixed Conditionals",
        "level": "B2",
        "category": "core",
        "workplace_track": "Powertrain & R&D Engineering",
        "estimated_time_minutes": 18,
        "description": "Evaluate past structural design decisions and their continuing impact on vehicle rigidity today.",
        "grammar_focus": "Mixed Conditionals (Type 3 + Type 2)"
    },
    {
        "test_id": "TTR-B2-002",
        "title": "International Defense Tender Negotiations: Modals of Deduction",
        "level": "B2",
        "category": "core",
        "workplace_track": "International Sales & Tenders",
        "estimated_time_minutes": 16,
        "description": "Deduce competitor pricing strategies and contract clauses with must have, can't have, might have.",
        "grammar_focus": "Past Modals of Speculation & Deduction"
    },
    {
        "test_id": "TTR-B2-003",
        "title": "Suspension Dynamic Load Testing: Participle Clauses",
        "level": "B2",
        "category": "core",
        "workplace_track": "Homologation, Testing & Field Operations",
        "estimated_time_minutes": 16,
        "description": "Condense technical test reports using present and past participle clauses (-ing and -ed).",
        "grammar_focus": "Participle Clauses replacing Relative and Adverbial Clauses"
    },
    {
        "test_id": "TTR-B2-004",
        "title": "High-Stakes Contract Bargaining: Inversion for Emphasis",
        "level": "B2",
        "category": "core",
        "workplace_track": "International Sales & Tenders",
        "estimated_time_minutes": 18,
        "description": "Utilize negative adverbials (under no circumstances, seldom, little did we know) for legal emphasis.",
        "grammar_focus": "Inversion with Negative and Restrictive Adverbs"
    },
    {
        "test_id": "TTR-B2-005",
        "title": "Metallurgical Failure Analysis: Third Conditional",
        "level": "B2",
        "category": "core",
        "workplace_track": "Powertrain & R&D Engineering",
        "estimated_time_minutes": 16,
        "description": "Analyze unfulfilled past outcomes in drive shaft fracture tests (If we had tempered the alloy...).",
        "grammar_focus": "Third Conditional (If + Past Perfect, would have + past participle)"
    },
    {
        "test_id": "TTR-B2-006",
        "title": "OEM Component Quality Governance: Subjunctive & Formal Directives",
        "level": "B2",
        "category": "core",
        "workplace_track": "Procurement & Supply Chain",
        "estimated_time_minutes": 16,
        "description": "Express strict requirements using formal subjunctive (demand that he be present, recommend that it undergo).",
        "grammar_focus": "Present Subjunctive in Formal Automotive Directives"
    },
    {
        "test_id": "TTR-B2-007",
        "title": "Homologation & UNECE Standards: Advanced Passive Reporting",
        "level": "B2",
        "category": "core",
        "workplace_track": "Homologation, Testing & Field Operations",
        "estimated_time_minutes": 16,
        "description": "Report certification status with impersonal passives (it is understood that, is acknowledged to be).",
        "grammar_focus": "Impersonal and Personal Passive Reporting Structures"
    },
    {
        "test_id": "TTR-B2-008",
        "title": "Tactical Vehicle Modifications: Cleft Sentences for Focus",
        "level": "B2",
        "category": "core",
        "workplace_track": "Powertrain & R&D Engineering",
        "estimated_time_minutes": 16,
        "description": "Structure technical presentations using What-clefts and It-clefts to highlight unique chassis advantages.",
        "grammar_focus": "Cleft Sentences (What really makes the difference is...)"
    },
    {
        "test_id": "TTR-B2-009",
        "title": "Cross-Border Commercial Disputes: Diplomatic Hedging",
        "level": "B2",
        "category": "core",
        "workplace_track": "International Sales & Tenders",
        "estimated_time_minutes": 16,
        "description": "Softening assertions in tense distributor meetings using would seem, appears to be, tend to think.",
        "grammar_focus": "Hedging, Modifying Words, and Epistemic Stance"
    },
    {
        "test_id": "TTR-B2-010",
        "title": "Tooling & Plant Upgrades: Causative Have & Get",
        "level": "B2",
        "category": "core",
        "workplace_track": "Quality Assurance & Assembly",
        "estimated_time_minutes": 15,
        "description": "Differentiate performing maintenance internally from having external contractors calibrate CNC machines.",
        "grammar_focus": "Causative Verbs (have/get something done vs have someone do)"
    },
    {
        "test_id": "TTR-B2-011",
        "title": "Global Supply Chain Disruptions: Advanced Concession Clauses",
        "level": "B2",
        "category": "core",
        "workplace_track": "Procurement & Supply Chain",
        "estimated_time_minutes": 16,
        "description": "Construct sophisticated arguments with notwithstanding, albeit, much as we try, in spite of.",
        "grammar_focus": "Complex Concession Clauses & Formal Connectors"
    },
    {
        "test_id": "TTR-B2-012",
        "title": "NATO STANAG Compliance: Nuances of Contractual Modals",
        "level": "B2",
        "category": "core",
        "workplace_track": "Homologation, Testing & Field Operations",
        "estimated_time_minutes": 18,
        "description": "Analyze mandatory military requirements versus optional recommendations: shall, will, must, may.",
        "grammar_focus": "Deontic Modals in Military & Legal Procurement Specifications"
    },
    {
        "test_id": "TTR-B2-013",
        "title": "Root Cause Analysis (8D Methodology): Complex Prepositional Phrases",
        "level": "B2",
        "category": "core",
        "workplace_track": "Quality Assurance & Assembly",
        "estimated_time_minutes": 16,
        "description": "Document corrective action paths: in accordance with, with a view to, by virtue of, in light of.",
        "grammar_focus": "Multi-word Prepositional Phrases in Formal Quality Reports"
    },
    {
        "test_id": "TTR-B2-014",
        "title": "Engine Telematics & CAN-Bus Protocols: Advanced Relative Clauses",
        "level": "B2",
        "category": "core",
        "workplace_track": "Powertrain & R&D Engineering",
        "estimated_time_minutes": 16,
        "description": "Construct precise electronics documentation using prepositional relative pronouns (in which, to whom, of which).",
        "grammar_focus": "Preposition Placement in Relative Clauses"
    },
    {
        "test_id": "TTR-B2-015",
        "title": "Assembly Line Robotics Stoppage: Wishes, Regrets & Would Rather",
        "level": "B2",
        "category": "core",
        "workplace_track": "Quality Assurance & Assembly",
        "estimated_time_minutes": 15,
        "description": "Formulate executive reflections on past breakdowns: I wish we had retrofitted, would rather you hadn't.",
        "grammar_focus": "Unreal Past with Wish, If Only, and Would Rather"
    },
    {
        "test_id": "TTR-B2-016",
        "title": "Vehicle Homologation Protocols: Nominalisation in Technical Writing",
        "level": "B2",
        "category": "core",
        "workplace_track": "Homologation, Testing & Field Operations",
        "estimated_time_minutes": 16,
        "description": "Transform verbal clauses into formal noun phrases to produce concise technical homologation briefs.",
        "grammar_focus": "Nominalisation and Dense Informational Syntax"
    },
    {
        "test_id": "TTR-B2-017",
        "title": "Hydrogen Fuel Cell Powertrain R&D: Advanced Gerund & Infinitive Structures",
        "level": "B2",
        "category": "core",
        "workplace_track": "Powertrain & R&D Engineering",
        "estimated_time_minutes": 16,
        "description": "Master nuanced patterns: dread thinking, object to releasing, facilitate testing, justify spending.",
        "grammar_focus": "Advanced Gerunds & Perfect Infinitives"
    },
    {
        "test_id": "TTR-B2-018",
        "title": "Distributor Exclusivity Agreements: Advanced Conditionals (Inversion)",
        "level": "B2",
        "category": "core",
        "workplace_track": "International Sales & Tenders",
        "estimated_time_minutes": 18,
        "description": "Formulate formal hypothetical conditions: Should the dealer breach..., Had the factory delivered...",
        "grammar_focus": "Inverted Conditional Clauses without 'If'"
    },
    {
        "test_id": "TTR-B2-019",
        "title": "Warranty Cost Allocation & Amortization: Financial Precision",
        "level": "B2",
        "category": "core",
        "workplace_track": "International Sales & Tenders",
        "estimated_time_minutes": 16,
        "description": "Communicate capital expenditure, operating margins, scrap costs, and salvage value precisely.",
        "grammar_focus": "Financial and Accounting Collocations & Syntactic Framing"
    },
    {
        "test_id": "TTR-B2-020",
        "title": "Dakar Rally Telemetry Analysis: Complex Adverbial Clauses",
        "level": "B2",
        "category": "core",
        "workplace_track": "Homologation, Testing & Field Operations",
        "estimated_time_minutes": 16,
        "description": "Correlate damper oil temperatures and terrain shocks using proportionate agreement (the higher... the faster).",
        "grammar_focus": "Double Comparatives & Proportionate Clauses (The more... the more...)"
    },
    {
        "test_id": "TTR-B2-021",
        "title": "Foreign Defense Delegation Presentations: Discourse Signposting",
        "level": "B2",
        "category": "core",
        "workplace_track": "International Sales & Tenders",
        "estimated_time_minutes": 16,
        "description": "Structure technical pitches with signposting: turning now to, to elaborate further, by contrast.",
        "grammar_focus": "Advanced Discourse Markers & Cohesive Devices"
    },
    {
        "test_id": "TTR-B2-022",
        "title": "Subcontractor Non-Disclosure Agreements: Legal Collocations",
        "level": "B2",
        "category": "core",
        "workplace_track": "Procurement & Supply Chain",
        "estimated_time_minutes": 16,
        "description": "Review intellectual property rights, non-circumvention terms, and breach remedies.",
        "grammar_focus": "Legalistic Phrasing & Contract Collocations"
    },
    {
        "test_id": "TTR-B2-023",
        "title": "Extreme Cold Starting Trials: Participles as Adjectives & Adverbs",
        "level": "B2",
        "category": "core",
        "workplace_track": "Homologation, Testing & Field Operations",
        "estimated_time_minutes": 15,
        "description": "Describe cold chamber engine crank tests using active and passive participle phrases.",
        "grammar_focus": "Dangling Participle Avoidance & Misplaced Modifiers"
    },
    {
        "test_id": "TTR-B2-024",
        "title": "Kopřivnice Plant Modernization: Expressing Nuanced Degrees",
        "level": "B2",
        "category": "core",
        "workplace_track": "General Automotive Manufacturing",
        "estimated_time_minutes": 15,
        "description": "Refine performance reports with adverbs of degree: marginal, negligible, substantial, paramount.",
        "grammar_focus": "Gradable vs Non-gradable Adjectives and Intensifiers"
    },
    {
        "test_id": "TTR-B2-025",
        "title": "Inter-Departmental Deadlocks: Collaborative Negotiation",
        "level": "B2",
        "category": "core",
        "workplace_track": "General Automotive Manufacturing",
        "estimated_time_minutes": 16,
        "description": "Navigate disagreements between Sales and Production over lead times with empathetic assertion.",
        "grammar_focus": "Diplomatic Language and Softening Techniques in Meetings"
    },
    {
        "test_id": "TTR-B2-026",
        "title": "Pneumatic Suspension Valve Fatigue: Passive Voice with Gerunds",
        "level": "B2",
        "category": "core",
        "workplace_track": "Quality Assurance & Assembly",
        "estimated_time_minutes": 16,
        "description": "Express ongoing passive actions: avoids being damaged, requires being overhauled, subjected to being tested.",
        "grammar_focus": "Passive Gerunds and Infinitives"
    },
    {
        "test_id": "TTR-B2-027",
        "title": "Global Logistics Bottlenecks: Three-Word Phrasal Verbs",
        "level": "B2",
        "category": "core",
        "workplace_track": "Procurement & Supply Chain",
        "estimated_time_minutes": 16,
        "description": "Master phrasal prepositional verbs: come up against, look down on, cut down on, put up with.",
        "grammar_focus": "Three-part Phrasal Verbs in Supply Chain Operations"
    },
    {
        "test_id": "TTR-B2-028",
        "title": "Heavy Duty Brake Dynamometer Reports: Cause & Effect Inversion",
        "level": "B2",
        "category": "core",
        "workplace_track": "Powertrain & R&D Engineering",
        "estimated_time_minutes": 16,
        "description": "Formulate scientific causal statements: So intense was the friction that the rotor warped.",
        "grammar_focus": "Inversion with 'So' and 'Such' for Dramatic Emphasis"
    },
    {
        "test_id": "TTR-B2-029",
        "title": "Overseas Government Bids: Formal Written Register & Tone",
        "level": "B2",
        "category": "core",
        "workplace_track": "International Sales & Tenders",
        "estimated_time_minutes": 18,
        "description": "Craft authoritative executive summaries and tender bid letters adhering to international protocols.",
        "grammar_focus": "Formal Tone, Register Transitions, and Professional Decorum"
    },
    {
        "test_id": "TTR-B2-030",
        "title": "Tatra Backbone Tube vs Ladder Frame: Comparative Rhetoric",
        "level": "B2",
        "category": "core",
        "workplace_track": "Powertrain & R&D Engineering",
        "estimated_time_minutes": 18,
        "description": "Argue the mechanical superiority of swinging half-axles against conventional beam axles.",
        "grammar_focus": "Persuasive Rhetorical Structures & Comparative Nuances"
    },
    {
        "test_id": "TTR-B2-031",
        "title": "IATF 16949 Quality Audit: Advanced Ellipsis & Substitution",
        "level": "B2",
        "category": "core",
        "workplace_track": "Quality Assurance & Assembly",
        "estimated_time_minutes": 15,
        "description": "Streamline technical audit dialogue using substitution (so, neither, one) and ellipsis.",
        "grammar_focus": "Ellipsis and Substitution in Fast Technical Communication"
    },
    {
        "test_id": "TTR-B2-032",
        "title": "Off-Road Vehicle Stability Trials: Compound Prepositions",
        "level": "B2",
        "category": "core",
        "workplace_track": "Homologation, Testing & Field Operations",
        "estimated_time_minutes": 15,
        "description": "Specify vehicle dynamics: in excess of, prior to, with regard to, irrespective of rollover threshold.",
        "grammar_focus": "Complex and Compound Prepositions in Dynamics Reports"
    },
    {
        "test_id": "TTR-B2-033",
        "title": "International Fleet Sales Contracts: Liquidated Damages & SLA",
        "level": "B2",
        "category": "core",
        "workplace_track": "International Sales & Tenders",
        "estimated_time_minutes": 18,
        "description": "Interpret and negotiate penalty clauses, delivery delays, and service level agreements.",
        "grammar_focus": "Conditional Liabilities & Contractual Precision"
    },
    {
        "test_id": "TTR-B2-034",
        "title": "Engine Emission Scrubber Failure: Past Speculation & Regret",
        "level": "B2",
        "category": "core",
        "workplace_track": "Powertrain & R&D Engineering",
        "estimated_time_minutes": 16,
        "description": "Express past possibilities and criticisms: could have avoided, ought to have detected, needn't have replaced.",
        "grammar_focus": "Perfect Modal Auxiliaries (Needn't have vs Didn't need to)"
    },
    {
        "test_id": "TTR-B2-035",
        "title": "Foreign Dealer Technical Training: Advanced Instructional Language",
        "level": "B2",
        "category": "core",
        "workplace_track": "After-Sales, Service & Training",
        "estimated_time_minutes": 16,
        "description": "Instruct international master mechanics on diagnostic software and CAN-bus troubleshooting.",
        "grammar_focus": "Pedagogical Phrasing & Technical Instruction at B2"
    },
    {
        "test_id": "TTR-B2-036",
        "title": "Assembly Line Ergonomics: Advanced Relative Clauses with Quantifiers",
        "level": "B2",
        "category": "core",
        "workplace_track": "General Automotive Manufacturing",
        "estimated_time_minutes": 16,
        "description": "Audit operator workstations using structures: all of which, none of whom, several of which.",
        "grammar_focus": "Quantifier + of which / of whom in Relative Clauses"
    },
    {
        "test_id": "TTR-B2-037",
        "title": "Tatra Force Military Chassis: Armor Level Specifications",
        "level": "B2",
        "category": "core",
        "workplace_track": "Powertrain & R&D Engineering",
        "estimated_time_minutes": 18,
        "description": "Define ballistic protection levels, STANAG 4569 compliance, and blast underbelly deflectors.",
        "grammar_focus": "Military Specification Grammar & Passive Framing"
    },
    {
        "test_id": "TTR-B2-038",
        "title": "Raw Material Price Hedging: Future Perfect & Continuous",
        "level": "B2",
        "category": "core",
        "workplace_track": "Procurement & Supply Chain",
        "estimated_time_minutes": 16,
        "description": "Forecast alloy steel inventory levels: will have produced, will be negotiating by Q4.",
        "grammar_focus": "Future Perfect and Future Continuous in Business Projections"
    },
    {
        "test_id": "TTR-B2-039",
        "title": "Customer Field Warranty Disputes: Managing Difficult Calls",
        "level": "B2",
        "category": "core",
        "workplace_track": "After-Sales, Service & Training",
        "estimated_time_minutes": 16,
        "description": "De-escalate frustrated fleet operators claiming gearbox defects due to abusive operation.",
        "grammar_focus": "De-escalation Strategies & Assertive Professional Dialogue"
    },
    {
        "test_id": "TTR-B2-040",
        "title": "Chassis Welding Non-Conformities: Passive Reporting Verbs",
        "level": "B2",
        "category": "core",
        "workplace_track": "Quality Assurance & Assembly",
        "estimated_time_minutes": 16,
        "description": "Report weld seam ultrasonic test results: are reputed to, have been shown to, are alleged to.",
        "grammar_focus": "Advanced Passive with Reporting Infinitive Verbs"
    },
    {
        "test_id": "TTR-B2-041",
        "title": "Overseas Mining Fleet Deliveries: Complex Time Connectors",
        "level": "B2",
        "category": "core",
        "workplace_track": "International Sales & Tenders",
        "estimated_time_minutes": 15,
        "description": "Structure shipping timeframes with no sooner... than, hardly... when, once, by the time.",
        "grammar_focus": "Time Connectors and Inverted Time Sequences"
    },
    {
        "test_id": "TTR-B2-042",
        "title": "Heavy Haulage Superstructures: Technical Collocations",
        "level": "B2",
        "category": "core",
        "workplace_track": "Powertrain & R&D Engineering",
        "estimated_time_minutes": 16,
        "description": "Detail tipper hydraulics, three-way dump bodies, and fifth-wheel couplings.",
        "grammar_focus": "Automotive Engineering Collocations & Phrasal Idioms"
    },
    {
        "test_id": "TTR-B2-043",
        "title": "Supplier Environmental Audits (ISO 14001): Cohesive Substitution",
        "level": "B2",
        "category": "core",
        "workplace_track": "Procurement & Supply Chain",
        "estimated_time_minutes": 15,
        "description": "Produce clear audit summaries avoiding tedious repetition through lexical substitution.",
        "grammar_focus": "Textual Cohesion and Lexical Variation"
    },
    {
        "test_id": "TTR-B2-044",
        "title": "Autonomous & Teleoperated Tatra Trucks: Speculative Futures",
        "level": "B2",
        "category": "core",
        "workplace_track": "Powertrain & R&D Engineering",
        "estimated_time_minutes": 16,
        "description": "Discuss future R&D trends in self-driving off-road military convoys using nuanced probability.",
        "grammar_focus": "Modal Certainty and Future Probability Phrases"
    },
    {
        "test_id": "TTR-B2-045",
        "title": "Executive Debriefing on Trade Sanctions: Nuanced Conditionals",
        "level": "B2",
        "category": "core",
        "workplace_track": "International Sales & Tenders",
        "estimated_time_minutes": 18,
        "description": "Assess geopolitical export restrictions: but for our local partner, were it not for the embargo.",
        "grammar_focus": "Conditionals with 'But for' and 'Were it not for'"
    },
    {
        "test_id": "TTR-B2-046",
        "title": "Tatra Phoenix Cab Ergonomics: Participial Adverbs & Sentence Modifiers",
        "level": "B2",
        "category": "core",
        "workplace_track": "General Automotive Manufacturing",
        "estimated_time_minutes": 15,
        "description": "Incorporate viewpoint and comment adverbs: technically speaking, remarkably, undeniably.",
        "grammar_focus": "Sentence Adverbs and Viewpoint Disjuncts"
    },
    {
        "test_id": "TTR-B2-047",
        "title": "Vehicle Crash Worthiness & Simulation: Inversion with Only & Not Only",
        "level": "B2",
        "category": "core",
        "workplace_track": "Homologation, Testing & Field Operations",
        "estimated_time_minutes": 16,
        "description": "Highlight occupant safety: Not only did the cab absorb the impact, but the tube also preserved integrity.",
        "grammar_focus": "Inversion with 'Not only... but also' and 'Only after'"
    },
    {
        "test_id": "TTR-B2-048",
        "title": "Supply Chain Tier-1 Audits: Complex Relative Clauses with Possessives",
        "level": "B2",
        "category": "core",
        "workplace_track": "Procurement & Supply Chain",
        "estimated_time_minutes": 16,
        "description": "Review supplier financial health: companies whose debt-to-equity ratio, the owners of which.",
        "grammar_focus": "Possessive Relative Clauses with 'Whose' and 'Of Which'"
    },
    {
        "test_id": "TTR-B2-049",
        "title": "Corporate Boardroom Strategy: Summarizing & Synthesizing",
        "level": "B2",
        "category": "core",
        "workplace_track": "General Automotive Manufacturing",
        "estimated_time_minutes": 18,
        "description": "Synthesize multiple stakeholder inputs into a coherent strategic corporate roadmap.",
        "grammar_focus": "Synthesis, Discourse Organization, and Executive Summary Structures"
    },
    {
        "test_id": "TTR-B2-050",
        "title": "Tatra Global Brand Positioning: Persuasive Argumentation",
        "level": "B2",
        "category": "core",
        "workplace_track": "International Sales & Tenders",
        "estimated_time_minutes": 18,
        "description": "Present the definitive value proposition of the Kopřivnice legacy against global competitors.",
        "grammar_focus": "Mastery Review: Complex Syntax & Persuasive Stylistics"
    },

    # =========================================================================
    # SPECIALIZED UNITS: 001 - 020
    # =========================================================================
    {
        "test_id": "TTR-SP-001",
        "title": "False Friends in Automotive Manufacturing & Assembly",
        "level": "B1/B2",
        "category": "specialized",
        "workplace_track": "Quality Assurance & Assembly",
        "estimated_time_minutes": 15,
        "description": "Czenglish traps on the shop floor: control vs check, fabricate vs manufacture, evidence vs records.",
        "grammar_focus": "Lexical False Friends & Terminology Accuracy"
    },
    {
        "test_id": "TTR-SP-002",
        "title": "False Friends in International Commercial Sales & Contracts",
        "level": "B1/B2",
        "category": "specialized",
        "workplace_track": "International Sales & Tenders",
        "estimated_time_minutes": 15,
        "description": "Czenglish errors in business deals: actual vs current, eventual vs possible, concurrence vs competition.",
        "grammar_focus": "Commercial Lexical False Cognates"
    },
    {
        "test_id": "TTR-SP-003",
        "title": "False Friends in Materials Science & Mechanical Engineering",
        "level": "B1/B2",
        "category": "specialized",
        "workplace_track": "Powertrain & R&D Engineering",
        "estimated_time_minutes": 15,
        "description": "Material false friends: transparent vs translucent, solid vs firm, plastic vs ductile, defect vs flaw.",
        "grammar_focus": "Materials Engineering Lexicon & False Cognates"
    },
    {
        "test_id": "TTR-SP-004",
        "title": "Tatra Central Backbone Tube & Chassis Nomenclature",
        "level": "B1/B2",
        "category": "specialized",
        "workplace_track": "Powertrain & R&D Engineering",
        "estimated_time_minutes": 18,
        "description": "Technical terminology of the unique Tatra concept: backbone tube, swinging half-axles, enclosed drive shafts.",
        "grammar_focus": "Proprietary Chassis Architecture Nomenclature"
    },
    {
        "test_id": "TTR-SP-005",
        "title": "Drivetrain, Differential Locks & Transfer Case Terminology",
        "level": "B1/B2",
        "category": "specialized",
        "workplace_track": "Powertrain & R&D Engineering",
        "estimated_time_minutes": 18,
        "description": "Master terminology: inter-axle vs inter-wheel differential locks, drop box, power take-off (PTO).",
        "grammar_focus": "Heavy Vehicle Powertrain & Torque Distribution Lexicon"
    },
    {
        "test_id": "TTR-SP-006",
        "title": "Heavy-Duty Suspension & Kingpin Steering Geometry",
        "level": "B1/B2",
        "category": "specialized",
        "workplace_track": "Powertrain & R&D Engineering",
        "estimated_time_minutes": 16,
        "description": "Nomenclature of suspension: air bellows, leaf springs, torsion bars, Kingpin inclination, caster, camber.",
        "grammar_focus": "Suspension & Steering Geometry Terminology"
    },
    {
        "test_id": "TTR-SP-007",
        "title": "Braking Systems, Retarders & Pneumatic Valves",
        "level": "B1/B2",
        "category": "specialized",
        "workplace_track": "Quality Assurance & Assembly",
        "estimated_time_minutes": 16,
        "description": "Technical terms: dual-circuit pneumatic brakes, engine Jake brake, electromagnetic & hydraulic retarder.",
        "grammar_focus": "Pneumatic & Retarder Braking Lexicon"
    },
    {
        "test_id": "TTR-SP-008",
        "title": "Cab Mounting, Superstructures & Bodybuilder Interfaces",
        "level": "B1/B2",
        "category": "specialized",
        "workplace_track": "General Automotive Manufacturing",
        "estimated_time_minutes": 16,
        "description": "Vocabulary for bodies: three-way tipper, hook lift, water tanker, subframe mounting, torsion-free brackets.",
        "grammar_focus": "Superstructure & Bodybuilder Integration Terminology"
    },
    {
        "test_id": "TTR-SP-009",
        "title": "Homologation, Axle Loads & Off-Road Angles",
        "level": "B1/B2",
        "category": "specialized",
        "workplace_track": "Homologation, Testing & Field Operations",
        "estimated_time_minutes": 16,
        "description": "Certification terms: gross vehicle weight (GVW), axle load distribution, approach, departure and ramp angles.",
        "grammar_focus": "Homologation & Vehicle Dimensions Lexicon"
    },
    {
        "test_id": "TTR-SP-010",
        "title": "Defense & Military Vehicle Specifications",
        "level": "B1/B2",
        "category": "specialized",
        "workplace_track": "International Sales & Tenders",
        "estimated_time_minutes": 18,
        "description": "Tactical terms: ballistic armor STANAG, run-flat inserts, blackout lighting, central tire inflation system (CTIS).",
        "grammar_focus": "Defense & Tactical Vehicle Technical Terms"
    },
    {
        "test_id": "TTR-SP-011",
        "title": "Telematics, CAN-Bus & Diagnostic Trouble Codes (DTC)",
        "level": "B1/B2",
        "category": "specialized",
        "workplace_track": "After-Sales, Service & Training",
        "estimated_time_minutes": 16,
        "description": "Electronics terminology: ECU, OBD-II, diagnostic trouble codes, sensor telemetry, CAN-bus baud rate.",
        "grammar_focus": "Automotive Telematics & On-Board Diagnostics Lexicon"
    },
    {
        "test_id": "TTR-SP-012",
        "title": "Alternative Powertrains: Hydrogen Fuel Cells & Hybrid Drive",
        "level": "B1/B2",
        "category": "specialized",
        "workplace_track": "Powertrain & R&D Engineering",
        "estimated_time_minutes": 18,
        "description": "Modern green tech: PEM fuel cell stack, hydrogen tanks at 700 bar, high-voltage battery pack, regenerative braking.",
        "grammar_focus": "Hydrogen & Electromobility Technical Jargon"
    },
    {
        "test_id": "TTR-SP-013",
        "title": "Dakar Rally Extreme Desert Engineering Jargon",
        "level": "B1/B2",
        "category": "specialized",
        "workplace_track": "Homologation, Testing & Field Operations",
        "estimated_time_minutes": 16,
        "description": "Racing vocabulary: sand dunes, washboard ripples, damper fade, bivouac repairs, navigation waypoint.",
        "grammar_focus": "Motorsport & Extreme Endurance Terminology"
    },
    {
        "test_id": "TTR-SP-014",
        "title": "Quality Metrology, CMM & Surface Finish Terminology",
        "level": "B1/B2",
        "category": "specialized",
        "workplace_track": "Quality Assurance & Assembly",
        "estimated_time_minutes": 15,
        "description": "Inspection jargon: coordinate measuring machine, surface roughness Ra, runout, tolerance stack-up, gage R&R.",
        "grammar_focus": "Metrology & Industrial Quality Control Jargon"
    },
    {
        "test_id": "TTR-SP-015",
        "title": "Commercial Logistics & Incoterms 2020 Definitions",
        "level": "B1/B2",
        "category": "specialized",
        "workplace_track": "International Sales & Tenders",
        "estimated_time_minutes": 16,
        "description": "International shipping: EXW, FCA, CPT, CIP, DAP, DDP, bill of lading, customs broker, freight forwarding.",
        "grammar_focus": "Incoterms 2020 & Global Freight Vocabulary"
    },
    {
        "test_id": "TTR-SP-016",
        "title": "Professional Idioms in International Sales & Negotiations",
        "level": "B1/B2",
        "category": "specialized",
        "workplace_track": "International Sales & Tenders",
        "estimated_time_minutes": 15,
        "description": "Commercial idioms: sweeten the deal, ball is in their court, iron out the kinks, close the loop, reach a stalemate.",
        "grammar_focus": "Business & Negotiation Idiomatic Expressions"
    },
    {
        "test_id": "TTR-SP-017",
        "title": "Shop Floor & Engineering Project Management Idioms",
        "level": "B1/B2",
        "category": "specialized",
        "workplace_track": "General Automotive Manufacturing",
        "estimated_time_minutes": 15,
        "description": "Manufacturing idioms: cut corners, back to the drawing board, rule of thumb, get down to brass tacks.",
        "grammar_focus": "Workshop & Operational Idiomatic Usage"
    },
    {
        "test_id": "TTR-SP-018",
        "title": "Diplomatic Softeners & Cross-Cultural Meeting Phrases",
        "level": "B1/B2",
        "category": "specialized",
        "workplace_track": "International Sales & Tenders",
        "estimated_time_minutes": 16,
        "description": "Polite phrasing: with all due respect, I take your point, but..., let us circle back, speaking off the record.",
        "grammar_focus": "Diplomatic Pragmatics & Softening Devices"
    },
    {
        "test_id": "TTR-SP-019",
        "title": "Mechanical Trouble Symptoms & Acoustic Descriptive Jargon",
        "level": "B1/B2",
        "category": "specialized",
        "workplace_track": "After-Sales, Service & Training",
        "estimated_time_minutes": 15,
        "description": "Describing noises and wear: whining gear, rattling valve, backlash, pitting, cavitating pump, scouring.",
        "grammar_focus": "Sensory & Acoustic Failure Diagnostics Vocabulary"
    },
    {
        "test_id": "TTR-SP-020",
        "title": "Pitching Tatra's Unique Selling Proposition (USP) Globally",
        "level": "B1/B2",
        "category": "specialized",
        "workplace_track": "International Sales & Tenders",
        "estimated_time_minutes": 18,
        "description": "High-impact sales vocabulary: extreme off-road passability, total cost of ownership (TCO), unparalleled durability.",
        "grammar_focus": "Persuasive Selling Proposition & Commercial Lexicon"
    }
]

def main():
    target_path = Path(__file__).resolve().parent.parent / "data" / "curriculum_manifest.json"
    with open(target_path, "w", encoding="utf-8") as f:
        json.dump(curriculum, f, indent=2, ensure_ascii=False)
    print(f"Generated manifest with {len(curriculum)} modules at {target_path}")

if __name__ == "__main__":
    main()
