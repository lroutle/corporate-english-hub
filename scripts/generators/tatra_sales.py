"""
Generator for all 80 Tatra Sales and Engineering modules (20 A2, 20 B1, 20 B2, 20 C2).
Preserves existing validated modules and procedural-generates the remainder with high pedagogical rigor.
"""

import sys
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(ROOT / "scripts"))

from curriculum_catalog import get_tatra_sales_curriculum
from generators.common import make_q, build_test_module, KEY_PATTERN

EXISTING_TESTS_DIR = ROOT / "tatra-sales-engineering" / "data" / "tests"

A2_SALES_SCENARIOS = [
    ("Our sales manager", "the revised quotation for twenty 8x8 chassis to the Egyptian ministry", "send", "sends", "sent", "sending", "Czech 'manažer posílá'. English 3rd person singular takes -s: 'sends'."),
    ("The dealership representative", "the proforma invoice before arranging the bank wire transfer", "review", "reviews", "reviewed", "reviewing", "Singular subject takes 'reviews' with 3rd person singular -s."),
    ("Our logistics coordinator", "the delivery schedule with the Hamburg sea freight forwarder", "confirm", "confirms", "confirmed", "confirming", "Czech 'koordinátor potvrzuje'. Use 'confirms'."),
    ("The prospective client", "about the payload capacity of the Tatra Phoenix mining tipper", "inquire", "inquires", "inquired", "inquiring", "Singular subject takes 'inquires'."),
    ("The export specialist", "all export customs documents into the digital freight portal", "upload", "uploads", "uploaded", "uploading", "Singular subject takes 'uploads'."),
    ("The defense liaison officer", "the VIP client delegation at Prague Airport tomorrow morning", "meet", "meets", "met", "meeting", "Singular subject takes 'meets'."),
    ("The technical sales engineer", "the chassis technical parameters during the video conference", "explain", "explains", "explained", "explaining", "Singular subject takes 'explains'."),
    ("The international distributor", "five spare drive axles under warranty reimbursement", "claim", "claims", "claimed", "claiming", "Singular subject takes 'claims'."),
    ("The commercial assistant", "order confirmation letters to foreign dealerships every Friday", "email", "emails", "emailed", "emailing", "Singular subject takes 'emails' with -s."),
    ("The procurement manager", "the contract payment milestone once shipping containers are sealed", "release", "releases", "released", "releasing", "Singular subject takes 'releases'.")
]

def generate_a2_question(module_meta, q_idx):
    qid = f"{module_meta['test_id']}-Q{q_idx+1}"
    target_k = KEY_PATTERN[q_idx % len(KEY_PATTERN)]
    sc = A2_SALES_SCENARIOS[q_idx % len(A2_SALES_SCENARIOS)]
    subj, context, v_base, v_3rd, v_past, v_ing, cz_note = sc
    mod_num = int(module_meta['test_id'].split('-')[-1])

    if mod_num in [2, 6, 14, 19]: # Polite Email Requests
        prompt = f"Could you please _____ {context} as soon as possible?"
        correct_text = v_base
        distractors = ["to " + v_base, v_3rd, v_ing]
        correct_exp = f"Polite modal request 'Could you please...' is followed by bare infinitive '{v_base}' without 'to'."
        distractor_exps = [
            f"'to {v_base}' is incorrect; modal 'could' does not take 'to'.",
            f"3rd person singular '{v_3rd}' cannot follow modal auxiliary 'could'.",
            f"Participle '{v_ing}' cannot follow modal auxiliary 'could'."
        ]
        cz_pt = f"Czech 'Mohl byste prosím poslat...'. After 'Could you please', use the bare verb '{v_base}' without 'to'."
    elif mod_num in [3, 8, 11]: # Past Simple
        prompt = f"Last week at the defense trade fair, {subj.lower()} _____ {context}."
        correct_text = v_past
        distractors = [v_base, "has " + v_past, "is " + v_ing]
        correct_exp = f"Completed past time reference 'Last week' strictly requires Past Simple '{v_past}'."
        distractor_exps = [
            f"Base form '{v_base}' lacks past inflection.",
            f"Present Perfect 'has {v_past}' cannot accompany closed past date 'Last week'.",
            f"Present Continuous describes current actions, not last week's events."
        ]
        cz_pt = f"Czech uses past tense for both, but English 'Last week' strictly triggers Past Simple ('{v_past}')."
    elif mod_num in [5, 17]: # Prepositions of Time & Logistics
        preps = ["by", "at", "on", "in", "until", "before", "during", "after", "within", "throughout"]
        target_p = preps[q_idx % len(preps)]
        prompt = f"The export consignment must clear customs _____ Friday afternoon to meet the vessel sailing date."
        correct_text = target_p
        distractors = [p for p in preps if p != target_p][:3]
        correct_exp = f"Preposition '{target_p}' correctly expresses the required time deadline or constraint."
        distractor_exps = [
            f"Preposition '{distractors[0]}' expresses incorrect temporal relationship.",
            f"Preposition '{distractors[1]}' does not fit the deadline context.",
            f"Preposition '{distractors[2]}' is ungrammatical with this time phrase."
        ]
        cz_pt = "Deadline prepositions: 'by Friday' = nejpozději do pátku. Do not confuse with 'until' (až do)."
    else: # Present Simple
        prompt = f"{subj} regularly _____ {context}."
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
        ("the irrevocable letter of credit (L/C)", "issue", "had been issued", "was issued", "has been issued", "issuing"),
        ("the bilateral commercial sales contract", "countersign", "had been countersigned", "was countersigned", "has been countersigned", "countersigning"),
        ("the ocean bill of lading clean-on-board endorsement", "receive", "had been received", "was received", "has been received", "receiving"),
        ("the customs export declaration for twenty defense trucks", "clear", "had been cleared", "was cleared", "has been cleared", "clearing"),
        ("the end-user certificate (EUC) authentication", "verify", "had been verified", "was verified", "has been verified", "verifying"),
        ("the 10% advance performance bond bank guarantee", "lodge", "had been lodged", "was lodged", "has been lodged", "lodging"),
        ("the sea freight insurance certificate covering 110% of CIF value", "endorse", "had been endorsed", "was endorsed", "has been endorsed", "endorsing"),
        ("the spare parts consignment dispatch note", "release", "had been released", "was released", "has been released", "releasing"),
        ("the official military homologation certificate", "grant", "had been granted", "was granted", "has been granted", "granting"),
        ("the final acceptance protocol by the client's inspection committee", "sign", "had been signed", "was signed", "has been signed", "signing")
    ]
    doc, action, had_been, was_v, has_been, v_ing = b1_contexts[q_idx % len(b1_contexts)]

    if mod_num in [1, 5, 13]: # Present Perfect vs Past Simple / Past Perfect
        prompt = f"By the time the container vessel docked at Alexandria port, {doc} _____ by the issuing bank."
        correct_text = had_been
        distractors = [was_v, has_been, "didn't " + action]
        correct_exp = f"Past Perfect Passive ('{had_been}') correctly expresses an action completed prior to the past docking event."
        distractor_exps = [
            f"Past Simple ('{was_v}') does not show priority before past docking.",
            f"Present Perfect ('{has_been}') cannot connect to a completed past narrative.",
            f"'didn't {action}' is active voice; commercial documents are acted upon passively."
        ]
        cz_pt = "Czech narrative uses past tense for both ('než loď přistála, akreditiv byl otevřen'). English contracts require Past Perfect."
    elif mod_num in [2, 7, 16]: # Incoterms 2020 Rules
        prompt = f"Under Incoterms 2020 DAP terms, the seller _____ responsible for unloading the trucks at the buyer's destination terminal."
        correct_text = "is not"
        distractors = ["is", "shall to be", "must to be"]
        correct_exp = "Under DAP (Delivered at Place), seller delivers ready for unloading; unloading is buyer's obligation."
        distractor_exps = [
            "'is' contradicts Incoterms 2020 DAP rules.",
            "'shall to be' is ungrammatical; modal 'shall' does not take 'to'.",
            "'must to be' is ungrammatical."
        ]
        cz_pt = "Incoterms 2020: Under DAP, risk transfers before unloading. Seller 'is not' responsible for offloading costs."
    else: # Commercial Negotiations & Modals
        prompt = f"If the defense ministry _____ the contract by June 30, Tatra will guarantee delivery before the fiscal year-end."
        correct_text = "signs"
        distractors = ["will sign", "would sign", "signed"]
        correct_exp = "First conditional if-clause requires Present Simple ('signs') for commercial offers."
        distractor_exps = [
            "Cannot use 'will' in the if-clause of commercial contracts.",
            "Cannot use 'would' in a real First Conditional commercial offer.",
            "Past 'signed' would create an unreal Second Conditional."
        ]
        cz_pt = "Contractual conditions: Never write *If the ministry will sign*. Use Present Simple: 'If the ministry signs'."

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
        ("The defense tender evaluation committee stipulated that Tatra _____ an irrevocable warranty bond for 5% of the total contract value.", "furnish", "furnishes", "shall furnish", "must to furnish", "Mandative subjunctive after 'stipulated that' requires base form 'furnish'."),
        ("Rarely _____ an international buyer agree to 100% advance payment without demanding a standby letter of credit.", "does", "is", "will", "has", "Negative restrictive 'Rarely' triggers auxiliary inversion: 'Rarely does an international buyer agree'."),
        ("Under no circumstances _____ accept payment from a third-party account not specified in the End-User Certificate.", "may our sales executives", "our sales executives may", "our sales executives must to", "shall our sales executives to", "Negative inversion: 'Under no circumstances may our sales executives accept'."),
        ("Had the distributor notified us of the import tariff increase earlier, we _____ the CIF quotation accordingly.", "would have adjusted", "would adjust", "had adjusted", "will adjust", "Inverted Third Conditional result clause: 'Had the distributor notified... we would have adjusted'."),
        ("It is vital that the export compliance officer _____ every chassis serial number against international military sanctions lists.", "cross-check", "cross-checks", "cross-checked", "must cross-checks", "Formulaic subjunctive after 'vital that' takes base form 'cross-check'."),
        ("Scarcely _____ the defense contract been signed in Abu Dhabi when geopolitical instability disrupted the maritime transit corridor.", "had", "was", "did", "has", "Negative inversion: 'Scarcely had the contract been signed... when...'."),
        ("If Tatra had not secured the EGAP export credit insurance policy, the company _____ significant sovereign default risk today.", "would face", "would have faced", "will face", "faces", "Mixed conditional: past condition ('had not secured') with present consequence ('today') takes 'would face'."),
        ("The tender board insisted that liquidated damages for delayed delivery _____ at a maximum ceiling of 5% of contract value.", "be capped", "is capped", "will be capped", "must to be capped", "Passive mandative subjunctive: 'insisted that damages be capped'."),
        ("Only by establishing a local assembly kit (CKD) joint venture _____ qualify for the mandatory 40% domestic industrial offset requirement.", "could our consortium", "our consortium could", "our consortium can", "was our consortium could", "Inversion after 'Only by...': 'could our consortium qualify'."),
        ("Were the ministry _____ the tender specifications to exclude all air-cooled engines, our legal counsel would file an immediate procurement protest.", "to revise", "revises", "will revise", "would revise", "Inverted Second Conditional: 'Were the ministry to revise...' expresses hypothetical future possibility.")
    ]
    prompt, correct_text, w1, w2, w3, rule = b2_scenarios[q_idx % len(b2_scenarios)]
    distractors = [w1, w2, w3]
    correct_exp = f"B2 commercial negotiation syntax: {rule}"
    distractor_exps = [
        f"Option '{w1}' fails to apply the required inversion or subjunctive base form.",
        f"Option '{w2}' is grammatically inappropriate for this formal commercial context.",
        f"Option '{w3}' is ungrammatical in standard business English."
    ]
    cz_pt = "High-stakes commercial tenders prioritize formal subjunctive ('insisted that it be capped') and negative inversion ('Rarely does a buyer agree')."

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
        ("The international arbitration tribunal mandated that the respondent sovereign state _____ all confiscated vehicle documentation forthwith.", "restitute", "restitutes", "shall restitute", "must to restitute", "Mandative subjunctive requires base form 'restitute' after 'mandated that'."),
        ("Seldom _____ an international court of arbitration upheld a claim of force majeure arising purely from predictable currency devaluations.", "has", "is", "was", "did", "Negative inversion: 'Seldom has an international court upheld'."),
        ("It is of paramount legal necessity that each consortium partner _____ strict joint and several liability under the EPCMV contract.", "disclaim", "disclaims", "will disclaim", "must to disclaim", "Formulaic subjunctive after 'paramount legal necessity that' requires base form 'disclaim'."),
        ("_____ the defense procurement agency to repudiate the bilateral offset memorandum, immediate recourse to the ICC in Paris would ensue.", "Were", "Had", "Should", "If were", "Second Conditional inversion with 'Were [subject] to [verb]' expresses formal hypothetical repudiation."),
        ("Not only _____ fail to open the irrevocable confirmed letter of credit on schedule, but the buyer also repudiated the demurrage invoice.", "did the sovereign buyer", "the sovereign buyer did", "was the sovereign buyer", "has the sovereign buyer", "Inversion after 'Not only': 'did the sovereign buyer fail'."),
        ("Under no circumstances _____ the arbitral tribunal to admit unverified third-country bill of lading affidavits into evidence.", "is", "are", "will", "has", "Negative inversion: 'Under no circumstances is the tribunal to admit'."),
        ("The lead commercial litigator insisted that all settlement funds _____ in an escrow account governed by Swiss federal law.", "be deposited", "are deposited", "will be deposited", "must to be deposited", "Passive mandative subjunctive: 'insisted that funds be deposited'."),
        ("Had the state enterprise not sovereignly indemnified the manufacturer against expropriation, the multimillion-dollar fleet delivery _____ halted.", "would have been", "would be", "had been", "will be", "Third Conditional passive result: 'would have been halted'."),
        ("Barely _____ the arbitral award been rendered in Zurich when the losing party initiated annulment proceedings in the federal supreme court.", "had", "was", "did", "has", "Inversion: 'Barely had the award been rendered... when...'."),
        ("The cross-border concession agreement stipulates that any dispute arising out of or in connection with this contract _____ referred to arbitration.", "be", "is", "will be", "shall to be", "Mandative subjunctive in arbitration agreements: 'stipulates that any dispute be referred'.")
    ]
    prompt, correct_text, w1, w2, w3, rule = c2_scenarios[q_idx % len(c2_scenarios)]
    distractors = [w1, w2, w3]
    correct_exp = f"C2 legal and arbitration discourse: {rule}"
    distractor_exps = [
        f"Option '{w1}' violates formal arbitration syntax or mandative subjunctive requirements.",
        f"Option '{w2}' is an ungrammatical indicative construction in legal agreements.",
        f"Option '{w3}' is completely non-standard in international contract law."
    ]
    cz_pt = "International arbitration and defense contracts demand strict subjunctive ('stipulate that dispute be referred') and auxiliary inversion ('Seldom has the court upheld')."

    opts = {target_k: correct_text}
    other_keys = [k for k in ["A", "B", "C", "D"] if k != target_k]
    exps = {"correct": correct_exp}
    for i, ok in enumerate(other_keys):
        opts[ok] = distractors[i]
        exps[f"wrong_{ok}"] = distractor_exps[i]

    return make_q(qid, prompt, opts, target_k, exps, cz_pt, module_meta["workplace_track"])

def generate_tatra_sales_modules():
    curriculum = get_tatra_sales_curriculum()
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
                    f"Master professional {mod['grammar_focus']} in technical sales and export contracts",
                    f"Eliminate common Czech interference errors in {mod['title'].lower()}",
                    "Demonstrate mastery in international negotiations and Incoterms documentation"
                ],
                questions=questions
            )
            all_modules[tid] = test_obj

    return all_modules

if __name__ == "__main__":
    mods = generate_tatra_sales_modules()
    print(f"Generated {len(mods)} Tatra Sales modules.")
