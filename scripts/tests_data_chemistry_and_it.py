"""
Test generators for Tapi Chemistry, Teva IT, and Teva Engineering advanced tests.
"""

def get_chem_and_it_tests(q_helper):
    q = q_helper
    tests = {}

    # =========================================================================
    # TAPI CHEMISTRY
    # =========================================================================

    # TAPI-CHEM-A2-002: Daily QC Testing & Analytical Weighing: Present Simple
    tests["TAPI-CHEM-A2-002"] = {
        "test_id": "TAPI-CHEM-A2-002",
        "title": "Daily QC Testing & Analytical Weighing: Present Simple",
        "level": "A2",
        "category": "core",
        "workplace_track": "Analytical Chemistry (HPLC, GC, Spectroscopy)",
        "estimated_time_minutes": 10,
        "description": "Describe daily analytical balance calibration, sample preparation, and reagent dilution using Present Simple.",
        "learning_objectives": [
            "Use Present Simple 3rd person -s for laboratory routines",
            "State standard analytical procedures with frequency adverbs",
            "Avoid Czenglish omission of auxiliary in laboratory questions"
        ],
        "questions": [
            q("TAPI-CHEM-A2-002-Q1", "The QC chemist _____ the analytical balance using certified calibration weights every morning.",
              {"A": "calibrate", "B": "calibrates", "C": "is calibrate", "D": "calibrating"}, "B",
              {"correct": "Singular subject 'chemist' takes 'calibrates' with 3rd person -s.", "wrong_A": "Lacks singular -s.", "wrong_C": "Ungrammatical.", "wrong_D": "Participle alone cannot be verb."},
              "Czech 'Chemik kalibruje'. Singular subject takes '-s': 'calibrates'.", "Analytical Chemistry (HPLC, GC, Spectroscopy)"),
            q("TAPI-CHEM-A2-002-Q2", "We always _____ volumetric flasks with ultrapure Milli-Q water before preparing buffer solutions.",
              {"A": "rinses", "B": "is rinse", "C": "rinse", "D": "rinsing"}, "C",
              {"correct": "Plural subject 'We' takes base verb 'rinse'.", "wrong_A": "'rinses' is singular.", "wrong_B": "Ungrammatical.", "wrong_D": "Participle alone cannot be verb."},
              "Czech 'Vždy vyplachujeme...'. Plural subject takes base verb: 'rinse'.", "Analytical Chemistry (HPLC, GC, Spectroscopy)"),
            q("TAPI-CHEM-A2-002-Q3", "The pH meter _____ a two-point buffer calibration before any titration testing.",
              {"A": "requires", "B": "require", "C": "is require", "D": "requiring"}, "A",
              {"correct": "Singular subject 'pH meter' takes 'requires'.", "wrong_B": "Lacks singular -s.", "wrong_C": "Ungrammatical.", "wrong_D": "Participle alone cannot be verb."},
              "Czech 'pH metr vyžaduje...'. Singular subject takes '-s': 'requires'.", "Analytical Chemistry (HPLC, GC, Spectroscopy)"),
            q("TAPI-CHEM-A2-002-Q4", "_____ the auto-sampler inject five microliters of solution for each chromatography vial?",
              {"A": "Is", "B": "Do", "C": "Are", "D": "Does"}, "D",
              {"correct": "Singular subject 'the auto-sampler' takes auxiliary 'Does' in Present Simple questions.", "wrong_A": "'Is' requires continuous -ing.", "wrong_B": "'Do' is plural.", "wrong_C": "'Are' is plural."},
              "Czech 'Dávkuje autosampler 5 mikrolitrů...?'. Question takes 'Does the auto-sampler inject...?'.", "Analytical Chemistry (HPLC, GC, Spectroscopy)"),
            q("TAPI-CHEM-A2-002-Q5", "Analytical chemists _____ magnetic stirrers to dissolve solid active ingredients completely.",
              {"A": "uses", "B": "use", "C": "are use", "D": "using"}, "B",
              {"correct": "Plural subject 'chemists' takes base verb 'use'.", "wrong_A": "'uses' is singular.", "wrong_C": "Ungrammatical.", "wrong_D": "Participle alone cannot be verb."},
              "Czech 'Chemici používají...'. Plural subject takes base verb: 'use'.", "Hazardous Reagents, Solvent Recovery & Lab Safety"),
            q("TAPI-CHEM-A2-002-Q6", "The laboratory technician _____ not leave volatile organic solvents uncovered on the bench.",
              {"A": "is", "B": "does", "C": "do", "D": "has"}, "B",
              {"correct": "Singular negative Present Simple takes 'does not leave'.", "wrong_A": "'is not leave' is ungrammatical.", "wrong_C": "'do' is plural.", "wrong_D": "'has' cannot negate action verbs like this."},
              "Czech 'Technik nenechává...'. Use 'does not leave'.", "Hazardous Reagents, Solvent Recovery & Lab Safety"),
            q("TAPI-CHEM-A2-002-Q7", "How often _____ the QC supervisor verify the HPLC baseline stability?",
              {"A": "is", "B": "do", "C": "are", "D": "does"}, "D",
              {"correct": "Singular supervisor subject takes auxiliary 'does': 'How often does the supervisor verify...?'.", "wrong_A": "'is' cannot pair with bare base verb 'verify'.", "wrong_B": "'do' is plural.", "wrong_C": "'are' is plural."},
              "Czech 'Jak často vedoucí ověřuje...?'. Use auxiliary 'does'.", "Analytical Chemistry (HPLC, GC, Spectroscopy)"),
            q("TAPI-CHEM-A2-002-Q8", "The ultrasonic degassing bath _____ dissolved air bubbles from the mobile phase in 15 minutes.",
              {"A": "removes", "B": "remove", "C": "is remove", "D": "removing"}, "A",
              {"correct": "Singular subject 'bath' takes 'removes' with 3rd person -s.", "wrong_B": "Lacks singular -s.", "wrong_C": "Ungrammatical.", "wrong_D": "Participle alone cannot be verb."},
              "Czech 'Ultrazvuková lázeň odstraňuje...'. Singular subject takes '-s': 'removes'.", "Analytical Chemistry (HPLC, GC, Spectroscopy)"),
            q("TAPI-CHEM-A2-002-Q9", "Lab technicians _____ all hazardous chemical reagents into certified waste drums.",
              {"A": "pours", "B": "is pour", "C": "pour", "D": "pouring"}, "C",
              {"correct": "Plural subject 'technicians' takes base verb 'pour'.", "wrong_A": "'pours' is singular.", "wrong_B": "Ungrammatical.", "wrong_D": "Participle alone cannot be verb."},
              "Czech 'Technici vylévají...'. Plural subject takes base verb: 'pour'.", "Hazardous Reagents, Solvent Recovery & Lab Safety"),
            q("TAPI-CHEM-A2-002-Q10", "The spectrophotometer _____ light absorbance at 254 nanometers automatically.",
              {"A": "measure", "B": "measures", "C": "is measure", "D": "measuring"}, "B",
              {"correct": "Singular subject 'spectrophotometer' takes 'measures' with 3rd person -s.", "wrong_A": "Lacks singular -s.", "wrong_C": "Ungrammatical.", "wrong_D": "Participle alone cannot be verb."},
              "Czech 'Spektrofotometr měří...'. Singular subject takes '-s': 'measures'.", "Analytical Chemistry (HPLC, GC, Spectroscopy)")
        ]
    }

    # TAPI-CHEM-B1-001: API Reactor Yield & Solvent Recovery: Present Perfect vs Past Simple
    tests["TAPI-CHEM-B1-001"] = {
        "test_id": "TAPI-CHEM-B1-001",
        "title": "API Reactor Yield & Solvent Recovery: Present Perfect vs Past Simple",
        "level": "B1",
        "category": "core",
        "workplace_track": "Organic Chemical Synthesis & Batch Reactors",
        "estimated_time_minutes": 15,
        "description": "Report chemical batch synthesis yields, solvent recovery percentages, and finished batch releases.",
        "learning_objectives": [
            "Distinguish Present Perfect (recent batch results) from Past Simple (stated times)",
            "Report chemical reaction yields using correct aspectual verbs",
            "Avoid Czech aspectual confusion in chemical production briefings"
        ],
        "questions": [
            q("TAPI-CHEM-B1-001-Q1", "We _____ three synthesis batches of active paracetamol this week.",
              {"A": "synthesized", "B": "have synthesized", "C": "are synthesize", "D": "synthesize"}, "B",
              {"correct": "Unfinished time frame ('this week') requires Present Perfect: 'have synthesized'.", "wrong_A": "'synthesized' requires finished time frame.", "wrong_C": "Ungrammatical.", "wrong_D": "'synthesize' is habitual present."},
              "Czech 'Tento týden jsme syntetizovali'. Unfinished time takes Present Perfect: 'have synthesized'.", "Organic Chemical Synthesis & Batch Reactors"),
            q("TAPI-CHEM-B1-001-Q2", "Yesterday at 14:00, the process chemist _____ the temperature in reactor 2.",
              {"A": "has adjusted", "B": "adjusting", "C": "adjusted", "D": "adjusts"}, "C",
              {"correct": "Specific completed past time ('Yesterday at 14:00') takes Past Simple: 'adjusted'.", "wrong_A": "Present Perfect cannot pair with specific past time 'yesterday'.", "wrong_B": "Participle cannot be verb.", "wrong_D": "'adjusts' is present."},
              "Czech 'Včera ve 14:00 chemik upravil...'. Specific past time takes Past Simple: 'adjusted'.", "Organic Chemical Synthesis & Batch Reactors"),
            q("TAPI-CHEM-B1-001-Q3", "The solvent recovery plant _____ 94% of the recycled acetone so far this month.",
              {"A": "has recovered", "B": "recovered", "C": "was recover", "D": "recovers"}, "A",
              {"correct": "'So far this month' denotes ongoing time up to the present, requiring Present Perfect: 'has recovered'.", "wrong_B": "'recovered' implies a closed past time frame.", "wrong_C": "Ungrammatical.", "wrong_D": "'recovers' is habitual present."},
              "Czech 'Zatím v tomto měsíci recyklovala...'. 'So far' requires Present Perfect: 'has recovered'.", "Hazardous Reagents, Solvent Recovery & Lab Safety"),
            q("TAPI-CHEM-B1-001-Q4", "_____ you already verified the purity profile of batch TAPI-2026-08?",
              {"A": "Did", "B": "Were", "C": "Do", "D": "Have"}, "D",
              {"correct": "'Already' with past participle 'verified' requires Present Perfect auxiliary 'Have you already verified'.", "wrong_A": "'Did you already verified' is ungrammatical (would need base 'verify').", "wrong_B": "'Were' is invalid.", "wrong_C": "'Do' is present."},
              "Czech 'Ověřil jste již čistotu...?'. With 'already' and past participle, use 'Have you already verified...'.", "Analytical Chemistry (HPLC, GC, Spectroscopy)"),
            q("TAPI-CHEM-B1-001-Q5", "The crystallizer temperature _____ suddenly during last night's night shift.",
              {"A": "has dropped", "B": "drops", "C": "dropped", "D": "is dropped"}, "C",
              {"correct": "Specific completed past period ('last night') requires Past Simple: 'dropped'.", "wrong_A": "Present Perfect cannot be used with 'last night'.", "wrong_B": "'drops' is present.", "wrong_D": "'is dropped' is passive."},
              "Czech 'Teplota včera v noci klesla'. 'Last night' takes Past Simple: 'dropped'.", "Organic Chemical Synthesis & Batch Reactors"),
            q("TAPI-CHEM-B1-001-Q6", "The analytical development lab _____ a new HPLC method for chiral separation last quarter.",
              {"A": "has validated", "B": "validated", "C": "is validate", "D": "validates"}, "B",
              {"correct": "Finished past time marker ('last quarter') takes Past Simple: 'validated'.", "wrong_A": "Present Perfect cannot pair with 'last quarter'.", "wrong_C": "Ungrammatical.", "wrong_D": "'validates' is present."},
              "Czech 'Laboratoř validovala metodu minulé čtvrtletí'. Past marker 'last quarter' requires Past Simple: 'validated'.", "Analytical Chemistry (HPLC, GC, Spectroscopy)"),
            q("TAPI-CHEM-B1-001-Q7", "We _____ the final release documentation to the QP yet; the assay test is still running.",
              {"A": "did not submit", "B": "are not submit", "C": "do not submit", "D": "have not submitted"}, "D",
              {"correct": "Negative clause with 'yet' referring to expectation up to now requires Present Perfect: 'have not submitted'.", "wrong_A": "'did not submit... yet' is colloquial American, but Present Perfect is strictly preferred in technical English.", "wrong_B": "Ungrammatical.", "wrong_C": "'do not submit' is present."},
              "Czech 'Zatím jsme nepředložili...'. 'Yet' takes Present Perfect: 'have not submitted'.", "Pharmacopeial Compliance, Impurity Profiling & Regulatory Submissions"),
            q("TAPI-CHEM-B1-001-Q8", "The synthesis reaction _____ for three hours before the cooling jacket was activated.",
              {"A": "had proceeded", "B": "proceeded", "C": "has proceeded", "D": "is proceeding"}, "A",
              {"correct": "Past event that occurred prior to another past action ('was activated') takes Past Perfect: 'had proceeded'.", "wrong_B": "'proceeded' is past simple.", "wrong_C": "'has proceeded' cannot pair with completed past reference.", "wrong_D": "Continuous present."},
              "Czech 'Reakce probíhala již tři hodiny předtím, než...'. Earlier past action takes Past Perfect: 'had proceeded'.", "Organic Chemical Synthesis & Batch Reactors"),
            q("TAPI-CHEM-B1-001-Q9", "The chemical synthesis team _____ just completed the trial synthesis of the active ingredient.",
              {"A": "did", "B": "was", "C": "has", "D": "is"}, "C",
              {"correct": "Adverb 'just' indicating recent completion takes Present Perfect: 'has just completed'.", "wrong_A": "'did' cannot pair with past participle 'completed'.", "wrong_B": "'was' would create passive.", "wrong_D": "'is' is present."},
              "Czech 'Tým právě dokončil...'. 'Just' with past participle takes Present Perfect: 'has just completed'.", "Organic Chemical Synthesis & Batch Reactors"),
            q("TAPI-CHEM-B1-001-Q10", "In 2025, TAPI Opava _____ over 150 metric tons of pharmaceutical intermediates.",
              {"A": "has produced", "B": "produced", "C": "was produce", "D": "produces"}, "B",
              {"correct": "Specific historical past year ('In 2025') requires Past Simple: 'produced'.", "wrong_A": "Present Perfect cannot be used with a specific past year like 'In 2025'.", "wrong_C": "Ungrammatical.", "wrong_D": "'produces' is present."},
              "Czech 'V roce 2025 vyrobila...'. Historical years take Past Simple: 'produced'.", "Organic Chemical Synthesis & Batch Reactors")
        ]
    }

    # =========================================================================
    # TEVA IT
    # =========================================================================

    # TEV-IT-A2-002: Daily Service Desk Support & User Tickets: Present Simple
    tests["TEV-IT-A2-002"] = {
        "test_id": "TEV-IT-A2-002",
        "title": "Daily Service Desk Support & User Tickets: Present Simple",
        "level": "A2",
        "category": "core",
        "workplace_track": "IT Service Desk & Enterprise Support",
        "estimated_time_minutes": 10,
        "description": "Handle IT helpdesk tickets, user account unlocks, and password resets using Present Simple.",
        "learning_objectives": [
            "Use Present Simple 3rd person singular for user ticket handling",
            "Formulate standard troubleshooting questions with 'do / does'",
            "Communicate ticket priorities (P1, P2, P3) accurately"
        ],
        "questions": [
            q("TEV-IT-A2-002-Q1", "The IT service desk technician _____ password reset requests in ServiceNow.",
              {"A": "process", "B": "processes", "C": "is process", "D": "processing"}, "B",
              {"correct": "Singular subject 'technician' takes 'processes' with -es.", "wrong_A": "Lacks 3rd person -es.", "wrong_C": "Ungrammatical.", "wrong_D": "Participle alone cannot be verb."},
              "Czech 'Technik zpracovává'. Singular subject takes '-es': 'processes'.", "IT Service Desk & Enterprise Support"),
            q("TEV-IT-A2-002-Q2", "We usually _____ high-priority P1 tickets within 15 minutes of escalation.",
              {"A": "resolves", "B": "is resolve", "C": "resolve", "D": "resolving"}, "C",
              {"correct": "Plural subject 'We' takes base verb 'resolve'.", "wrong_A": "'resolves' is singular.", "wrong_B": "Ungrammatical.", "wrong_D": "Participle alone cannot be verb."},
              "Czech 'Běžně řešíme P1 tikety...'. Plural subject takes base verb: 'resolve'.", "IT Service Desk & Enterprise Support"),
            q("TEV-IT-A2-002-Q3", "The enterprise VPN client _____ automatically when the laptop connects to home Wi-Fi.",
              {"A": "launches", "B": "launch", "C": "is launch", "D": "launching"}, "A",
              {"correct": "Singular subject 'VPN client' takes 'launches' with -es.", "wrong_B": "Lacks singular -es.", "wrong_C": "Ungrammatical.", "wrong_D": "Participle alone cannot be verb."},
              "Czech 'VPN klient se spouští'. Singular subject takes '-es': 'launches'.", "IT Service Desk & Enterprise Support"),
            q("TEV-IT-A2-002-Q4", "_____ the user have administrative rights on the corporate workstation?",
              {"A": "Is", "B": "Do", "C": "Are", "D": "Does"}, "D",
              {"correct": "Singular subject 'the user' takes auxiliary 'Does' in Present Simple questions.", "wrong_A": "'Is' requires continuous -ing.", "wrong_B": "'Do' is plural.", "wrong_C": "'Are' is plural."},
              "Czech 'Má uživatel administrátorská práva?'. Singular question takes 'Does the user have...?'.", "IT Service Desk & Enterprise Support"),
            q("TEV-IT-A2-002-Q5", "System administrators _____ new employee accounts in Active Directory.",
              {"A": "creates", "B": "create", "C": "is create", "D": "creating"}, "B",
              {"correct": "Plural subject 'administrators' takes base verb 'create'.", "wrong_A": "'creates' is singular.", "wrong_C": "Ungrammatical.", "wrong_D": "Participle alone cannot be verb."},
              "Czech 'Správci vytvářejí...'. Plural subject takes base verb: 'create'.", "IT Service Desk & Enterprise Support"),
            q("TEV-IT-A2-002-Q6", "The user account _____ not unlock automatically after three consecutive failed attempts.",
              {"A": "is", "B": "does", "C": "do", "D": "has"}, "B",
              {"correct": "Singular negative Present Simple takes 'does not unlock'.", "wrong_A": "'is not unlock' is ungrammatical.", "wrong_C": "'do' is plural.", "wrong_D": "'has' cannot negate action verbs like this."},
              "Czech 'Účet se neodemkne automaticky'. Use 'does not unlock'.", "IT Service Desk & Enterprise Support"),
            q("TEV-IT-A2-002-Q7", "How often _____ the backup system duplicate the database to the cloud?",
              {"A": "is", "B": "do", "C": "are", "D": "does"}, "D",
              {"correct": "Singular subject 'backup system' takes auxiliary 'does': 'How often does the system duplicate...?'.", "wrong_A": "'is' cannot pair with bare base verb 'duplicate'.", "wrong_B": "'do' is plural.", "wrong_C": "'are' is plural."},
              "Czech 'Jak často zálohovací systém duplikuje...?'. Question requires auxiliary 'does'.", "Cloud Architecture & Hybrid Infrastructure (AWS & Azure)"),
            q("TEV-IT-A2-002-Q8", "The security scanner _____ all inbound email attachments for malicious macros.",
              {"A": "inspects", "B": "inspect", "C": "is inspect", "D": "inspecting"}, "A",
              {"correct": "Singular subject 'scanner' takes 'inspects' with 3rd person -s.", "wrong_B": "Lacks singular -s.", "wrong_C": "Ungrammatical.", "wrong_D": "Participle alone cannot be verb."},
              "Czech 'Bezpečnostní skener kontroluje...'. Singular subject takes '-s': 'inspects'.", "Enterprise Cybersecurity, Threat Hunting & Zero Trust"),
            q("TEV-IT-A2-002-Q9", "Our service desk technicians _____ support in both Czech and English.",
              {"A": "provides", "B": "is provide", "C": "provide", "D": "providing"}, "C",
              {"correct": "Plural subject 'technicians' takes base verb 'provide'.", "wrong_A": "'provides' is singular.", "wrong_B": "Ungrammatical.", "wrong_D": "Participle alone cannot be verb."},
              "Czech 'Technici poskytují...'. Plural subject takes base verb: 'provide'.", "IT Service Desk & Enterprise Support"),
            q("TEV-IT-A2-002-Q10", "The multi-factor authentication (MFA) prompt _____ after 30 days of inactivity.",
              {"A": "expire", "B": "expires", "C": "is expire", "D": "expiring"}, "B",
              {"correct": "Singular subject 'prompt' takes 'expires' with 3rd person -s.", "wrong_A": "Lacks singular -s.", "wrong_C": "Ungrammatical.", "wrong_D": "Participle alone cannot be verb."},
              "Czech 'Platnost vyprší po 30 dnech'. Singular subject takes '-s': 'expires'.", "Enterprise Cybersecurity, Threat Hunting & Zero Trust")
        ]
    }

    # TEV-IT-B2-001: Zero Trust Security Architecture: Inversion for Emphasis
    tests["TEV-IT-B2-001"] = {
        "test_id": "TEV-IT-B2-001",
        "title": "Zero Trust Security Architecture: Inversion for Emphasis",
        "level": "B2",
        "category": "core",
        "workplace_track": "Enterprise Cybersecurity, Threat Hunting & Zero Trust",
        "estimated_time_minutes": 16,
        "description": "Formulate strict Zero Trust cybersecurity policies, micro-segmentation mandates, and IAM privilege restrictions using inversion.",
        "learning_objectives": [
            "Apply negative inversion in enterprise cybersecurity policies (Under no circumstances, Seldom)",
            "Articulate Zero Trust conditional access rules with precision",
            "Avoid typical Czenglish word order mistakes in security policy drafting"
        ],
        "questions": [
            q("TEV-IT-B2-001-Q1", "Under no circumstances _____ developers hardcode production database credentials into GitHub repositories.",
              {"A": "developers may", "B": "may developers", "C": "developers should", "D": "must developers to"}, "B",
              {"correct": "Fronted negative phrase 'Under no circumstances' requires subject-auxiliary inversion: 'may developers'.", "wrong_A": "Lacks required inversion.", "wrong_C": "Direct word order violates the formal inversion rule.", "wrong_D": "'must... to' is ungrammatical."},
              "Czech 'Za žádných okolností nesmí vývojáři...'. Negative inversion: 'Under no circumstances may developers...'.", "Enterprise Cybersecurity, Threat Hunting & Zero Trust"),
            q("TEV-IT-B2-001-Q2", "Seldom _____ a single compromised endpoint penetrate beyond the micro-segmented VLAN.",
              {"A": "an adversary does", "B": "is", "C": "does", "D": "has"}, "C",
              {"correct": "Fronted restrictive adverb 'Seldom' followed by singular subject 'endpoint' and base verb 'penetrate' requires dummy auxiliary 'does'.", "wrong_A": "Lacks required inversion.", "wrong_B": "'is' cannot invert with base action verb 'penetrate'.", "wrong_D": "'has' would require past participle 'penetrated'."},
              "Czech 'Zřídkakdy pronikne...'. Fronted 'Seldom' forces inversion: 'Seldom does a single endpoint penetrate...'.", "Enterprise Cybersecurity, Threat Hunting & Zero Trust"),
            q("TEV-IT-B2-001-Q3", "Not only _____ the Zero Trust architecture enforce continuous authentication, but it also encrypts all east-west data traffic.",
              {"A": "does", "B": "is", "C": "has", "D": "will"}, "A",
              {"correct": "Fronted correlative 'Not only' with base action verb 'enforce' demands auxiliary inversion 'does'.", "wrong_B": "'is' cannot invert with base action verb 'enforce'.", "wrong_C": "'has' would require past participle 'enforced'.", "wrong_D": "'will' expresses future prediction rather than current policy."},
              "Czech 'Nejenže architektura vynucuje..., ale také...'. Use auxiliary 'does': 'Not only does the architecture enforce...'.", "Enterprise Cybersecurity, Threat Hunting & Zero Trust"),
            q("TEV-IT-B2-001-Q4", "Only after completing privileged access authentication _____ a system engineer access the production Kubernetes cluster.",
              {"A": "can to", "B": "a system engineer can", "C": "is", "D": "can"}, "D",
              {"correct": "Fronted restrictive phrase 'Only after completing...' requires modal inversion 'can a system engineer access'.", "wrong_A": "'can to' is ungrammatical.", "wrong_B": "Lacks required subject-auxiliary inversion.", "wrong_C": "'is' cannot pair with base verb 'access'."},
              "Czech 'Teprve po dokončení ověření může inženýr přistoupit...'. Fronted 'Only after...' forces inversion: 'can an engineer access...'.", "Enterprise Cybersecurity, Threat Hunting & Zero Trust"),
            q("TEV-IT-B2-001-Q5", "Scarcely had the SOC analyst isolated the infected host _____ the ransomware attempted to communicate with its C2 server.",
              {"A": "than", "B": "that", "C": "when", "D": "after"}, "C",
              {"correct": "'Scarcely had [action]... when [second action]' is the strictly required correlative pair.", "wrong_A": "'than' pairs with 'No sooner', not 'Scarcely'.", "wrong_B": "'that' cannot introduce temporal correlative clause.", "wrong_D": "'after' is redundant with past perfect inversion."},
              "Czech 'Sotva analytik izoloval stanici, když v tom...'. Correlative pair for 'Scarcely had...' is always 'WHEN'.", "Enterprise Cybersecurity, Threat Hunting & Zero Trust"),
            q("TEV-IT-B2-001-Q6", "On no account _____ unencrypted backups be stored on public cloud storage buckets.",
              {"A": "may", "B": "should be", "C": "are to", "D": "must to"}, "A",
              {"correct": "Fronted negative phrase 'On no account' requires auxiliary inversion 'may backups be stored'.", "wrong_B": "'should be' creates double passive 'should be be stored'.", "wrong_C": "'are to' is syntactically invalid here.", "wrong_D": "'must to' is ungrammatical."},
              "Czech 'V žádném případě nesmí být zálohy ukládány...'. Formal policy inversion: 'On no account may unencrypted backups be stored...'.", "Cloud Architecture & Hybrid Infrastructure (AWS & Azure)"),
            q("TEV-IT-B2-001-Q7", "Little _____ the intruder realize that the honeypot database was tracking every malicious query.",
              {"A": "was", "B": "did", "C": "has", "D": "had"}, "B",
              {"correct": "Fronted restrictive adverb 'Little' followed by base lexical verb 'realize' demands past auxiliary inversion 'did'.", "wrong_A": "'was' cannot invert with base action verb 'realize'.", "wrong_C": "'has' would require past participle 'realized'.", "wrong_D": "'had' creates incorrect double past perfect."},
              "Czech 'Útočník si vůbec neuvědomoval, že...'. Formal dramatic negative inversion: 'Little did the intruder realize...'.", "Enterprise Cybersecurity, Threat Hunting & Zero Trust"),
            q("TEV-IT-B2-001-Q8", "No sooner had the perimeter firewall rule been deployed _____ traffic throughput dropped by 18 percent.",
              {"A": "than", "B": "when", "C": "that", "D": "as"}, "A",
              {"correct": "'No sooner had [action]... than [second action]' is the required correlative conjunction.", "wrong_B": "'when' pairs with 'Hardly' or 'Scarcely', not 'No sooner'.", "wrong_C": "'that' is incorrect.", "wrong_D": "'as' is informal."},
              "Czech 'Sotva bylo pravidlo nasazeno, než propustnost klesla'. Always pair 'No sooner had...' with 'THAN'.", "Cloud Architecture & Hybrid Infrastructure (AWS & Azure)"),
            q("TEV-IT-B2-001-Q9", "At no time _____ the Active Directory domain controllers allowed to process outbound internet connections directly.",
              {"A": "are", "B": "do", "C": "have", "D": "will"}, "A",
              {"correct": "Passive construction 'allowed' takes auxiliary 'are': 'At no time are domain controllers allowed to...'.", "wrong_B": "'do' is for active verbs, not passive state.", "wrong_C": "'have' would require past participle 'been allowed'.", "wrong_D": "'will' is future."},
              "Czech 'Řadiče domény nemají v žádném okamžiku povolen přístup...'. Passive inversion: 'At no time are controllers allowed...'.", "Enterprise Cybersecurity, Threat Hunting & Zero Trust"),
            q("TEV-IT-B2-001-Q10", "Only by implementing hardware security keys (FIDO2) _____ the enterprise eliminate credential phishing attacks completely.",
              {"A": "can", "B": "is", "C": "did", "D": "has"}, "A",
              {"correct": "Fronted restrictive phrase 'Only by implementing...' requires modal inversion 'can the enterprise eliminate'.", "wrong_B": "'is' cannot pair with base verb 'eliminate'.", "wrong_C": "'did' refers to completed past action, not general technical capability.", "wrong_D": "'has' would require past participle 'eliminated'."},
              "Czech 'Pouze zavedením hardwarových klíčů může společnost eliminovat...'. Fronted 'Only by...' forces inversion: 'can the enterprise eliminate...'.", "Enterprise Cybersecurity, Threat Hunting & Zero Trust")
        ]
    }

    return tests

print("Chem and IT tests defined.")
