#!/usr/bin/env python3
"""
Full Autonomous Ecosystem Builder for 5 Independent Corporate Testing Suites:
1. Tatra Engineering (tatra-engineering)
2. Tatra Sales and Engineering (tatra-sales-engineering)
3. Teva Engineering (teva-engineering)
4. Tapi Chemistry (tapi-chemistry)
5. Teva IT (teva-it)

Features:
- Dedicated branding, schemas, engines, portals, and runners for each suite.
- Lower Tier (CEFR A2 Foundation) specifically engineered for Czech adult learners who find B1 difficult.
- Balanced option distribution across A, B, C, D (no position bias / not all A).
- Complete decoupling between Tatra, Teva, and Tapi.
- Executive Master Hub (c:/tmp/00-Mycat/index.html) uniting all 5 corporate programs.
"""

import os
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
from build_all_five_suites import (
    SUITES,
    generate_schema,
    generate_css,
    generate_app_js,
    generate_runner_html,
    generate_index_html,
    generate_validator_py
)

# Balanced key distribution cycle
KEY_CYCLE = ["B", "C", "A", "D", "C", "B", "D", "A", "C", "B"]

def create_question(qid, prompt, options_dict, correct_key, explanations, cz_note, track):
    """
    options_dict: {"A": text, "B": text, "C": text, "D": text}
    explanations: {"correct": text, "wrong_A": text, ...}
    """
    options = [{"key": k, "text": options_dict[k]} for k in ["A", "B", "C", "D"]]
    return {
        "id": qid,
        "prompt": prompt,
        "options": options,
        "correct_key": correct_key,
        "explanations": explanations,
        "cz_learning_point": cz_note,
        "workplace_track": track
    }

# =============================================================================
# SUITE 1: TATRA ENGINEERING
# =============================================================================
tatra_eng_manifest = [
    # Tier 0: A2 Foundation
    {
        "test_id": "TTR-ENG-A2-001",
        "title": "Workshop Tools, Fasteners & PPE: Present Simple & Imperatives",
        "level": "A2",
        "category": "core",
        "workplace_track": "Workshop Assembly & Line Tooling",
        "estimated_time_minutes": 10,
        "description": "Essential English for identifying assembly tools, fasteners, safety gear, and giving simple workshop instructions.",
        "grammar_focus": "Imperatives & Present Simple (have/has, wear, use)"
    },
    {
        "test_id": "TTR-ENG-A2-002",
        "title": "Daily Shift Routines & Machine Operation: Present Simple",
        "level": "A2",
        "category": "core",
        "workplace_track": "Workshop Assembly & Line Tooling",
        "estimated_time_minutes": 10,
        "description": "Describe daily line routines, standard maintenance tasks, and shift schedules with correct 3rd person singular agreement.",
        "grammar_focus": "Present Simple 3rd Person (-s / -es) & Frequency Adverbs"
    },
    {
        "test_id": "TTR-ENG-A2-003",
        "title": "Yesterday's Workshop Faults & Defective Parts: Past Simple",
        "level": "A2",
        "category": "core",
        "workplace_track": "Quality Assurance & Testing",
        "estimated_time_minutes": 12,
        "description": "Report broken parts, line stoppages, and replaced bolts using high-frequency regular and irregular past verbs.",
        "grammar_focus": "Past Simple Regular (-ed) & Irregular Verbs (broke, replaced, stopped)"
    },
    {
        "test_id": "TTR-ENG-A2-004",
        "title": "Chassis Geometry & Tool Locations: Prepositions of Place",
        "level": "A2",
        "category": "core",
        "workplace_track": "Central Backbone Tube & Chassis R&D",
        "estimated_time_minutes": 10,
        "description": "State exact locations around the truck chassis: under the tube, inside the cab, between the half-axles, next to the engine.",
        "grammar_focus": "Prepositions of Place (under, on, in, between, next to)"
    },
    {
        "test_id": "TTR-ENG-A2-005",
        "title": "Plant Warning Signs & Crane Safety: Can & Must",
        "level": "A2",
        "category": "core",
        "workplace_track": "Workshop Assembly & Line Tooling",
        "estimated_time_minutes": 10,
        "description": "Understand mandatory safety symbols, PPE requirements, and basic prohibitions on the Kopřivnice shop floor.",
        "grammar_focus": "Modals of Ability & Obligation (can, must, must not)"
    },
    # Tier 1: B1
    {
        "test_id": "TTR-ENG-B1-001",
        "title": "Chassis Assembly & Torque Verification: Past Simple vs Past Perfect",
        "level": "B1",
        "category": "core",
        "workplace_track": "Central Backbone Tube & Chassis R&D",
        "estimated_time_minutes": 15,
        "description": "Sequence of events and passive verification during backbone tube assembly and flange torquing.",
        "grammar_focus": "Past Simple vs Past Perfect Passive"
    },
    # Tier 2: B2
    {
        "test_id": "TTR-ENG-B2-001",
        "title": "Torsional Stiffness & Finite Element Analysis: Mixed Conditionals",
        "level": "B2",
        "category": "core",
        "workplace_track": "Central Backbone Tube & Chassis R&D",
        "estimated_time_minutes": 18,
        "description": "Analyze chassis stress simulation results and hypothetical frame deformations using mixed conditionals.",
        "grammar_focus": "Mixed Conditionals (Type 3 condition to Type 2 result)"
    },
    # Tier 3: Specialized
    {
        "test_id": "TTR-ENG-SP-001",
        "title": "Backbone Tube, Swinging Half-Axles & CTIS Technical Jargon",
        "level": "B1/B2",
        "category": "specialized",
        "workplace_track": "Central Backbone Tube & Chassis R&D",
        "estimated_time_minutes": 16,
        "description": "Master proprietary Tatra technical terms: central load-bearing tube, swing axles, drop box, and CTIS.",
        "grammar_focus": "Automotive Engineering Jargon & Nomenclature"
    }
]

# Sample A2 Test for Tatra Engineering
tatra_eng_a2_001 = {
    "test_id": "TTR-ENG-A2-001",
    "title": "Workshop Tools, Fasteners & PPE: Present Simple & Imperatives",
    "level": "A2",
    "category": "core",
    "workplace_track": "Workshop Assembly & Line Tooling",
    "estimated_time_minutes": 10,
    "description": "Essential English for identifying assembly tools, fasteners, safety gear, and giving simple workshop instructions.",
    "learning_objectives": [
        "Use simple imperatives for safe workshop instructions (wear, check, tighten)",
        "Apply basic present simple verbs for tool usage",
        "Avoid basic Czech word order and pronoun omission errors"
    ],
    "questions": [
        create_question(
            "TTR-ENG-A2-001-Q1",
            "Always _____ safety goggles before you start grinding the chassis weld.",
            {"A": "wearing", "B": "wear", "C": "wears", "D": "to wear"},
            "B",
            {
                "correct": "Imperative sentences use the base form of the verb ('wear') without '-ing' or 'to'.",
                "wrong_A": "'-ing' form cannot be used as a command or instruction.",
                "wrong_C": "'wears' is third person singular, not an imperative command.",
                "wrong_D": "Infinitive with 'to' cannot be used for direct instructions."
            },
            "Czech uses the imperative 'Noste / Mějte nasazené'. In English, simply use the base verb 'Wear'.",
            "Workshop Assembly & Line Tooling"
        ),
        create_question(
            "TTR-ENG-A2-001-Q2",
            "Where _____ the pneumatic torque wrench for the wheel hub bolts?",
            {"A": "is located", "B": "are", "C": "is", "D": "does"},
            "C",
            {
                "correct": "For singular noun 'wrench', the simple question is 'Where is the wrench?'.",
                "wrong_A": "'Where is located the wrench' has incorrect inverted word order for basic English.",
                "wrong_B": "'are' is plural, but 'wrench' is singular.",
                "wrong_D": "'does' requires another main action verb like 'Where does the wrench go?'."
            },
            "Czech word order is 'Kde je utahovák?'. In English, keep it simple: 'Where is the [item]?'.",
            "Workshop Assembly & Line Tooling"
        ),
        create_question(
            "TTR-ENG-A2-001-Q3",
            "The assembly technician _____ all M16 bolts to 250 Nm every morning.",
            {"A": "tightens", "B": "tighten", "C": "is tighten", "D": "tightening"},
            "A",
            {
                "correct": "Third person singular subject ('The technician') requires '-s' on the verb in Present Simple ('tightens').",
                "wrong_B": "'tighten' lacks the mandatory singular '-s' ending.",
                "wrong_C": "Ungrammatical verb phrase.",
                "wrong_D": "Participle '-ing' alone cannot be the main verb."
            },
            "Czechs frequently forget the third person singular '-s' (*He tighten* instead of *He tightens*).",
            "Workshop Assembly & Line Tooling"
        ),
        create_question(
            "TTR-ENG-A2-001-Q4",
            "Do not _____ the hydraulic lifting table while the warning light is red!",
            {"A": "moving", "B": "to move", "C": "moves", "D": "move"},
            "D",
            {
                "correct": "Negative imperative 'Do not' is followed by the bare base form ('move').",
                "wrong_A": "'-ing' cannot follow 'Do not' in commands.",
                "wrong_B": "'to' cannot follow auxiliary 'do'.",
                "wrong_C": "'-s' form cannot follow 'do not'."
            },
            "Czech 'Nehýbejte s...'. In English, always use 'Do not + base form'.",
            "Workshop Assembly & Line Tooling"
        ),
        create_question(
            "TTR-ENG-A2-001-Q5",
            "Our workshop _____ three overhead cranes for heavy chassis frames.",
            {"A": "is having", "B": "have", "C": "has", "D": "having"},
            "C",
            {
                "correct": "Singular subject 'Our workshop' takes 'has' for possession in Present Simple.",
                "wrong_A": "Stative verb 'have' (possession) is not used in continuous aspect.",
                "wrong_B": "'have' is plural, but 'workshop' is singular.",
                "wrong_D": "Incomplete verb form."
            },
            "Czech 'Naše dílna má'. Remember singular subject takes 'has', not 'have'.",
            "Workshop Assembly & Line Tooling"
        ),
        create_question(
            "TTR-ENG-A2-001-Q6",
            "_____ these oil containers into the hazardous waste area immediately.",
            {"A": "Take", "B": "Taking", "C": "Takes", "D": "You take"},
            "A",
            {
                "correct": "Direct imperative begins with base verb 'Take'.",
                "wrong_B": "Participle '-ing' cannot initiate an imperative command.",
                "wrong_C": "Third-person form cannot initiate a command.",
                "wrong_D": "Adding 'You' makes it an unusual declarative sentence rather than a standard SOP instruction."
            },
            "In English instructions and SOPs, start directly with the verb: 'Take / Put / Check'.",
            "Workshop Assembly & Line Tooling"
        ),
        create_question(
            "TTR-ENG-A2-001-Q7",
            "The apprentice _____ how to operate the pneumatic riveting tool yet.",
            {"A": "doesn't knows", "B": "not know", "C": "is not know", "D": "doesn't know"},
            "D",
            {
                "correct": "Negative Present Simple for singular subject is 'doesn't + base form' ('doesn't know').",
                "wrong_A": "'doesn't' already carries the third person marker, so verb remains base 'know', not 'knows'.",
                "wrong_B": "Missing auxiliary 'doesn't'.",
                "wrong_C": "Ungrammatical construction."
            },
            "Czech 'neví'. In English, never say *he doesn't knows* or *he not know*. Use 'doesn't know'.",
            "Workshop Assembly & Line Tooling"
        ),
        create_question(
            "TTR-ENG-A2-001-Q8",
            "_____ safety shoes required in this assembly hall?",
            {"A": "Are", "B": "Is", "C": "Do", "D": "Does"},
            "A",
            {
                "correct": "'Safety shoes' is plural, so the question begins with 'Are'.",
                "wrong_B": "'Is' is singular, but 'shoes' is plural.",
                "wrong_C": "'Do' cannot be used with passive participle/adjective 'required' without another verb.",
                "wrong_D": "'Does' is singular."
            },
            "Czech 'Jsou bezpečnostní boty povinné?'. 'Shoes' is plural in English $\rightarrow$ 'Are safety shoes...?'.",
            "Workshop Assembly & Line Tooling"
        ),
        create_question(
            "TTR-ENG-A2-001-Q9",
            "Please _____ the oil level before starting the diesel test bench.",
            {"A": "checking", "B": "check", "C": "checks", "D": "to check"},
            "B",
            {
                "correct": "'Please' is followed by the base imperative verb form ('check').",
                "wrong_A": "'-ing' cannot follow 'Please' in an instruction.",
                "wrong_C": "'-s' form is incorrect.",
                "wrong_D": "Infinitive with 'to' is ungrammatical after 'Please'."
            },
            "Czech 'Prosím zkontrolujte...'. In English, 'Please + base verb' ('Please check').",
            "Workshop Assembly & Line Tooling"
        ),
        create_question(
            "TTR-ENG-A2-001-Q10",
            "This torque wrench _____ accurate to within 2 Newton-meters.",
            {"A": "are", "B": "is", "C": "have", "D": "has"},
            "B",
            {
                "correct": "Singular subject 'wrench' takes 'is' with the adjective 'accurate'.",
                "wrong_A": "'are' is plural.",
                "wrong_C": "'have' cannot connect subject to an adjective.",
                "wrong_D": "'has' cannot connect subject to an adjective."
            },
            "Czech 'Tento klíč je přesný'. Subject 'wrench' is singular $\rightarrow$ 'is accurate'.",
            "Workshop Assembly & Line Tooling"
        )
    ]
}

# =============================================================================
# SUITE 2: TATRA SALES AND ENGINEERING
# =============================================================================
tatra_sales_manifest = [
    {
        "test_id": "TTR-SALES-A2-001",
        "title": "Customer Inquiries, Vehicle Pricing & Stock: Present Simple",
        "level": "A2",
        "category": "core",
        "workplace_track": "Technical Vehicle Specifications & Pitching",
        "estimated_time_minutes": 10,
        "description": "Essential English for answering foreign dealer inquiries about truck prices, models in stock, and basic lead times.",
        "grammar_focus": "Question Formation (How much, How many, Is/Are) & Present Simple"
    },
    {
        "test_id": "TTR-SALES-A2-002",
        "title": "Polite Email Requests to Foreign Dealers: Can, Could & Please",
        "level": "A2",
        "category": "core",
        "workplace_track": "Warranty Claims & Dealer Network Service",
        "estimated_time_minutes": 10,
        "description": "Draft clear, professional emails asking for VIN numbers, photos of damaged axles, and signed delivery notes.",
        "grammar_focus": "Polite Modals (Can you, Could you please, Would you like)"
    },
    {
        "test_id": "TTR-SALES-A2-003",
        "title": "Trade Fairs & Client Negotiations: Past Simple",
        "level": "A2",
        "category": "core",
        "workplace_track": "Commercial Negotiation & Payment Milestones",
        "estimated_time_minutes": 12,
        "description": "Report on international expo meetings (IDET, Eurosatory) and customer discussions using past simple regular and irregular verbs.",
        "grammar_focus": "Past Simple (met, discussed, agreed, signed, showed)"
    },
    {
        "test_id": "TTR-SALES-A2-004",
        "title": "Truck Quantities, Weights & Prices: Numbers & Quantifiers",
        "level": "A2",
        "category": "core",
        "workplace_track": "Export Logistics & Incoterms 2020",
        "estimated_time_minutes": 10,
        "description": "Accurately state vehicle payload in kilograms, container load counts, discount percentages, and currency amounts.",
        "grammar_focus": "Numbers, Quantifiers (much/many, some/any) & Units"
    },
    {
        "test_id": "TTR-SALES-A2-005",
        "title": "Delivery Deadlines & Shipping Schedules: Prepositions of Time",
        "level": "A2",
        "category": "core",
        "workplace_track": "Export Logistics & Incoterms 2020",
        "estimated_time_minutes": 10,
        "description": "Specify exact contract deadlines using at, on, in, by, and until without typical Czech preposition errors.",
        "grammar_focus": "Prepositions of Time (on Friday, in October, by 15:00)"
    },
    {
        "test_id": "TTR-SALES-B1-001",
        "title": "Spare Parts Dispatch & Export Clearance: Present Perfect vs Past Simple",
        "level": "B1",
        "category": "core",
        "workplace_track": "Export Logistics & Incoterms 2020",
        "estimated_time_minutes": 15,
        "description": "Differentiate completed past delivery milestones with dates from ongoing dispatch status to foreign dealers.",
        "grammar_focus": "Present Perfect vs Past Simple with Time Markers"
    },
    {
        "test_id": "TTR-SALES-B2-001",
        "title": "High-Stakes Defense Tender Bargaining: Inversion for Emphasis",
        "level": "B2",
        "category": "core",
        "workplace_track": "Defense & Government Tenders (NATO STANAG)",
        "estimated_time_minutes": 18,
        "description": "Employ formal negative adverbial inversion to assert non-negotiable warranty limits and contractual boundaries.",
        "grammar_focus": "Inversion with Negative Adverbials (Under no circumstances, Seldom)"
    },
    {
        "test_id": "TTR-SALES-SP-001",
        "title": "Professional Negotiation Idioms & Incoterms 2020 Definitions",
        "level": "B1/B2",
        "category": "specialized",
        "workplace_track": "Export Logistics & Incoterms 2020",
        "estimated_time_minutes": 16,
        "description": "Master international shipping terms (EXW, FOB, CIF, DAP) and business negotiation idioms (sweeten the deal, ball is in their court).",
        "grammar_focus": "Incoterms 2020 & Commercial Negotiation Idioms"
    }
]

# Sample A2 Test for Tatra Sales
tatra_sales_a2_001 = {
    "test_id": "TTR-SALES-A2-001",
    "title": "Customer Inquiries, Vehicle Pricing & Stock: Present Simple",
    "level": "A2",
    "category": "core",
    "workplace_track": "Technical Vehicle Specifications & Pitching",
    "estimated_time_minutes": 10,
    "description": "Essential English for answering foreign dealer inquiries about truck prices, models in stock, and basic lead times.",
    "learning_objectives": [
        "Ask and answer basic customer questions about vehicle availability",
        "Use correct question word order with 'How much' and 'How many'",
        "Eliminate Czech preposition and word order transfer in sales inquiries"
    ],
    "questions": [
        create_question(
            "TTR-SALES-A2-001-Q1",
            "How much _____ a standard 6x6 Tatra Phoenix chassis cost under EXW terms?",
            {"A": "is", "B": "does", "C": "do", "D": "has"},
            "B",
            {
                "correct": "Singular subject 'chassis' with main action verb 'cost' requires auxiliary 'does'.",
                "wrong_A": "'is' cannot be used with base verb 'cost'.",
                "wrong_C": "'do' is plural.",
                "wrong_D": "'has' cannot form this question."
            },
            "Czech 'Kolik stojí...?'. In English questions with verbs, use 'How much does [subject] cost?'.",
            "Technical Vehicle Specifications & Pitching"
        ),
        create_question(
            "TTR-SALES-A2-001-Q2",
            "How many 8x8 military trucks _____ currently available in factory stock?",
            {"A": "is", "B": "does", "C": "are", "D": "have"},
            "C",
            {
                "correct": "'How many trucks' is plural and asks about existence, taking 'are'.",
                "wrong_A": "'is' is singular.",
                "wrong_B": "'does' is singular auxiliary.",
                "wrong_D": "'have' does not match the existence structure."
            },
            "Czech 'Kolik nákladních vozů je skladem?'. Plural subject requires 'are'.",
            "Technical Vehicle Specifications & Pitching"
        ),
        create_question(
            "TTR-SALES-A2-001-Q3",
            "Our sales department _____ technical datasheets in English and German.",
            {"A": "provides", "B": "provide", "C": "is provide", "D": "providing"},
            "A",
            {
                "correct": "Singular corporate subject 'Our sales department' takes 'provides' with singular '-s'.",
                "wrong_B": "Missing third person singular '-s'.",
                "wrong_C": "Ungrammatical verb phrase.",
                "wrong_D": "Participle alone cannot be finite verb."
            },
            "Czech 'Naše obchodní oddělení poskytuje'. Remember singular department takes '-s' in English.",
            "Technical Vehicle Specifications & Pitching"
        ),
        create_question(
            "TTR-SALES-A2-001-Q4",
            "When _____ the customer need the final commercial invoice?",
            {"A": "do", "B": "is", "C": "are", "D": "does"},
            "D",
            {
                "correct": "Singular subject 'the customer' requires auxiliary 'does' in Present Simple questions.",
                "wrong_A": "'do' is plural.",
                "wrong_B": "'is' cannot pair with main verb 'need'.",
                "wrong_C": "'are' is plural."
            },
            "Czech 'Kdy zákazník potřebuje...?'. In English: 'When does the customer need...?'.",
            "Commercial Negotiation & Payment Milestones"
        ),
        create_question(
            "TTR-SALES-A2-001-Q5",
            "The client _____ not want the standard manual transmission; they prefer automatic.",
            {"A": "do", "B": "is", "C": "does", "D": "are"},
            "C",
            {
                "correct": "Singular subject 'The client' takes 'does not want'.",
                "wrong_A": "'do' is plural.",
                "wrong_B": "'is not want' is ungrammatical.",
                "wrong_D": "'are' is plural."
            },
            "Czech 'Zákazník nechce'. Use 'does not want', never *is not want*.",
            "Technical Vehicle Specifications & Pitching"
        ),
        create_question(
            "TTR-SALES-A2-001-Q6",
            "_____ you send us your company VAT number before we prepare the quotation?",
            {"A": "Can", "B": "Do", "C": "Are", "D": "Have"},
            "A",
            {
                "correct": "Modal 'Can' expresses a polite commercial request ('Can you send us...?').",
                "wrong_B": "'Do you send' asks about habitual routine, not a request.",
                "wrong_C": "'Are you send' is ungrammatical.",
                "wrong_D": "'Have you send' violates participle grammar."
            },
            "In commercial email requests, start with 'Can you send us...' or 'Could you please send us...'.",
            "Commercial Negotiation & Payment Milestones"
        ),
        create_question(
            "TTR-SALES-A2-001-Q7",
            "All export prices in this price list _____ valid until the end of November.",
            {"A": "is", "B": "has", "C": "are", "D": "have"},
            "C",
            {
                "correct": "Plural subject 'All export prices' takes 'are'.",
                "wrong_A": "'is' is singular.",
                "wrong_B": "'has' cannot connect subject to adjective 'valid'.",
                "wrong_D": "'have' cannot connect subject to adjective 'valid'."
            },
            "Czech 'Všechny exportní ceny jsou platné'. 'Prices' is plural $\rightarrow$ 'are valid'.",
            "Export Logistics & Incoterms 2020"
        ),
        create_question(
            "TTR-SALES-A2-001-Q8",
            "The Australian mining buyer _____ five Phoenix dump trucks every quarter.",
            {"A": "buys", "B": "buy", "C": "is buy", "D": "buying"},
            "A",
            {
                "correct": "Singular subject 'The buyer' requires 3rd person singular 'buys'.",
                "wrong_B": "'buy' lacks singular '-s'.",
                "wrong_C": "Invalid verb phrase.",
                "wrong_D": "Participle alone cannot be main verb."
            },
            "Czech 'Australský těžař kupuje'. Add '-s' to third person singular: 'buys'.",
            "Commercial Negotiation & Payment Milestones"
        ),
        create_question(
            "TTR-SALES-A2-001-Q9",
            "Is the spare parts catalog available _____ our online dealer portal?",
            {"A": "at", "B": "on", "C": "in", "D": "to"},
            "B",
            {
                "correct": "Websites, portals, and digital platforms always take the preposition 'on' ('on our portal').",
                "wrong_A": "'at' is used for physical locations or specific email addresses.",
                "wrong_C": "Czechs often say *in the portal* translated from 'v portálu'. English requires 'on the portal'.",
                "wrong_D": "'to' denotes direction."
            },
            "Czechs say 'v portálu / na internetu'. In English, always use 'on our website / on the dealer portal'.",
            "Warranty Claims & Dealer Network Service"
        ),
        create_question(
            "TTR-SALES-A2-001-Q10",
            "We _____ have these specific all-terrain tires in stock today.",
            {"A": "aren't", "B": "don't", "C": "doesn't", "D": "haven't"},
            "B",
            {
                "correct": "Subject 'We' takes 'don't have' in Present Simple.",
                "wrong_A": "'aren't have' is ungrammatical.",
                "wrong_C": "'doesn't' is for third person singular (he/she/it).",
                "wrong_D": "'haven't' as main verb negation without 'got' is non-standard in modern commercial English."
            },
            "Czech 'Nemáme skladem'. In English, say 'We don't have in stock'.",
            "Technical Vehicle Specifications & Pitching"
        )
    ]
}

# =============================================================================
# SUITE 3: TEVA ENGINEERING
# =============================================================================
teva_eng_manifest = [
    {
        "test_id": "TEV-ENG-A2-001",
        "title": "Cleanroom Gowning, Airlocks & PPE: Imperatives & Must",
        "level": "A2",
        "category": "core",
        "workplace_track": "Cleanroom HVAC Cascades & Differential Pressure",
        "estimated_time_minutes": 10,
        "description": "Essential English for sterile gowning procedures, airlock entry steps, and mandatory cleanroom hygiene rules.",
        "grammar_focus": "Imperatives (wash, put on, sanitize) & Modals (must, do not)"
    },
    {
        "test_id": "TEV-ENG-A2-002",
        "title": "Sterile Line Sensor Readings & Status: Present Simple",
        "level": "A2",
        "category": "core",
        "workplace_track": "SCADA, PLC & Industrial Sensors",
        "estimated_time_minutes": 10,
        "description": "Describe real-time machine states, temperature readings, and pressure indicators on the shop floor.",
        "grammar_focus": "Present Simple 3rd Person (-s) & Stative Verbs"
    },
    {
        "test_id": "TEV-ENG-A2-003",
        "title": "Yesterday's Machine Stoppages & Maintenance: Past Simple",
        "level": "A2",
        "category": "core",
        "workplace_track": "Sterile Compounding & Filling Line Automation",
        "estimated_time_minutes": 12,
        "description": "Report equipment breakdowns, replaced O-rings, and cleaned nozzles using high-frequency past tense verbs.",
        "grammar_focus": "Past Simple Regular (-ed) & Irregular Verbs (failed, stopped, cleaned, replaced)"
    },
    {
        "test_id": "TEV-ENG-A2-004",
        "title": "Cleanroom Airflow & Sensor Positions: Prepositions of Place",
        "level": "A2",
        "category": "core",
        "workplace_track": "Cleanroom HVAC Cascades & Differential Pressure",
        "estimated_time_minutes": 10,
        "description": "Specify component positions inside laminar flow hoods, beneath HEPA filters, and between airlocks.",
        "grammar_focus": "Prepositions of Place (under, inside, above, next to, between)"
    },
    {
        "test_id": "TEV-ENG-A2-005",
        "title": "Autoclave Cycles & Temperatures: Numbers & Measurements",
        "level": "A2",
        "category": "core",
        "workplace_track": "Tablet Compression & Lyophilization Equipment",
        "estimated_time_minutes": 10,
        "description": "Communicate sterilizer temperatures in Celsius (121°C), cycle times in minutes, and steam pressure in bar.",
        "grammar_focus": "Technical Numbers, Units & Temperature Phrasing"
    },
    {
        "test_id": "TEV-ENG-B1-001",
        "title": "Cleanroom HVAC Pressure Alarms: Past Simple vs Past Perfect",
        "level": "B1",
        "category": "core",
        "workplace_track": "Cleanroom HVAC Cascades & Differential Pressure",
        "estimated_time_minutes": 15,
        "description": "Master sequence of events in environmental deviation logs and differential pressure loss investigations.",
        "grammar_focus": "Past Simple vs Past Perfect Passive"
    },
    {
        "test_id": "TEV-ENG-B2-001",
        "title": "21 CFR Part 11 Electronic Records & CSV: Subjunctive & Directives",
        "level": "B2",
        "category": "core",
        "workplace_track": "Computerized System Validation (CSV & GAMP 5)",
        "estimated_time_minutes": 16,
        "description": "Draft formal regulatory compliance mandates for audit trails, password aging, and validated automated systems.",
        "grammar_focus": "Present Subjunctive & Formal Directives"
    },
    {
        "test_id": "TEV-ENG-SP-001",
        "title": "Computerized System Validation (CSV) & GAMP 5 Nomenclature",
        "level": "B1/B2",
        "category": "specialized",
        "workplace_track": "Computerized System Validation (CSV & GAMP 5)",
        "estimated_time_minutes": 16,
        "description": "Master pharmaceutical validation terminology: URS, FRS, IQ, OQ, PQ, traceability matrix, and audit trail review.",
        "grammar_focus": "Pharmaceutical Validation & GAMP 5 Nomenclature"
    }
]

# Sample A2 Test for Teva Engineering
teva_eng_a2_001 = {
    "test_id": "TEV-ENG-A2-001",
    "title": "Cleanroom Gowning, Airlocks & PPE: Imperatives & Must",
    "level": "A2",
    "category": "core",
    "workplace_track": "Cleanroom HVAC Cascades & Differential Pressure",
    "estimated_time_minutes": 10,
    "description": "Essential English for sterile gowning procedures, airlock entry steps, and mandatory cleanroom hygiene rules.",
    "learning_objectives": [
        "Give and follow clear cleanroom gowning instructions",
        "Use modal 'must' and 'do not' for GxP hygiene protocols",
        "Avoid Czech mother-tongue errors with basic modal verbs"
    ],
    "questions": [
        create_question(
            "TEV-ENG-A2-001-Q1",
            "Always _____ your hands with sterile disinfectant before entering Grade B airlock.",
            {"A": "washing", "B": "wash", "C": "washes", "D": "to wash"},
            "B",
            {
                "correct": "Imperative instruction uses the base form 'wash'.",
                "wrong_A": "'-ing' cannot be used for direct commands.",
                "wrong_C": "Third person '-es' cannot form an imperative.",
                "wrong_D": "'to' infinitive is ungrammatical."
            },
            "Czech 'Vždy si umyjte ruce'. In English, direct instructions use base verb: 'Always wash'.",
            "Cleanroom HVAC Cascades & Differential Pressure"
        ),
        create_question(
            "TEV-ENG-A2-001-Q2",
            "All personnel _____ wear sterile nitrile gloves in the cleanroom suite.",
            {"A": "must to", "B": "have", "C": "must", "D": "are"},
            "C",
            {
                "correct": "Modal 'must' is followed directly by the bare infinitive ('must wear').",
                "wrong_A": "Never use 'to' after 'must' (*must to wear* is a frequent Czenglish error).",
                "wrong_B": "'have wear' is ungrammatical; it would need 'have to wear'.",
                "wrong_D": "'are wear' is invalid."
            },
            "Never say *must to wear*. Modal 'must' takes the bare verb without 'to': 'must wear'.",
            "Cleanroom HVAC Cascades & Differential Pressure"
        ),
        create_question(
            "TEV-ENG-A2-001-Q3",
            "Do not _____ both airlock doors at the same time!",
            {"A": "opens", "B": "opening", "C": "to open", "D": "open"},
            "D",
            {
                "correct": "Negative imperative 'Do not' requires the base verb 'open'.",
                "wrong_A": "Third person '-s' is invalid after 'Do not'.",
                "wrong_B": "'-ing' form cannot follow 'Do not'.",
                "wrong_C": "'to open' is invalid after 'Do not'."
            },
            "Czech 'Neotvírejte obě dveře současně'. Use 'Do not open'.",
            "Cleanroom HVAC Cascades & Differential Pressure"
        ),
        create_question(
            "TEV-ENG-A2-001-Q4",
            "The technician _____ the differential pressure gauge on the wall every two hours.",
            {"A": "checks", "B": "check", "C": "is check", "D": "checking"},
            "A",
            {
                "correct": "Singular subject 'The technician' requires singular '-s' in Present Simple ('checks').",
                "wrong_B": "'check' lacks third person '-s'.",
                "wrong_C": "Ungrammatical.",
                "wrong_D": "Participle alone cannot be the main verb."
            },
            "Czech 'Technik kontroluje'. Third person singular in English requires '-s': 'checks'.",
            "SCADA, PLC & Industrial Sensors"
        ),
        create_question(
            "TEV-ENG-A2-001-Q5",
            "Where _____ the sterile shoe cover dispenser located?",
            {"A": "are", "B": "is", "C": "does", "D": "do"},
            "B",
            {
                "correct": "Singular subject 'dispenser' takes 'is'.",
                "wrong_A": "'are' is plural.",
                "wrong_C": "'does' is not used with passive adjective 'located'.",
                "wrong_D": "'do' is plural."
            },
            "Czech 'Kde se nachází dávkovač návleků?'. Singular subject $\rightarrow$ 'Where is the dispenser...?'.",
            "Cleanroom HVAC Cascades & Differential Pressure"
        ),
        create_question(
            "TEV-ENG-A2-001-Q6",
            "You _____ touch sterile vial stoppers with bare hands under any circumstances!",
            {"A": "must not", "B": "don't have to", "C": "haven't to", "D": "needn't"},
            "A",
            {
                "correct": "'Must not' expresses life-critical strict prohibition (Czech 'nesmíte').",
                "wrong_B": "'Don't have to' means it is optional (nemusíte), which is a critical hygiene hazard!",
                "wrong_C": "'Haven't to' is ungrammatical.",
                "wrong_D": "'Needn't' means lack of necessity, not strict prohibition."
            },
            "Czech 'Nesmíte' = 'must not'. Do not confuse with 'nemusíte' ('don't have to').",
            "Sterile Compounding & Filling Line Automation"
        ),
        create_question(
            "TEV-ENG-A2-001-Q7",
            "The cleanroom autoclave _____ a digital data logger for temperature records.",
            {"A": "have", "B": "is having", "C": "has", "D": "having"},
            "C",
            {
                "correct": "Singular subject 'The autoclave' takes 'has' for possession.",
                "wrong_A": "'have' is plural.",
                "wrong_B": "Stative 'have' does not take continuous aspect.",
                "wrong_D": "Incomplete verb."
            },
            "Czech 'Autokláv má'. Singular subject takes 'has', not 'have'.",
            "Tablet Compression & Lyophilization Equipment"
        ),
        create_question(
            "TEV-ENG-A2-001-Q8",
            "Please _____ the yellow emergency stop button if the conveyor jams.",
            {"A": "press", "B": "pressing", "C": "presses", "D": "to press"},
            "A",
            {
                "correct": "Polite imperative takes base form 'press' after 'Please'.",
                "wrong_B": "'-ing' cannot follow 'Please'.",
                "wrong_C": "Third person '-es' is incorrect.",
                "wrong_D": "Infinitive with 'to' is invalid after 'Please'."
            },
            "Czech 'Prosím stiskněte...'. In English: 'Please press the button'.",
            "Sterile Compounding & Filling Line Automation"
        ),
        create_question(
            "TEV-ENG-A2-001-Q9",
            "Differential pressure between Grade B and Grade C _____ currently 15 Pascals.",
            {"A": "are", "B": "have", "C": "is", "D": "has"},
            "C",
            {
                "correct": "Uncountable/singular subject 'Differential pressure' takes 'is'.",
                "wrong_A": "'are' is plural.",
                "wrong_B": "'have' cannot link to a measurement predicate.",
                "wrong_D": "'has' is incorrect for state/value."
            },
            "Czech 'Tlakový rozdíl je...'. 'Pressure' is singular $\rightarrow$ 'is 15 Pascals'.",
            "Cleanroom HVAC Cascades & Differential Pressure"
        ),
        create_question(
            "TEV-ENG-A2-001-Q10",
            "Operators _____ not enter the filling suite without complete sterile gowning.",
            {"A": "do", "B": "may", "C": "are", "D": "can"},
            "B",
            {
                "correct": "'May not' (or 'must not') expresses formal regulatory prohibition in GMP SOPs.",
                "wrong_A": "'do not enter' would require bare imperative syntax.",
                "wrong_C": "'are not enter' is ungrammatical.",
                "wrong_D": "'can not' expresses lack of physical ability rather than formal regulatory prohibition."
            },
            "In pharmaceutical GMP standards, 'nesmí vstoupit' is formally rendered as 'may not enter' or 'must not enter'.",
            "Cleanroom HVAC Cascades & Differential Pressure"
        )
    ]
}

# =============================================================================
# SUITE 4: TAPI CHEMISTRY
# =============================================================================
tapi_chem_manifest = [
    {
        "test_id": "TAPI-CHEM-A2-001",
        "title": "Laboratory Glassware, Reagents & Fume Hoods: Imperatives & Must",
        "level": "A2",
        "category": "core",
        "workplace_track": "Hazardous Reagents, Solvent Recovery & Lab Safety",
        "estimated_time_minutes": 10,
        "description": "Essential English for handling beakers, pipettes, chemical reagents, and lab safety rules under the fume hood.",
        "grammar_focus": "Imperatives (wear, label, pour, store) & Safety Modals (must, do not)"
    },
    {
        "test_id": "TAPI-CHEM-A2-002",
        "title": "Daily QC Testing & Analytical Weighing: Present Simple",
        "level": "A2",
        "category": "core",
        "workplace_track": "Analytical Chemistry (HPLC, GC, Spectroscopy)",
        "estimated_time_minutes": 10,
        "description": "Describe daily laboratory testing procedures, analytical balance calibration, and sample dilution routines.",
        "grammar_focus": "Present Simple 3rd Person (-s) & Laboratory Frequency Adverbs"
    },
    {
        "test_id": "TAPI-CHEM-A2-003",
        "title": "Yesterday's Chemical Synthesis & Titration: Past Simple",
        "level": "A2",
        "category": "core",
        "workplace_track": "Organic Chemical Synthesis & Batch Reactors",
        "estimated_time_minutes": 12,
        "description": "Report on reaction batches, added solvents, and measured pH values using regular and irregular past verbs.",
        "grammar_focus": "Past Simple (mixed, weighed, dissolved, heated, recorded)"
    },
    {
        "test_id": "TAPI-CHEM-A2-004",
        "title": "Chemical Storage & Reagent Cabinets: Prepositions of Place",
        "level": "A2",
        "category": "core",
        "workplace_track": "Hazardous Reagents, Solvent Recovery & Lab Safety",
        "estimated_time_minutes": 10,
        "description": "Accurately state chemical locations: in the acid cabinet, under the fume hood, on the top shelf, next to the HPLC.",
        "grammar_focus": "Prepositions of Place (in, on, under, inside, next to)"
    },
    {
        "test_id": "TAPI-CHEM-A2-005",
        "title": "Temperatures, Milligrams & Liquid Volumes: Units & Numbers",
        "level": "A2",
        "category": "core",
        "workplace_track": "In-Process Control (IPC) & Out-of-Specification",
        "estimated_time_minutes": 10,
        "description": "Accurately communicate chemical quantities: 250 milliliters, 0.05 milligrams, pH 7.4, and 80 degrees Celsius.",
        "grammar_focus": "Chemical Units, Decimal Numbers & Quantities"
    },
    {
        "test_id": "TAPI-CHEM-B1-001",
        "title": "API Reactor Yield & Solvent Recovery: Present Perfect vs Past Simple",
        "level": "B1",
        "category": "core",
        "workplace_track": "Organic Chemical Synthesis & Batch Reactors",
        "estimated_time_minutes": 15,
        "description": "Differentiate completed past synthesis campaigns from ongoing solvent distillation and IPC batch status.",
        "grammar_focus": "Present Perfect vs Past Simple with Time Markers"
    },
    {
        "test_id": "TAPI-CHEM-B2-001",
        "title": "HPLC Chromatography Out-of-Specification (OOS): Third Conditional",
        "level": "B2",
        "category": "core",
        "workplace_track": "Analytical Chemistry (HPLC, GC, Spectroscopy)",
        "estimated_time_minutes": 16,
        "description": "Investigate chromatography peak tailing and unexpected impurity spikes in historical batch testing.",
        "grammar_focus": "Third Conditional (If + Past Perfect, would have + V3)"
    },
    {
        "test_id": "TAPI-CHEM-SP-001",
        "title": "False Friends in Chemical Synthesis & Lab Testing",
        "level": "B1/B2",
        "category": "specialized",
        "workplace_track": "Pharmacopeial Compliance (Ph. Eur., USP)",
        "estimated_time_minutes": 16,
        "description": "Dismantle false cognates in chemistry: charge (batch vs poplatek), recipe (master formula vs recept), plastic (ductile vs plastový).",
        "grammar_focus": "Chemical Synthesis & QC False Cognates"
    }
]

# Sample A2 Test for Tapi Chemistry
tapi_chem_a2_001 = {
    "test_id": "TAPI-CHEM-A2-001",
    "title": "Laboratory Glassware, Reagents & Fume Hoods: Imperatives & Must",
    "level": "A2",
    "category": "core",
    "workplace_track": "Hazardous Reagents, Solvent Recovery & Lab Safety",
    "estimated_time_minutes": 10,
    "description": "Essential English for handling beakers, pipettes, chemical reagents, and lab safety rules under the fume hood.",
    "learning_objectives": [
        "Use simple laboratory imperatives (pour, label, store, heat)",
        "Apply modal 'must' and 'do not' for chemical safety",
        "Avoid basic Czech transfer in lab SOPs"
    ],
    "questions": [
        create_question(
            "TAPI-CHEM-A2-001-Q1",
            "Always _____ the chemical reagent bottle immediately after taking a sample.",
            {"A": "closing", "B": "close", "C": "closed", "D": "to close"},
            "B",
            {
                "correct": "Imperative instruction uses base form 'close'.",
                "wrong_A": "'-ing' cannot form direct instruction.",
                "wrong_C": "Past tense cannot form instruction.",
                "wrong_D": "'to' infinitive is ungrammatical."
            },
            "Czech 'Vždy uzavřete lahev'. In English, direct instructions take the base verb 'Always close'.",
            "Hazardous Reagents, Solvent Recovery & Lab Safety"
        ),
        create_question(
            "TAPI-CHEM-A2-001-Q2",
            "You _____ pour concentrated sulfuric acid into water, never water into acid!",
            {"A": "can", "B": "must to", "C": "are", "D": "must"},
            "D",
            {
                "correct": "Safety rule uses 'must' followed by bare infinitive ('must pour').",
                "wrong_A": "'can' implies optional choice, which is dangerous.",
                "wrong_B": "'must to' is ungrammatical (*must to* is a common Czenglish error).",
                "wrong_C": "'are' cannot pair with base verb 'pour'."
            },
            "Never say *must to*. Use 'must + base verb': 'You must pour acid into water'.",
            "Hazardous Reagents, Solvent Recovery & Lab Safety"
        ),
        create_question(
            "TAPI-CHEM-A2-001-Q3",
            "Do not _____ volatile organic solvents outside the certified fume hood!",
            {"A": "heating", "B": "to heat", "C": "heat", "D": "heats"},
            "C",
            {
                "correct": "Negative imperative 'Do not' requires base verb 'heat'.",
                "wrong_A": "'-ing' cannot follow 'Do not'.",
                "wrong_B": "'to' cannot follow 'Do not'.",
                "wrong_D": "'-s' form cannot follow 'Do not'."
            },
            "Czech 'Nezahřívejte těkavá rozpouštědla'. Use 'Do not heat'.",
            "Hazardous Reagents, Solvent Recovery & Lab Safety"
        ),
        create_question(
            "TAPI-CHEM-A2-001-Q4",
            "The analytical chemist _____ the pH buffer solution before each titration test.",
            {"A": "calibrates", "B": "calibrate", "C": "is calibrate", "D": "calibrating"},
            "A",
            {
                "correct": "Singular subject 'The chemist' takes 'calibrates' with third person '-s'.",
                "wrong_B": "'calibrate' lacks singular '-s'.",
                "wrong_C": "Invalid verb phrase.",
                "wrong_D": "Participle alone cannot be predicate."
            },
            "Czech 'Chemik kalibruje'. Third person singular in English requires '-s': 'calibrates'.",
            "Analytical Chemistry (HPLC, GC, Spectroscopy)"
        ),
        create_question(
            "TAPI-CHEM-A2-001-Q5",
            "Where _____ the safety data sheet (SDS) for this solvent stored?",
            {"A": "does", "B": "do", "C": "is", "D": "are"},
            "C",
            {
                "correct": "Singular subject 'sheet' takes 'is' with passive participle 'stored'.",
                "wrong_A": "'does' is auxiliary for action verbs, not passive state.",
                "wrong_B": "'do' is plural.",
                "wrong_D": "'are' is plural."
            },
            "Czech 'Kde je uložen bezpečnostní list?'. Singular subject takes 'Where is the sheet stored?'.",
            "Hazardous Reagents, Solvent Recovery & Lab Safety"
        ),
        create_question(
            "TAPI-CHEM-A2-001-Q6",
            "Lab technicians _____ wear chemical-resistant nitrile gloves when handling acetone.",
            {"A": "must", "B": "must to", "C": "have", "D": "are"},
            "A",
            {
                "correct": "Modal 'must' is followed directly by bare infinitive ('must wear').",
                "wrong_B": "'must to' is ungrammatical.",
                "wrong_C": "'have' requires 'to'.",
                "wrong_D": "'are wear' is invalid."
            },
            "Never say *must to wear*. Always use 'must wear'.",
            "Hazardous Reagents, Solvent Recovery & Lab Safety"
        ),
        create_question(
            "TAPI-CHEM-A2-001-Q7",
            "Please _____ every glass flask with the batch number and expiration date.",
            {"A": "labeling", "B": "labels", "C": "to label", "D": "label"},
            "D",
            {
                "correct": "'Please' is followed by base imperative verb 'label'.",
                "wrong_A": "'-ing' cannot follow 'Please'.",
                "wrong_B": "'-s' form is incorrect.",
                "wrong_C": "'to' is invalid after 'Please'."
            },
            "Czech 'Prosím označte...'. In English, use 'Please label every flask'.",
            "Hazardous Reagents, Solvent Recovery & Lab Safety"
        ),
        create_question(
            "TAPI-CHEM-A2-001-Q8",
            "The analytical balance in lab 3 _____ accurate to four decimal places.",
            {"A": "are", "B": "is", "C": "have", "D": "has"},
            "B",
            {
                "correct": "Singular subject 'balance' takes 'is' with adjective 'accurate'.",
                "wrong_A": "'are' is plural.",
                "wrong_C": "'have' cannot link to an adjective.",
                "wrong_D": "'has' cannot link to an adjective."
            },
            "Czech 'Váha je přesná'. Singular subject $\\rightarrow$ 'is accurate'.",
            "Analytical Chemistry (HPLC, GC, Spectroscopy)"
        ),
        create_question(
            "TAPI-CHEM-A2-001-Q9",
            "The sample solution _____ not dissolve at room temperature; it requires heating.",
            {"A": "is", "B": "do", "C": "does", "D": "are"},
            "C",
            {
                "correct": "Singular subject 'The solution' takes 'does not dissolve'.",
                "wrong_A": "'is not dissolve' is ungrammatical.",
                "wrong_B": "'do' is plural.",
                "wrong_D": "'are' is plural."
            },
            "Czech 'Roztok se nerozpouští'. Say 'does not dissolve', not *is not dissolve*.",
            "Organic Chemical Synthesis & Batch Reactors"
        ),
        create_question(
            "TAPI-CHEM-A2-001-Q10",
            "All flammable waste solvents must be poured _____ the dedicated red container.",
            {"A": "to", "B": "into", "C": "on", "D": "under"},
            "B",
            {
                "correct": "'Pour into' indicates movement into an enclosed vessel or container.",
                "wrong_A": "'to' denotes direction toward, but liquid goes inside $\\rightarrow$ 'into'.",
                "wrong_C": "'on' means onto the outer surface.",
                "wrong_D": "'under' means beneath."
            },
            "Czech 'nalít do nádoby'. English uses 'pour into the container'.",
            "Hazardous Reagents, Solvent Recovery & Lab Safety"
        )
    ]
}

# =============================================================================
# SUITE 5: TEVA IT
# =============================================================================
teva_it_manifest = [
    {
        "test_id": "TEV-IT-A2-001",
        "title": "Hardware Setup, Peripherals & Cables: Imperatives & Can",
        "level": "A2",
        "category": "core",
        "workplace_track": "IT Infrastructure & Cloud Operations",
        "estimated_time_minutes": 10,
        "description": "Essential English for connecting monitors, docking stations, network cables, and basic reboot instructions.",
        "grammar_focus": "Imperatives (connect, plug in, reboot) & Modals (can, can't)"
    },
    {
        "test_id": "TEV-IT-A2-002",
        "title": "Daily Service Desk Support & User Tickets: Present Simple",
        "level": "A2",
        "category": "core",
        "workplace_track": "ITIL Global Service Desk & Incident Escalation",
        "estimated_time_minutes": 10,
        "description": "Describe daily ticket assignment, closing P3 tickets, and password reset routines with correct third person agreement.",
        "grammar_focus": "Present Simple 3rd Person (-s) & Frequency Adverbs"
    },
    {
        "test_id": "TEV-IT-A2-003",
        "title": "Yesterday's Network Outage & Server Restarts: Past Simple",
        "level": "A2",
        "category": "core",
        "workplace_track": "IT Infrastructure & Cloud Operations",
        "estimated_time_minutes": 12,
        "description": "Report on server reboots, network card failures, and restored VPN connections using regular and irregular past verbs.",
        "grammar_focus": "Past Simple (crashed, restarted, reset, failed, restored)"
    },
    {
        "test_id": "TEV-IT-A2-004",
        "title": "Server Rack Connections & Ports: Prepositions of Place",
        "level": "A2",
        "category": "core",
        "workplace_track": "IT Infrastructure & Cloud Operations",
        "estimated_time_minutes": 10,
        "description": "Specify hardware connections: into port 1, behind the server rack, on top of the switch, between the routers.",
        "grammar_focus": "Prepositions of Place (into, behind, on top of, between)"
    },
    {
        "test_id": "TEV-IT-A2-005",
        "title": "Cybersecurity Warnings & Password Rules: Must & Must Not",
        "level": "A2",
        "category": "core",
        "workplace_track": "Cybersecurity, IAM & Zero Trust Architecture",
        "estimated_time_minutes": 10,
        "description": "Understand corporate IT security rules: never share passwords, verify email links, and lock workstations.",
        "grammar_focus": "Modals of Obligation & Prohibition (must, must not, don't)"
    },
    {
        "test_id": "TEV-IT-B1-001",
        "title": "Cloud Server Outage Post-Mortems: Past Simple vs Past Perfect",
        "level": "B1",
        "category": "core",
        "workplace_track": "IT Infrastructure & Cloud Operations",
        "estimated_time_minutes": 15,
        "description": "Chronological reporting of AWS database failovers and automated pod restarts in post-incident reviews.",
        "grammar_focus": "Past Simple vs Past Perfect Passive"
    },
    {
        "test_id": "TEV-IT-B2-001",
        "title": "Zero Trust Security Architecture: Inversion for Emphasis",
        "level": "B2",
        "category": "core",
        "workplace_track": "Cybersecurity, IAM & Zero Trust Architecture",
        "estimated_time_minutes": 18,
        "description": "Draft formal IT security policy statements using negative and restrictive adverbial inversion.",
        "grammar_focus": "Inversion with Negative Adverbials (Under no circumstances, Seldom)"
    },
    {
        "test_id": "TEV-IT-SP-001",
        "title": "False Friends in IT & Software Development",
        "level": "B1/B2",
        "category": "specialized",
        "workplace_track": "Software Engineering, APIs & Microservices",
        "estimated_time_minutes": 16,
        "description": "Dismantle IT false cognates: actual (current vs real), eventual (possible vs final), control (check vs direct), evidence (records vs proof).",
        "grammar_focus": "IT & Software Development False Cognates"
    }
]

# Sample A2 Test for Teva IT
teva_it_a2_001 = {
    "test_id": "TEV-IT-A2-001",
    "title": "Hardware Setup, Peripherals & Cables: Imperatives & Can",
    "level": "A2",
    "category": "core",
    "workplace_track": "IT Infrastructure & Cloud Operations",
    "estimated_time_minutes": 10,
    "description": "Essential English for connecting monitors, docking stations, network cables, and basic reboot instructions.",
    "learning_objectives": [
        "Give basic IT support instructions (plug in, restart, connect)",
        "Use modal 'can' and 'can't' for hardware compatibility",
        "Avoid basic Czech word order mistakes in IT inquiries"
    ],
    "questions": [
        create_question(
            "TEV-IT-A2-001-Q1",
            "Please _____ your laptop and check if the Wi-Fi connects.",
            {"A": "rebooting", "B": "reboot", "C": "reboots", "D": "to reboot"},
            "B",
            {
                "correct": "Polite imperative after 'Please' uses base form 'reboot'.",
                "wrong_A": "'-ing' cannot follow 'Please'.",
                "wrong_C": "Third person '-s' is incorrect.",
                "wrong_D": "'to' is invalid after 'Please'."
            },
            "Czech 'Prosím restartujte...'. In English, say 'Please reboot / Please restart'.",
            "IT Infrastructure & Cloud Operations"
        ),
        create_question(
            "TEV-IT-A2-001-Q2",
            "You _____ connect this external monitor using an HDMI cable.",
            {"A": "can to", "B": "are", "C": "can", "D": "have"},
            "C",
            {
                "correct": "Modal 'can' takes bare infinitive ('can connect').",
                "wrong_A": "'can to' is ungrammatical (never use 'to' after 'can').",
                "wrong_B": "'are connect' is invalid.",
                "wrong_D": "'have connect' is ungrammatical."
            },
            "Never say *can to connect*. Always say 'You can connect'.",
            "IT Infrastructure & Cloud Operations"
        ),
        create_question(
            "TEV-IT-A2-001-Q3",
            "Do not _____ the USB flash drive while the file transfer is in progress!",
            {"A": "disconnect", "B": "disconnecting", "C": "disconnects", "D": "to disconnect"},
            "A",
            {
                "correct": "Negative imperative 'Do not' requires base verb 'disconnect'.",
                "wrong_B": "'-ing' cannot follow 'Do not'.",
                "wrong_C": "'-s' form cannot follow 'Do not'.",
                "wrong_D": "'to' cannot follow 'Do not'."
            },
            "Czech 'Neodpojujte flash disk'. Use 'Do not disconnect'.",
            "IT Infrastructure & Cloud Operations"
        ),
        create_question(
            "TEV-IT-A2-001-Q4",
            "The service desk technician _____ all incoming P3 tickets within four hours.",
            {"A": "assign", "B": "assigns", "C": "is assign", "D": "assigning"},
            "B",
            {
                "correct": "Singular subject 'The technician' takes 'assigns' with third person '-s'.",
                "wrong_A": "'assign' lacks singular '-s'.",
                "wrong_C": "Invalid verb phrase.",
                "wrong_D": "Participle alone cannot be predicate."
            },
            "Czech 'Technik přiřazuje'. Third person singular in English requires '-s': 'assigns'.",
            "ITIL Global Service Desk & Incident Escalation"
        ),
        create_question(
            "TEV-IT-A2-001-Q5",
            "Where _____ the network Ethernet cable connected?",
            {"A": "does", "B": "is", "C": "are", "D": "do"},
            "B",
            {
                "correct": "Singular subject 'cable' takes 'is' with passive participle 'connected'.",
                "wrong_A": "'does' is auxiliary for action verbs.",
                "wrong_C": "'are' is plural.",
                "wrong_D": "'do' is plural."
            },
            "Czech 'Kde je zapojen kabel?'. Singular subject $\rightarrow$ 'Where is the cable connected?'.",
            "IT Infrastructure & Cloud Operations"
        ),
        create_question(
            "TEV-IT-A2-001-Q6",
            "Users _____ never share their Windows login passwords with anyone.",
            {"A": "must", "B": "must to", "C": "have", "D": "are"},
            "A",
            {
                "correct": "Modal 'must' is followed directly by bare verb 'share' ('must never share').",
                "wrong_B": "'must to' is ungrammatical.",
                "wrong_C": "'have' requires 'to'.",
                "wrong_D": "'are' is invalid."
            },
            "Never say *must to*. Always use 'must never share'.",
            "Cybersecurity, IAM & Zero Trust Architecture"
        ),
        create_question(
            "TEV-IT-A2-001-Q7",
            "The user _____ not remember their corporate VPN password.",
            {"A": "is", "B": "does", "C": "do", "D": "are"},
            "B",
            {
                "correct": "Singular subject 'The user' takes 'does not remember'.",
                "wrong_A": "'is not remember' is ungrammatical.",
                "wrong_C": "'do' is plural.",
                "wrong_D": "'are' is plural."
            },
            "Czech 'Uživatel si nepamatuje'. In English: 'does not remember'.",
            "ITIL Global Service Desk & Incident Escalation"
        ),
        create_question(
            "TEV-IT-A2-001-Q8",
            "Please plug the docking station power adapter _____ the wall outlet.",
            {"A": "into", "B": "to", "C": "on", "D": "under"},
            "A",
            {
                "correct": "'Plug into' is the fixed phrasal verb for electrical connectors entering an outlet.",
                "wrong_B": "'to' is incomplete for plugging into an outlet.",
                "wrong_C": "'on' means resting on top.",
                "wrong_D": "'under' means beneath."
            },
            "Czech 'zapojit do zásuvky'. In English: 'plug into the wall outlet'.",
            "IT Infrastructure & Cloud Operations"
        ),
        create_question(
            "TEV-IT-A2-001-Q9",
            "Both cloud server instances _____ currently running in the Azure North Europe region.",
            {"A": "is", "B": "are", "C": "has", "D": "have"},
            "B",
            {
                "correct": "Plural subject 'Both server instances' takes 'are'.",
                "wrong_A": "'is' is singular.",
                "wrong_C": "'has' is singular.",
                "wrong_D": "'have' cannot pair with '-ing' continuous without 'been'."
            },
            "Czech 'Oba servery běží'. Plural subject takes 'are running'.",
            "IT Infrastructure & Cloud Operations"
        ),
        create_question(
            "TEV-IT-A2-001-Q10",
            "Can you _____ me your employee ID number so I can unlock your account?",
            {"A": "gives", "B": "giving", "C": "give", "D": "to give"},
            "C",
            {
                "correct": "Modal question 'Can you' is followed by the bare infinitive 'give'.",
                "wrong_A": "Third person '-s' is invalid after modal 'can'.",
                "wrong_B": "'-ing' cannot follow modal 'can'.",
                "wrong_D": "'to' cannot follow modal 'can'."
            },
            "Czech 'Můžete mi dát...?'. Never say *Can you to give me*. Use 'Can you give me...?'.",
            "ITIL Global Service Desk & Incident Escalation"
        )
    ]
}

# Mapping of suite to data
ALL_SUITE_DATA = {
    "tatra-engineering": {
        "manifest": tatra_eng_manifest,
        "sample_test": tatra_eng_a2_001
    },
    "tatra-sales-engineering": {
        "manifest": tatra_sales_manifest,
        "sample_test": tatra_sales_a2_001
    },
    "teva-engineering": {
        "manifest": teva_eng_manifest,
        "sample_test": teva_eng_a2_001
    },
    "tapi-chemistry": {
        "manifest": tapi_chem_manifest,
        "sample_test": tapi_chem_a2_001
    },
    "teva-it": {
        "manifest": teva_it_manifest,
        "sample_test": teva_it_a2_001
    }
}

def generate_master_corporate_hub():
    """
    Generates the master portal index.html at root (c:/tmp/00-Mycat/index.html)
    giving direct visual access to all 5 independent corporate suites.
    """
    return """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Corporate English Testing Suites | Executive Master Hub</title>
  <style>
    :root {
      --navy-dark: #0b1528;
      --navy-slate: #1e293b;
      --text-main: #0f172a;
      --text-muted: #64748b;
      --bg: #f8fafc;
      --card-bg: #ffffff;
      --border: #e2e8f0;
      --shadow: 0 4px 6px -1px rgba(0,0,0,0.1), 0 2px 4px -2px rgba(0,0,0,0.1);
      --font: 'Inter', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
    }
    * { box-sizing: border-box; margin: 0; padding: 0; }
    body { font-family: var(--font); background: var(--bg); color: var(--text-main); line-height: 1.6; min-height: 100vh; display: flex; flex-direction: column; }
    
    .master-header {
      background: linear-gradient(135deg, #0b1528 0%, #1e293b 100%);
      color: #fff;
      padding: 30px 24px;
      border-bottom: 4px solid #38bdf8;
      box-shadow: var(--shadow);
    }
    .header-inner { max-width: 1200px; margin: 0 auto; }
    .master-header h1 { font-size: 2.2rem; font-weight: 800; letter-spacing: -0.02em; margin-bottom: 8px; }
    .master-header p { color: #94a3b8; font-size: 1.05rem; max-width: 820px; }

    .main-wrap { max-width: 1200px; margin: 36px auto; padding: 0 20px; flex: 1; width: 100%; }

    .a2-banner {
      background: #fefce8;
      border: 1px solid #fef08a;
      border-left: 6px solid #eab308;
      border-radius: 12px;
      padding: 20px 24px;
      margin-bottom: 32px;
      display: flex;
      gap: 16px;
      align-items: flex-start;
    }
    .a2-banner h3 { color: #854d0e; font-size: 1.15rem; margin-bottom: 4px; font-weight: 700; }
    .a2-banner p { color: #713f12; font-size: 0.95rem; }

    .suites-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
      gap: 24px;
      margin-bottom: 48px;
    }
    .suite-card {
      background: #fff;
      border: 1px solid var(--border);
      border-radius: 16px;
      padding: 30px;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      box-shadow: var(--shadow);
      position: relative;
      overflow: hidden;
      transition: all 0.25s ease;
    }
    .suite-card:hover {
      transform: translateY(-4px);
      box-shadow: 0 12px 24px -4px rgba(0,0,0,0.12);
    }
    .suite-top-bar { height: 6px; position: absolute; top: 0; left: 0; right: 0; }
    
    .suite-badge {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      font-size: 0.8rem;
      font-weight: 800;
      text-transform: uppercase;
      padding: 4px 10px;
      border-radius: 9999px;
      margin-bottom: 14px;
    }
    .suite-title { font-size: 1.45rem; font-weight: 800; color: var(--navy-dark); margin-bottom: 8px; }
    .suite-company { font-size: 0.88rem; font-weight: 700; color: var(--text-muted); margin-bottom: 12px; }
    .suite-desc { font-size: 0.93rem; color: #475569; margin-bottom: 20px; line-height: 1.55; }

    .tier-pills { display: flex; flex-wrap: wrap; gap: 6px; margin-bottom: 22px; }
    .tier-pill { font-size: 0.75rem; font-weight: 700; padding: 3px 8px; border-radius: 4px; }
    .pill-a2 { background: #fef08a; color: #854d0e; }
    .pill-b1 { background: #dbeafe; color: #1e40af; }
    .pill-b2 { background: #e0e7ff; color: #3730a3; }
    .pill-c2 { background: #fae8ff; color: #86198f; }
    .pill-sp { background: #fef3c7; color: #92400e; }

    .suite-launch-btn {
      display: inline-flex;
      align-items: center;
      justify-content: center;
      gap: 8px;
      padding: 12px 20px;
      border-radius: 8px;
      color: #fff;
      text-decoration: none;
      font-weight: 700;
      font-size: 0.95rem;
      transition: opacity 0.2s;
    }
    .suite-launch-btn:hover { opacity: 0.92; }

    .footer {
      background: #fff;
      border-top: 1px solid var(--border);
      padding: 24px 20px;
      text-align: center;
      color: var(--text-muted);
      font-size: 0.85rem;
    }
  </style>
</head>
<body>
  <header class="master-header">
    <div class="header-inner">
      <h1>Executive Corporate English Testing Hub</h1>
      <p>
        Standalone interactive English diagnostic suites customized for Czech automotive manufacturing, international technical sales, pharmaceutical facilities, chemical API synthesis, and global enterprise IT.
      </p>
    </div>
  </header>

  <div class="main-wrap">
    <div class="a2-banner">
      <span style="font-size: 1.8rem; line-height: 1;">🎓</span>
      <div>
        <h3>New Pedagogical Tier: CEFR A2 (Pre-Intermediate Foundation)</h3>
        <p>
          Designed specifically for adult Czech professionals who find B1 challenging. Every suite now features foundational A2 modules focusing on essential tools, basic shift reporting, simple past incidents, and workplace safety rules with minimal cognitive load and instant mother-tongue Czenglish contrastive feedback.
        </p>
      </div>
    </div>

    <div class="suites-grid">
      <!-- Suite 1: Tatra Engineering -->
      <article class="suite-card">
        <div class="suite-top-bar" style="background: #c51230;"></div>
        <div>
          <span class="suite-badge" style="background: #fee2e2; color: #991b1b;">🚛 Heavy Automotive R&D</span>
          <h2 class="suite-title">Tatra Engineering</h2>
          <div class="suite-company">TATRA TRUCKS a.s. | Kopřivnice</div>
          <p class="suite-desc">
            Central backbone tube chassis, swinging half-axles, V8/Paccar engines, air suspension, CAD/FEA simulation, and factory workshop assembly lines.
          </p>
          <div class="tier-pills">
            <span class="tier-pill pill-a2">Tier 0: A2 Foundation</span>
            <span class="tier-pill pill-b1">Tier 1: B1 Operational</span>
            <span class="tier-pill pill-b2">Tier 2: B2 Advanced</span>
            <span class="tier-pill pill-c2">Tier 3: C2 Mastery</span>
            <span class="tier-pill pill-sp">Specialized Jargon</span>
          </div>
        </div>
        <a href="tatra-engineering/index.html" class="suite-launch-btn" style="background: #c51230;">
          Launch Tatra Engineering Suite →
        </a>
      </article>

      <!-- Suite 2: Tatra Sales and Engineering -->
      <article class="suite-card">
        <div class="suite-top-bar" style="background: #990011;"></div>
        <div>
          <span class="suite-badge" style="background: #ffedd5; color: #9a3412;">🤝 Defense Tenders & Export</span>
          <h2 class="suite-title">Tatra Sales and Engineering</h2>
          <div class="suite-company">TATRA TRUCKS a.s. | International Sales</div>
          <p class="suite-desc">
            NATO STANAG defense bids, Incoterms 2020 export logistics, technical customer vehicle handover, commercial contract disputes, and international dealer management.
          </p>
          <div class="tier-pills">
            <span class="tier-pill pill-a2">Tier 0: A2 Foundation</span>
            <span class="tier-pill pill-b1">Tier 1: B1 Operational</span>
            <span class="tier-pill pill-b2">Tier 2: B2 Advanced</span>
            <span class="tier-pill pill-c2">Tier 3: C2 Mastery</span>
            <span class="tier-pill pill-sp">Negotiation Idioms</span>
          </div>
        </div>
        <a href="tatra-sales-engineering/index.html" class="suite-launch-btn" style="background: #990011;">
          Launch Sales & Engineering Suite →
        </a>
      </article>

      <!-- Suite 3: Teva Engineering -->
      <article class="suite-card">
        <div class="suite-top-bar" style="background: #0050aa;"></div>
        <div>
          <span class="suite-badge" style="background: #e0f2fe; color: #0369a1;">💊 Pharma Process & Automation</span>
          <h2 class="suite-title">Teva Engineering</h2>
          <div class="suite-company">TEVA PHARMACEUTICALS | Plant Facilities & Validation</div>
          <p class="suite-desc">
            Cleanroom HVAC pressure cascades, sterile filling lines, SCADA/PLC automation, tablet compression presses, lyophilization, and GAMP 5 CSV validation.
          </p>
          <div class="tier-pills">
            <span class="tier-pill pill-a2">Tier 0: A2 Foundation</span>
            <span class="tier-pill pill-b1">Tier 1: B1 Operational</span>
            <span class="tier-pill pill-b2">Tier 2: B2 Advanced</span>
            <span class="tier-pill pill-c2">Tier 3: C2 Mastery</span>
            <span class="tier-pill pill-sp">GxP & CSV Jargon</span>
          </div>
        </div>
        <a href="teva-engineering/index.html" class="suite-launch-btn" style="background: #0050aa;">
          Launch Teva Engineering Suite →
        </a>
      </article>

      <!-- Suite 4: Tapi Chemistry -->
      <article class="suite-card">
        <div class="suite-top-bar" style="background: #059669;"></div>
        <div>
          <span class="suite-badge" style="background: #d1fae5; color: #065f46;">🧪 API Chemical Synthesis & QC</span>
          <h2 class="suite-title">Tapi Chemistry</h2>
          <div class="suite-company">TAPI (Teva Active Pharmaceutical Ingredients)</div>
          <p class="suite-desc">
            Organic chemical batch synthesis, HPLC/GC chromatography, spectroscopy, hazardous reagents under fume hoods, solvent recovery, and Ph. Eur./USP pharmacopeial standards.
          </p>
          <div class="tier-pills">
            <span class="tier-pill pill-a2">Tier 0: A2 Foundation</span>
            <span class="tier-pill pill-b1">Tier 1: B1 Operational</span>
            <span class="tier-pill pill-b2">Tier 2: B2 Advanced</span>
            <span class="tier-pill pill-c2">Tier 3: C2 Mastery</span>
            <span class="tier-pill pill-sp">Chemical False Friends</span>
          </div>
        </div>
        <a href="tapi-chemistry/index.html" class="suite-launch-btn" style="background: #059669;">
          Launch Tapi Chemistry Suite →
        </a>
      </article>

      <!-- Suite 5: Teva IT -->
      <article class="suite-card">
        <div class="suite-top-bar" style="background: #4338ca;"></div>
        <div>
          <span class="suite-badge" style="background: #ede9fe; color: #5b21b6;">💻 Cloud, DevOps & Cybersecurity</span>
          <h2 class="suite-title">Teva IT</h2>
          <div class="suite-company">TEVA PHARMACEUTICALS | Global Digital & IT</div>
          <p class="suite-desc">
            AWS/Azure cloud infrastructure, Docker/Kubernetes, Zero Trust cybersecurity, IAM, ITIL service desk P1 incident response, and SAP S/4HANA enterprise integration.
          </p>
          <div class="tier-pills">
            <span class="tier-pill pill-a2">Tier 0: A2 Foundation</span>
            <span class="tier-pill pill-b1">Tier 1: B1 Operational</span>
            <span class="tier-pill pill-b2">Tier 2: B2 Advanced</span>
            <span class="tier-pill pill-c2">Tier 3: C2 Mastery</span>
            <span class="tier-pill pill-sp">Agile & Cloud Jargon</span>
          </div>
        </div>
        <a href="teva-it/index.html" class="suite-launch-btn" style="background: #4338ca;">
          Launch Teva IT Suite →
        </a>
      </article>
    </div>
  </div>

  <footer class="footer">
    <p><strong>Corporate English Assessment Ecosystem</strong> | Czech Adult Professional Pair-Programming Architecture</p>
    <p style="margin-top: 4px; font-size: 0.8rem;">Completely Separated Modular Environments | Integrated NotebookLM Exporter Engine</p>
  </footer>
</body>
</html>
"""

def generate_roadmap_md(suite_key, conf, manifest):
    a2_items = [m for m in manifest if m['level'] == 'A2']
    b1_items = [m for m in manifest if m['level'] == 'B1']
    b2_items = [m for m in manifest if m['level'] == 'B2']
    sp_items = [m for m in manifest if m['category'] == 'specialized']

    md = f"""# {conf['name']}: Master Curriculum Roadmap

## 1. Executive Overview & Audience
- **Organization:** {conf['company']}
- **Department/Division:** {conf['division']}
- **Target Audience:** {conf['prompt_context']}
- **CEFR Proficiency Coverage:** **A2 (Pre-Intermediate Foundation)**, **B1 (Intermediate Operational)**, **B2 (Upper-Intermediate Advanced)**, and **Specialized Units**.

---

## 2. Pedagogical Rationale for Tier 0 (CEFR A2 Foundation)
To accommodate learners who find B1 challenging, the **A2 Foundation Tier** provides:
1. **Zero Cognitive Overload:** Short, direct technical prompts focusing on concrete workplace objects, tools, and immediate physical actions.
2. **Foundational Syntax Mastery:**
   - Present Simple habits and third person singular agreement (*he checks*, *the pump operates*).
   - Past Simple regular *-ed* and essential irregular verbs (*broke*, *stopped*, *replaced*, *lost*, *cut*).
   - Basic modals (*can / can't* for capability, *must / do not* for safety).
   - Prepositions of place (*under*, *inside*, *on*, *between*, *next to*).
3. **Czenglish Elimination at the Root:** Removing subject pronoun omissions (*"Is working"* $\\rightarrow$ *"It is working"*), word order inversions in basic questions, and confusion between *have* and *be*.

---

## 3. Curriculum Syllabus Index ({len(manifest)} Modules)

### Tier 0: CEFR A2 Foundation Modules ({len(a2_items)} Items)
"""
    for m in a2_items:
        md += f"- **{m['test_id']}:** {m['title']} *(Track: {m['workplace_track']})*\n"

    md += f"\n### Tier 1: CEFR B1 Operational Modules ({len(b1_items)} Items)\n"
    for m in b1_items:
        md += f"- **{m['test_id']}:** {m['title']} *(Track: {m['workplace_track']})*\n"

    md += f"\n### Tier 2: CEFR B2 Advanced Modules ({len(b2_items)} Items)\n"
    for m in b2_items:
        md += f"- **{m['test_id']}:** {m['title']} *(Track: {m['workplace_track']})*\n"

    md += f"\n### Tier 3: Specialized Units ({len(sp_items)} Items)\n"
    for m in sp_items:
        md += f"- **{m['test_id']}:** {m['title']} *(Track: {m['workplace_track']})*\n"

    md += f"""\n---\n\n## 4. Google NotebookLM Integration
Every module includes a one-click **NotebookLM Export** feature generating a Markdown digest of missed items with a custom audio debrief prompt:
> *"Act as two senior technology training hosts debriefing Czech professionals from {conf['company']} on this module. Discuss the common English grammatical mistakes made by Czech native speakers, explain why these errors occur, and model how to express these concepts with precision in authentic workplace scenarios."*
"""
    return md

def build_all():
    print("Building 5 Independent Testing Suites...")

    # 1. Master Hub
    master_hub_path = ROOT / "index.html"
    with open(master_hub_path, "w", encoding="utf-8") as f:
        f.write(generate_master_corporate_hub())
    print(f"  [OK] Master Hub generated at {master_hub_path.name}")

    with open(ROOT / "Launch_Master_Hub.bat", "w", encoding="utf-8") as f:
        f.write('@echo off\r\necho Launching Master Corporate English Hub in your default browser...\r\nstart "" "index.html"\r\n')

    with open(ROOT / "Start_Local_Server.bat", "w", encoding="utf-8") as f:
        f.write('@echo off\r\necho Starting Local HTTP Server on port 8088...\r\nstart "" "http://localhost:8088/index.html"\r\npython -m http.server 8088\r\n')

    # 2. Build each suite
    for suite_key, conf in SUITES.items():
        suite_dir = ROOT / suite_key
        suite_data = ALL_SUITE_DATA[suite_key]
        manifest = suite_data["manifest"]
        sample_test = suite_data["sample_test"]

        # Ensure directories
        (suite_dir / "schema").mkdir(parents=True, exist_ok=True)
        (suite_dir / "engine").mkdir(parents=True, exist_ok=True)
        (suite_dir / "data" / "tests").mkdir(parents=True, exist_ok=True)
        (suite_dir / "scripts").mkdir(parents=True, exist_ok=True)

        # schema/test_schema.json
        with open(suite_dir / "schema" / "test_schema.json", "w", encoding="utf-8") as f:
            json.dump(generate_schema(suite_key, conf), f, indent=2, ensure_ascii=False)

        # engine/styles.css
        with open(suite_dir / "engine" / "styles.css", "w", encoding="utf-8") as f:
            f.write(generate_css(conf))

        # engine/app.js
        with open(suite_dir / "engine" / "app.js", "w", encoding="utf-8") as f:
            f.write(generate_app_js(suite_key, conf))

        # test_runner.html
        with open(suite_dir / "test_runner.html", "w", encoding="utf-8") as f:
            f.write(generate_runner_html(suite_key, conf))

        # index.html
        with open(suite_dir / "index.html", "w", encoding="utf-8") as f:
            f.write(generate_index_html(suite_key, conf))

        # data/curriculum_manifest.json
        with open(suite_dir / "data" / "curriculum_manifest.json", "w", encoding="utf-8") as f:
            json.dump(manifest, f, indent=2, ensure_ascii=False)

        # data/manifest.js (Offline direct load without CORS)
        with open(suite_dir / "data" / "manifest.js", "w", encoding="utf-8") as f:
            f.write(f"window.CURRICULUM_MANIFEST = {json.dumps(manifest, indent=2, ensure_ascii=False)};\n")

        # sample test in data/tests/
        test_file_path = suite_dir / "data" / "tests" / f"{sample_test['test_id']}.json"
        with open(test_file_path, "w", encoding="utf-8") as f:
            json.dump(sample_test, f, indent=2, ensure_ascii=False)

        # data/tests_registry.js (Offline direct load without CORS)
        tests_in_suite = {}
        for tf in (suite_dir / "data" / "tests").glob("*.json"):
            try:
                with open(tf, "r", encoding="utf-8") as f:
                    t_obj = json.load(f)
                    tests_in_suite[t_obj["test_id"]] = t_obj
            except Exception:
                pass
        tests_in_suite[sample_test["test_id"]] = sample_test

        with open(suite_dir / "data" / "tests_registry.js", "w", encoding="utf-8") as f:
            f.write(f"window.TEST_REGISTRY = window.TEST_REGISTRY || {{}};\nObject.assign(window.TEST_REGISTRY, {json.dumps(tests_in_suite, indent=2, ensure_ascii=False)});\n")

        # Launch_Suite.bat (1-click Windows launcher)
        with open(suite_dir / "Launch_Suite.bat", "w", encoding="utf-8") as f:
            f.write(f'@echo off\r\necho Launching {conf["name"]} in default web browser...\r\nstart "" "index.html"\r\n')

        # scripts/validate_tests.py
        with open(suite_dir / "scripts" / "validate_tests.py", "w", encoding="utf-8") as f:
            f.write(generate_validator_py(suite_key, conf))

        # CURRICULUM_ROADMAP.md
        with open(suite_dir / "CURRICULUM_ROADMAP.md", "w", encoding="utf-8") as f:
            f.write(generate_roadmap_md(suite_key, conf, manifest))

        # README.md
        with open(suite_dir / "README.md", "w", encoding="utf-8") as f:
            f.write(f"# {conf['name']} English Testing Suite\n\nIndependent, production-ready assessment environment for **{conf['company']}** ({conf['division']}).\n\nStart local server and open `index.html`.")

        print(f"  [OK] Suite '{suite_key}' ({conf['name']}) generated with A2 tier and balanced answer keys.")

    print("\nAll 5 suites successfully generated!")

if __name__ == "__main__":
    build_all()
