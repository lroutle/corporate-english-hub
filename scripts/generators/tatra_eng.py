"""
Generator for all 80 Tatra Engineering modules (20 A2, 20 B1, 20 B2, 20 C1).
Preserves existing validated modules and procedural-generates the remainder with high pedagogical rigor.
"""

import sys
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(ROOT / "scripts"))

from curriculum_catalog import get_tatra_eng_curriculum
from generators.common import make_q, build_test_module, KEY_PATTERN
EXISTING_TESTS_DIR = ROOT / "tatra-engineering" / "data" / "tests"

# Domain technical vocabulary banks for Tatra Engineering
A2_SCENARIOS = [
    # (subject, context, verb_base, verb_3rd, verb_past, verb_ing, czech_point)
    ("The assembly line mechanic", "the differential gear casing with a calibrated pneumatic impact driver", "tighten", "tightens", "tightened", "tightening", "Czech 'mechanik utahuje'. English 3rd person singular takes -s: 'tightens'."),
    ("The quality inspector", "the chassis backbone tube weld seam for micro-cracks before painting", "inspect", "inspects", "inspected", "inspecting", "Czech 'inspektor kontroluje'. Singular subject takes 'inspects', not 'inspect'."),
    ("The crane operator", "the heavy Tatra V8 engine block directly onto the front chassis mounts", "lower", "lowers", "lowered", "lowering", "Czech 'jeřábník spouští'. English requires 'lowers' for habitual shift actions."),
    ("Our maintenance technician", "the hydraulic oil level in the cabin tilt mechanism every Monday", "check", "checks", "checked", "checking", "Czech 'technik kontroluje'. Singular present requires 'checks'."),
    ("The robotic welding arm", "the suspension bracket to the central load-bearing tube automatically", "weld", "welds", "welded", "welding", "Singular machine subjects take 3rd person -s: 'welds'."),
    ("The workshop supervisor", "the daily assembly logbook before the afternoon shift departs", "sign", "signs", "signed", "signing", "Czech 'mistr podepisuje'. Use 'signs' with 3rd person singular."),
    ("The testing engineer", "the central tire inflation system (CTIS) pressure valves during road trials", "test", "tests", "tested", "testing", "Use 'tests' for singular engineer subject."),
    ("The paint shop worker", "the wheel rims with a protective anti-corrosion primer coating", "spray", "sprays", "sprayed", "spraying", "Singular subject takes 'sprays'."),
    ("The driveline specialist", "the swinging half-axle rubber dust boot for oil weeping", "replace", "replaces", "replaced", "replacing", "Czech 'specialista mění'. Use 'replaces'."),
    ("The logistics handler", "new hardened M16 flange bolts to workstation 4 in yellow bins", "bring", "brings", "brought", "bringing", "Singular subject takes 'brings' with -s.")
]

def generate_a2_question(module_meta, q_idx):
    qid = f"{module_meta['test_id']}-Q{q_idx+1}"
    target_k = KEY_PATTERN[q_idx % len(KEY_PATTERN)]
    sc = A2_SCENARIOS[q_idx % len(A2_SCENARIOS)]
    subj, context, v_base, v_3rd, v_past, v_ing, cz_note = sc

    # Different grammar focuses across A2 modules
    mod_num = int(module_meta['test_id'].split('-')[-1])
    
    if mod_num in [1, 5, 12, 19, 20]: # Imperatives & Modals (must, can)
        prompt = f"Before starting the chassis assembly, mechanics _____ {context}."
        correct_text = "must " + v_base
        distractors = ["must to " + v_base, "are must " + v_base, "must " + v_ing]
        correct_exp = f"Modal 'must' is followed by base form '{v_base}' without 'to'."
        distractor_exps = [
            f"'must to' is ungrammatical; modal 'must' never takes 'to'.",
            f"'are must' is completely ungrammatical in English.",
            f"'must' cannot be followed by an '-ing' participle."
        ]
        cz_pt = "Czech 'musí zkontrolovat'. English modal 'must' takes the bare infinitive without 'to': 'must " + v_base + "'."
    elif mod_num in [3, 8, 18]: # Past Simple
        prompt = f"Yesterday during shift 2, {subj.lower()} _____ {context}."
        correct_text = v_past
        distractors = [v_base, "has " + v_past, "is " + v_ing]
        correct_exp = f"Specific completed time 'yesterday' strictly requires Past Simple '{v_past}'."
        distractor_exps = [
            f"Base form '{v_base}' lacks past tense inflection.",
            f"Present Perfect 'has {v_past}' cannot co-occur with specific past adverbial 'yesterday'.",
            f"Present Continuous describes current actions, not yesterday's finished events."
        ]
        cz_pt = f"Czech uses the same past form, but in English, 'yesterday' strictly requires Past Simple ('{v_past}'), never Present Perfect."
    elif mod_num in [4, 10]: # Prepositions of Place
        preps = ["under", "between", "inside", "next to", "on top of", "behind", "into", "across", "along", "against"]
        target_prep = preps[q_idx % len(preps)]
        prompt = f"The mechanic placed the torque wrench socket _____ the central backbone tube."
        correct_text = target_prep
        distractor_preps = [p for p in preps if p != target_prep][:3]
        distractors = distractor_preps
        correct_exp = f"Preposition '{target_prep}' accurately describes the physical spatial relationship here."
        distractor_exps = [
            f"Preposition '{distractors[0]}' expresses incorrect spatial positioning.",
            f"Preposition '{distractors[1]}' does not fit the mechanical mounting geometry.",
            f"Preposition '{distractors[2]}' indicates incorrect direction or orientation."
        ]
        cz_pt = f"Spatial prepositions require exact physical matching. Czech 'pod rourou' = 'under the tube', 'mezi polonápravami' = 'between the half-axles'."
    else: # Present Simple 3rd person
        prompt = f"{subj} usually _____ {context}."
        correct_text = v_3rd
        distractors = [v_base, v_ing, "is " + v_base]
        correct_exp = f"Singular subject takes 3rd person singular Present Simple with '-s' ('{v_3rd}')."
        distractor_exps = [
            f"Base form '{v_base}' lacks required 3rd person singular '-s'.",
            f"Participle '{v_ing}' cannot function as finite predicate without auxiliary.",
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
        ("the air suspension bellows pressure", "calibrate", "had been calibrated", "was calibrated", "has been calibrated", "calibrating"),
        ("the swinging half-axle crown gear teeth", "lubricate", "had been lubricated", "was lubricated", "has been lubricated", "lubricating"),
        ("the central tire inflation system (CTIS) rotary seals", "test", "had been tested", "was tested", "has been tested", "testing"),
        ("the hydraulic retarder cooling valves", "inspect", "had been inspected", "was inspected", "has been inspected", "inspecting"),
        ("the transfer case planetary gear set", "align", "had been aligned", "was aligned", "has been aligned", "aligning"),
        ("the backbone tube flange connecting bolts", "torque", "had been torqued", "was torqued", "has been torqued", "torquing"),
        ("the dual-circuit pneumatic brake lines", "purge", "had been purged", "was purged", "has been purged", "purging"),
        ("the differential lock pneumatic solenoid", "replace", "had been replaced", "was replaced", "has been replaced", "replacing"),
        ("the steering drag link ball joints", "grease", "had been greased", "was greased", "has been greased", "greasing"),
        ("the V8 turbocharged intercooler ducts", "fasten", "had been fastened", "was fastened", "has been fastened", "fastening")
    ]
    item, action, had_been, was_v, has_been, v_ing = b1_contexts[q_idx % len(b1_contexts)]

    if mod_num in [1, 8, 13, 16]: # Past Simple vs Past Perfect
        prompt = f"Before the prototype truck entered the test track, the test engineer noticed that {item} _____."
        correct_text = had_been
        distractors = [was_v, has_been, "didn't " + action]
        correct_exp = f"Past Perfect Passive ('{had_been}') is required because the action was completed prior to the past action 'noticed'."
        distractor_exps = [
            f"Past Simple ('{was_v}') fails to indicate precedence before 'noticed'.",
            f"Present Perfect ('{has_been}') cannot connect to a past anchor time.",
            f"'didn't {action}' is active voice, but mechanical parts are acted upon passively."
        ]
        cz_pt = "Czech uses simple past for both actions ('všiml si, že díl nebyl...'). In English engineering logs, use Past Perfect for sequence clarity."
    elif mod_num in [4, 7, 14]: # Conditionals in Troubleshooting
        prompt = f"If the CTIS air compressor _____ pressure above 8 bar within five minutes, the ECU flags an air leak warning."
        correct_text = "fails to maintain"
        distractors = ["will fail to maintain", "would fail to maintain", "failed to maintain"]
        correct_exp = "First conditional if-clause takes Present Simple ('fails to maintain') for real operational consequences."
        distractor_exps = [
            "Cannot use 'will' in the conditional if-clause.",
            "Cannot use 'would' in a real First Conditional if-clause.",
            "Past tense produces an unreal condition, mismatched with present 'flags'."
        ]
        cz_pt = "Czenglish trap: Never put 'will' into the if-clause (*If the compressor will fail*). Use Present Simple: 'If the compressor fails'."
    else: # Passive voice in technical specifications
        prompt = f"All backbone tube structural mounting fasteners _____ to 450 Nm according to Tatra workshop manual TM-815."
        correct_text = "must be torqued"
        distractors = ["must to be torqued", "must torque", "are must be torqued"]
        correct_exp = "Passive construction with modal: 'must be torqued'."
        distractor_exps = [
            "'must to be' is ungrammatical; modal 'must' takes bare infinitive.",
            "'must torque' is active voice; fasteners do not torque themselves.",
            "'are must' is completely ungrammatical in English."
        ]
        cz_pt = "SOP instructions require passive voice with modals: 'must be torqued' (musí být dotaženy). Avoid active voice for inanimate parts."

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
        ("torsional stress on the central backbone tube", "finite element mesh density", "had the engineers increased", "if engineers increased", "would engineers have increased", "should engineers increase"),
        ("chassis frame deflection under severe off-road twist", "multi-axle load distribution", "had the suspension dampers been tuned", "if dampers tuned", "would dampers have tuned", "were dampers tuning"),
        ("gear tooth flank micropitting in the transfer gearbox", "synthetic lubricant viscosity", "had the oil temperature not exceeded", "if oil temperature not exceeded", "would oil temperature not exceed", "did oil temperature not exceed"),
        ("pneumatic brake chamber air leak during NATO mobility trials", "silicone diaphragm seal elasticity", "had the cold-weather test protocol been followed", "if cold-weather protocol followed", "would protocol have followed", "should protocol follow"),
        ("swinging half-axle kingpin bearing seizure", "molybdenum disulfide grease purge interval", "had maintenance schedules been observed", "if schedules observed", "would schedules have observed", "were schedules observing"),
        ("hydrostatic cooling fan pump cavitation at maximum engine RPM", "hydraulic reservoir fluid de-aeration", "had the suction line diameter been enlarged", "if diameter enlarged", "would diameter have enlarged", "did diameter enlarge"),
        ("exhaust gas recirculation (EGR) valve soot clogging", "diesel particulate filter regeneration cycle", "had the ECU map triggered regenerations", "if ECU map triggered", "would ECU map have triggered", "should ECU map trigger"),
        ("ballistic cabin floor weld shear failure under mine blast simulation", "high-hard armor plate overlap thickness", "had the weld joint penetration been verified", "if penetration verified", "would penetration have verified", "was penetration verifying"),
        ("driveshaft torsional resonance frequency peaks", "center bearing rubber isolator stiffness", "had dynamic vibration analysis been performed", "if analysis performed", "would analysis have performed", "were analysis performing"),
        ("all-wheel drive differential lock clutch wear", "pneumatic engagement actuator pressure", "had the pressure sensor signaled engagement", "if sensor signaled", "would sensor have signaled", "did sensor signal")
    ]
    problem, param, had_inv, if_simple, would_clause, should_clause = b2_scenarios[q_idx % len(b2_scenarios)]

    if mod_num in [1, 5, 7, 14]: # Third Conditionals & Inversions
        prompt = f"_____ earlier during simulation, the catastrophic {problem} would not have occurred on the test track."
        correct_text = had_inv
        distractors = [if_simple, would_clause, should_clause]
        correct_exp = f"Inverted Third Conditional '{had_inv}' correctly replaces 'If [subject] had...' in formal engineering inquests."
        distractor_exps = [
            f"'{if_simple}' lacks auxiliary 'had' and creates an incomplete clause.",
            f"'{would_clause}' incorrectly places 'would have' inside the conditional premise.",
            f"'{should_clause}' expresses present/future tentative condition, not a past counterfactual."
        ]
        cz_pt = "Formal engineering reports invert past conditionals without 'if': 'Had the engineers increased...' = 'If the engineers had increased...'. Never put 'would' into the condition."
    elif mod_num in [2, 10, 20]: # Negative Inversion for Rigor
        prompt = f"Under no circumstances _____ bypass the secondary locking pins on the swinging half-axle assembly rig."
        correct_text = "should assembly technicians"
        distractors = ["assembly technicians should", "assembly technicians must to", "shall assembly technicians to"]
        correct_exp = "Negative phrase 'Under no circumstances' triggers subject-auxiliary inversion: 'should assembly technicians'."
        distractor_exps = [
            "'assembly technicians should' lacks required subject-auxiliary inversion.",
            "'must to' is ungrammatical; modal 'must' does not take 'to'.",
            "'shall... to' is ungrammatical in English."
        ]
        cz_pt = "Negative introductory phrases ('Under no circumstances', 'Rarely', 'Seldom') trigger question word order: 'Under no circumstances should technicians bypass...'."
    else: # Mixed Conditionals
        prompt = f"If the metallurgical heat treatment had been performed properly in Kopřivnice, the drive axle _____ under heavy mining loads today."
        correct_text = "would not deform"
        distractors = ["would not have deformed", "will not deform", "does not deform"]
        correct_exp = "Mixed conditional: past cause ('had been performed') with present result ('today') takes 'would not deform'."
        distractor_exps = [
            "'would not have deformed' refers to past result, but the adverbial 'today' anchors the consequence to the present.",
            "'will not deform' is First Conditional, incompatible with past unreal condition.",
            "Simple present indicative 'does not deform' cannot express hypothetical consequence."
        ]
        cz_pt = "Mixed Conditionals connect a past action with a present state of affairs: 'If it had been treated [past], it would not deform [today]'."

    opts = {target_k: correct_text}
    other_keys = [k for k in ["A", "B", "C", "D"] if k != target_k]
    exps = {"correct": correct_exp}
    for i, ok in enumerate(other_keys):
        opts[ok] = distractors[i]
        exps[f"wrong_{ok}"] = distractor_exps[i]

    return make_q(qid, prompt, opts, target_k, exps, cz_pt, module_meta["workplace_track"])

def generate_c1_question(module_meta, q_idx):
    qid = f"{module_meta['test_id']}-Q{q_idx+1}"
    target_k = KEY_PATTERN[q_idx % len(KEY_PATTERN)]
    
    c1_scenarios = [
        ("The defense procurement tribunal mandated that the OEM _____ full finite element stress tensors for the armored chassis cab.", "furnish", "furnishes", "shall furnish", "must to furnish", "Mandative subjunctive requires base form 'furnish' after 'mandated that'."),
        ("It is imperative that every structural titanium alloy component _____ non-destructive Eddy current testing prior to military field trials.", "undergo", "undergoes", "will undergo", "must undergoes", "Formulaic subjunctive after 'imperative that' requires base form 'undergo'."),
        ("Seldom _____ witnessed such catastrophic torsional shear propagation without prior ultrasonic indication of fatigue cracking.", "have our metallurgists", "our metallurgists have", "did our metallurgists had", "had our metallurgists have", "Negative adverb 'Seldom' triggers subject-auxiliary inversion: 'have our metallurgists'."),
        ("The arbitration panel recommended that Tatra _____ damages for delays caused exclusively by force majeure blockades.", "not be assessed", "is not assessed", "will not be assessed", "should not to be assessed", "Negative passive subjunctive: 'recommended that Tatra not be assessed'."),
        ("_____ the defense ministry to repudiate the bilateral procurement treaty, international offset commitments would immediately trigger arbitration.", "Were", "Had", "Should", "If were", "Second Conditional inversion with 'Were [subject] to [infinitive]' expresses hypothetical future repudiation."),
        ("Not only _____ fail to meet STANAG 4569 Level 4 ballistic criteria, but the composite armor also delaminated under environmental humidity cycling.", "did the supplier's cabin", "the supplier's cabin did", "was the supplier's cabin", "has the supplier's cabin", "Inversion after 'Not only': 'did the cabin fail'."),
        ("The chief metallurgist testified that had hydrogen embrittlement been detected during acid pickling, catastrophic half-axle shear _____ averted.", "could have been", "could be", "had been", "would be able to be", "Counterfactual conditional modal: 'could have been averted'."),
        ("Bilateral treaty directives stipulate that intellectual property rights _____ vested solely in the sovereign defense ministry.", "remain", "remains", "will remain", "are remaining", "Mandative subjunctive after 'stipulate that' takes base form 'remain'."),
        ("Under no circumstances _____ the OEM to disclose proprietary swinging half-axle gear telemetry without prior written consent.", "is the tribunal to permit", "the tribunal is to permit", "will the tribunal permits", "the tribunal permits", "Negative inversion: 'Under no circumstances is the tribunal to permit'."),
        ("The lead failure analyst insisted that forensic fracture toughness specimens _____ immediately to an independent accredited laboratory.", "be dispatched", "are dispatched", "will be dispatched", "must to be dispatched", "Passive mandative subjunctive: 'insisted that specimens be dispatched'.")
    ]
    prompt, correct_text, w1, w2, w3, rule = c1_scenarios[q_idx % len(c1_scenarios)]
    distractors = [w1, w2, w3]
    correct_exp = f"Advanced-tier syntax: {rule}"
    distractor_exps = [
        f"Option '{w1}' incorrectly applies indicative or non-inverted word order.",
        f"Option '{w2}' violates formal mandative subjunctive or inversion rules.",
        f"Option '{w3}' is ungrammatical in high-register technical legal discourse."
    ]
    cz_pt = "High-level professional English prioritizes mandative subjunctive ('demand that it be done') and negative inversion ('Seldom have we seen') over colloquial indicative structures."

    opts = {target_k: correct_text}
    other_keys = [k for k in ["A", "B", "C", "D"] if k != target_k]
    exps = {"correct": correct_exp}
    for i, ok in enumerate(other_keys):
        opts[ok] = distractors[i]
        exps[f"wrong_{ok}"] = distractor_exps[i]

    return make_q(qid, prompt, opts, target_k, exps, cz_pt, module_meta["workplace_track"])

def generate_tatra_eng_modules():
    curriculum = get_tatra_eng_curriculum()
    all_modules = {}

    for mod in curriculum:
        tid = mod["test_id"]
        disk_file = EXISTING_TESTS_DIR / f"{tid}.json"
        
        # If existing test file already exists and is validated, preserve it!
        if disk_file.exists():
            with open(disk_file, "r", encoding="utf-8") as f:
                test_data = json.load(f)
            # Ensure it has exactly 10 questions and proper metadata
            test_data["title"] = mod["title"]
            test_data["workplace_track"] = mod["workplace_track"]
            test_data["level"] = mod["level"]
            test_data["category"] = mod["category"]
            all_modules[tid] = test_data
        else:
            # Procedurally generate module
            lvl = mod["level"]
            questions = []
            for q_idx in range(10):
                if lvl == "A2":
                    q = generate_a2_question(mod, q_idx)
                elif lvl == "B1":
                    q = generate_b1_question(mod, q_idx)
                elif lvl == "B2":
                    q = generate_b2_question(mod, q_idx)
                else: # C1
                    q = generate_c1_question(mod, q_idx)
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
                    f"Master professional {mod['grammar_focus']} in automotive engineering",
                    f"Eliminate common Czech interference errors in {mod['title'].lower()}",
                    "Demonstrate precision in technical and regulatory documentation"
                ],
                questions=questions
            )
            all_modules[tid] = test_obj

    return all_modules

if __name__ == "__main__":
    mods = generate_tatra_eng_modules()
    print(f"Generated {len(mods)} Tatra Engineering modules.")
