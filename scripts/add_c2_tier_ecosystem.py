#!/usr/bin/env python3
"""
Adds the CEFR C2 (Executive Mastery) Tier across all 5 Independent Corporate Testing Suites:
1. Tatra Engineering (TTR-ENG-C2-001)
2. Tatra Sales and Engineering (TTR-SALES-C2-001)
3. Teva Engineering (TEV-ENG-C2-001)
4. Tapi Chemistry (TAPI-CHEM-C2-001)
5. Teva IT (TEV-IT-C2-001)

Features:
- Balanced answer keys (cycling B, C, A, D, C, B, D, A, C, B) with max single key <= 30%.
- Authentic workplace C2 topics: forensic metallurgical disputes, ICC defense tender arbitration,
  unannounced FDA 483 audit defense, nitrosamine impurity monograph harmonization, and enterprise breach disclosures.
- Advanced C2 grammar: negative inversion, formal subjunctive, complex hedging, past modal deduction,
  inverted conditionals (Had/Were/Should).
- Czech contrastive linguistic tips tailored to senior engineers and executives.
- Updates curriculum manifests, tests_registry.js, and distribution packages.
"""

import os
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

def create_q(qid, prompt, options_dict, correct_key, explanations, cz_note, track):
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
# 1. TATRA ENGINEERING C2 (TTR-ENG-C2-001)
# =============================================================================
tatra_eng_c2_001 = {
    "test_id": "TTR-ENG-C2-001",
    "title": "Forensic Failure Analysis, Structural Metallurgy & NATO Offsets: Negative Inversion & Nuanced Hedging",
    "level": "C2",
    "category": "core",
    "workplace_track": "Forensic Root Cause Analysis, NATO Trials & Joint-Venture Steering",
    "estimated_time_minutes": 20,
    "description": "Executive and lead engineering diagnostics: negative inversion in structural failure forensics, diplomatic hedging in joint steering committees, and subjunctive specifications under NATO STANAG trials.",
    "learning_objectives": [
        "Master negative inversion for high-stakes safety and metallurgical directives",
        "Apply diplomatic hedging in forensic engineering dispute committees",
        "Formulate formal inverted conditionals in structural failure reports"
    ],
    "questions": [
        create_q(
            "TTR-ENG-C2-001-Q1",
            "Under no circumstances _____ the central backbone tube torsional stress limit be exceeded during the accelerated rough-terrain endurance trial.",
            {"A": "the engineers should permit", "B": "should the engineers permit", "C": "the engineers will permit", "D": "must the engineers to permit"},
            "B",
            {
                "correct": "Negative restrictive phrase 'Under no circumstances' at the front of a clause requires subject-auxiliary inversion ('should the engineers permit').",
                "wrong_A": "Lacks required subject-auxiliary inversion after fronted negative phrase.",
                "wrong_C": "Direct word order is ungrammatical following fronted 'Under no circumstances'.",
                "wrong_D": "Modal 'must' cannot be followed by an infinitive with 'to' (*to permit*)."
            },
            "Czech speakers naturally use standard word order ('Za žádných okolností inženýři nesmí dovolit'). In English, fronted negative adverbials trigger formal inversion: 'Under no circumstances should the engineers permit'.",
            "Forensic Root Cause Analysis, NATO Trials & Joint-Venture Steering"
        ),
        create_q(
            "TTR-ENG-C2-001-Q2",
            "The microscopic transgranular fracture patterns _____ that hydrogen embrittlement occurred during the electroplating process, rather than sheer mechanical overload.",
            {"A": "are definitively testifying", "B": "manifestly proving beyond dispute", "C": "would tentatively suggest", "D": "are bound to undeniably show"},
            "C",
            {
                "correct": "At C2 executive level, epistemic modal hedging ('would tentatively suggest') avoids unprovable dogmatic claims in official forensic failure investigations before metallurgical chemical testing is concluded.",
                "wrong_A": "'Definitively testifying' is inappropriately dogmatic and stylistically clumsy for an engineering failure hypothesis.",
                "wrong_B": "Prematurely asserts proof beyond dispute without supporting mass spectroscopy data.",
                "wrong_D": "'Undeniably show' ignores required technical epistemic caution in dispute committees."
            },
            "Czech engineers often translate 'Jednoznačně to dokazuje' literally as *it definitely proves*. In C2 international forensic disputes, diplomatic hedging ('would tentatively suggest') protects liability.",
            "Forensic Root Cause Analysis, NATO Trials & Joint-Venture Steering"
        ),
        create_q(
            "TTR-ENG-C2-001-Q3",
            "_____ the metallurgical testing laboratory executed ultrasonic resonance screening on the swinging half-axles, the fatigue micro-fissures would have been identified prior to field deployment.",
            {"A": "Had", "B": "If", "C": "Were", "D": "Should"},
            "A",
            {
                "correct": "Inverted third conditional ('Had the laboratory executed...') omits 'if' and front-inverts the auxiliary 'had' for high-register formal forensic reporting.",
                "wrong_B": "'If' would require standard word order ('If the laboratory had executed...').",
                "wrong_C": "'Were' pairs with present/future counterfactuals ('Were the lab to execute...'), not completed past actions.",
                "wrong_D": "'Should' introduces future conditional possibility, not past counterfactual failure."
            },
            "Czech 'Kdyby zkušební laboratoř provedla...'. High-register technical English omits 'if' via inversion: 'Had the laboratory executed...'.",
            "Central Backbone Tube & Chassis R&D"
        ),
        create_q(
            "TTR-ENG-C2-001-Q4",
            "The Chief Technical Officer requested that every weld seam on the tactical 8x8 chassis frame _____ re-examined using magnetic particle inspection prior to NATO STANAG 4569 ballistic testing.",
            {"A": "be", "B": "is", "C": "must be", "D": "to be"},
            "A",
            {
                "correct": "Mandative subjunctive requires the base verb 'be' in subordinate clauses depending on verbs of formal demand/request ('requested that every weld seam be re-examined').",
                "wrong_B": "Indicative 'is' violates the formal mandative subjunctive register expected in defense engineering specifications.",
                "wrong_C": "Modal 'must be' is redundant and colloquially informal in a formal subjunctive clause following 'requested that'.",
                "wrong_D": "Infinitive 'to be' is ungrammatical as the predicate of a finite 'that'-clause."
            },
            "Czech 'CTO požádal, aby každý svar byl přezkoumán'. English mandative subjunctive uses the bare base form: 'requested that every weld seam be re-examined'.",
            "Forensic Root Cause Analysis, NATO Trials & Joint-Venture Steering"
        ),
        create_q(
            "TTR-ENG-C2-001-Q5",
            "Seldom _____ a heavy-duty chassis design combine independent swinging half-axles with a central backbone tube while retaining such high torsional rigidity.",
            {"A": "has seen", "B": "an automotive engineer sees", "C": "does", "D": "is seeing"},
            "C",
            {
                "correct": "Fronted restrictive frequency adverb 'Seldom' requires subject-auxiliary inversion with auxiliary 'does' ('Seldom does a chassis design combine...').",
                "wrong_A": "Lacks subject and creates ungrammatical passive/active confusion.",
                "wrong_B": "Standard word order violates inversion rule after fronted 'Seldom'.",
                "wrong_D": "Stative verb 'combine' does not take continuous aspect here."
            },
            "Czech 'Málokdy se vidí...' or 'Zřídka kdy konstrukce spojuje...'. In English, fronted 'Seldom' forces inversion: 'Seldom does a chassis design combine...'.",
            "Central Backbone Tube & Chassis R&D"
        ),
        create_q(
            "TTR-ENG-C2-001-Q6",
            "The client's arbitration claim is predicated on the assertion that the differential lock failure was caused by defective cast iron, _____ evidence indicates severe operator misapplication.",
            {"A": "irrespective", "B": "whereas empirical", "C": "in spite", "D": "despite that"},
            "B",
            {
                "correct": "'Whereas empirical' introduces a sharp, formal legal contrast between the adversary's subjective assertion and objective metallurgical findings.",
                "wrong_A": "'Irrespective' requires preposition 'of' and does not connect two independent clauses.",
                "wrong_C": "'In spite' requires 'of' and cannot take a finite clause directly.",
                "wrong_D": "'Despite that' is clumsy and informal compared to the elegant contrastive connector 'whereas'."
            },
            "Czech 'zatímco empirické důkazy ukazují...'. In legal/technical disputes, use 'whereas empirical evidence indicates...', avoiding awkward prepositions.",
            "Forensic Root Cause Analysis, NATO Trials & Joint-Venture Steering"
        ),
        create_q(
            "TTR-ENG-C2-001-Q7",
            "Scarcely had the prototype vehicle commenced the desert sand dune trial _____ the central tyre inflation system (CTIS) pressure manifold reported a critical pressure drop.",
            {"A": "than", "B": "that", "C": "after", "D": "when"},
            "D",
            {
                "correct": "'Scarcely had [action]... when [second action]' is the correlative grammatical structure for two rapid successive events.",
                "wrong_A": "'Than' pairs with 'No sooner had...', not 'Scarcely'.",
                "wrong_B": "'That' cannot serve as the correlative conjunction for 'Scarcely'.",
                "wrong_C": "'After' creates redundancy with the past perfect auxiliary."
            },
            "Czech 'Sotva vozidlo zahájilo... když v tom...'. English requires 'Scarcely had [subject] [verb]... WHEN...', whereas 'No sooner' pairs with 'THAN'.",
            "Central Backbone Tube & Chassis R&D"
        ),
        create_q(
            "TTR-ENG-C2-001-Q8",
            "_____ there be any discrepancy between the CAD finite element analysis and the physical strain gauge readings, the suspension linkage must undergo destructive tensile testing.",
            {"A": "Should", "B": "Were", "C": "Had", "D": "If so"},
            "A",
            {
                "correct": "Inverted first conditional ('Should there be...') denotes formal potential contingency in technical test protocols, equivalent to 'If there should be'.",
                "wrong_B": "'Were there to be' would be used for hypothetical counterfactuals, but 'there be' requires 'Should'.",
                "wrong_C": "'Had there been' indicates past counterfactual, not future procedural contingency.",
                "wrong_D": "'If so' cannot act as a subordinate conditional conjunction."
            },
            "Czech 'Pokud by nastala jakákoliv odchylka...'. In formal technical protocols, use 'Should there be any discrepancy...', omitting 'if'.",
            "Central Backbone Tube & Chassis R&D"
        ),
        create_q(
            "TTR-ENG-C2-001-Q9",
            "The catastrophic shear failure of the transfer case pinion gear cannot _____ to torsional vibration resonance alone without factoring in low lubricant viscosity at extreme operating temperatures.",
            {"A": "definitely attribute", "B": "be having attributed", "C": "plausibly be attributed", "D": "attribute itself"},
            "C",
            {
                "correct": "Passive modal construction with epistemic adverb ('cannot plausibly be attributed') accurately qualifies the scientific limits of a root-cause hypothesis.",
                "wrong_A": "Active voice 'attribute' cannot apply when the gear failure is the grammatical subject.",
                "wrong_B": "Ungrammatical compound progressive passive participle.",
                "wrong_D": "'Attribute itself' is a literal Czech reflexive translation error (*přisuzovat se*)."
            },
            "Czech 'nelze to věrohodně přičítat pouze...'. Do not translate reflexively (*attribute itself*). Use passive modal 'cannot plausibly be attributed to...'.",
            "Forensic Root Cause Analysis, NATO Trials & Joint-Venture Steering"
        ),
        create_q(
            "TTR-ENG-C2-001-Q10",
            "Not only _____ the swinging half-axle design attenuate severe shock loads over rocky terrain, but it also minimizes tire sidewall scrub compared to conventional rigid axle beams.",
            {"A": "is", "B": "does", "C": "has", "D": "will"},
            "B",
            {
                "correct": "Fronted correlative 'Not only' with base action verb 'attenuate' requires dummy auxiliary 'does' for inversion ('Not only does the design attenuate...').",
                "wrong_A": "'Is' cannot invert with base action verb 'attenuate'.",
                "wrong_C": "'Has' would require past participle 'attenuated'.",
                "wrong_D": "'Will' implies future promise rather than verified inherent engineering capability."
            },
            "Czech 'Nejenže konstrukce tlumí..., ale také...'. English requires auxiliary inversion: 'Not only does the design attenuate..., but it also...'.",
            "Central Backbone Tube & Chassis R&D"
        )
    ]
}

# =============================================================================
# 2. TATRA SALES & ENGINEERING C2 (TTR-SALES-C2-001)
# =============================================================================
tatra_sales_c2_001 = {
    "test_id": "TTR-SALES-C2-001",
    "title": "International Defense Tender Arbitration, ICC Jurisdiction & Force Majeure: Contractual Subjunctive & Risk Hedging",
    "level": "C2",
    "category": "core",
    "workplace_track": "International Contract Law, ICC Arbitration & Defense Tender Litigation",
    "estimated_time_minutes": 20,
    "description": "Executive sales and contract legal engineering: drafting liquidated damages indemnities, managing ICC Paris arbitration clauses, navigating split liability under Incoterms 2020 DPU/DAP, and diplomatic de-escalation of foreign ministry disputes.",
    "learning_objectives": [
        "Master mandative and formulaic subjunctive in international military procurement contracts",
        "Formulate precise risk transfer stipulations under Incoterms 2020 rules",
        "Utilize high-register diplomatic hedging in multi-million dollar defense contract negotiations"
    ],
    "questions": [
        create_q(
            "TTR-SALES-C2-001-Q1",
            "Be it resolved that Tatra Trucks _____ harmless the defense ministry against any third-party patent infringement claims arising from the proprietary pneumatic suspension system.",
            {"A": "shall hold", "B": "hold", "C": "holds", "D": "is holding"},
            "B",
            {
                "correct": "Formulaic legal subjunctive ('Be it resolved that [entity] hold harmless...') uses the bare base form 'hold' without third-person '-s' or modal auxiliary.",
                "wrong_A": "'Shall hold' is standard contractual obligation, but follows standard clauses, not the archaic formulaic subjunctive preamble 'Be it resolved that'.",
                "wrong_C": "Indicative 'holds' violates the formulaic legal subjunctive mood.",
                "wrong_D": "Continuous aspect is completely inappropriate in legal indemnity deeds."
            },
            "Czech 'Budiž ujednáno, že Tatra Trucks odškodní...'. Formal legal preambles use formulaic subjunctive base forms: 'Be it resolved that Tatra Trucks hold harmless...'.",
            "International Contract Law, ICC Arbitration & Defense Tender Litigation"
        ),
        create_q(
            "TTR-SALES-C2-001-Q2",
            "Under the agreed Incoterms 2020 DPU (Delivered at Place Unloaded) terms, at what exact juncture _____ to the procurement authority?",
            {"A": "transfers the risk of damage", "B": "the risk of accidental loss is transferring", "C": "does the risk of loss pass", "D": "passes the risk of damage"},
            "C",
            {
                "correct": "Formal interrogative syntax requires auxiliary inversion ('does the risk of loss pass') for clean, unambiguous commercial arbitration clarity.",
                "wrong_A": "Lacks required auxiliary verb 'does' in direct technical inquiry.",
                "wrong_B": "Indirect word order without inversion cannot form a direct question.",
                "wrong_D": "Inversion of full lexical verb ('passes the risk') is archaic and grammatically incorrect in modern commercial English."
            },
            "Czech 'v jakém okamžiku přechází riziko škody na...?'. In English, questions require auxiliary 'does': 'At what exact juncture does the risk of loss pass...?'",
            "Commercial Contracts, Incoterms 2020 & Risk Transfer"
        ),
        create_q(
            "TTR-SALES-C2-001-Q3",
            "_____ the ministry to invoke the force majeure clause prematurely due to port customs congestion, our legal counsel would immediately initiate ICC expedited arbitration proceedings.",
            {"A": "Were", "B": "If", "C": "Had", "D": "Should"},
            "A",
            {
                "correct": "Inverted second conditional ('Were the ministry to invoke...') denotes a formal hypothetical future contingency with dignified diplomatic distance.",
                "wrong_B": "'If' would require standard word order ('If the ministry were to invoke...').",
                "wrong_C": "'Had' pairs with past counterfactual participles, not the infinitive 'to invoke'.",
                "wrong_D": "'Should' would be followed by bare infinitive 'invoke', not 'to invoke'."
            },
            "Czech 'Kdyby ministerstvo předčasně uplatnilo...'. Formal diplomatic legal phrasing inverts 'were': 'Were the ministry to invoke...'.",
            "International Contract Law, ICC Arbitration & Defense Tender Litigation"
        ),
        create_q(
            "TTR-SALES-C2-001-Q4",
            "It is stipulated in section 14.2 that the supplier _____ penalty payments in the event that spare parts deliveries fail to achieve the 98% operational availability metric.",
            {"A": "remit", "B": "remits", "C": "shall remit", "D": "to remit"},
            "A",
            {
                "correct": "Mandative subjunctive after passive verb of requirement ('It is stipulated that [entity] remit...') requires base verb 'remit'.",
                "wrong_B": "Third person singular 'remits' is indicative, whereas legal stipulations require the subjunctive base form.",
                "wrong_C": "'Shall remit' is common in drafting, but when introduced by 'It is stipulated that...', the subjunctive bare form 'remit' is the most refined legal register.",
                "wrong_D": "Infinitive 'to remit' cannot stand as the main predicate of a 'that'-clause."
            },
            "Czech 'Je stanoveno, že dodavatel uhradí...'. English mandative subjunctive uses base form: 'It is stipulated that the supplier remit...'.",
            "International Contract Law, ICC Arbitration & Defense Tender Litigation"
        ),
        create_q(
            "TTR-SALES-C2-001-Q5",
            "Only by providing an unconditional standby letter of credit from an internationally rated tier-1 bank _____ the tender evaluation committee permit the bid bond exemption.",
            {"A": "will", "B": "does", "C": "did", "D": "would"},
            "A",
            {
                "correct": "Fronted restrictive phrase 'Only by providing...' requires subject-auxiliary inversion with future modal 'will' ('will the committee permit').",
                "wrong_B": "'Does' refers to general habit, whereas tender evaluations are specific future conditional determinations.",
                "wrong_C": "'Did' refers to completed past action, conflicting with the prospective tender evaluation process.",
                "wrong_D": "'Would' requires a counterfactual condition, which is absent here."
            },
            "Czech 'Pouze předložením neodvolatelného akreditivu výbor povolí...'. In English, fronted 'Only by...' demands inversion: 'Only by providing... will the committee permit...'.",
            "International Defense Bids & NATO STANAG Tenders"
        ),
        create_q(
            "TTR-SALES-C2-001-Q6",
            "Our negotiation posture must remain uncompromising regarding warranty ceilings, _____ we risk setting an adverse contractual precedent across all Eastern European defense tenders.",
            {"A": "otherwise", "B": "lest", "C": "in case", "D": "unless"},
            "B",
            {
                "correct": "Formal conjunction 'lest' ('for fear that / in order to avoid') introduces an adverse risk and pairs with subjunctive or indicative in elevated diplomatic English.",
                "wrong_A": "'Otherwise' is an adverb requiring a semicolon or coordinator, not a subordinating conjunction.",
                "wrong_C": "'In case' indicates precaution, not avoidance of a direct hazard.",
                "wrong_D": "'Unless' means 'except if', which reverses the intended causal meaning."
            },
            "Czech 'abychom neriskovali... / jinak hrozí, že...'. High-level diplomatic English uses 'lest' ('lest we risk setting an adverse precedent').",
            "Executive Contract Negotiation & Dealer Relations"
        ),
        create_q(
            "TTR-SALES-C2-001-Q7",
            "No sooner had the bilateral tender contract been signed in Abu Dhabi _____ the ministry issued an addendum demanding supplementary cold-weather cabin modifications.",
            {"A": "when", "B": "that", "C": "as", "D": "than"},
            "D",
            {
                "correct": "'No sooner had [action]... than [second action]' is the strictly required correlative pair in high-level English.",
                "wrong_A": "'When' pairs with 'Scarcely' or 'Hardly', not 'No sooner'.",
                "wrong_B": "'That' cannot introduce the temporal correlative clause.",
                "wrong_C": "'As' is colloquial and grammatically invalid here."
            },
            "Czech 'Sotva byla smlouva podepsána, než ministerstvo vydalo dodatek'. Always pair 'No sooner had...' with 'THAN'.",
            "International Defense Bids & NATO STANAG Tenders"
        ),
        create_q(
            "TTR-SALES-C2-001-Q8",
            "_____ the military attache inquire regarding our export licensing status under EU dual-use regulations, reassure him that our authorization dossier is already before the licensing board.",
            {"A": "Should", "B": "Were", "C": "Could", "D": "Had"},
            "A",
            {
                "correct": "Inverted first conditional ('Should the attache inquire...') represents formal diplomatic courtesy for possible future inquiries.",
                "wrong_B": "'Were the attache to inquire' would be acceptable, but 'Were' cannot pair directly with bare infinitive 'inquire'.",
                "wrong_C": "'Could' cannot form an inverted conditional clause of this type.",
                "wrong_D": "'Had' pairs with past counterfactual actions."
            },
            "Czech 'Kdyby se vojenský atašé dotazoval...'. Formal diplomatic correspondence uses 'Should [subject] [base verb]...': 'Should the attache inquire...'.",
            "Executive Contract Negotiation & Dealer Relations"
        ),
        create_q(
            "TTR-SALES-C2-001-Q9",
            "The arbitration panel ruled that the delayed vehicle commissioning was _____ attributable to port blockades rather than any defect in Tatra's powertrain components.",
            {"A": "unquestionably", "B": "unequivocally", "C": "principally", "D": "hardly"},
            "C",
            {
                "correct": "In high-stakes dispute resolution, nuanced legal qualification ('principally attributable' = chiefly/primarily) accurately allocates proportional liability without absolute overclaiming.",
                "wrong_A": "'Unquestionably' is rhetorically aggressive and weakens evidentiary arbitration credibility.",
                "wrong_B": "'Unequivocally' is excessively absolute when dealing with multi-factor logistics delays.",
                "wrong_D": "'Hardly' reverses the intended meaning, suggesting Tatra was to blame."
            },
            "Czech 'převážně / v hlavní míře přičitatelné'. In arbitration findings, 'principally attributable' balances evidentiary accuracy and legal liability.",
            "International Contract Law, ICC Arbitration & Defense Tender Litigation"
        ),
        create_q(
            "TTR-SALES-C2-001-Q10",
            "Not for one moment _____ our commercial negotiation team consider conceding sovereign immunity jurisdiction to a local foreign domestic court.",
            {"A": "is", "B": "did", "C": "has", "D": "would"},
            "B",
            {
                "correct": "Fronted negative phrase 'Not for one moment' with past action verb 'consider' demands past auxiliary inversion 'did' ('Not for one moment did our team consider...').",
                "wrong_A": "'Is' cannot pair with past lexical verb 'consider'.",
                "wrong_C": "'Has' would require past participle 'considered'.",
                "wrong_D": "'Would' suggests hypothetical willingness rather than an emphatic historical fact."
            },
            "Czech 'Ani na jediný okamžik náš tým neuvažoval...'. Inverted negative construction: 'Not for one moment did our team consider...'.",
            "International Contract Law, ICC Arbitration & Defense Tender Litigation"
        )
    ]
}

# =============================================================================
# 3. TEVA ENGINEERING C2 (TEV-ENG-C2-001)
# =============================================================================
teva_eng_c2_001 = {
    "test_id": "TEV-ENG-C2-001",
    "title": "Unannounced FDA/EMA Regulatory Inspection Defense & GAMP 5 Data Integrity Disputes: Diplomatic Counter-Argumentation",
    "level": "C2",
    "category": "core",
    "workplace_track": "Regulatory Health Authority Audits, GAMP 5 & Computerized System Validation",
    "estimated_time_minutes": 20,
    "description": "Lead CSV and sterile facility engineering responses: addressing FDA Form 483 inspection observations, defending SCADA audit trails, and framing cleanroom HVAC cascade mitigations without admitting willful non-compliance.",
    "learning_objectives": [
        "Master diplomatic counter-argumentation during high-stakes health authority audits",
        "Formulate precise passive hedging in computerized system validation (CSV) audit defenses",
        "Utilize formal mandative and inverted structures in regulatory corrective action plans"
    ],
    "questions": [
        create_q(
            "TEV-ENG-C2-001-Q1",
            "On no account _____ authorized cleanroom operators share administrative credentials to bypass electronic signature controls on the Lyophilizer SCADA terminal.",
            {"A": "the personnel may", "B": "may authorized", "C": "personnel should", "D": "are to"},
            "B",
            {
                "correct": "Fronted negative restrictive prepositional phrase 'On no account' requires subject-auxiliary inversion ('may authorized cleanroom operators share').",
                "wrong_A": "Lacks required inversion after fronted negative phrase.",
                "wrong_C": "Direct word order violates the formal inversion rule.",
                "wrong_D": "'Are to' creates invalid syntax with the sentence structure."
            },
            "Czech 'Za žádných okolností nesmí operátoři sdílet...'. In formal GMP SOPs and audit responses, use fronted inversion: 'On no account may authorized operators share...'.",
            "Computerized System Validation (CSV & GAMP 5)"
        ),
        create_q(
            "TEV-ENG-C2-001-Q2",
            "While the FDA inspector noted an apparent audit trail gap, our forensic server telemetry _____ that the system was undergoing pre-scheduled NTP synchronization.",
            {"A": "categorically proves beyond all shadow of doubt", "B": "unmistakably and undeniably asserts", "C": "would appear to substantiate", "D": "is shouting out"},
            "C",
            {
                "correct": "In regulatory audit responses, diplomatic epistemic hedging ('would appear to substantiate') demonstrates objective scientific rigor without triggering regulatory antagonism.",
                "wrong_A": "Excessively emotional and absolute phrasing ('beyond all shadow of doubt') is considered unprofessional in official FDA 483 responses.",
                "wrong_B": "Confrontational and unscientific register.",
                "wrong_D": "Colloquial idiom completely out of place in pharmaceutical regulatory governance."
            },
            "Czech 'se zdá potvrzovat / nasvědčuje tomu'. In FDA 483 responses, avoid belligerent claims; use refined hedging like 'would appear to substantiate'.",
            "Regulatory Health Authority Audits, GAMP 5 & Computerized System Validation"
        ),
        create_q(
            "TEV-ENG-C2-001-Q3",
            "_____ the computerized building management system (BMS) executed an automated failover during the cleanroom pressure drop, the Grade B aseptic envelope would have remained compromised.",
            {"A": "Had not", "B": "Were not", "C": "Had", "D": "Should not"},
            "A",
            {
                "correct": "Inverted third conditional negative ('Had not the computerized BMS executed...' or 'Had the computerized BMS not executed...') describes a past counterfactual disaster that was successfully prevented.",
                "wrong_B": "'Were not' cannot pair with past participle 'executed'.",
                "wrong_C": "Positive 'Had' would mean the failure occurred BECAUSE of the failover, reversing the causal reality.",
                "wrong_D": "'Should not' applies to future possibilities, not historical past incidents."
            },
            "Czech 'Kdyby systém neprovedl automatické přepnutí...'. High-register validation reporting inverts 'had': 'Had the BMS not executed...'.",
            "Cleanroom HVAC Cascades & Differential Pressure"
        ),
        create_q(
            "TEV-ENG-C2-001-Q4",
            "The Corporate Quality Assurance Directorate mandated that the validation lead engineer _____ an immediate retrospection audit of all GAMP Category 4 configurable software packages.",
            {"A": "undertake", "B": "undertakes", "C": "shall undertake", "D": "is undertaking"},
            "A",
            {
                "correct": "Mandative subjunctive after 'mandated that' requires the uninflected base verb 'undertake'.",
                "wrong_B": "Third person singular 'undertakes' violates the mandative subjunctive mood required in formal quality directives.",
                "wrong_C": "'Shall undertake' is valid in contractual obligations, but after 'mandated that', standard high-register English uses the bare subjunctive.",
                "wrong_D": "Continuous aspect is incorrect in formal administrative directives."
            },
            "Czech 'vedení nařídilo, aby vedoucí inženýr provedl...'. Mandative subjunctive: 'mandated that the engineer undertake...'.",
            "Computerized System Validation (CSV & GAMP 5)"
        ),
        create_q(
            "TEV-ENG-C2-001-Q5",
            "Rarely _____ an unannounced regulatory health inspection uncover zero computerized system validation discrepancies across an entire multi-suite sterile filling facility.",
            {"A": "an inspector does", "B": "is", "C": "does", "D": "has"},
            "C",
            {
                "correct": "Fronted negative frequency adverb 'Rarely' followed by singular subject 'an inspection' and base verb 'uncover' requires dummy auxiliary inversion 'does' ('Rarely does an inspection uncover...').",
                "wrong_A": "Lacks required inversion after fronted restrictive adverb.",
                "wrong_B": "'Is' cannot invert with base action verb 'uncover'.",
                "wrong_D": "'Has' would require past participle 'uncovered'."
            },
            "Czech 'Zřídkakdy neohlášená inspekce neodhalí...'. English fronted 'Rarely' forces inversion: 'Rarely does an unannounced inspection uncover...'.",
            "Regulatory Health Authority Audits, GAMP 5 & Computerized System Validation"
        ),
        create_q(
            "TEV-ENG-C2-001-Q6",
            "The engineering remediation plan must be executed rigorously, _____ the regulatory body serve a formal Warning Letter against the sterile manufacturing plant.",
            {"A": "in order not", "B": "lest", "C": "unless that", "D": "otherwise that"},
            "B",
            {
                "correct": "Formal conjunction 'lest' ('for fear that') introduces a severe regulatory consequence and takes the subjunctive verb 'serve'.",
                "wrong_A": "'In order not' requires infinitive with 'to', not a full clause with subject.",
                "wrong_C": "'Unless that' is ungrammatical in standard English.",
                "wrong_D": "'Otherwise that' is a literal Czenglish transfer error (*jinak aby ne*)."
            },
            "Czech 'aby inspekční orgán nevydal varovný dopis...'. Formal English uses 'lest [subject] [subjunctive verb]': 'lest the regulatory body serve a Warning Letter'.",
            "Regulatory Health Authority Audits, GAMP 5 & Computerized System Validation"
        ),
        create_q(
            "TEV-ENG-C2-001-Q7",
            "Hardly had the CIP (Clean-in-Place) caustic wash cycle terminated _____ the inline conductivity sensor recorded an out-of-specification rinse water reading.",
            {"A": "than", "B": "that", "C": "after", "D": "when"},
            "D",
            {
                "correct": "'Hardly had [event]... when [second event]' is the strictly required correlative conjunction in formal technical reporting.",
                "wrong_A": "'Than' pairs with 'No sooner', not 'Hardly'.",
                "wrong_B": "'That' cannot act as the correlative conjunction for 'Hardly'.",
                "wrong_C": "'After' is grammatically redundant with past perfect auxiliary inversion."
            },
            "Czech 'Sotva skončil promývací cyklus, když v tom...'. 'Hardly had...' must always be paired with 'WHEN'.",
            "Cleanroom HVAC Cascades & Differential Pressure"
        ),
        create_q(
            "TEV-ENG-C2-001-Q8",
            "_____ an audit trail discrepancy arise in the batch release record, the Qualified Person (QP) must suspend lot disposition immediately.",
            {"A": "Should", "B": "Were", "C": "Had", "D": "If so"},
            "A",
            {
                "correct": "Inverted first conditional ('Should an audit trail discrepancy arise...') represents formal GMP standard operating procedure phrasing for future eventualities.",
                "wrong_B": "'Were' would require 'to arise', not bare infinitive 'arise'.",
                "wrong_C": "'Had' pairs with past counterfactual events, not future disposition procedures.",
                "wrong_D": "'If so' cannot act as a subordinate conditional clause conjunction."
            },
            "Czech 'Pokud by vznikla jakákoliv nesrovnalost...'. In formal SOP guidelines, use 'Should an audit trail discrepancy arise...'.",
            "Computerized System Validation (CSV & GAMP 5)"
        ),
        create_q(
            "TEV-ENG-C2-001-Q9",
            "The observed particle count excursion during vial stoppling cannot _____ solely to operator gowning shedding without evaluating HEPA filter face velocity.",
            {"A": "conclusively ascribe", "B": "ascribe itself", "C": "rationally be ascribed", "D": "be having ascribed"},
            "C",
            {
                "correct": "Passive modal construction with cognitive hedging ('cannot rationally be ascribed to...') accurately qualifies root cause analysis in pharmaceutical quality risk management.",
                "wrong_A": "Active voice 'ascribe' cannot have the inanimate excursion as its subject.",
                "wrong_B": "'Ascribe itself' is a direct Czenglish reflexive error (*připisovat se*).",
                "wrong_D": "Ungrammatical progressive passive construction."
            },
            "Czech 'odchylku nelze rozumně přičítat pouze...'. Do not translate reflexively (*ascribe itself*). Use passive modal 'cannot rationally be ascribed to...'.",
            "Sterile Compounding & Filling Line Automation"
        ),
        create_q(
            "TEV-ENG-C2-001-Q10",
            "Little _____ the plant automation team realize that a legacy firmware update on the programmable logic controller would corrupt historical 21 CFR Part 11 electronic signatures.",
            {"A": "was", "B": "did", "C": "has", "D": "had"},
            "B",
            {
                "correct": "Fronted restrictive adverb 'Little' followed by base lexical verb 'realize' requires past auxiliary inversion 'did' ('Little did the team realize...').",
                "wrong_A": "'Was' cannot invert with base action verb 'realize'.",
                "wrong_C": "'Has' would require past participle 'realized'.",
                "wrong_D": "'Had' creates awkward double-past perfect with 'would corrupt'."
            },
            "Czech 'Tým si vůbec neuvědomoval, že...'. Formal dramatic negative inversion in incident post-mortems: 'Little did the plant automation team realize...'.",
            "Computerized System Validation (CSV & GAMP 5)"
        )
    ]
}

# =============================================================================
# 4. TAPI CHEMISTRY C2 (TAPI-CHEM-C2-001)
# =============================================================================
tapi_chem_c2_001 = {
    "test_id": "TAPI-CHEM-C2-001",
    "title": "Pharmacopeial Monograph Harmonization, Nitrosamine Mutagenic Risk Defenses & ICH Q2(R2) Disputes",
    "level": "C2",
    "category": "core",
    "workplace_track": "Pharmacopeial Compliance, Impurity Profiling & Regulatory Submissions",
    "estimated_time_minutes": 20,
    "description": "Expert analytical chemistry defenses: arguing chromatographic peak co-elution resolution, justifying mutagenic nitrosamine purge factors, and negotiating monograph variations with EDQM/USP pharmacopeial committees.",
    "learning_objectives": [
        "Master scientific epistemic hedging in pharmacopeial monograph dispute committees",
        "Formulate precise negative inversion in analytical method validation reports",
        "Articulate complex risk-based impurity arguments adhering to ICH Q2(R2) and ICH M7"
    ],
    "questions": [
        create_q(
            "TAPI-CHEM-C2-001-Q1",
            "At no time _____ the synthesis reaction temperature exceed 45°C during the exothermic addition of thionyl chloride, lest thermal degradation generate genotoxic impurities.",
            {"A": "the operator must permit", "B": "must the batch operator permit", "C": "the batch operator will permit", "D": "must the operator to permit"},
            "B",
            {
                "correct": "Fronted negative restrictive phrase 'At no time' requires subject-auxiliary inversion ('must the batch operator permit').",
                "wrong_A": "Lacks required inversion after fronted negative phrase.",
                "wrong_C": "Standard word order violates the formal inversion rule.",
                "wrong_D": "Modal 'must' cannot pair with infinitive 'to permit'."
            },
            "Czech 'V žádném okamžiku nesmí operátor překročit...'. In English batch manufacturing records, use fronted inversion: 'At no time must the operator permit...'.",
            "Organic Chemical Synthesis & Batch Reactors"
        ),
        create_q(
            "TAPI-CHEM-C2-001-Q2",
            "The trace peak observed at relative retention time (RRT) 1.24 _____ to co-eluting excipient degradation rather than an unclassified mutagenic nitrosamine precursor.",
            {"A": "manifestly and unquestionably corresponds", "B": "definitely screams out evidence", "C": "would tentatively seem attributable", "D": "is undeniably bound to pertain"},
            "C",
            {
                "correct": "In health authority analytical disputes, sophisticated epistemic hedging ('would tentatively seem attributable') is essential until LC-MS/MS fragment validation confirms the molecular formula.",
                "wrong_A": "Prematurely absolute claim without orthogonal mass spectrometry validation.",
                "wrong_B": "Colloquial and highly unprofessional.",
                "wrong_D": "Aggressive, unscientific register."
            },
            "Czech 'by se předběžně dalo přičítat...'. In pharmacopeial analytical reports, use elegant scientific hedging: 'would tentatively seem attributable'.",
            "Analytical Chemistry (HPLC, GC, Spectroscopy)"
        ),
        create_q(
            "TAPI-CHEM-C2-001-Q3",
            "_____ the analytical development team validated the chiral HPLC stationary phase at lower flow rates, the enantiomeric purity resolution would have met ICH Q2(R2) acceptance criteria.",
            {"A": "Had", "B": "If", "C": "Were", "D": "Should"},
            "A",
            {
                "correct": "Inverted third conditional ('Had the analytical team validated...') expresses formal past counterfactual technical conditions without using 'if'.",
                "wrong_B": "'If' requires uninverted syntax ('If the analytical team had validated...').",
                "wrong_C": "'Were' pairs with present/future hypothetical conditions, not past completed validation studies.",
                "wrong_D": "'Should' expresses future contingencies."
            },
            "Czech 'Kdyby tým validoval...'. In elevated technical chemistry reporting, omit 'if' via inversion: 'Had the analytical development team validated...'.",
            "Analytical Chemistry (HPLC, GC, Spectroscopy)"
        ),
        create_q(
            "TAPI-CHEM-C2-001-Q4",
            "The European Directorate for the Quality of Medicines (EDQM) requested that the API manufacturer _____ the limit of detection (LOD) for residual dimethylformamide to 10 ppm.",
            {"A": "lower", "B": "lowers", "C": "must lower", "D": "to lower"},
            "A",
            {
                "correct": "Mandative subjunctive after 'requested that' requires the uninflected base verb 'lower'.",
                "wrong_B": "Third person singular 'lowers' violates the required mandative subjunctive mood.",
                "wrong_C": "Modal 'must' is redundant and colloquially informal in a formal subjunctive clause.",
                "wrong_D": "Infinitive 'to lower' is ungrammatical as the finite verb of a 'that'-clause."
            },
            "Czech 'EDQM požadovalo, aby výrobce snížil...'. English mandative subjunctive uses the bare base verb: 'requested that the manufacturer lower...'.",
            "Pharmacopeial Compliance, Impurity Profiling & Regulatory Submissions"
        ),
        create_q(
            "TAPI-CHEM-C2-001-Q5",
            "Under no circumstances _____ hazardous chlorinated solvents be disposed of into the standard aqueous effluent recovery pipeline.",
            {"A": "an operator can", "B": "is", "C": "may", "D": "will an operator to"},
            "C",
            {
                "correct": "Fronted negative phrase 'Under no circumstances' followed by passive subject 'hazardous solvents' requires auxiliary inversion 'may' ('Under no circumstances may hazardous solvents be disposed...').",
                "wrong_A": "Lacks required auxiliary-subject inversion.",
                "wrong_B": "'Is' cannot pair with plural passive subject 'solvents'.",
                "wrong_D": "'Will... to' is ungrammatical."
            },
            "Czech 'Za žádných okolností nesmí být rozpouštědla vypouštěna...'. Formal inversion: 'Under no circumstances may hazardous solvents be disposed of...'.",
            "Hazardous Reagents, Solvent Recovery & Lab Safety"
        ),
        create_q(
            "TAPI-CHEM-C2-001-Q6",
            "The regulatory dossier must demonstrate a purge factor of greater than 1000 for mutagenic acyl chlorides, _____ the European Medicines Agency reject the marketing authorization.",
            {"A": "otherwise that", "B": "lest", "C": "in case", "D": "for that"},
            "B",
            {
                "correct": "Formal conjunction 'lest' ('for fear that') introduces a severe regulatory consequence and takes the subjunctive verb 'reject'.",
                "wrong_A": "'Otherwise that' is a literal Czech translation mistake (*jinak aby*).",
                "wrong_C": "'In case' expresses precaution, not consequence.",
                "wrong_D": "'For that' is archaic and ungrammatical in modern regulatory English."
            },
            "Czech 'aby Evropská léková agentura nezamítla...'. High-register regulatory submission English uses 'lest [agency] [subjunctive verb]': 'lest the EMA reject...'.",
            "Pharmacopeial Compliance, Impurity Profiling & Regulatory Submissions"
        ),
        create_q(
            "TAPI-CHEM-C2-001-Q7",
            "Scarcely had the crystallization slurry been cooled to 5°C _____ the active pharmaceutical ingredient began precipitating in the undesired polymorphic form.",
            {"A": "than", "B": "that", "C": "after", "D": "when"},
            "D",
            {
                "correct": "'Scarcely had [action]... when [second action]' is the strictly required correlative pair.",
                "wrong_A": "'Than' pairs with 'No sooner had...', not 'Scarcely'.",
                "wrong_B": "'That' cannot act as correlative temporal conjunction.",
                "wrong_C": "'After' is redundant with past perfect auxiliary inversion."
            },
            "Czech 'Sotva byla krystalizační suspenze ochlazena, když v tom...'. Correlative pair for 'Scarcely had...' is always 'WHEN'.",
            "Organic Chemical Synthesis & Batch Reactors"
        ),
        create_q(
            "TAPI-CHEM-C2-001-Q8",
            "_____ an unknown chromatographic impurity exceed the 0.05% identification threshold, the QC laboratory must isolate the fraction for nuclear magnetic resonance (NMR) characterization.",
            {"A": "Should", "B": "Were", "C": "Had", "D": "If so"},
            "A",
            {
                "correct": "Inverted first conditional ('Should an unknown impurity exceed...') represents formal pharmacopeial SOP protocol phrasing for future analytical deviations.",
                "wrong_B": "'Were' would require 'to exceed', not bare infinitive 'exceed'.",
                "wrong_C": "'Had' pairs with past counterfactual events, not future test requirements.",
                "wrong_D": "'If so' cannot act as a subordinate conditional clause conjunction."
            },
            "Czech 'Pokud by neznámá nečistota překročila...'. In formal pharmacopeial testing SOPs, use 'Should an unknown impurity exceed...'.",
            "Analytical Chemistry (HPLC, GC, Spectroscopy)"
        ),
        create_q(
            "TAPI-CHEM-C2-001-Q9",
            "The minor baseline drift observed during the gas chromatography run cannot _____ to column bleeding alone without evaluating septa deterioration.",
            {"A": "definitely impute", "B": "impute itself", "C": "legitimately be imputed", "D": "be having imputed"},
            "C",
            {
                "correct": "Passive modal construction with technical hedging ('cannot legitimately be imputed to...') accurately frames chromatographic root-cause attribution in official QC investigations.",
                "wrong_A": "Active voice 'impute' cannot take the inanimate baseline drift as its subject.",
                "wrong_B": "'Impute itself' is a literal Czech reflexive translation error (*přičítat se*).",
                "wrong_D": "Ungrammatical progressive passive construction."
            },
            "Czech 'posun základní linie nelze oprávněně přičítat pouze...'. Do not translate reflexively (*impute itself*). Use passive modal 'cannot legitimately be imputed to...'.",
            "Analytical Chemistry (HPLC, GC, Spectroscopy)"
        ),
        create_q(
            "TAPI-CHEM-C2-001-Q10",
            "Not only _____ the multi-step convergent chemical synthesis increase overall API yield, but it also curtails the formation of genotoxic reaction intermediates.",
            {"A": "is", "B": "does", "C": "has", "D": "will"},
            "B",
            {
                "correct": "Fronted correlative 'Not only' with base action verb 'increase' demands dummy auxiliary inversion 'does' ('Not only does the synthesis increase...').",
                "wrong_A": "'Is' cannot invert with base action verb 'increase'.",
                "wrong_C": "'Has' would require past participle 'increased'.",
                "wrong_D": "'Will' implies future promise rather than verified chemical fact."
            },
            "Czech 'Nejenže vícestupňová syntéza zvyšuje výtěžek..., ale také...'. English requires auxiliary inversion: 'Not only does the synthesis increase..., but it also...'.",
            "Organic Chemical Synthesis & Batch Reactors"
        )
    ]
}

# =============================================================================
# 5. TEVA IT C2 (TEV-IT-C2-001)
# =============================================================================
teva_it_c2_001 = {
    "test_id": "TEV-IT-C2-001",
    "title": "Enterprise Zero Trust Breach Disclosure, Global Cloud SLA Litigation & Board-Level Incident Governance",
    "level": "C2",
    "category": "core",
    "workplace_track": "Cybersecurity Crisis Communication, Cloud SLA Litigation & Global Compliance",
    "estimated_time_minutes": 20,
    "description": "Chief Information Security Officer (CISO) and lead architect communications: managing board-level cybersecurity crisis disclosures, litigating hyperscale cloud provider SLA failures, and framing GDPR/NIS2 breach timelines with forensic precision.",
    "learning_objectives": [
        "Master high-stakes cybersecurity crisis communication and forensic hedging",
        "Formulate board-level executive risk disclosures under GDPR and NIS2 directives",
        "Utilize negative inversion and subjunctive mandates in global cloud SLA dispute litigation"
    ],
    "questions": [
        create_q(
            "TEV-IT-C2-001-Q1",
            "Under no circumstances _____ enterprise privileged access management (PAM) tokens be stored in unencrypted repository configuration files.",
            {"A": "developers will allow", "B": "may developers allow", "C": "developers must", "D": "are developers to"},
            "B",
            {
                "correct": "Fronted negative restrictive phrase 'Under no circumstances' requires subject-auxiliary inversion ('may developers allow').",
                "wrong_A": "Lacks required inversion after fronted negative phrase.",
                "wrong_C": "Direct word order violates the formal inversion rule.",
                "wrong_D": "'Are developers to' creates invalid syntax with the sentence structure."
            },
            "Czech 'Za žádných okolností nesmí vývojáři ukládat...'. In enterprise cybersecurity policies and audit findings, use fronted inversion: 'Under no circumstances may developers allow...'.",
            "Enterprise Cybersecurity, Threat Hunting & Zero Trust"
        ),
        create_q(
            "TEV-IT-C2-001-Q2",
            "The preliminary SIEM packet capture data _____ that the unauthorized data exfiltration occurred via compromised API credentials rather than an internal insider threat.",
            {"A": "unequivocally proves beyond any argument whatsoever", "B": "is definitely yelling proof", "C": "would seem to indicate", "D": "is undeniably bound to reveal"},
            "C",
            {
                "correct": "In board-level breach disclosures and legal regulatory filings, forensic hedging ('would seem to indicate') prevents making premature assertions before digital forensics completes memory dump analysis.",
                "wrong_A": "Unprofessionally absolute and premature for ongoing cyber incident forensics.",
                "wrong_B": "Colloquial and completely unacceptable in executive communications.",
                "wrong_D": "Aggressive, unverified register."
            },
            "Czech 'by se zdálo nasvědčovat tomu, že...'. In cybersecurity forensics and GDPR breach notices, use prudent hedging: 'would seem to indicate'.",
            "Cybersecurity Crisis Communication, Cloud SLA Litigation & Global Compliance"
        ),
        create_q(
            "TEV-IT-C2-001-Q3",
            "_____ the Kubernetes orchestration cluster maintained geo-redundant automated state reconciliation, the multi-region cloud outage would not have disrupted SAP ERP batch transactions.",
            {"A": "Had", "B": "If", "C": "Were", "D": "Should"},
            "A",
            {
                "correct": "Inverted third conditional ('Had the cluster maintained...') denotes a past counterfactual architectural condition without using 'if'.",
                "wrong_B": "'If' would require uninverted syntax ('If the cluster had maintained...').",
                "wrong_C": "'Were' pairs with present/future hypothetical conditions, not completed past outages.",
                "wrong_D": "'Should' expresses future potential contingencies."
            },
            "Czech 'Kdyby cluster udržoval geo-redundanci...'. In executive cloud infrastructure post-mortems, invert 'had': 'Had the cluster maintained...'.",
            "Cloud Architecture & Hybrid Infrastructure (AWS & Azure)"
        ),
        create_q(
            "TEV-IT-C2-001-Q4",
            "The Global Chief Information Security Officer (CISO) mandated that the enterprise identity provider _____ immediate multi-factor re-authentication across all European tenant domains.",
            {"A": "enforce", "B": "enforces", "C": "shall enforce", "D": "is enforcing"},
            "A",
            {
                "correct": "Mandative subjunctive after 'mandated that' requires the uninflected base verb 'enforce'.",
                "wrong_B": "Third person singular 'enforces' violates the mandative subjunctive mood required in formal security directives.",
                "wrong_C": "'Shall enforce' is used in contracts, but standard high-register executive English uses the bare subjunctive following 'mandated that'.",
                "wrong_D": "Continuous aspect is incorrect in formal administrative directives."
            },
            "Czech 'CISO nařídil, aby poskytovatel identity vynutil...'. Mandative subjunctive: 'mandated that the provider enforce...'.",
            "Enterprise Cybersecurity, Threat Hunting & Zero Trust"
        ),
        create_q(
            "TEV-IT-C2-001-Q5",
            "Seldom _____ a Tier-IV public cloud hyperscaler suffer simultaneous availability zone power failures resulting in catastrophic database quorum loss.",
            {"A": "a cloud provider does", "B": "is", "C": "does", "D": "has"},
            "C",
            {
                "correct": "Fronted restrictive frequency adverb 'Seldom' followed by singular subject 'a hyperscaler' and base verb 'suffer' requires dummy auxiliary inversion 'does' ('Seldom does a cloud hyperscaler suffer...').",
                "wrong_A": "Lacks required inversion after fronted restrictive adverb.",
                "wrong_B": "'Is' cannot invert with base action verb 'suffer'.",
                "wrong_D": "'Has' would require past participle 'suffered'."
            },
            "Czech 'Málokdy se stane, že by poskytovatel cloudu utrpěl...'. Fronted 'Seldom' forces inversion: 'Seldom does a hyperscaler suffer...'.",
            "Cloud Architecture & Hybrid Infrastructure (AWS & Azure)"
        ),
        create_q(
            "TEV-IT-C2-001-Q6",
            "All cloud service level agreement (SLA) breach notices must be filed within 72 hours of incident resolution, _____ the enterprise forfeit its legal right to financial service credits.",
            {"A": "in order that", "B": "lest", "C": "unless that", "D": "otherwise that"},
            "B",
            {
                "correct": "Formal conjunction 'lest' ('for fear that') introduces a severe financial/legal forfeiture and takes the subjunctive verb 'forfeit'.",
                "wrong_A": "'In order that' indicates purpose, which reverses the intended prohibitive meaning.",
                "wrong_C": "'Unless that' is ungrammatical in standard English.",
                "wrong_D": "'Otherwise that' is a literal Czenglish transfer error (*jinak aby ne*)."
            },
            "Czech 'aby společnost neztratila své právní právo na slevu...'. Formal commercial contract English uses 'lest [subject] [subjunctive verb]': 'lest the enterprise forfeit...'.",
            "Cybersecurity Crisis Communication, Cloud SLA Litigation & Global Compliance"
        ),
        create_q(
            "TEV-IT-C2-001-Q7",
            "No sooner had the Red Team penetrated the peripheral VPN gateway _____ the automated Zero Trust endpoint containment policy severed the compromised session.",
            {"A": "when", "B": "that", "C": "as", "D": "than"},
            "D",
            {
                "correct": "'No sooner had [action]... than [second action]' is the strictly required correlative pair in high-level English.",
                "wrong_A": "'When' pairs with 'Scarcely' or 'Hardly', not 'No sooner'.",
                "wrong_B": "'That' cannot introduce the temporal correlative clause.",
                "wrong_C": "'As' is colloquial and grammatically invalid here."
            },
            "Czech 'Sotva útočník pronikl... než systém okamžitě odpojil relaci'. Always pair 'No sooner had...' with 'THAN'.",
            "Enterprise Cybersecurity, Threat Hunting & Zero Trust"
        ),
        create_q(
            "TEV-IT-C2-001-Q8",
            "_____ an unauthorized data breach impact EU citizen personal identifiable information (PII), the Data Protection Officer must notify the supervisory authority within 72 hours under GDPR Article 33.",
            {"A": "Should", "B": "Were", "C": "Had", "D": "If so"},
            "A",
            {
                "correct": "Inverted first conditional ('Should an unauthorized breach impact...') denotes formal regulatory compliance protocol phrasing for future eventualities.",
                "wrong_B": "'Were' would require 'to impact', not bare infinitive 'impact'.",
                "wrong_C": "'Had' pairs with past counterfactual events, not future compliance notification procedures.",
                "wrong_D": "'If so' cannot act as a subordinate conditional clause conjunction."
            },
            "Czech 'Pokud by neoprávněný únik zasáhl...'. In formal compliance protocols, use 'Should a data breach impact...'.",
            "Cybersecurity Crisis Communication, Cloud SLA Litigation & Global Compliance"
        ),
        create_q(
            "TEV-IT-C2-001-Q9",
            "The latency degradation experienced by remote users cannot _____ solely to domestic ISP peering bottlenecks without auditing enterprise egress proxy logs.",
            {"A": "unquestionably blame", "B": "blame itself", "C": "plausibly be attributed", "D": "be having blamed"},
            "C",
            {
                "correct": "Passive modal construction with technical hedging ('cannot plausibly be attributed to...') accurately qualifies root cause analysis in complex distributed IT enterprise networks.",
                "wrong_A": "Active voice 'blame' cannot take the inanimate latency degradation as its subject.",
                "wrong_B": "'Blame itself' is a literal Czech reflexive error (*přičítat se*).",
                "wrong_D": "Ungrammatical progressive passive construction."
            },
            "Czech 'zhoršení odezvy nelze věrohodně přičítat pouze...'. Do not translate reflexively (*blame itself*). Use passive modal 'cannot plausibly be attributed to...'.",
            "Cloud Architecture & Hybrid Infrastructure (AWS & Azure)"
        ),
        create_q(
            "TEV-IT-C2-001-Q10",
            "Not for one second _____ the enterprise incident response team consider paying a ransomware extortion demand in cryptocurrency.",
            {"A": "is", "B": "did", "C": "has", "D": "would"},
            "B",
            {
                "correct": "Fronted negative phrase 'Not for one second' with past action verb 'consider' requires past auxiliary inversion 'did' ('Not for one second did the team consider...').",
                "wrong_A": "'Is' cannot invert with past lexical verb 'consider'.",
                "wrong_C": "'Has' would require past participle 'considered'.",
                "wrong_D": "'Would' suggests hypothetical willingness rather than an emphatic historical fact."
            },
            "Czech 'Ani na vteřinu tým neuvažoval o zaplacení...'. Inverted negative construction: 'Not for one second did the team consider...'.",
            "Enterprise Cybersecurity, Threat Hunting & Zero Trust"
        )
    ]
}

ALL_C2_TESTS = {
    "tatra-engineering": tatra_eng_c2_001,
    "tatra-sales-engineering": tatra_sales_c2_001,
    "teva-engineering": teva_eng_c2_001,
    "tapi-chemistry": tapi_chem_c2_001,
    "teva-it": teva_it_c2_001
}

def install_c2():
    print("Installing C2 (Executive Mastery Tier) across all 5 suites...\n")

    for suite_slug, test_data in ALL_C2_TESTS.items():
        suite_dir = ROOT / suite_slug
        tests_dir = suite_dir / "data" / "tests"
        tests_dir.mkdir(parents=True, exist_ok=True)

        # 1. Save C2 test JSON
        test_file = tests_dir / f"{test_data['test_id']}.json"
        with open(test_file, "w", encoding="utf-8") as f:
            json.dump(test_data, f, indent=2, ensure_ascii=False)
        print(f"  [OK] Saved {test_file.name} in {suite_slug}")

        # 2. Update curriculum manifest JSON & manifest.js
        manifest_file = suite_dir / "data" / "curriculum_manifest.json"
        with open(manifest_file, "r", encoding="utf-8") as f:
            manifest = json.load(f)

        # Check if C2 already in manifest
        c2_entry = {
            "test_id": test_data["test_id"],
            "title": test_data["title"],
            "level": "C2",
            "category": "core",
            "workplace_track": test_data["workplace_track"],
            "estimated_time_minutes": test_data["estimated_time_minutes"],
            "description": test_data["description"],
            "grammar_focus": "Negative Inversion, Formal Subjunctive & Executive Epistemic Hedging"
        }
        
        # Replace or append
        manifest = [m for m in manifest if m["test_id"] != test_data["test_id"]]
        manifest.append(c2_entry)

        with open(manifest_file, "w", encoding="utf-8") as f:
            json.dump(manifest, f, indent=2, ensure_ascii=False)

        with open(suite_dir / "data" / "manifest.js", "w", encoding="utf-8") as f:
            f.write(f"window.CURRICULUM_MANIFEST = {json.dumps(manifest, indent=2, ensure_ascii=False)};\n")

        # 3. Update tests_registry.js for offline runner
        tests_in_suite = {}
        for tf in tests_dir.glob("*.json"):
            try:
                with open(tf, "r", encoding="utf-8") as f:
                    t_obj = json.load(f)
                    tests_in_suite[t_obj["test_id"]] = t_obj
            except Exception:
                pass

        with open(suite_dir / "data" / "tests_registry.js", "w", encoding="utf-8") as f:
            f.write(f"window.TEST_REGISTRY = window.TEST_REGISTRY || {{}};\nObject.assign(window.TEST_REGISTRY, {json.dumps(tests_in_suite, indent=2, ensure_ascii=False)});\n")

        print(f"  [OK] Updated manifest and tests_registry for {suite_slug}")

    print("\nAll C2 tests successfully generated and integrated!")

if __name__ == "__main__":
    install_c2()
