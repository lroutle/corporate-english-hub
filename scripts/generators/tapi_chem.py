"""
Generator for all 80 Tapi Chemistry modules (20 A2, 20 B1, 20 B2, 20 C2).
Preserves existing validated modules and procedural-generates the remainder with high pedagogical rigor.
"""

import sys
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(ROOT / "scripts"))

from curriculum_catalog import get_tapi_chem_curriculum
from generators.common import make_q, build_test_module, KEY_PATTERN

EXISTING_TESTS_DIR = ROOT / "tapi-chemistry" / "data" / "tests"

A2_CHEM_SCENARIOS = [
    ("The analytical chemist", "5.0 grams of active pharmaceutical substance on the analytical balance", "weigh", "weighs", "weighed", "weighing", "Czech 'chemik váží'. English 3rd person singular takes -s: 'weighs'."),
    ("The laboratory technician", "the volumetric flask with high-purity HPLC-grade water to the mark", "fill", "fills", "filled", "filling", "Singular subject takes 'fills' with -s."),
    ("The QC analyst", "the pH electrode in the standard pH 7.0 buffer solution carefully", "immerse", "immerses", "immersed", "immersing", "Singular subject takes 'immerses'."),
    ("The process operator", "the temperature of the jacketed synthesis reactor every fifteen minutes", "check", "checks", "checked", "checking", "Singular subject takes 'checks'."),
    ("The lab assistant", "the rotary evaporator vacuum pump before heating the water bath", "start", "starts", "started", "starting", "Singular subject takes 'starts'."),
    ("The organic chemist", "the crystalline precipitate using a Buchner funnel and filter paper", "filter", "filters", "filtered", "filtering", "Singular subject takes 'filters'."),
    ("The safety officer", "all flammable solvent carboys in the explosion-proof yellow cabinet", "store", "stores", "stored", "storing", "Singular subject takes 'stores'."),
    ("The titration specialist", "the Karl Fischer reagent factor before running the moisture sample", "calibrate", "calibrates", "calibrated", "calibrating", "Singular subject takes 'calibrates'."),
    ("The shift technician", "the analytical test results into the digital Laboratory Information Management System (LIMS)", "enter", "enters", "entered", "entering", "Singular subject takes 'enters'."),
    ("The cleaning staff", "the laminar flow fume hood stainless steel bench with isopropanol wipes", "clean", "cleans", "cleaned", "cleaning", "Singular subject takes 'cleans'.")
]

def generate_a2_question(module_meta, q_idx):
    qid = f"{module_meta['test_id']}-Q{q_idx+1}"
    target_k = KEY_PATTERN[q_idx % len(KEY_PATTERN)]
    sc = A2_CHEM_SCENARIOS[q_idx % len(A2_CHEM_SCENARIOS)]
    subj, context, v_base, v_3rd, v_past, v_ing, cz_note = sc
    mod_num = int(module_meta['test_id'].split('-')[-1])

    if mod_num in [1, 12, 19, 20]: # Imperatives & Lab Safety
        prompt = f"Always make sure to _____ {context} following approved laboratory SOPs."
        correct_text = v_base
        distractors = ["to " + v_base, v_3rd, v_ing]
        correct_exp = f"'make sure to' takes base form '{v_base}' without double-to or grammatical endings."
        distractor_exps = [
            f"'to {v_base}' creates ungrammatical double 'to'.",
            f"3rd person '{v_3rd}' cannot follow infinitive marker 'to'.",
            f"Participle '{v_ing}' does not form the standard infinitive directive here."
        ]
        cz_pt = f"Czech 'ujistěte se, že zkontrolujete'. After 'make sure to', use base verb '{v_base}'."
    elif mod_num in [3, 10]: # Past Simple
        prompt = f"Yesterday afternoon in the synthesis lab, {subj.lower()} _____ {context}."
        correct_text = v_past
        distractors = [v_base, "has " + v_past, "is " + v_ing]
        correct_exp = f"Specific completed past time 'Yesterday afternoon' strictly requires Past Simple '{v_past}'."
        distractor_exps = [
            f"Base form '{v_base}' lacks past tense marking.",
            f"Present Perfect 'has {v_past}' cannot accompany 'yesterday'.",
            f"Present Continuous describes current actions, not yesterday's finished events."
        ]
        cz_pt = f"Czech uses the same past tense, but in English, 'yesterday' strictly triggers Past Simple ('{v_past}')."
    elif mod_num in [4, 18]: # Prepositions of Place
        preps = ["inside", "between", "under", "next to", "above", "behind", "into", "across", "along", "against"]
        target_p = preps[q_idx % len(preps)]
        prompt = f"Store all concentrated reagent bottles _____ the ventilated safety cabinet."
        correct_text = target_p
        distractors = [p for p in preps if p != target_p][:3]
        correct_exp = f"Preposition '{target_p}' accurately describes the physical laboratory location."
        distractor_exps = [
            f"Preposition '{distractors[0]}' expresses incorrect spatial positioning.",
            f"Preposition '{distractors[1]}' is incompatible with the cabinet layout.",
            f"Preposition '{distractors[2]}' indicates wrong direction."
        ]
        cz_pt = "Laboratory spatial prepositions: 'inside the cabinet' = uvnitř skříně."
    else: # Present Simple
        prompt = f"{subj} usually _____ {context}."
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
        ("the crude synthetic API batch", "dissolve", "had been dissolved", "was dissolved", "has been dissolved", "dissolving"),
        ("the HPLC C18 reverse-phase column", "equilibrate", "had been equilibrated", "was equilibrated", "has been equilibrated", "equilibrating"),
        ("the Karl Fischer titration solvent vessel", "titrate", "had been titrated", "was titrated", "has been titrated", "titrating"),
        ("the rotary evaporator solvent trap", "empty", "had been emptied", "was emptied", "has been emptied", "emptying"),
        ("the recrystallization cooling brine jacket", "chill", "had been chilled", "was chilled", "has been chilled", "chilling"),
        ("the Buchner funnel vacuum filtration cake", "wash", "had been washed", "was washed", "has been washed", "washing"),
        ("the analytical balance draft shield", "clean", "had been cleaned", "was cleaned", "has been cleaned", "cleaning"),
        ("the In-Process Control (IPC) reaction sample", "neutralize", "had been neutralized", "was neutralized", "has been neutralized", "neutralizing"),
        ("the gas chromatography inlet septum", "replace", "had been replaced", "was replaced", "has been replaced", "replacing"),
        ("the UV-Vis spectrophotometer lamp alignment", "calibrate", "had been calibrated", "was calibrated", "has been calibrated", "calibrating")
    ]
    item, action, had_been, was_v, has_been, v_ing = b1_contexts[q_idx % len(b1_contexts)]

    if mod_num in [1, 4, 14]: # Past Simple vs Past Perfect
        prompt = f"Before starting the automated HPLC injection sequence, the analyst noted that {item} _____."
        correct_text = had_been
        distractors = [was_v, has_been, "didn't " + action]
        correct_exp = f"Past Perfect Passive ('{had_been}') correctly expresses priority before the past action 'noted'."
        distractor_exps = [
            f"Past Simple ('{was_v}') fails to indicate completion prior to 'noted'.",
            f"Present Perfect ('{has_been}') cannot connect to a past reference frame.",
            f"'didn't {action}' is active voice; analytical reagents and samples are acted upon passively."
        ]
        cz_pt = "In analytical QC logs, use Past Perfect Passive to document steps completed before an observation was made."
    elif mod_num in [3, 8]: # Conditionals in Chromatography
        prompt = f"If the mobile phase degassing unit _____ during run 4, the HPLC baseline will exhibit excessive noise."
        correct_text = "fails"
        distractors = ["will fail", "would fail", "failed"]
        correct_exp = "First conditional if-clause takes Present Simple ('fails') for real physical consequences."
        distractor_exps = [
            "Cannot use 'will' in conditional if-clauses.",
            "Cannot use 'would' in a real First Conditional.",
            "Past tense 'failed' creates an unreal condition, mismatched with 'will exhibit'."
        ]
        cz_pt = "Never use 'will' in the if-clause of analytical troubleshooting (*If the pump will fail*). Use Present Simple: 'If the pump fails'."
    else: # Passive voice in Chemistry SOPs
        prompt = f"All volumetric glassware _____ with high-purity solvent prior to analytical trace analysis."
        correct_text = "must be rinsed"
        distractors = ["must to be rinsed", "must rinse", "are must be rinsed"]
        correct_exp = "Passive construction with modal: 'must be rinsed'."
        distractor_exps = [
            "'must to be' is ungrammatical; modal 'must' takes bare infinitive.",
            "'must rinse' is active voice; glassware does not rinse itself.",
            "'are must' is completely ungrammatical in English."
        ]
        cz_pt = "Analytical chemistry SOPs strictly require passive voice with modals: 'must be rinsed' (musí být vypláchnuto)."

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
        ("The pharmacopeial monograph requires that the chromatographic peak resolution between API and impurity A _____ not less than 2.0.", "be", "is", "will be", "must to be", "Mandative subjunctive after 'requires that' takes base form 'be'."),
        ("Under no circumstances _____ discard the original chromatographic raw data files without prior QA authorization.", "may analysts", "analysts may", "analysts must to", "shall analysts to", "Negative inversion: 'Under no circumstances may analysts discard'."),
        ("It is essential that each Karl Fischer reagent factor determination _____ performed in triplicate.", "be", "is", "was", "must to be", "Formulaic subjunctive after 'essential that' requires base form 'be'."),
        ("Had the QC chemist verified the column equilibration time, the baseline drift _____ prevented.", "would have been", "would be", "had been", "will be", "Inverted Third Conditional passive result: 'would have been prevented'."),
        ("The OOS SOP mandates that Phase I laboratory investigations _____ within three working days.", "be concluded", "are concluded", "were concluded", "will be concluded", "Passive mandative subjunctive: 'mandates that investigations be concluded'."),
        ("Rarely _____ an analytical method validation pass specificity challenge without baseline separation of synthetic degradation products.", "does", "is", "will", "has", "Negative inversion: 'Rarely does an analytical method pass'."),
        ("If the reaction mixture had been quenched at 0°C on schedule, toxic exotherm decomposition _____ today.", "would not threaten", "would not have threatened", "will not threaten", "does not threaten", "Mixed conditional: past condition ('had been quenched') with present outcome ('today') takes 'would not threaten'."),
        ("The ICH Q2(R2) guideline stipulates that method detection limit (LOD) calculations _____ substantiated by signal-to-noise ratios.", "be", "are", "will be", "must to be", "Mandative subjunctive: 'stipulates that calculations be substantiated'."),
        ("Only by conducting comprehensive forced degradation stress testing _____ establish the stability-indicating nature of the HPLC method.", "can the analytical scientist", "the analytical scientist can", "the analytical scientist could", "was the analytical scientist can", "Inversion after 'Only by...': 'can the scientist establish'."),
        ("Were the jacketed reactor _____ a sudden runaway exotherm, emergency cooling brine injection would trigger automatically.", "to undergo", "undergoes", "will undergo", "would undergo", "Inverted Second Conditional: 'Were the reactor to undergo...' expresses formal hypothetical condition.")
    ]
    prompt, correct_text, w1, w2, w3, rule = b2_scenarios[q_idx % len(b2_scenarios)]
    distractors = [w1, w2, w3]
    correct_exp = f"B2 analytical & organic chemistry syntax: {rule}"
    distractor_exps = [
        f"Option '{w1}' violates formal mandative subjunctive or inversion rules.",
        f"Option '{w2}' applies inappropriate indicative or non-inverted phrasing.",
        f"Option '{w3}' is ungrammatical in formal scientific chemistry discourse."
    ]
    cz_pt = "Advanced analytical chemistry reporting demands strict mandative subjunctive ('mandates that it be concluded') and auxiliary inversion ('Rarely does a method pass')."

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
        ("The international pharmacopeial harmonization commission mandated that all nitrosamine testing thresholds _____ harmonized across Ph. Eur. and USP monographs.", "be", "is", "shall be", "must to be", "Mandative subjunctive requires base form 'be' after 'mandated that'."),
        ("Seldom _____ regulatory agencies accepted retrospective toxicological justifications for genotoxic impurities without comprehensive Ames test data.", "have", "are", "were", "did", "Negative inversion: 'Seldom have regulatory agencies accepted'."),
        ("It is of paramount scientific necessity that every chiral chromatographic method _____ validated against enantiomeric inversion.", "be", "is", "will be", "must to be", "Formulaic subjunctive: 'paramount scientific necessity that every method be validated'."),
        ("_____ the patent holder to establish crystal lattice polymorphism priority, competing generic API manufacturers would face an immediate market injunction.", "Were", "Had", "Should", "If were", "Second Conditional inversion with 'Were [subject] to [verb]' expresses formal hypothetical patent claim."),
        ("Not only _____ fail to detect the trace nitrosamine contaminant, but the analytical method also exhibited severe chromatographic peak fronting.", "did the supplier's laboratory", "the supplier's laboratory did", "was the supplier's laboratory", "has the supplier's laboratory", "Inversion after 'Not only': 'did the laboratory fail'."),
        ("Under no circumstances _____ the Qualified Person (QP) to release an API batch pending investigation of unassigned out-of-trend impurity peaks.", "is", "are", "will", "has", "Negative inversion: 'Under no circumstances is the QP to release'."),
        ("The lead toxicologist insisted that the mutagenic risk calculation _____ strictly according to ICH M7 linear extrapolation guidelines.", "be performed", "is performed", "will be performed", "must to be performed", "Passive mandative subjunctive: 'insisted that calculation be performed'."),
        ("Had the chemical development team not modified the catalytic hydrogenation pathway, genotoxic hydrazine formation _____ avoided.", "would not have been", "would not be", "had not been", "will not be", "Third Conditional counterfactual: 'would not have been avoided'."),
        ("Barely _____ the European Directorate (EDQM) granted the Certificate of Suitability (CEP) when unannounced impurity audits were initiated.", "had", "was", "did", "has", "Inversion: 'Barely had the EDQM granted... when...'."),
        ("The international API supply contract stipulates that any chemical impurity exceeding 0.05% _____ quantified and toxicologically characterized.", "be", "is", "will be", "shall to be", "Mandative subjunctive in supply quality agreements: 'stipulates that any impurity be quantified'.")
    ]
    prompt, correct_text, w1, w2, w3, rule = c2_scenarios[q_idx % len(c2_scenarios)]
    distractors = [w1, w2, w3]
    correct_exp = f"C2 chemical patent litigation & toxicological discourse: {rule}"
    distractor_exps = [
        f"Option '{w1}' violates formal mandative subjunctive or inversion rules.",
        f"Option '{w2}' applies indicative or non-inverted phrasing unsuited to regulatory litigation.",
        f"Option '{w3}' is completely non-standard in international pharmacopeial jurisprudence."
    ]
    cz_pt = "High-level scientific and regulatory chemistry discourse requires absolute command of mandative subjunctive ('insisted that it be performed') and inversion ('Seldom have agencies accepted')."

    opts = {target_k: correct_text}
    other_keys = [k for k in ["A", "B", "C", "D"] if k != target_k]
    exps = {"correct": correct_exp}
    for i, ok in enumerate(other_keys):
        opts[ok] = distractors[i]
        exps[f"wrong_{ok}"] = distractor_exps[i]

    return make_q(qid, prompt, opts, target_k, exps, cz_pt, module_meta["workplace_track"])

def generate_tapi_chem_modules():
    curriculum = get_tapi_chem_curriculum()
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
                    f"Master professional {mod['grammar_focus']} in organic API synthesis and QC analysis",
                    f"Eliminate common Czech interference errors in {mod['title'].lower()}",
                    "Demonstrate precision in HPLC, Karl Fischer, and pharmacopeial compliance documentation"
                ],
                questions=questions
            )
            all_modules[tid] = test_obj

    return all_modules

if __name__ == "__main__":
    mods = generate_tapi_chem_modules()
    print(f"Generated {len(mods)} Tapi Chemistry modules.")
