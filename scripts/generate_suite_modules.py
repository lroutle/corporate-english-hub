#!/usr/bin/env python3
"""
Tatra Trucks Interactive English Testing Suite - Multi-Module Content Builder
Generates high-fidelity, production-grade test modules strictly compliant with schema/test_schema.json.
"""

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
TESTS_DIR = BASE_DIR / "data" / "tests"
TESTS_DIR.mkdir(parents=True, exist_ok=True)

modules_data = [
    # -------------------------------------------------------------------------
    # TTR-B1-003: Shift Handover & Daily Line Routines
    # -------------------------------------------------------------------------
    {
        "test_id": "TTR-B1-003",
        "title": "Shift Handover & Daily Line Routines: Present Simple vs Continuous",
        "level": "B1",
        "category": "core",
        "workplace_track": "Quality Assurance & Assembly",
        "estimated_time_minutes": 12,
        "description": "Distinguish permanent shop floor standard operating procedures from temporary deviations and ongoing maintenance tasks during shift handovers.",
        "learning_objectives": [
            "Use Present Simple for habitual assembly routines and factory procedures",
            "Use Present Continuous for current line stoppages, temporary repairs, and active tasks",
            "Avoid Czech aspectual confusion during oral and written shift briefings"
        ],
        "questions": [
            {
                "id": "TTR-B1-003-Q1",
                "prompt": "Normally, our shift _____ the central backbone tube flanges at station 3, but today we _____ station 4 while the torque sensor is being calibrated.",
                "options": [
                    {"key": "A", "text": "assembles / are using"},
                    {"key": "B", "text": "is assembling / use"},
                    {"key": "C", "text": "assemble / are used"},
                    {"key": "D", "text": "assembles / use"}
                ],
                "correct_key": "A",
                "explanations": {
                    "correct": "Present Simple ('assembles') describes the permanent daily routine; Present Continuous ('are using') expresses the temporary arrangement 'today'.",
                    "wrong_B": "Inverts the tenses: continuous cannot express general routine signaled by 'normally'.",
                    "wrong_C": "Subject 'our shift' is singular ('assembles'), and 'are used' is passive.",
                    "wrong_D": "Both in simple present fails to capture the temporary nature of 'today'."
                },
                "cz_learning_point": "Czech uses present tense for both ('normálně montuje... ale dnes používáme'). In English, temporary activities require Present Continuous.",
                "workplace_track": "Quality Assurance & Assembly"
            },
            {
                "id": "TTR-B1-003-Q2",
                "prompt": "Listen! The pneumatic pump on line 2 _____ an unusual rattling noise right now.",
                "options": [
                    {"key": "A", "text": "is making"},
                    {"key": "B", "text": "makes"},
                    {"key": "C", "text": "is make"},
                    {"key": "D", "text": "make"}
                ],
                "correct_key": "A",
                "explanations": {
                    "correct": "'Listen!' and 'right now' indicate an action occurring at the exact moment of speaking, requiring Present Continuous ('is making').",
                    "wrong_B": "Present Simple would suggest the pump routinely rattles, rather than an immediate diagnostic concern.",
                    "wrong_C": "Missing '-ing' suffix in present continuous.",
                    "wrong_D": "Plural verb form with singular subject 'pump'."
                },
                "cz_learning_point": "Sensory imperatives like 'Listen!' or 'Look!' always signal Present Continuous in English.",
                "workplace_track": "Quality Assurance & Assembly"
            },
            {
                "id": "TTR-B1-003-Q3",
                "prompt": "Every morning at 06:15, the shift supervisor _____ the digital production board to confirm delivery targets.",
                "options": [
                    {"key": "A", "text": "reviews"},
                    {"key": "B", "text": "is reviewing"},
                    {"key": "C", "text": "review"},
                    {"key": "D", "text": "has review"}
                ],
                "correct_key": "A",
                "explanations": {
                    "correct": "'Every morning at 06:15' specifies a habitual routine, demanding Present Simple 3rd person ('reviews').",
                    "wrong_B": "Present continuous is incorrect for recurring scheduled habits.",
                    "wrong_C": "Missing 3rd person singular '-s' ending.",
                    "wrong_D": "Ungrammatical verbal form."
                },
                "cz_learning_point": "Recurring time adverbs like 'every morning' or 'regularly' require Present Simple.",
                "workplace_track": "Quality Assurance & Assembly"
            },
            {
                "id": "TTR-B1-003-Q4",
                "prompt": "The lead technician cannot take your call because he _____ the final brake bleeder check on cab 14.",
                "options": [
                    {"key": "A", "text": "is currently performing"},
                    {"key": "B", "text": "performs currently"},
                    {"key": "C", "text": "is perform"},
                    {"key": "D", "text": "currently perform"}
                ],
                "correct_key": "A",
                "explanations": {
                    "correct": "Action in progress preventing another action requires Present Continuous ('is currently performing').",
                    "wrong_B": "Present simple cannot explain what is actively blocking the phone call.",
                    "wrong_C": "Missing participle ending '-ing'.",
                    "wrong_D": "Subject-verb agreement error with singular 'he'."
                },
                "cz_learning_point": "Czech uses 'právě provádí' in present tense. English requires 'is + verb-ing'.",
                "workplace_track": "Quality Assurance & Assembly"
            },
            {
                "id": "TTR-B1-003-Q5",
                "prompt": "Why _____ safety goggles while handling pressurized hydraulic fluids at this bench?",
                "options": [
                    {"key": "A", "text": "aren't you wearing"},
                    {"key": "B", "text": "don't you wearing"},
                    {"key": "C", "text": "aren't you wear"},
                    {"key": "D", "text": "you aren't wearing"}
                ],
                "correct_key": "A",
                "explanations": {
                    "correct": "Present Continuous question for immediate safety non-compliance happening now: 'aren't you wearing'.",
                    "wrong_B": "Auxiliary 'don't' cannot pair with '-ing' participle.",
                    "wrong_C": "'aren't you' requires '-ing' participle, not base form.",
                    "wrong_D": "Direct question requires inversion of auxiliary and subject."
                },
                "cz_learning_point": "In Czech, 'Proč nemáš brýle?' is simple present. In English, active wearing of clothes at this moment takes continuous form.",
                "workplace_track": "Quality Assurance & Assembly"
            },
            {
                "id": "TTR-B1-003-Q6",
                "prompt": "Tatra Trucks _____ its heavy-duty tactical vehicles under extreme temperature conditions from -40°C to +55°C.",
                "options": [
                    {"key": "A", "text": "operates and tests"},
                    {"key": "B", "text": "is operating and testing"},
                    {"key": "C", "text": "operate and test"},
                    {"key": "D", "text": "are operating and testing"}
                ],
                "correct_key": "A",
                "explanations": {
                    "correct": "A permanent technical capability and company fact takes Present Simple ('operates and tests').",
                    "wrong_B": "Continuous would suggest a temporary test rather than an enduring engineering standard.",
                    "wrong_C": "Missing 3rd person singular agreement for corporate entity.",
                    "wrong_D": "Plural auxiliary with singular corporate subject."
                },
                "cz_learning_point": "General scientific and technical capabilities are expressed in Present Simple.",
                "workplace_track": "Quality Assurance & Assembly"
            },
            {
                "id": "TTR-B1-003-Q7",
                "prompt": "At present, the paint shop _____ a high-solids polyurethane primer to improve salt-spray corrosion resistance.",
                "options": [
                    {"key": "A", "text": "is trialing"},
                    {"key": "B", "text": "trials"},
                    {"key": "C", "text": "trial"},
                    {"key": "D", "text": "has trial"}
                ],
                "correct_key": "A",
                "explanations": {
                    "correct": "'At present' indicates a current, temporary trial in progress, requiring Present Continuous ('is trialing').",
                    "wrong_B": "Present simple would indicate permanent routine, not a temporary trial.",
                    "wrong_C": "Agreement error.",
                    "wrong_D": "Malformed verb form."
                },
                "cz_learning_point": "Phrases like 'at present' or 'currently' strongly indicate temporary processes in Present Continuous.",
                "workplace_track": "Quality Assurance & Assembly"
            },
            {
                "id": "TTR-B1-003-Q8",
                "prompt": "The automated laser cutting machine _____ an oil change every 500 operating hours according to the service manual.",
                "options": [
                    {"key": "A", "text": "requires"},
                    {"key": "B", "text": "is requiring"},
                    {"key": "C", "text": "require"},
                    {"key": "D", "text": "requiring"}
                ],
                "correct_key": "A",
                "explanations": {
                    "correct": "Stative verb 'require' expressing a technical manual requirement cannot be used in the continuous form; use Present Simple ('requires').",
                    "wrong_B": "'Require' is a stative verb and is not used in continuous aspect.",
                    "wrong_C": "Subject-verb agreement error with singular subject 'machine'.",
                    "wrong_D": "Participle alone cannot act as the main verb."
                },
                "cz_learning_point": "Stative verbs (require, contain, consist of, belong, know) never take continuous aspect in English technical writing.",
                "workplace_track": "Quality Assurance & Assembly"
            },
            {
                "id": "TTR-B1-003-Q9",
                "prompt": "During the afternoon shift, team members _____ safety checklists before shutting down their power tools.",
                "options": [
                    {"key": "A", "text": "always complete"},
                    {"key": "B", "text": "are always completing"},
                    {"key": "C", "text": "always completes"},
                    {"key": "D", "text": "complete always"}
                ],
                "correct_key": "A",
                "explanations": {
                    "correct": "Adverb of frequency 'always' precedes the main verb in Present Simple ('always complete') for routine standard procedure.",
                    "wrong_B": "'Are always completing' would express irritation or an annoying habit rather than standard procedure.",
                    "wrong_C": "Plural subject 'team members' takes plural verb 'complete', not 'completes'.",
                    "wrong_D": "Word order error: frequency adverb goes before the main verb."
                },
                "cz_learning_point": "In English, standard adverbs of frequency (always, often, usually) are placed immediately before the main verb.",
                "workplace_track": "Quality Assurance & Assembly"
            },
            {
                "id": "TTR-B1-003-Q10",
                "prompt": "What _____ on the dynamometer test bench over there? Is that the new Euro 7 engine prototype?",
                "options": [
                    {"key": "A", "text": "are they testing"},
                    {"key": "B", "text": "do they test"},
                    {"key": "C", "text": "are they test"},
                    {"key": "D", "text": "they are testing"}
                ],
                "correct_key": "A",
                "explanations": {
                    "correct": "Observing an action occurring at this instant over there requires Present Continuous question form ('are they testing').",
                    "wrong_B": "Present simple asks about routine testing policy, not what is mounted on the dyno right now.",
                    "wrong_C": "Missing '-ing' in continuous verb phrase.",
                    "wrong_D": "Question requires inverted word order."
                },
                "cz_learning_point": "Czech 'Co tam testují?' is identical in aspect. In English, active observation requires Present Continuous.",
                "workplace_track": "Quality Assurance & Assembly"
            }
        ]
    },

    # -------------------------------------------------------------------------
    # TTR-B1-005: Factory Safety Directives & ISO Standards: Modals of Obligation
    # -------------------------------------------------------------------------
    {
        "test_id": "TTR-B1-005",
        "title": "Factory Safety Directives & ISO Standards: Modals of Obligation",
        "level": "B1",
        "category": "core",
        "workplace_track": "Quality Assurance & Assembly",
        "estimated_time_minutes": 12,
        "description": "Apply must, have to, must not, and don't have to accurately in workshop PPE regulations, hazardous material protocols, and ISO 9001/45001 compliance.",
        "learning_objectives": [
            "Differentiate external obligation ('have to') from speaker authority ('must')",
            "Distinguish absolute prohibition ('must not') from absence of obligation ('don't have to')",
            "Avoid critical Czenglish safety rule misinterpretations"
        ],
        "questions": [
            {
                "id": "TTR-B1-005-Q1",
                "prompt": "Under Tatra plant safety regulations, all shop floor visitors _____ steel-toe safety boots at all times.",
                "options": [
                    {"key": "A", "text": "have to wear"},
                    {"key": "B", "text": "must to wear"},
                    {"key": "C", "text": "don't have to wear"},
                    {"key": "D", "text": "are wearing"}
                ],
                "correct_key": "A",
                "explanations": {
                    "correct": "'Have to wear' (or 'must wear') expresses mandatory institutional obligation imposed by external regulations.",
                    "wrong_B": "Modal verb 'must' is followed directly by base form, never by 'to' infinitive ('must to wear' is ungrammatical).",
                    "wrong_C": "'Don't have to' means it is optional, which violates safety rules.",
                    "wrong_D": "Present continuous does not express a regulatory obligation."
                },
                "cz_learning_point": "Never add 'to' after 'must' (*must to wear* is an extremely common Czenglish slip). Use 'must wear' or 'have to wear'.",
                "workplace_track": "Quality Assurance & Assembly"
            },
            {
                "id": "TTR-B1-005-Q2",
                "prompt": "You _____ touch the high-voltage battery disconnect switch on the hybrid prototype without certified insulated gloves!",
                "options": [
                    {"key": "A", "text": "must not"},
                    {"key": "B", "text": "don't have to"},
                    {"key": "C", "text": "haven't to"},
                    {"key": "D", "text": "needn't"}
                ],
                "correct_key": "A",
                "explanations": {
                    "correct": "'Must not' expresses strict, life-critical prohibition (Czech 'nesmíš').",
                    "wrong_B": "'Don't have to' means lack of necessity (nemusíš), meaning you can if you want—a fatal misunderstanding in high-voltage safety!",
                    "wrong_C": "'Haven't to' is an invalid English modal auxiliary.",
                    "wrong_D": "'Needn't' means lack of necessity, not strict prohibition."
                },
                "cz_learning_point": "Czech 'nemusíš' = 'don't have to / needn't', while 'nesmíš' = 'must not'. Confusing these two in safety contexts can cause severe accidents.",
                "workplace_track": "Quality Assurance & Assembly"
            },
            {
                "id": "TTR-B1-005-Q3",
                "prompt": "Line technicians _____ manually log torque values on paper anymore, because the smart wrenches upload data via Wi-Fi automatically.",
                "options": [
                    {"key": "A", "text": "don't have to"},
                    {"key": "B", "text": "must not"},
                    {"key": "C", "text": "can't"},
                    {"key": "D", "text": "should not"}
                ],
                "correct_key": "A",
                "explanations": {
                    "correct": "'Don't have to' expresses that the task is no longer necessary (absence of obligation).",
                    "wrong_B": "'Must not' means it is forbidden, whereas it is simply automated and unnecessary.",
                    "wrong_C": "'Can't' implies lack of physical ability.",
                    "wrong_D": "'Should not' expresses negative moral or advisory recommendation."
                },
                "cz_learning_point": "Czech 'nemusí' is correctly rendered as 'don't have to' or 'don't need to'.",
                "workplace_track": "Quality Assurance & Assembly"
            },
            {
                "id": "TTR-B1-005-Q4",
                "prompt": "Before dispatching the vehicle for rail shipment, the export team _____ obtain a certified phytosanitary clearance for wooden shipping cradles.",
                "options": [
                    {"key": "A", "text": "has to"},
                    {"key": "B", "text": "must to"},
                    {"key": "C", "text": "should to"},
                    {"key": "D", "text": "is having"}
                ],
                "correct_key": "A",
                "explanations": {
                    "correct": "'Has to' reflects 3rd person singular agreement with 'team' expressing mandatory export law requirement.",
                    "wrong_B": "'Must to' is ungrammatical; modals take bare infinitive.",
                    "wrong_C": "'Should' cannot be followed by 'to'.",
                    "wrong_D": "'Is having' does not express modal obligation."
                },
                "cz_learning_point": "Modals like 'must' and 'should' never take 'to' (*must to*, *should to* are incorrect).",
                "workplace_track": "Quality Assurance & Assembly"
            },
            {
                "id": "TTR-B1-005-Q5",
                "prompt": "Because the assembly line suffered a breakdown yesterday, the chassis department _____ work an extra weekend shift.",
                "options": [
                    {"key": "A", "text": "had to"},
                    {"key": "B", "text": "musted"},
                    {"key": "C", "text": "has had to"},
                    {"key": "D", "text": "must"}
                ],
                "correct_key": "A",
                "explanations": {
                    "correct": "The past tense of modal obligation ('must / have to') is always 'had to'.",
                    "wrong_B": "'Musted' does not exist; 'must' has no past tense form.",
                    "wrong_C": "Present perfect does not match the past temporal marker 'yesterday'.",
                    "wrong_D": "'Must' cannot be used for past completed obligations."
                },
                "cz_learning_point": "Czech uses past tense of 'muset' ('museli jsme'). In English, the past tense of 'must' is always 'had to'.",
                "workplace_track": "Quality Assurance & Assembly"
            },
            {
                "id": "TTR-B1-005-Q6",
                "prompt": "Operators _____ operate the 50-ton overhead gantry crane unless they hold an active certification badge.",
                "options": [
                    {"key": "A", "text": "are not permitted to"},
                    {"key": "B", "text": "don't have to"},
                    {"key": "C", "text": "need not"},
                    {"key": "D", "text": "should not to"}
                ],
                "correct_key": "A",
                "explanations": {
                    "correct": "'Are not permitted to' (or 'must not') expresses formal safety prohibition without authorization.",
                    "wrong_B": "'Don't have to' would make certification optional, which is unsafe and illegal.",
                    "wrong_C": "'Need not' means it is unnecessary.",
                    "wrong_D": "'Should not to' is grammatically incorrect."
                },
                "cz_learning_point": "In safety directives, 'není povoleno' is formally rendered as 'are not permitted to' or 'are strictly prohibited from'.",
                "workplace_track": "Quality Assurance & Assembly"
            },
            {
                "id": "TTR-B1-005-Q7",
                "prompt": "Does the welding team _____ submit an 8D non-conformity report for minor cosmetic spatter?",
                "options": [
                    {"key": "A", "text": "have to"},
                    {"key": "B", "text": "must"},
                    {"key": "C", "text": "ought"},
                    {"key": "D", "text": "needs"}
                ],
                "correct_key": "A",
                "explanations": {
                    "correct": "Questions with auxiliary 'Do / Does' require 'have to' for obligation ('Does the team have to submit...?').",
                    "wrong_B": "'Must' does not form questions with 'Does' (*Does the team must...?* is ungrammatical).",
                    "wrong_C": "'Ought' requires 'to', but is not used with 'Does'.",
                    "wrong_D": "Auxiliary 'Does' already carries 3rd person '-s', so base form 'need to' or 'have to' is required."
                },
                "cz_learning_point": "You cannot ask '*Must the team...*' in standard workplace English; always ask 'Does the team have to...?'",
                "workplace_track": "Quality Assurance & Assembly"
            },
            {
                "id": "TTR-B1-005-Q8",
                "prompt": "During emergency fire drills, all workshop personnel _____ evacuate immediately via marked exit corridors.",
                "options": [
                    {"key": "A", "text": "must"},
                    {"key": "B", "text": "ought"},
                    {"key": "C", "text": "might"},
                    {"key": "D", "text": "can"}
                ],
                "correct_key": "A",
                "explanations": {
                    "correct": "'Must' conveys urgent, non-negotiable imperative directly from emergency safety protocols.",
                    "wrong_B": "'Ought' requires 'to'.",
                    "wrong_C": "'Might' denotes weak possibility.",
                    "wrong_D": "'Can' expresses optional capability, not an emergency evacuation mandate."
                },
                "cz_learning_point": "Emergency notices use 'must' + bare infinitive to signal non-negotiable compliance.",
                "workplace_track": "Quality Assurance & Assembly"
            },
            {
                "id": "TTR-B1-005-Q9",
                "prompt": "You _____ clean the test cell floors today; the industrial sanitation contractor handles that on Friday evenings.",
                "options": [
                    {"key": "A", "text": "needn't"},
                    {"key": "B", "text": "must not"},
                    {"key": "C", "text": "can't"},
                    {"key": "D", "text": "aren't"}
                ],
                "correct_key": "A",
                "explanations": {
                    "correct": "'Needn't' (or 'don't need to') indicates that the task is unnecessary.",
                    "wrong_B": "'Must not' implies that cleaning the floor is strictly forbidden.",
                    "wrong_C": "'Can't' denotes inability.",
                    "wrong_D": "'Aren't' cannot stand alone before a base verb."
                },
                "cz_learning_point": "Czech 'nemusíš' = 'needn't' or 'don't have to'. Avoid using 'must not' when you simply mean 'it is not necessary'.",
                "workplace_track": "Quality Assurance & Assembly"
            },
            {
                "id": "TTR-B1-005-Q10",
                "prompt": "According to IATF 16949 standards, all measuring equipment _____ recalibrated at least once every twelve months.",
                "options": [
                    {"key": "A", "text": "must be"},
                    {"key": "B", "text": "has to"},
                    {"key": "C", "text": "must to be"},
                    {"key": "D", "text": "should be to"}
                ],
                "correct_key": "A",
                "explanations": {
                    "correct": "'Must be recalibrated' combines modal obligation with passive voice for equipment.",
                    "wrong_B": "'Has to' lacks the passive auxiliary 'be'.",
                    "wrong_C": "'Must to be' is grammatically incorrect.",
                    "wrong_D": "'Should be to' is ungrammatical."
                },
                "cz_learning_point": "In quality certifications, components require passive modal constructions ('must be inspected / must be recalibrated').",
                "workplace_track": "Quality Assurance & Assembly"
            }
        ]
    },

    # -------------------------------------------------------------------------
    # TTR-B1-018: Incoterms & Export Contracts: Zero & First Conditionals
    # -------------------------------------------------------------------------
    {
        "test_id": "TTR-B1-018",
        "title": "Incoterms & Export Contracts: Zero & First Conditionals",
        "level": "B1",
        "category": "core",
        "workplace_track": "International Sales & Tenders",
        "estimated_time_minutes": 14,
        "description": "Determine insurance liability, FOB vs CIF terms, and risk transitions when quoting vehicle prices to overseas buyers using conditional structures.",
        "learning_objectives": [
            "Use Zero Conditional for established trade rules and legal consequences",
            "Use First Conditional for commercial negotiations, volume discounts, and payment terms",
            "Avoid using 'will' in conditional time and if-clauses"
        ],
        "questions": [
            {
                "id": "TTR-B1-018-Q1",
                "prompt": "If an overseas buyer _____ vehicles under EXW (Ex Works) terms, the buyer _____ all transport costs and risks from our Kopřivnice factory gates.",
                "options": [
                    {"key": "A", "text": "purchases / assumes"},
                    {"key": "B", "text": "will purchase / assumes"},
                    {"key": "C", "text": "purchases / will assume"},
                    {"key": "D", "text": "purchased / assumes"}
                ],
                "correct_key": "A",
                "explanations": {
                    "correct": "Zero Conditional (If + Present Simple, Present Simple) expresses universal trade definitions and contractual rules.",
                    "wrong_B": "'Will' is forbidden inside conditional clauses.",
                    "wrong_C": "First conditional can express a single transaction, but general trade rules are best defined by Zero Conditional.",
                    "wrong_D": "Past simple in condition clashes with present rule."
                },
                "cz_learning_point": "For permanent commercial definitions (Incoterms), use Zero Conditional: If + Present Simple, Present Simple.",
                "workplace_track": "International Sales & Tenders"
            },
            {
                "id": "TTR-B1-018-Q2",
                "prompt": "If the mining conglomerate _____ twenty Tatra Phoenix tippers by Friday, we _____ a 5% fleet concession.",
                "options": [
                    {"key": "A", "text": "orders / will provide"},
                    {"key": "B", "text": "will order / will provide"},
                    {"key": "C", "text": "orders / provide"},
                    {"key": "D", "text": "ordered / will provide"}
                ],
                "correct_key": "A",
                "explanations": {
                    "correct": "First Conditional (If + Present Simple, will + base form) is standard for real commercial offers and negotiations.",
                    "wrong_B": "Never use 'will' in the if-clause (*If the client will order* is a classic Czenglish error).",
                    "wrong_C": "Zero conditional is too weak for a contingent commercial promise.",
                    "wrong_D": "Mixed past and future indicative without hypothetical modal."
                },
                "cz_learning_point": "Czech says 'Když objednají (budoucí čas)... poskytneme'. In English, never use 'will' after 'if' in First Conditional.",
                "workplace_track": "International Sales & Tenders"
            },
            {
                "id": "TTR-B1-018-Q3",
                "prompt": "We cannot dispatch the vehicles unless the client's bank _____ an irrevocable letter of credit.",
                "options": [
                    {"key": "A", "text": "issues"},
                    {"key": "B", "text": "will issue"},
                    {"key": "C", "text": "doesn't issue"},
                    {"key": "D", "text": "is issue"}
                ],
                "correct_key": "A",
                "explanations": {
                    "correct": "'Unless' means 'if not' and takes Present Simple in positive form ('unless the bank issues').",
                    "wrong_B": "No 'will' after 'unless'.",
                    "wrong_C": "'Unless' already contains negative meaning; adding 'doesn't' creates an erroneous double negative.",
                    "wrong_D": "Malformed verb form."
                },
                "cz_learning_point": "'Unless' = 'pokud ne'. Never add a negative verb after 'unless' (*unless the bank doesn't issue* is incorrect).",
                "workplace_track": "International Sales & Tenders"
            },
            {
                "id": "TTR-B1-018-Q4",
                "prompt": "As soon as the export vessel _____ at the port of destination, the marine insurance policy under CIF terms _____.",
                "options": [
                    {"key": "A", "text": "docks / expires"},
                    {"key": "B", "text": "will dock / expires"},
                    {"key": "C", "text": "docks / will expire"},
                    {"key": "D", "text": "docked / expires"}
                ],
                "correct_key": "A",
                "explanations": {
                    "correct": "Zero conditional rule with 'as soon as': when the event occurs, the legal coverage terminates.",
                    "wrong_B": "'Will' is not permitted in time clauses with 'as soon as'.",
                    "wrong_C": "Refers to a specific future boat rather than the universal CIF legal rule.",
                    "wrong_D": "Tense mismatch."
                },
                "cz_learning_point": "Time clauses (as soon as, when, before, after) follow the same rule as if-clauses: use Present Simple, not 'will'.",
                "workplace_track": "International Sales & Tenders"
            },
            {
                "id": "TTR-B1-018-Q5",
                "prompt": "If our sales department _____ prices on DAP (Delivered at Place) terms, who _____ import customs clearance?",
                "options": [
                    {"key": "A", "text": "quotes / handles"},
                    {"key": "B", "text": "will quote / handles"},
                    {"key": "C", "text": "quotes / will handle to"},
                    {"key": "D", "text": "is quote / handles"}
                ],
                "correct_key": "A",
                "explanations": {
                    "correct": "Zero conditional inquiry about standard trade definitions under Incoterms 2020.",
                    "wrong_B": "Incorrect future auxiliary inside if-clause.",
                    "wrong_C": "'Will handle to' is ungrammatical.",
                    "wrong_D": "Syntactically invalid verb form."
                },
                "cz_learning_point": "Under DAP terms, the buyer is always responsible for import clearance and duties.",
                "workplace_track": "International Sales & Tenders"
            },
            {
                "id": "TTR-B1-018-Q6",
                "prompt": "If raw steel prices _____ rising at the current rate, our unit manufacturing costs _____ by at least 4% next quarter.",
                "options": [
                    {"key": "A", "text": "continue / will increase"},
                    {"key": "B", "text": "will continue / increase"},
                    {"key": "C", "text": "continues / will increase"},
                    {"key": "D", "text": "continued / will increase"}
                ],
                "correct_key": "A",
                "explanations": {
                    "correct": "First Conditional: plural subject 'prices' takes plural present 'continue', and main clause takes 'will increase'.",
                    "wrong_B": "'Will' cannot appear in the conditional clause.",
                    "wrong_C": "Subject-verb agreement error ('prices' is plural).",
                    "wrong_D": "Past simple cannot pair with 'will' in real future conditionals."
                },
                "cz_learning_point": "Avoid Czech transfer of future tense into conditional clauses.",
                "workplace_track": "International Sales & Tenders"
            },
            {
                "id": "TTR-B1-018-Q7",
                "prompt": "The distributor will forfeit their exclusivity rights in the Baltic region provided that they _____ their annual quota of 15 vehicles.",
                "options": [
                    {"key": "A", "text": "fail to meet"},
                    {"key": "B", "text": "will fail to meet"},
                    {"key": "C", "text": "don't fail to meet"},
                    {"key": "D", "text": "failed to meet"}
                ],
                "correct_key": "A",
                "explanations": {
                    "correct": "'Provided that' acts as a conditional conjunction followed by Present Simple ('fail to meet').",
                    "wrong_B": "Future 'will' is forbidden after 'provided that'.",
                    "wrong_C": "Double negative reverses the contractual meaning.",
                    "wrong_D": "Past tense does not match future consequence 'will forfeit'."
                },
                "cz_learning_point": "'Provided that' (za předpokladu, že) introduces a conditional clause taking Present Simple.",
                "workplace_track": "International Sales & Tenders"
            },
            {
                "id": "TTR-B1-018-Q8",
                "prompt": "What steps _____ if the maritime shipping line notifies us of general average damages during transit?",
                "options": [
                    {"key": "A", "text": "will we take"},
                    {"key": "B", "text": "do we take will"},
                    {"key": "C", "text": "we will take"},
                    {"key": "D", "text": "are we take"}
                ],
                "correct_key": "A",
                "explanations": {
                    "correct": "First Conditional question requires inverted main clause: 'will we take'.",
                    "wrong_B": "Nonsensical word order.",
                    "wrong_C": "Direct question requires inversion of auxiliary 'will' and subject 'we'.",
                    "wrong_D": "Malformed verb phrase."
                },
                "cz_learning_point": "In interrogative conditionals, invert the subject and auxiliary in the main clause ('What will we do if...?').",
                "workplace_track": "International Sales & Tenders"
            },
            {
                "id": "TTR-B1-018-Q9",
                "prompt": "If payment _____ within 30 days of commercial invoice receipt, a 1.5% monthly late interest penalty will apply.",
                "options": [
                    {"key": "A", "text": "is not received"},
                    {"key": "B", "text": "will not be received"},
                    {"key": "C", "text": "does not receive"},
                    {"key": "D", "text": "is not receiving"}
                ],
                "correct_key": "A",
                "explanations": {
                    "correct": "Present Simple Passive ('is not received') inside the if-clause for an incoming payment.",
                    "wrong_B": "Future passive 'will not be received' cannot be placed in the conditional clause.",
                    "wrong_C": "Active voice implies payment is an agent that receives something.",
                    "wrong_D": "Continuous aspect is inappropriate for transactional cutoff date."
                },
                "cz_learning_point": "Czech commercial contracts often use passive ('nebude-li platba přijata'). In English, use Present Simple Passive in the if-clause.",
                "workplace_track": "International Sales & Tenders"
            },
            {
                "id": "TTR-B1-018-Q10",
                "prompt": "Incoterms rules state that if goods _____ damaged while on board under FOB terms, the loss _____ to the buyer.",
                "options": [
                    {"key": "A", "text": "are / falls"},
                    {"key": "B", "text": "will be / falls"},
                    {"key": "C", "text": "are / will be fallen"},
                    {"key": "D", "text": "were / falls"}
                ],
                "correct_key": "A",
                "explanations": {
                    "correct": "Zero Conditional for universal trade definition: 'are damaged' (condition) + 'falls to the buyer' (result).",
                    "wrong_B": "'Will' is not used in conditional clauses.",
                    "wrong_C": "'Will be fallen' is passive of an intransitive verb (fall), which is grammatically invalid.",
                    "wrong_D": "Tense clash."
                },
                "cz_learning_point": "Under FOB (Free on Board), risk passes to the buyer the moment goods cross the ship's rail.",
                "workplace_track": "International Sales & Tenders"
            }
        ]
    },

    # -------------------------------------------------------------------------
    # TTR-B2-004: High-Stakes Contract Bargaining: Inversion for Emphasis
    # -------------------------------------------------------------------------
    {
        "test_id": "TTR-B2-004",
        "title": "High-Stakes Contract Bargaining: Inversion for Emphasis",
        "level": "B2",
        "category": "core",
        "workplace_track": "International Sales & Tenders",
        "estimated_time_minutes": 18,
        "description": "Utilize negative and restrictive adverbials (under no circumstances, seldom, little did we know, on no account) to add decisive legal and rhetorical force to high-stakes defense contracts and tender proposals.",
        "learning_objectives": [
            "Construct inverted sentence structures following negative and restrictive adverbials",
            "Employ inversion with 'Not only... but also' and 'Hardly... when'",
            "Apply high-register rhetorical emphasis in international contract correspondence"
        ],
        "questions": [
            {
                "id": "TTR-B2-004-Q1",
                "prompt": "Under no circumstances _____ to accept unlimited liability clauses in foreign government defense procurement tenders.",
                "options": [
                    {"key": "A", "text": "is Tatra prepared"},
                    {"key": "B", "text": "Tatra is prepared"},
                    {"key": "C", "text": "does Tatra prepared"},
                    {"key": "D", "text": "prepared Tatra"}
                ],
                "correct_key": "A",
                "explanations": {
                    "correct": "When a sentence begins with negative adverbial 'Under no circumstances', inversion of auxiliary and subject is required ('is Tatra prepared').",
                    "wrong_B": "Lacks inversion (standard declarative order cannot follow initial negative adverbials).",
                    "wrong_C": "Auxiliary 'does' requires base form 'prepare', not participle 'prepared'.",
                    "wrong_D": "Corrupt archaic word order without auxiliary verb."
                },
                "cz_learning_point": "Czech relies on word order freedom and intonation ('Za žádných okolností není Tatra ochotna'). In English, an initial negative adverbial strictly triggers inversion (question word order).",
                "workplace_track": "International Sales & Tenders"
            },
            {
                "id": "TTR-B2-004-Q2",
                "prompt": "Seldom _____ a competitor offer a heavy off-road vehicle with independent swinging half-axles at this price point.",
                "options": [
                    {"key": "A", "text": "does"},
                    {"key": "B", "text": "is"},
                    {"key": "C", "text": "has"},
                    {"key": "D", "text": "did"}
                ],
                "correct_key": "A",
                "explanations": {
                    "correct": "'Seldom' is a restrictive adverbial triggering inversion; 'does a competitor offer' correctly inverts the present simple.",
                    "wrong_B": "'Is a competitor offer' violates English auxiliary syntax.",
                    "wrong_C": "'Has' would require past participle 'offered'.",
                    "wrong_D": "'Did' refers to the past, but the statement describes a general commercial market reality."
                },
                "cz_learning_point": "Restrictive adverbs like 'seldom', 'rarely', and 'hardly' placed at the start of a sentence require do/does/did inversion.",
                "workplace_track": "International Sales & Tenders"
            },
            {
                "id": "TTR-B2-004-Q3",
                "prompt": "Not only _____ to deliver all fifty military tactical trucks ahead of schedule, but we also agreed to provide complimentary on-site maintenance training.",
                "options": [
                    {"key": "A", "text": "did our team manage"},
                    {"key": "B", "text": "our team managed"},
                    {"key": "C", "text": "had our team manage"},
                    {"key": "D", "text": "was our team managed"}
                ],
                "correct_key": "A",
                "explanations": {
                    "correct": "'Not only' at the beginning of a clause requires inversion: auxiliary 'did' + subject 'our team' + base verb 'manage'.",
                    "wrong_B": "Lacks inverted word order.",
                    "wrong_C": "'Had' requires past participle 'managed'.",
                    "wrong_D": "Passive voice 'was managed' distorts the meaning."
                },
                "cz_learning_point": "Czech 'Nejenže se našemu týmu podařilo...' In English, 'Not only did our team manage...' provides authoritative executive emphasis.",
                "workplace_track": "International Sales & Tenders"
            },
            {
                "id": "TTR-B2-004-Q4",
                "prompt": "Hardly _____ the ink dried on the preliminary MOU when the ministry demanded a 10% price concession.",
                "options": [
                    {"key": "A", "text": "had"},
                    {"key": "B", "text": "was"},
                    {"key": "C", "text": "did"},
                    {"key": "D", "text": "has"}
                ],
                "correct_key": "A",
                "explanations": {
                    "correct": "'Hardly had [subject] [past participle]... when [past simple]' is a fixed high-level inverted structure for rapid sequential events.",
                    "wrong_B": "'Was' cannot form the past perfect construction.",
                    "wrong_C": "'Did' would take base form 'dry', not past participle 'dried'.",
                    "wrong_D": "Present perfect 'has' clashes with past narrative 'demanded'."
                },
                "cz_learning_point": "Czech 'Sotva inkoust uschl...' translates into formal English as 'Hardly had the ink dried... when...'.",
                "workplace_track": "International Sales & Tenders"
            },
            {
                "id": "TTR-B2-004-Q5",
                "prompt": "On no account _____ the factory release the homologation certificates prior to receiving formal bank confirmation of payment.",
                "options": [
                    {"key": "A", "text": "should"},
                    {"key": "B", "text": "ought"},
                    {"key": "C", "text": "the factory should"},
                    {"key": "D", "text": "is"}
                ],
                "correct_key": "A",
                "explanations": {
                    "correct": "'On no account should the factory release...' provides legalistic inverted prohibition.",
                    "wrong_B": "'Ought' requires 'to'.",
                    "wrong_C": "Fails to invert the subject and modal.",
                    "wrong_D": "'Is' does not fit base verb 'release'."
                },
                "cz_learning_point": "In legal and compliance documents, 'V žádném případě...' is translated as 'On no account should...'.",
                "workplace_track": "International Sales & Tenders"
            },
            {
                "id": "TTR-B2-004-Q6",
                "prompt": "Only after extensive field trials in the Australian outback _____ that the cooling system was completely dust-resistant.",
                "options": [
                    {"key": "A", "text": "did the mining client concede"},
                    {"key": "B", "text": "the mining client conceded"},
                    {"key": "C", "text": "conceded the mining client"},
                    {"key": "D", "text": "has the mining client conceded"}
                ],
                "correct_key": "A",
                "explanations": {
                    "correct": "Clauses introduced by 'Only after [time/clause]' trigger inversion in the main clause: 'did the client concede'.",
                    "wrong_B": "Main clause lacks inversion.",
                    "wrong_C": "Inversion in English requires an auxiliary verb ('did'), not inversion of main verb.",
                    "wrong_D": "Present perfect clashes with past narrative 'was'."
                },
                "cz_learning_point": "Notice that 'Only after...' does NOT invert the 'after' clause itself, but inverts the MAIN clause that follows.",
                "workplace_track": "International Sales & Tenders"
            },
            {
                "id": "TTR-B2-004-Q7",
                "prompt": "Little _____ that the defense ministry had already drafted the final tender evaluation matrix before our meeting.",
                "options": [
                    {"key": "A", "text": "did our negotiators suspect"},
                    {"key": "B", "text": "our negotiators suspected"},
                    {"key": "C", "text": "suspected our negotiators"},
                    {"key": "D", "text": "had our negotiators suspected"}
                ],
                "correct_key": "A",
                "explanations": {
                    "correct": "'Little did our negotiators suspect' expresses that they had no idea whatsoever (inverted with 'did').",
                    "wrong_B": "Lacks inversion.",
                    "wrong_C": "Requires auxiliary 'did'.",
                    "wrong_D": "Idiomatic 'little did someone know/suspect' uses 'did', not 'had'."
                },
                "cz_learning_point": "Czech 'Vůbec netušili, že...' translates elegantly into executive English as 'Little did they suspect that...'.",
                "workplace_track": "International Sales & Tenders"
            },
            {
                "id": "TTR-B2-004-Q8",
                "prompt": "At no time _____ that the delivery lead times would be shortened to less than ninety days.",
                "options": [
                    {"key": "A", "text": "did we guarantee"},
                    {"key": "B", "text": "we guaranteed"},
                    {"key": "C", "text": "guaranteed we"},
                    {"key": "D", "text": "have we guaranteed"}
                ],
                "correct_key": "A",
                "explanations": {
                    "correct": "'At no time did we guarantee...' is the formal contractual denial of a commitment.",
                    "wrong_B": "Un-inverted word order.",
                    "wrong_C": "Corrupt syntax.",
                    "wrong_D": "Present perfect does not match the past perspective 'would be shortened'."
                },
                "cz_learning_point": "In dispute settlement emails, 'Nikdy jsme nezaručili' is expressed with maximum legal force as 'At no time did we guarantee...'.",
                "workplace_track": "International Sales & Tenders"
            },
            {
                "id": "TTR-B2-004-Q9",
                "prompt": "So complex _____ the international homologation criteria that our engineering team required six months of pre-certification testing.",
                "options": [
                    {"key": "A", "text": "were"},
                    {"key": "B", "text": "was"},
                    {"key": "C", "text": "did"},
                    {"key": "D", "text": "are"}
                ],
                "correct_key": "A",
                "explanations": {
                    "correct": "Inversion with 'So + adjective': 'So complex were the criteria that...' (criteria is plural).",
                    "wrong_B": "'Criteria' is plural (singular is 'criterion'), so 'was' is a grammatical agreement error.",
                    "wrong_C": "'Did' cannot pair with adjective 'complex'.",
                    "wrong_D": "Past event 'required' demands past plural 'were'."
                },
                "cz_learning_point": "Remember that 'criteria' is plural in English (like 'data'). The inversion takes 'were', not 'was'.",
                "workplace_track": "International Sales & Tenders"
            },
            {
                "id": "TTR-B2-004-Q10",
                "prompt": "No sooner had the commercial director opened the discussion _____ the overseas delegate raised objections to the warranty duration.",
                "options": [
                    {"key": "A", "text": "than"},
                    {"key": "B", "text": "when"},
                    {"key": "C", "text": "that"},
                    {"key": "D", "text": "then"}
                ],
                "correct_key": "A",
                "explanations": {
                    "correct": "'No sooner had [past participle]... than...' is the exact comparative correlative pair in English.",
                    "wrong_B": "'When' is used with 'Hardly / Scarcely', not with 'No sooner'.",
                    "wrong_C": "'That' does not form this correlative structure.",
                    "wrong_D": "'Then' is a common spelling/confusion error for comparative 'than'."
                },
                "cz_learning_point": "Correlative pairs: 'Hardly... when', but 'No sooner... THAN'. Do not mix them up.",
                "workplace_track": "International Sales & Tenders"
            }
        ]
    },

    # -------------------------------------------------------------------------
    # TTR-SP-016: Professional Idioms in International Sales & Negotiations
    # -------------------------------------------------------------------------
    {
        "test_id": "TTR-SP-016",
        "title": "Professional Idioms in International Sales & Negotiations",
        "level": "B1/B2",
        "category": "specialized",
        "workplace_track": "International Sales & Tenders",
        "estimated_time_minutes": 15,
        "description": "Master nuanced business idioms used during international automotive fleet sales, dealer conferences, and cross-border commercial bargaining.",
        "learning_objectives": [
            "Deploy idiomatic business metaphors with confidence in meetings and negotiations",
            "Avoid literal translations of Czech idioms into English commercial discussions",
            "Understand idiomatic nuances used by international fleet buyers and military procurement officials"
        ],
        "questions": [
            {
                "id": "TTR-SP-016-Q1",
                "prompt": "We have submitted our best possible CIF pricing; now the _____ is in their court to finalize the contract.",
                "options": [
                    {"key": "A", "text": "ball"},
                    {"key": "B", "text": "truck"},
                    {"key": "C", "text": "card"},
                    {"key": "D", "text": "game"}
                ],
                "correct_key": "A",
                "explanations": {
                    "correct": "'The ball is in their court' is a classic negotiation idiom meaning it is now their responsibility or turn to take action.",
                    "wrong_B": "Literal replacement that ruins the idiomatic expression.",
                    "wrong_C": "Non-standard phrase.",
                    "wrong_D": "Incorrect metaphor."
                },
                "cz_learning_point": "Czech says 'míč je na jejich straně hřiště'. In English, the exact idiom is 'the ball is in their court'.",
                "workplace_track": "International Sales & Tenders"
            },
            {
                "id": "TTR-SP-016-Q2",
                "prompt": "To _____ the deal for the municipal fire department, we included three years of free spare parts and oil filters.",
                "options": [
                    {"key": "A", "text": "sweeten"},
                    {"key": "B", "text": "sugar"},
                    {"key": "C", "text": "soften"},
                    {"key": "D", "text": "grease"}
                ],
                "correct_key": "A",
                "explanations": {
                    "correct": "'Sweeten the deal' means to add extra incentives or perks to make a commercial proposal more attractive to the buyer.",
                    "wrong_B": "'Sugar the deal' is non-standard.",
                    "wrong_C": "'Soften the deal' means to make terms less harsh, not add attractive bonuses.",
                    "wrong_D": "'Grease' (e.g. grease palms) implies bribery, which is completely inappropriate."
                },
                "cz_learning_point": "Czech 'osladit / vylepšit nabídku' translates to 'sweeten the deal' or 'sweeten the pot'.",
                "workplace_track": "International Sales & Tenders"
            },
            {
                "id": "TTR-SP-016-Q3",
                "prompt": "Both legal teams spent four hours in the boardroom trying to _____ out the kinks in the intellectual property licensing agreement.",
                "options": [
                    {"key": "A", "text": "iron"},
                    {"key": "B", "text": "hammer"},
                    {"key": "C", "text": "weld"},
                    {"key": "D", "text": "file"}
                ],
                "correct_key": "A",
                "explanations": {
                    "correct": "'Iron out the kinks' (or 'iron out wrinkles/details') means to resolve small remaining problems or complications.",
                    "wrong_B": "The phrase is 'hammer out an agreement', but with 'kinks' the fixed collocation is 'iron out'.",
                    "wrong_C": "Literal welding metaphor not found in this idiom.",
                    "wrong_D": "Incorrect verb."
                },
                "cz_learning_point": "Czech 'vychytat mouchy / vyhladit nesrovnalosti' is translated idiomatically as 'iron out the kinks'.",
                "workplace_track": "International Sales & Tenders"
            },
            {
                "id": "TTR-SP-016-Q4",
                "prompt": "Let's stop discussing minor administrative details and get down to _____ tacks: what is the bottom-line price per vehicle?",
                "options": [
                    {"key": "A", "text": "brass"},
                    {"key": "B", "text": "copper"},
                    {"key": "C", "text": "steel"},
                    {"key": "D", "text": "iron"}
                ],
                "correct_key": "A",
                "explanations": {
                    "correct": "'Get down to brass tacks' is a well-known English idiom meaning to focus on the essential facts or core issues.",
                    "wrong_B": "Incorrect metal.",
                    "wrong_C": "Incorrect metal.",
                    "wrong_D": "Incorrect metal."
                },
                "cz_learning_point": "Czech 'přejít k jádru pudla / k věci' translates idiomatically to 'get down to brass tacks'.",
                "workplace_track": "International Sales & Tenders"
            },
            {
                "id": "TTR-SP-016-Q5",
                "prompt": "Neither side was willing to compromise on delivery penalty rates, and the negotiations reached a complete _____.",
                "options": [
                    {"key": "A", "text": "stalemate"},
                    {"key": "B", "text": "check"},
                    {"key": "C", "text": "blockade"},
                    {"key": "D", "text": "deadlock-end"}
                ],
                "correct_key": "A",
                "explanations": {
                    "correct": "'Reach a stalemate' (or 'reach an impasse / deadlock') means reaching a situation where neither side can make progress.",
                    "wrong_B": "'Check' is a chess threat, not a stalemate.",
                    "wrong_C": "'Blockade' refers to military naval cordons.",
                    "wrong_D": "Malformed compound."
                },
                "cz_learning_point": "Czech 'patová situace' translates to 'stalemate' (e.g. 'reach a stalemate' or 'end in stalemate').",
                "workplace_track": "International Sales & Tenders"
            },
            {
                "id": "TTR-SP-016-Q6",
                "prompt": "Before we sign the final distribution agreement, I want to touch _____ with our homologation engineer regarding local emissions.",
                "options": [
                    {"key": "A", "text": "base"},
                    {"key": "B", "text": "ground"},
                    {"key": "C", "text": "flange"},
                    {"key": "D", "text": "wire"}
                ],
                "correct_key": "A",
                "explanations": {
                    "correct": "'Touch base with [someone]' means to make brief contact or confer with someone to update status.",
                    "wrong_B": "'Touch ground' is literal aviation contact.",
                    "wrong_C": "Mechanical part, not an idiom.",
                    "wrong_D": "'Touch wire' is non-idiomatic."
                },
                "cz_learning_point": "Czech 'spojit se s někým / krátce to zkonzultovat' is very commonly expressed in corporate English as 'touch base'.",
                "workplace_track": "International Sales & Tenders"
            },
            {
                "id": "TTR-SP-016-Q7",
                "prompt": "Our sales team was caught off _____ when the competitor announced a 10-year chassis warranty at the trade fair.",
                "options": [
                    {"key": "A", "text": "guard"},
                    {"key": "B", "text": "hand"},
                    {"key": "C", "text": "track"},
                    {"key": "D", "text": "step"}
                ],
                "correct_key": "A",
                "explanations": {
                    "correct": "'Caught off guard' means surprised and unprepared for an unexpected development.",
                    "wrong_B": "'Off hand' means impromptu or without prior thought.",
                    "wrong_C": "'Off track' means diverted from the subject.",
                    "wrong_D": "'Off step' is non-standard."
                },
                "cz_learning_point": "Czech 'být zaskočen / nachytán na švestkách' translates to 'be caught off guard'.",
                "workplace_track": "International Sales & Tenders"
            },
            {
                "id": "TTR-SP-016-Q8",
                "prompt": "If we want to close this defense deal before fiscal year-end, we need to _____ a compromise that satisfies both ministries.",
                "options": [
                    {"key": "A", "text": "hammer out"},
                    {"key": "B", "text": "knock off"},
                    {"key": "C", "text": "cut out"},
                    {"key": "D", "text": "break down"}
                ],
                "correct_key": "A",
                "explanations": {
                    "correct": "'Hammer out a compromise / agreement' means to negotiate persistently until a mutually acceptable solution is forged.",
                    "wrong_B": "'Knock off' means reduce price or stop working.",
                    "wrong_C": "'Cut out' means eliminate.",
                    "wrong_D": "'Break down' means collapse or fail mechanically."
                },
                "cz_learning_point": "Czech 'vyjednat po těžkém boji kompromis' is expressed as 'hammer out a compromise'.",
                "workplace_track": "International Sales & Tenders"
            },
            {
                "id": "TTR-SP-016-Q9",
                "prompt": "The foreign dealer was clearly playing his cards close to his _____ during the pricing negotiations.",
                "options": [
                    {"key": "A", "text": "chest"},
                    {"key": "B", "text": "head"},
                    {"key": "C", "text": "table"},
                    {"key": "D", "text": "sleeves"}
                ],
                "correct_key": "A",
                "explanations": {
                    "correct": "'Play cards close to one's chest' means to be very secretive and cautious about revealing one's plans or real intentions.",
                    "wrong_B": "Incorrect anatomy.",
                    "wrong_C": "Playing on the table means open transparency (opposite meaning).",
                    "wrong_D": "Having something up one's sleeve is a secret trick, but the idiom with cards close is 'chest'."
                },
                "cz_learning_point": "Czech 'neodkrývat karty / držet karty při těle' translates to 'play one's cards close to one's chest'.",
                "workplace_track": "International Sales & Tenders"
            },
            {
                "id": "TTR-SP-016-Q10",
                "prompt": "I will send a follow-up email tomorrow morning to close the _____ on all unanswered technical questions.",
                "options": [
                    {"key": "A", "text": "loop"},
                    {"key": "B", "text": "circle"},
                    {"key": "C", "text": "ring"},
                    {"key": "D", "text": "circuit"}
                ],
                "correct_key": "A",
                "explanations": {
                    "correct": "'Close the loop' means to finalize, resolve, and confirm the conclusion of an open communication or task.",
                    "wrong_B": "'Close the circle' is a geometric phrase.",
                    "wrong_C": "'Ring' is not part of this idiom.",
                    "wrong_D": "'Close the circuit' is an electrical action, not an organizational communication idiom."
                },
                "cz_learning_point": "Czech 'dotáhnout věc do konce a potvrdit to' is idiomatically 'close the loop'.",
                "workplace_track": "International Sales & Tenders"
            }
        ]
    }
]

def main():
    generated = 0
    for m in modules_data:
        test_file = TESTS_DIR / f"{m['test_id']}.json"
        with open(test_file, "w", encoding="utf-8") as f:
            json.dump(m, f, indent=2, ensure_ascii=False)
        print(f"Generated {test_file.name}")
        generated += 1
    print(f"Successfully wrote {generated} test modules.")

if __name__ == "__main__":
    main()
