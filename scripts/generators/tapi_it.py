"""
Generator for all 80 Tapi IT modules (20 A2, 20 B1, 20 B2, 20 C1).
Preserves existing validated modules and procedural-generates the remainder with high pedagogical rigor.
"""

import sys
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(ROOT / "scripts"))

from curriculum_catalog import get_tapi_it_curriculum
from generators.common import make_q, build_test_module, KEY_PATTERN

EXISTING_TESTS_DIR = ROOT / "tapi-it" / "data" / "tests"

A2_IT_SCENARIOS = [
    ("The service desk technician", "the user's Active Directory password via the IT support portal", "reset", "resets", "reset", "resetting", "Czech 'technik resetuje'. English 3rd person singular takes -s: 'resets'."),
    ("The system administrator", "the virtual domain controller server after installing security patches", "restart", "restarts", "restarted", "restarting", "Singular subject takes 'restarts' with -s."),
    ("The network technician", "the Cat6 ethernet cable directly into patch panel port 12", "plug", "plugs", "plugged", "plugging", "Singular subject takes 'plugs'."),
    ("The cybersecurity analyst", "the endpoint antivirus status on every newly enrolled laptop", "verify", "verifies", "verified", "verifying", "Verb ending in consonant+y changes to -ies: 'verifies'."),
    ("The IT support engineer", "the network printer driver using the automated software catalog", "install", "installs", "installed", "installing", "Singular subject takes 'installs'."),
    ("The infrastructure specialist", "the temperature inside server rack B-04 every morning", "check", "checks", "checked", "checking", "Singular subject takes 'checks'."),
    ("The helpdesk agent", "the high-priority ticket to the Tier 2 networking team", "escalate", "escalates", "escalated", "escalating", "Singular subject takes 'escalates'."),
    ("The database administrator", "the automated off-site cloud backup status every night", "monitor", "monitors", "monitored", "monitoring", "Singular subject takes 'monitors'."),
    ("The cloud operations technician", "unassigned IP addresses from the corporate DHCP scope", "release", "releases", "released", "releasing", "Singular subject takes 'releases'."),
    ("The workstation engineer", "the external USB-C docking station with dual DisplayPort monitors", "configure", "configures", "configured", "configuring", "Singular subject takes 'configures'.")
]

def generate_a2_question(module_meta, q_idx):
    qid = f"{module_meta['test_id']}-Q{q_idx+1}"
    target_k = KEY_PATTERN[q_idx % len(KEY_PATTERN)]
    sc = A2_IT_SCENARIOS[q_idx % len(A2_IT_SCENARIOS)]
    subj, context, v_base, v_3rd, v_past, v_ing, cz_note = sc
    mod_num = int(module_meta['test_id'].split('-')[-1])

    if mod_num in [1, 5, 13, 19, 20]: # Imperatives & Cybersecurity Rules
        prompt = f"Always make sure that you _____ {context} to comply with IT security policy."
        correct_text = v_base
        distractors = ["to " + v_base, v_3rd, v_ing]
        correct_exp = f"'make sure that you' is followed by base verb '{v_base}' in the present tense clause."
        distractor_exps = [
            f"'to {v_base}' is ungrammatical; finite that-clause requires base verb, not infinitive with 'to'.",
            f"3rd person singular '{v_3rd}' cannot agree with subject 'you'.",
            f"Participle '{v_ing}' cannot act as finite verb without auxiliary."
        ]
        cz_pt = f"Czech 'ujistěte se, že resetujete'. In English that-clauses with 'you', use base form: 'that you {v_base}'."
    elif mod_num in [3, 10]: # Past Simple
        prompt = f"Yesterday during the network maintenance window, {subj.lower()} _____ {context}."
        correct_text = v_past
        distractors = [v_base, "has " + v_past, "is " + v_ing]
        correct_exp = f"Specific completed past time 'Yesterday' strictly requires Past Simple '{v_past}'."
        distractor_exps = [
            f"Base form '{v_base}' lacks past tense marking.",
            f"Present Perfect 'has {v_past}' cannot co-occur with 'yesterday'.",
            f"Present Continuous describes current actions, not yesterday's finished events."
        ]
        cz_pt = f"Czech uses the same past tense, but in English, 'yesterday' strictly triggers Past Simple ('{v_past}')."
    elif mod_num in [4, 18]: # Prepositions of Place
        preps = ["into", "inside", "between", "behind", "underneath", "above", "across", "along", "against", "from"]
        target_p = preps[q_idx % len(preps)]
        prompt = f"Connect the fiber optic patch lead _____ the primary core switch SFP port."
        correct_text = target_p
        distractors = [p for p in preps if p != target_p][:3]
        correct_exp = f"Preposition '{target_p}' accurately identifies the physical hardware connection."
        distractor_exps = [
            f"Preposition '{distractors[0]}' expresses incorrect spatial positioning.",
            f"Preposition '{distractors[1]}' does not fit the port connection geometry.",
            f"Preposition '{distractors[2]}' indicates wrong direction."
        ]
        cz_pt = "IT cabling prepositions: 'into the port' = do portu."
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
        ("the primary database cluster failover", "trigger", "had been triggered", "was triggered", "has been triggered", "triggering"),
        ("the Active Directory domain controller sync", "restore", "had been restored", "was restored", "has been restored", "restoring"),
        ("the cloud firewall security rule update", "deploy", "had been deployed", "was deployed", "has been deployed", "deploying"),
        ("the corrupted virtual machine snapshot", "rollback", "had been rolled back", "was rolled back", "has been rolled back", "rolling back"),
        ("the DNS cache resolution discrepancy", "flush", "had been flushed", "was flushed", "has been flushed", "flushing"),
        ("the critical operating system kernel patch", "install", "had been installed", "was installed", "has been installed", "installing"),
        ("the multi-factor authentication (MFA) token", "re-synchronize", "had been re-synchronized", "was re-synchronized", "has been re-synchronized", "re-synchronizing"),
        ("the isolated ransomware quarantine subnet", "activate", "had been activated", "was activated", "has been activated", "activating"),
        ("the off-site encrypted disaster recovery backup", "verify", "had been verified", "was verified", "has been verified", "verifying"),
        ("the VPN gateway SSL certificate renewal", "complete", "had been completed", "was completed", "has been completed", "completing")
    ]
    sys_event, action, had_been, was_v, has_been, v_ing = b1_contexts[q_idx % len(b1_contexts)]

    if mod_num in [1, 4, 16]: # Past Simple vs Past Perfect
        prompt = f"By the time the CISO initiated the incident escalation call, {sys_event} _____ by the DevOps engineers."
        correct_text = had_been
        distractors = [was_v, has_been, "didn't " + action]
        correct_exp = f"Past Perfect Passive ('{had_been}') is required because the DevOps action occurred prior to the CISO's past call."
        distractor_exps = [
            f"Past Simple ('{was_v}') fails to indicate precedence before 'initiated'.",
            f"Present Perfect ('{has_been}') cannot connect to a past narrative frame.",
            f"'didn't {action}' is active voice; IT systems and backups are acted upon passively."
        ]
        cz_pt = "In IT post-mortems, use Past Perfect Passive to document infrastructure changes completed prior to an outage detection."
    elif mod_num in [3, 13]: # Conditionals in Networking
        prompt = f"If the secondary fiber link _____ during high traffic load, the BGP router will reroute packets automatically."
        correct_text = "fails"
        distractors = ["will fail", "would fail", "failed"]
        correct_exp = "First conditional if-clause takes Present Simple ('fails') for automated network routing rules."
        distractor_exps = [
            "Cannot use 'will' in conditional if-clauses.",
            "Cannot use 'would' in a real First Conditional.",
            "Past tense 'failed' creates an unreal condition, mismatched with 'will reroute'."
        ]
        cz_pt = "Never use 'will' in network troubleshooting if-clauses (*If the link will fail*). Use Present Simple: 'If the link fails'."
    else: # Passive voice in IT policies
        prompt = f"All production cloud server access credentials _____ every ninety days under corporate security baseline standards."
        correct_text = "must be rotated"
        distractors = ["must to be rotated", "must rotate", "are must be rotated"]
        correct_exp = "Passive construction with modal: 'must be rotated'."
        distractor_exps = [
            "'must to be' is ungrammatical; modal 'must' takes bare infinitive.",
            "'must rotate' is active voice; credentials do not rotate themselves.",
            "'are must' is completely ungrammatical in English."
        ]
        cz_pt = "Enterprise security policies strictly require passive voice with modals: 'must be rotated' (musí být obměňovány)."

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
        ("The Zero Trust security policy requires that every API microservice request _____ mutual TLS certificates before granting access.", "validate", "validates", "shall validate", "must to validate", "Mandative subjunctive after 'requires that' takes base form 'validate'."),
        ("Under no circumstances _____ allow remote desktop protocol (RDP) ports to remain exposed to the public internet.", "should engineers", "engineers should", "engineers must to", "shall engineers to", "Negative inversion: 'Under no circumstances should engineers allow'."),
        ("It is imperative that all multi-tenant cloud storage buckets _____ encrypted with customer-managed KMS keys.", "be", "is", "was", "must to be", "Formulaic subjunctive after 'imperative that' requires base form 'be'."),
        ("Had the cloud architect configured multi-region redundancy, the availability zone outage _____ service downtime.", "would not have caused", "would not cause", "had not caused", "will not cause", "Inverted Third Conditional result: 'would not have caused'."),
        ("The SOC 2 Type II audit report mandates that administrative privileged access logs _____ retained for at least 365 days.", "be", "are", "were", "will be", "Passive mandative subjunctive: 'mandates that logs be retained'."),
        ("Rarely _____ an advanced persistent threat (APT) penetrate an enterprise network without prior reconnaissance of vulnerable VPN endpoints.", "does", "is", "will", "has", "Negative inversion: 'Rarely does an APT penetrate'."),
        ("If the CI/CD pipeline had automated static application security testing (SAST), the vulnerability _____ in production today.", "would not exist", "would not have existed", "will not exist", "does not exist", "Mixed conditional: past condition ('had automated') with present consequence ('today') takes 'would not exist'."),
        ("The 21 CFR Part 11 guidance stipulates that computerized system audit trails _____ secure, computer-generated, and time-stamped.", "be", "are", "will be", "must to be", "Mandative subjunctive in GxP IT guidance: 'stipulates that audit trails be secure'."),
        ("Only by enforcing strict least-privilege role-based access control (RBAC) _____ mitigate the blast radius of compromised credentials.", "can organizations", "organizations can", "organizations could", "was organizations can", "Inversion after 'Only by...': 'can organizations mitigate'."),
        ("Were the container cluster _____ a distributed denial-of-service (DDoS) flood, automated ingress rate-limiting rules would mitigate the impact.", "to suffer", "suffers", "will suffer", "would suffer", "Inverted Second Conditional: 'Were the cluster to suffer...' expresses formal hypothetical condition.")
    ]
    prompt, correct_text, w1, w2, w3, rule = b2_scenarios[q_idx % len(b2_scenarios)]
    distractors = [w1, w2, w3]
    correct_exp = f"B2 cybersecurity & cloud architecture syntax: {rule}"
    distractor_exps = [
        f"Option '{w1}' violates formal mandative subjunctive or inversion rules.",
        f"Option '{w2}' applies inappropriate indicative or non-inverted phrasing.",
        f"Option '{w3}' is ungrammatical in formal enterprise IT discourse."
    ]
    cz_pt = "Enterprise cybersecurity directives require rigorous mandative subjunctive ('mandates that logs be retained') and auxiliary inversion ('Rarely does an APT penetrate')."

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
        ("The European Data Protection Board mandated that the enterprise cloud provider _____ all transatlantic telemetry transfers pending adequacy review.", "suspend", "suspends", "shall suspend", "must to suspend", "Mandative subjunctive requires base form 'suspend' after 'mandated that'."),
        ("Seldom _____ international commercial arbitral tribunals awarded punitive damages against hyperscale cloud providers for unannounced SLA defaults.", "have", "are", "were", "did", "Negative inversion: 'Seldom have arbitral tribunals awarded'."),
        ("It is of paramount corporate governance necessity that the Chief Information Security Officer (CISO) _____ direct reporting access to the Board.", "retain", "retains", "will retain", "must to retain", "Formulaic subjunctive: 'paramount governance necessity that the CISO retain'."),
        ("_____ the cloud infrastructure provider to repudiate the 99.999% high-availability service level agreement, catastrophic business interruption liability would ensue.", "Were", "Had", "Should", "If were", "Second Conditional inversion with 'Were [subject] to [verb]' expresses formal hypothetical repudiation."),
        ("Not only _____ fail to implement timely zero-day mitigation patches, but the enterprise also concealed the ransomware breach for forty-eight hours.", "did the third-party vendor", "the third-party vendor did", "was the third-party vendor", "has the third-party vendor", "Inversion after 'Not only': 'did the vendor fail'."),
        ("Under no circumstances _____ the corporate incident response team to pay ransom extortions without prior approval from sovereign sanctions authorities.", "is", "are", "will", "has", "Negative inversion: 'Under no circumstances is the team to pay'."),
        ("The Lead Forensic Investigator insisted that digital chain of custody records _____ preserved in immutable write-once-read-many (WORM) storage.", "be", "are", "were", "will be", "Passive mandative subjunctive: 'insisted that records be preserved'."),
        ("Had the enterprise not decoupled its active directory forest from the breached subsidiary, lateral ransomware propagation _____ the entire global domain.", "would have paralyzed", "would paralyze", "had paralyzed", "will paralyze", "Third Conditional counterfactual: 'would have paralyzed'."),
        ("Barely _____ the digital forensics team completed memory snapshot acquisition when the nation-state threat actor initiated self-deleting wiper routines.", "had", "was", "did", "has", "Inversion: 'Barely had the team completed... when...'."),
        ("The multi-million dollar cloud services master agreement stipulates that all customer data encryption keys _____ exclusively under customer escrow control.", "remain", "remains", "will remain", "shall to remain", "Mandative subjunctive in SLA contracts: 'stipulates that keys remain under customer control'.")
    ]
    prompt, correct_text, w1, w2, w3, rule = c1_scenarios[q_idx % len(c1_scenarios)]
    distractors = [w1, w2, w3]
    correct_exp = f"C1 cloud litigation & cyber governance discourse: {rule}"
    distractor_exps = [
        f"Option '{w1}' violates formal mandative subjunctive or inversion rules.",
        f"Option '{w2}' applies inappropriate indicative or non-inverted syntax in formal legal IT discourse.",
        f"Option '{w3}' is completely non-standard in international cyber jurisprudence."
    ]
    cz_pt = "Executive cyber governance and cloud contract litigation demand absolute mastery of mandative subjunctive ('mandated that it suspend') and inversion ('Seldom have tribunals awarded')."

    opts = {target_k: correct_text}
    other_keys = [k for k in ["A", "B", "C", "D"] if k != target_k]
    exps = {"correct": correct_exp}
    for i, ok in enumerate(other_keys):
        opts[ok] = distractors[i]
        exps[f"wrong_{ok}"] = distractor_exps[i]

    return make_q(qid, prompt, opts, target_k, exps, cz_pt, module_meta["workplace_track"])

def generate_tapi_it_modules():
    curriculum = get_tapi_it_curriculum()
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
                    f"Master professional {mod['grammar_focus']} in enterprise IT infrastructure and cloud operations",
                    f"Eliminate common Czech interference errors in {mod['title'].lower()}",
                    "Demonstrate precision in Zero Trust architecture, ITIL incident management, and cyber governance"
                ],
                questions=questions
            )
            all_modules[tid] = test_obj

    return all_modules

if __name__ == "__main__":
    mods = generate_tapi_it_modules()
    print(f"Generated {len(mods)} Tapi IT modules.")
