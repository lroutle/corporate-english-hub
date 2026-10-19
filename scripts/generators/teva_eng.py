"""
Generator for all 80 Teva Engineering modules (20 A2, 20 B1, 20 B2, 20 C2).
Preserves existing validated modules and procedural-generates the remainder with high pedagogical rigor.
"""

import sys
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(ROOT / "scripts"))

from curriculum_catalog import get_teva_eng_curriculum
from generators.common import make_q, build_test_module, KEY_PATTERN

EXISTING_TESTS_DIR = ROOT / "teva-engineering" / "data" / "tests"

A2_TEVA_SCENARIOS = [
    ("The cleanroom operator", "sterile nitrile gloves before passing through the Grade B airlock", "wear", "wears", "wore", "wearing", "Czech 'operátor nosí'. English 3rd person singular takes -s: 'wears'."),
    ("The validation technician", "the differential pressure display on panel DP-04 every morning", "check", "checks", "checked", "checking", "Singular subject takes 'checks' with -s."),
    ("The automation engineer", "the emergency stop button on the blistering line immediately", "press", "presses", "pressed", "pressing", "Verb ending in -ss takes -es: 'presses'."),
    ("The autoclave operator", "the temperature recording chart at the end of each sterilization cycle", "sign", "signs", "signed", "signing", "Czech 'operátor podepisuje'. Use 'signs'."),
    ("The HVAC specialist", "the pre-filter cartridge in air handling unit AHU-02 once a month", "replace", "replaces", "replaced", "replacing", "Singular subject takes 'replaces'."),
    ("The maintenance technician", "the peristaltic pump roller assembly before starting sterile batch compounding", "lubricate", "lubricates", "lubricated", "lubricating", "Singular subject takes 'lubricates'."),
    ("The calibration technician", "the certified digital manometer across the cleanroom pressure barrier", "connect", "connects", "connected", "connecting", "Singular subject takes 'connects'."),
    ("The packaging operator", "defective glass ampoules into the designated biohazard sharps container", "discard", "discards", "discarded", "discarding", "Singular subject takes 'discards'."),
    ("The shift supervisor", "the automated SCADA batch release report before leaving the floor", "print", "prints", "printed", "printing", "Singular subject takes 'prints'."),
    ("The facility technician", "the pure steam generator boiler pressure reading in bar gauge", "record", "records", "recorded", "recording", "Singular subject takes 'records'.")
]

def generate_a2_question(module_meta, q_idx):
    qid = f"{module_meta['test_id']}-Q{q_idx+1}"
    target_k = KEY_PATTERN[q_idx % len(KEY_PATTERN)]
    sc = A2_TEVA_SCENARIOS[q_idx % len(A2_TEVA_SCENARIOS)]
    subj, context, v_base, v_3rd, v_past, v_ing, cz_note = sc
    mod_num = int(module_meta['test_id'].split('-')[-1])

    if mod_num in [1, 7, 19, 20]: # Imperatives & Safety Directives
        prompt = f"Always remember to _____ {context} to prevent cleanroom contamination."
        correct_text = v_base
        distractors = ["to " + v_base, v_3rd, v_ing]
        correct_exp = f"'remember to' is followed by base infinitive '{v_base}' without double-to or inflections."
        distractor_exps = [
            f"'to {v_base}' causes ungrammatical double 'to'.",
            f"3rd person '{v_3rd}' cannot follow infinitive marker 'to'.",
            f"Participle '{v_ing}' does not form the standard infinitive directive here."
        ]
        cz_pt = f"Czech 'nezapomeňte zkontrolovat'. After 'remember to', use base form '{v_base}'."
    elif mod_num in [3, 10, 18]: # Past Simple
        prompt = f"Yesterday during the evening shift, {subj.lower()} _____ {context}."
        correct_text = v_past
        distractors = [v_base, "has " + v_past, "is " + v_ing]
        correct_exp = f"Specific past adverbial 'Yesterday' strictly requires Past Simple '{v_past}'."
        distractor_exps = [
            f"Base form '{v_base}' lacks past tense marking.",
            f"Present Perfect 'has {v_past}' cannot accompany 'yesterday'.",
            f"Present Continuous describes current actions, not yesterday's finished events."
        ]
        cz_pt = f"Czech uses the same past tense, but in English, 'yesterday' strictly triggers Past Simple ('{v_past}')."
    elif mod_num in [4, 12, 13]: # Prepositions of Place
        preps = ["inside", "between", "above", "next to", "under", "behind", "into", "across", "along", "against"]
        target_p = preps[q_idx % len(preps)]
        prompt = f"The differential pressure sensor is mounted on the wall _____ the airlock doors."
        correct_text = target_p
        distractors = [p for p in preps if p != target_p][:3]
        correct_exp = f"Preposition '{target_p}' accurately identifies the physical cleanroom placement."
        distractor_exps = [
            f"Preposition '{distractors[0]}' expresses incorrect spatial positioning.",
            f"Preposition '{distractors[1]}' is incompatible with the wall mount geometry.",
            f"Preposition '{distractors[2]}' indicates wrong direction."
        ]
        cz_pt = "Cleanroom spatial prepositions: 'between the airlock doors' = mezi dveřmi propusti."
    else: # Present Simple
        prompt = f"{subj} routinely _____ {context}."
        correct_text = v_3rd
        distractors = [v_base, v_ing, "is " + v_base]
        correct_exp = f"Singular subject takes 3rd person singular Present Simple with '-s' ('{v_3rd}')."
        distractor_exps = [
            f"Base form '{v_base}' lacks singular '-s'.",
            f"Participle '{v_ing}' cannot act as finite verb without auxiliary.",
            f"'is {v_base}' is an ungrammatical verb phrase."
        ]
        cz_pt = cz_note

    opts = {target_k: correct_text}
    other_keys = [k for k in ["A", "B", "C", "D"] if k != target_k]
    exps = {"correct": correct_exp}
    for i, ok in enumerate(other_keys):
        opts[ok] = distractors[i]
        exps[f"wrong_{ok}"] = distractor_exps[i]

    return make_q(qid, prompt, opts, target_k, exps, cz_pt, module_meta["workplace_track"])

def generate_b1_question(module_meta, q_idx):
    qid = f"{module_meta['test_id']}-Q{q_idx+1}"
    target_k = KEY_PATTERN[q_idx % len(KEY_PATTERN)]
    mod_num = int(module_meta['test_id'].split('-')[-1])

    b1_contexts = [
        ("the cleanroom differential pressure cascade", "restore", "had been restored", "was restored", "has been restored", "restoring"),
        ("the HEPA filter DOP aerosol penetration test", "execute", "had been executed", "was executed", "has been executed", "executing"),
        ("the automated autoclave chamber thermocouple calibration", "verify", "had been verified", "was verified", "has been verified", "verifying"),
        ("the WFI distribution loop ozone sanitization cycle", "complete", "had been completed", "was completed", "has been completed", "completing"),
        ("the sterile filling needle peristaltic pump tubing", "sanitize", "had been sanitized", "was sanitized", "has been sanitized", "sanitizing"),
        ("the Lyophilizer condenser vacuum seal integrity", "test", "had been tested", "was tested", "has been tested", "testing"),
        ("the SCADA automated alarm threshold limits", "reconfigure", "had been reconfigured", "was reconfigured", "has been reconfigured", "reconfiguring"),
        ("the rotary tablet press upper punch lubrication", "inspect", "had been inspected", "was inspected", "has been inspected", "inspecting"),
        ("the vaporized hydrogen peroxide (VHP) decontamination protocol", "validate", "had been validated", "was validated", "has been validated", "validating"),
        ("the cleanroom air change rate per hour calculation", "audit", "had been audited", "was audited", "has been audited", "auditing")
    ]
    system, action, had_been, was_v, has_been, v_ing = b1_contexts[q_idx % len(b1_contexts)]

    if mod_num in [1, 6, 16]: # Past Simple vs Past Perfect
        prompt = f"By the time the QA compliance auditor entered the sterile suite, {system} _____ by facility engineering."
        correct_text = had_been
        distractors = [was_v, has_been, "didn't " + action]
        correct_exp = f"Past Perfect Passive ('{had_been}') is required because the engineering action preceded the auditor's past entry."
        distractor_exps = [
            f"Past Simple ('{was_v}') fails to indicate completion prior to 'entered'.",
            f"Present Perfect ('{has_been}') cannot connect to completed past reference frame 'entered'.",
            f"'didn't {action}' is active voice; cleanroom systems are acted upon passively."
        ]
        cz_pt = "Czech narrative uses past tense for both ('než vstoupil, systém byl zkontrolován'). In GxP engineering reports, use Past Perfect."
    elif mod_num in [3, 13]: # Conditionals in SCADA & HVAC
        prompt = f"If the cleanroom differential pressure _____ below 15 Pascals, the SCADA alarm triggers a visual red beacon."
        correct_text = "drops"
        distractors = ["will drop", "would drop", "dropped"]
        correct_exp = "First conditional if-clause takes Present Simple ('drops') for automated physical rules."
        distractor_exps = [
            "Cannot use 'will' in the conditional if-clause.",
            "Cannot use 'would' in a real First Conditional.",
            "Past tense 'dropped' forms an unreal condition, mismatched with present 'triggers'."
        ]
        cz_pt = "Never use 'will' in conditional if-clauses (*If pressure will drop*). Use Present Simple: 'If pressure drops'."
    else: # Passive voice in GMP SOPs
        prompt = f"All sterile filling equipment parts _____ according to validated SOP-ENG-204 prior to batch compounding."
        correct_text = "must be autoclaved"
        distractors = ["must to be autoclaved", "must autoclave", "are must be autoclaved"]
        correct_exp = "Passive construction with modal: 'must be autoclaved'."
        distractor_exps = [
            "'must to be' is ungrammatical; modal 'must' takes bare infinitive.",
            "'must autoclave' is active voice; parts do not autoclave themselves.",
            "'are must' is completely ungrammatical in English."
        ]
        cz_pt = "GxP SOP phrasing strictly requires passive voice with modals: 'must be autoclaved' (musí být autoklávovány)."

    opts = {target_k: correct_text}
    other_keys = [k for k in ["A", "B", "C", "D"] if k != target_k]
    exps = {"correct": correct_exp}
    for i, ok in enumerate(other_keys):
        opts[ok] = distractors[i]
        exps[f"wrong_{ok}"] = distractor_exps[i]

    return make_q(qid, prompt, opts, target_k, exps, cz_pt, module_meta["workplace_track"])

def generate_b2_question(module_meta, q_idx):
    qid = f"{module_meta['test_id']}-Q{q_idx+1}"
    target_k = KEY_PATTERN[q_idx % len(KEY_PATTERN)]
    mod_num = int(module_meta['test_id'].split('-')[-1])

    b2_scenarios = [
        ("The GAMP 5 validation protocol requires that the computerized SCADA system _____ all audit trail events in an unalterable database.", "archive", "archives", "shall archive", "must to archive", "Mandative subjunctive after 'requires that' takes base form 'archive'."),
        ("Under no circumstances _____ allow unauthorized maintenance personnel to bypass the cleanroom interlock logic.", "should technicians", "technicians should", "technicians must to", "shall technicians to", "Negative inversion: 'Under no circumstances should technicians allow'."),
        ("It is imperative that each electronic batch record signature _____ authenticated with biometric or multi-factor credentials.", "be", "is", "will be", "must to be", "Formulaic subjunctive after 'imperative that' requires base form 'be'."),
        ("Had the HVAC engineering team tuned the PID loop parameters earlier, the differential pressure excursion _____ averted.", "would have been", "would be", "had been", "will be", "Inverted Third Conditional passive result: 'would have been averted'."),
        ("The Lead CSV Engineer insisted that GAMP Category 4 configured software _____ rigorously re-qualified post-patching.", "be", "is", "was", "will be", "Passive mandative subjunctive: 'insisted that software be re-qualified'."),
        ("Rarely _____ an unannounced regulatory audit occur without immediate inspection of computerized system audit trail logs.", "does", "is", "will", "has", "Negative inversion: 'Rarely does an audit occur'."),
        ("If the cleanroom HEPA filters had been integrity tested on schedule, particle count contamination _____ an issue today.", "would not be", "would not have been", "will not be", "is not", "Mixed conditional: past action ('had been tested') with present state ('today') takes 'would not be'."),
        ("The FDA guidance stipulates that automated batch release algorithms _____ subjected to challenging worst-case boundary tests.", "be", "are", "will be", "must to be", "Mandative subjunctive in FDA guidelines: 'stipulates that algorithms be subjected'."),
        ("Only by executing comprehensive User Requirements Specifications (URS) _____ achieve seamless Operational Qualification (OQ).", "can the validation team", "the validation team can", "the validation team could", "was the validation team can", "Inversion after 'Only by...': 'can the validation team achieve'."),
        ("Were the computerized filling line _____ an unexplained sensor drift, automated emergency stop routines would halt production immediately.", "to experience", "experiences", "will experience", "would experience", "Inverted Second Conditional: 'Were the filling line to experience...' expresses formal hypothetical condition.")
    ]
    prompt, correct_text, w1, w2, w3, rule = b2_scenarios[q_idx % len(b2_scenarios)]
    distractors = [w1, w2, w3]
    correct_exp = f"B2 GxP validation syntax: {rule}"
    distractor_exps = [
        f"Option '{w1}' violates formal mandative subjunctive or inversion rules.",
        f"Option '{w2}' applies inappropriate indicative or non-inverted syntax.",
        f"Option '{w3}' is ungrammatical in standard pharmaceutical engineering documentation."
    ]
    cz_pt = "Pharmaceutical validation English strictly prioritizes mandative subjunctive ('mandate that it be tested') and auxiliary inversion ('Under no circumstances should technicians bypass')."

    opts = {target_k: correct_text}
    other_keys = [k for k in ["A", "B", "C", "D"] if k != target_k]
    exps = {"correct": correct_exp}
    for i, ok in enumerate(other_keys):
        opts[ok] = distractors[i]
        exps[f"wrong_{ok}"] = distractor_exps[i]

    return make_q(qid, prompt, opts, target_k, exps, cz_pt, module_meta["workplace_track"])

def generate_c2_question(module_meta, q_idx):
    qid = f"{module_meta['test_id']}-Q{q_idx+1}"
    target_k = KEY_PATTERN[q_idx % len(KEY_PATTERN)]
    
    c2_scenarios = [
        ("The regulatory inspection panel mandated that the pharmaceutical manufacturer _____ immediate root cause corrective actions regarding data integrity.", "institute", "institutes", "shall institute", "must to institute", "Mandative subjunctive requires base form 'institute' after 'mandated that'."),
        ("Seldom _____ regulatory health authorities accepted electronic audit trail gaps without issuing formal Form FDA 483 inspectional observations.", "have", "are", "were", "did", "Negative inversion: 'Seldom have regulatory health authorities accepted'."),
        ("It is of paramount regulatory importance that all automated sterile filling robotics _____ validated against Annex 1 barrier isolation standards.", "be", "is", "will be", "must to be", "Formulaic subjunctive: 'paramount regulatory importance that all robotics be validated'."),
        ("_____ the engineering contractor to default on the cleanroom EPCMV commissioning milestone, liquidated damages would immediately become enforceable.", "Were", "Had", "Should", "If were", "Second Conditional inversion with 'Were [subject] to [verb]' expresses formal hypothetical breach."),
        ("Not only _____ fail to maintain the 15-Pascal airlock pressure cascade, but the emergency damper actuator also malfunctioned during the smoke test.", "did the HVAC system", "the HVAC system did", "was the HVAC system", "has the HVAC system", "Inversion after 'Not only': 'did the HVAC system fail'."),
        ("Under no circumstances _____ the Qualified Person (QP) to authorize commercial batch release while critical deviation investigations remain unresolved.", "is", "are", "will", "has", "Negative inversion: 'Under no circumstances is the QP to authorize'."),
        ("The Lead Forensic Auditor insisted that all SCADA database audit trail logs _____ directly to the EMA inspection team without editorial redaction.", "be presented", "are presented", "will be presented", "must to be presented", "Passive mandative subjunctive: 'insisted that logs be presented'."),
        ("Had the cleanroom design team not isolated the lyophilization condenser room, toxic refrigerant vapor leakage _____ into the sterile core.", "would have migrated", "would migrate", "had migrated", "will migrate", "Third Conditional counterfactual: 'would have migrated'."),
        ("Barely _____ the unannounced FDA inspection concluded when European health authorities served an unannounced inspection notice on line 3.", "had", "was", "did", "has", "Inversion: 'Barely had the inspection concluded... when...'."),
        ("The international GMP harmonization treaty specifies that computerized electronic batch signatures _____ equivalent to traditional handwritten signatures.", "be deemed", "is deemed", "will be deemed", "shall to be deemed", "Mandative subjunctive in regulatory treaties: 'specifies that signatures be deemed equivalent'.")
    ]
    prompt, correct_text, w1, w2, w3, rule = c2_scenarios[q_idx % len(c2_scenarios)]
    distractors = [w1, w2, w3]
    correct_exp = f"C2 regulatory inspection & litigation discourse: {rule}"
    distractor_exps = [
        f"Option '{w1}' fails to apply the mandatory subjunctive base form or subject-auxiliary inversion.",
        f"Option '{w2}' inappropriately uses indicative forms in regulatory legal directives.",
        f"Option '{w3}' is ungrammatical in international GxP jurisprudence."
    ]
    cz_pt = "Regulatory audit defense demands absolute mastery of mandative subjunctive ('mandated that the firm institute') and formal inversion ('Seldom have authorities accepted')."

    opts = {target_k: correct_text}
    other_keys = [k for k in ["A", "B", "C", "D"] if k != target_k]
    exps = {"correct": correct_exp}
    for i, ok in enumerate(other_keys):
        opts[ok] = distractors[i]
        exps[f"wrong_{ok}"] = distractor_exps[i]

    return make_q(qid, prompt, opts, target_k, exps, cz_pt, module_meta["workplace_track"])

def generate_teva_eng_modules():
    curriculum = get_teva_eng_curriculum()
    all_modules = {}

    for mod in curriculum:
        tid = mod["test_id"]
        disk_file = EXISTING_TESTS_DIR / f"{tid}.json"
        
        if disk_file.exists():
            with open(disk_file, "r", encoding="utf-8") as f:
                test_data = json.load(f)
            test_data["title"] = mod["title"]
            test_data["workplace_track"] = mod["workplace_track"]
            test_data["level"] = mod["level"]
            test_data["category"] = mod["category"]
            all_modules[tid] = test_data
        else:
            lvl = mod["level"]
            questions = []
            for q_idx in range(10):
                if lvl == "A2":
                    q = generate_a2_question(mod, q_idx)
                elif lvl == "B1":
                    q = generate_b1_question(mod, q_idx)
                elif lvl == "B2":
                    q = generate_b2_question(mod, q_idx)
                else: # C2
                    q = generate_c2_question(mod, q_idx)
                questions.append(q)

            test_obj = build_test_module(
                test_id=tid,
                title=mod["title"],
                level=mod["level"],
                category=mod["category"],
                track=mod["workplace_track"],
                est_time=mod["estimated_time_minutes"],
                description=mod["description"],
                objectives=[
                    f"Master professional {mod['grammar_focus']} in pharmaceutical engineering and cleanroom automation",
                    f"Eliminate common Czech interference errors in {mod['title'].lower()}",
                    "Demonstrate precision in GAMP 5, CSV, and regulatory inspection compliance"
                ],
                questions=questions
            )
            all_modules[tid] = test_obj

    return all_modules

if __name__ == "__main__":
    mods = generate_teva_eng_modules()
    print(f"Generated {len(mods)} Teva Engineering modules.")
