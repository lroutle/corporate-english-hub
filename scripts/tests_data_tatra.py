"""
Test generators for missing Tatra Engineering and Tatra Sales modules.
"""

def get_tatra_tests(q_helper):
    q = q_helper
    tests = {}

    # -------------------------------------------------------------------------
    # TTR-ENG-A2-002: Daily Shift Routines & Machine Operation: Present Simple
    # -------------------------------------------------------------------------
    tests["TTR-ENG-A2-002"] = {
        "test_id": "TTR-ENG-A2-002",
        "title": "Daily Shift Routines & Machine Operation: Present Simple",
        "level": "A2",
        "category": "core",
        "workplace_track": "Workshop Assembly & Line Tooling",
        "estimated_time_minutes": 10,
        "description": "Describe daily line routines, machine startups, and shift schedules with correct 3rd person singular agreement.",
        "learning_objectives": [
            "Apply Present Simple 3rd person singular -s/-es for machine actions",
            "Use frequency adverbs (always, usually, never) in shift routines",
            "Avoid Czenglish omission of auxiliary 'does' in questions"
        ],
        "questions": [
            q("TTR-ENG-A2-002-Q1", "The morning shift _____ at 06:00 sharp at the Kopřivnice assembly hall.",
              {"A": "start", "B": "starts", "C": "starting", "D": "is start"}, "B",
              {"correct": "Singular subject 'The morning shift' takes 'starts' with 3rd person -s.",
               "wrong_A": "'start' lacks singular -s.", "wrong_C": "'-ing' cannot be the main verb.", "wrong_D": "Invalid verb phrase."},
              "Czech 'Ranní směna začíná'. In English, singular subjects take '-s': 'starts'.", "Workshop Assembly & Line Tooling"),

            q("TTR-ENG-A2-002-Q2", "The hydraulic press operator always _____ the pressure gauge before starting a cycle.",
              {"A": "is check", "B": "checking", "C": "checks", "D": "check"}, "C",
              {"correct": "Singular subject 'operator' takes 'checks' with 3rd person -s.",
               "wrong_A": "Ungrammatical.", "wrong_B": "Participle alone cannot be predicate.", "wrong_D": "Lacks singular -s."},
              "Czech 'Operátor vždy kontroluje'. Use 'checks' with 3rd person -s.", "Workshop Assembly & Line Tooling"),

            q("TTR-ENG-A2-002-Q3", "_____ the robot arm lubricate the chassis pins automatically?",
              {"A": "Does", "B": "Do", "C": "Is", "D": "Are"}, "A",
              {"correct": "Singular subject 'the robot arm' takes auxiliary 'Does' in Present Simple questions.",
               "wrong_B": "'Do' is for plural subjects.", "wrong_C": "'Is' requires continuous '-ing'.", "wrong_D": "'Are' is plural."},
              "Czech 'Maže rameno čepy automaticky?'. Singular question takes 'Does the arm lubricate...'.", "Workshop Assembly & Line Tooling"),

            q("TTR-ENG-A2-002-Q4", "Mechanics _____ the torque wrench setting at the beginning of each shift.",
              {"A": "calibrates", "B": "is calibrating", "C": "calibrating", "D": "calibrate"}, "D",
              {"correct": "Plural subject 'Mechanics' takes base verb 'calibrate'.",
               "wrong_A": "'calibrates' is singular.", "wrong_B": "'is' is singular.", "wrong_C": "Participle alone cannot be verb."},
              "Czech 'Mechanici kalibrují'. Plural subject takes base form without -s: 'calibrate'.", "Workshop Assembly & Line Tooling"),

            q("TTR-ENG-A2-002-Q5", "The air compressor usually _____ off when pressure reaches 10 bar.",
              {"A": "shut", "B": "is shut", "C": "shuts", "D": "shutting"}, "C",
              {"correct": "Singular subject 'compressor' takes 'shuts'.",
               "wrong_A": "'shut' lacks 3rd person -s.", "wrong_B": "'is shut' expresses passive state.", "wrong_D": "Participle alone cannot be verb."},
              "Czech 'Kompresor se vypíná'. Singular subject $\\rightarrow$ 'shuts off'.", "Workshop Assembly & Line Tooling"),

            q("TTR-ENG-A2-002-Q6", "The line manager _____ not approve overtime without prior written notification.",
              {"A": "is", "B": "does", "C": "do", "D": "has"}, "B",
              {"correct": "Singular negative Present Simple requires 'does not approve'.",
               "wrong_A": "'is not approve' is ungrammatical.", "wrong_C": "'do' is plural.", "wrong_D": "'has' cannot negate action verbs like this."},
              "Czech 'Vedoucí neschvaluje'. Use 'does not approve', not *is not approve*.", "Workshop Assembly & Line Tooling"),

            q("TTR-ENG-A2-002-Q7", "How often _____ maintenance inspect the overhead crane cables?",
              {"A": "is", "B": "do", "C": "are", "D": "does"}, "D",
              {"correct": "Singular collective/department subject 'maintenance' takes auxiliary 'does'.",
               "wrong_A": "'is' cannot pair with bare base verb 'inspect'.", "wrong_B": "'do' is plural.", "wrong_C": "'are' is plural."},
              "Czech 'Jak často údržba kontroluje...?'. Question requires 'does maintenance inspect...?'.", "Workshop Assembly & Line Tooling"),

            q("TTR-ENG-A2-002-Q8", "We _____ use worn sockets on pneumatic impact wrenches.",
              {"A": "never", "B": "are never", "C": "do never", "D": "not"}, "A",
              {"correct": "Frequency adverb 'never' is placed directly before lexical verb 'use'.",
               "wrong_B": "'are never' cannot pair with bare verb 'use'.", "wrong_C": "'do never' is ungrammatical.", "wrong_D": "'not' requires auxiliary 'do'."},
              "Czech 'Nikdy nepoužíváme...'. English word order: 'We never use...'.", "Workshop Assembly & Line Tooling"),

            q("TTR-ENG-A2-002-Q9", "The final inspection team _____ every chassis number against the SAP production order.",
              {"A": "verify", "B": "is verify", "C": "verifies", "D": "verifying"}, "C",
              {"correct": "Singular team subject takes 'verifies' with -es.",
               "wrong_A": "'verify' lacks 3rd person -es.", "wrong_B": "Ungrammatical.", "wrong_D": "Participle alone cannot be main verb."},
              "Czech 'Tým ověřuje'. Singular subject takes '-es': 'verifies'.", "Quality Assurance & Testing"),

            q("TTR-ENG-A2-002-Q10", "Assembly line 2 _____ heavy 8x8 defense trucks, while line 1 builds commercial tippers.",
              {"A": "produce", "B": "produces", "C": "is produce", "D": "producing"}, "B",
              {"correct": "Singular subject 'Line 2' takes 'produces'.",
               "wrong_A": "Lacks 3rd person -s.", "wrong_C": "Ungrammatical.", "wrong_D": "Participle alone cannot be verb."},
              "Czech 'Linka 2 vyrábí'. Use 'produces' with 3rd person -s.", "Workshop Assembly & Line Tooling")
        ]
    }

    # -------------------------------------------------------------------------
    # TTR-ENG-A2-003: Yesterday's Workshop Faults & Defective Parts: Past Simple
    # -------------------------------------------------------------------------
    tests["TTR-ENG-A2-003"] = {
        "test_id": "TTR-ENG-A2-003",
        "title": "Yesterday's Workshop Faults & Defective Parts: Past Simple",
        "level": "A2",
        "category": "core",
        "workplace_track": "Quality Assurance & Testing",
        "estimated_time_minutes": 12,
        "description": "Report broken parts, line stoppages, and replaced bolts using high-frequency regular and irregular past verbs.",
        "learning_objectives": [
            "Use Past Simple regular (-ed) and irregular verbs (broke, stopped, found)",
            "Ask and answer simple past questions about workshop equipment",
            "Avoid using present tense with past time markers like 'yesterday'"
        ],
        "questions": [
            q("TTR-ENG-A2-003-Q1", "Yesterday, the assembly line _____ for 45 minutes due to an electrical failure.",
              {"A": "stop", "B": "stopped", "C": "was stop", "D": "stopping"}, "B",
              {"correct": "Regular verb 'stop' doubles the consonant and adds -ed: 'stopped'.",
               "wrong_A": "'stop' is present tense.", "wrong_C": "Ungrammatical.", "wrong_D": "Participle alone cannot be verb."},
              "Czech 'Včera se linka zastavila'. With 'yesterday', always use Past Simple: 'stopped'.", "Quality Assurance & Testing"),

            q("TTR-ENG-A2-003-Q2", "The technician _____ a crack in the swinging half-axle housing during the ultrasonic test.",
              {"A": "find", "B": "finded", "C": "found", "D": "was find"}, "C",
              {"correct": "Irregular past tense of 'find' is 'found'.",
               "wrong_A": "'find' is present.", "wrong_B": "'finded' is incorrect irregular morphology.", "wrong_D": "Ungrammatical."},
              "Czech 'Technik našel prasklinu'. Irregular verb: 'find $\\rightarrow$ found'.", "Quality Assurance & Testing"),

            q("TTR-ENG-A2-003-Q3", "We _____ all damaged flange bolts before the endurance test started.",
              {"A": "replaced", "B": "replace", "C": "were replace", "D": "replacing"}, "A",
              {"correct": "Regular past tense is 'replaced'.",
               "wrong_B": "'replace' is present tense.", "wrong_C": "Ungrammatical.", "wrong_D": "Participle alone cannot be verb."},
              "Czech 'Vyměnili jsme...'. Use past form 'replaced'.", "Workshop Assembly & Line Tooling"),

            q("TTR-ENG-A2-003-Q4", "_____ you calibrate the digital torque wrench before tightening the flange?",
              {"A": "Were", "B": "Do", "C": "Have", "D": "Did"}, "D",
              {"correct": "Past Simple questions use auxiliary 'Did' + base verb ('Did you calibrate').",
               "wrong_A": "'Were' cannot pair with bare base verb 'calibrate'.", "wrong_B": "'Do' is present.", "wrong_C": "'Have' requires past participle 'calibrated'."},
              "Czech 'Zkalibroval jste...?'. Past Simple questions use 'Did you calibrate...'.", "Workshop Assembly & Line Tooling"),

            q("TTR-ENG-A2-003-Q5", "The transfer case oil pressure _____ sharply during the high-speed dyno run.",
              {"A": "drop", "B": "was drop", "C": "dropped", "D": "dropping"}, "C",
              {"correct": "Regular verb 'drop' doubles the consonant: 'dropped'.",
               "wrong_A": "'drop' is present tense.", "wrong_B": "Ungrammatical.", "wrong_D": "Participle alone cannot be verb."},
              "Czech 'Tlak oleje prudce klesl'. Use Past Simple 'dropped'.", "Central Backbone Tube & Chassis R&D"),

            q("TTR-ENG-A2-003-Q6", "The operator _____ not notice the yellow warning lamp on the dashboard.",
              {"A": "was", "B": "did", "C": "does", "D": "is"}, "B",
              {"correct": "Negative Past Simple takes auxiliary 'did not' + base verb 'notice'.",
               "wrong_A": "'was not' requires adjective or -ing.", "wrong_C": "'does' is present tense.", "wrong_D": "'is' is present tense."},
              "Czech 'Operátor si nevšiml'. Use 'did not notice', not *was not notice*.", "Quality Assurance & Testing"),

            q("TTR-ENG-A2-003-Q7", "Why _____ the hydraulic lift stop working at 14:00 yesterday?",
              {"A": "does", "B": "is", "C": "was", "D": "did"}, "D",
              {"correct": "Past question takes auxiliary 'did' + subject + base verb: 'Why did the lift stop...'.",
               "wrong_A": "'does' is present.", "wrong_B": "'is' is present.", "wrong_C": "'was' cannot pair with bare verb 'stop'."},
              "Czech 'Proč výtah přestal fungovat?'. In past questions, use auxiliary 'did'.", "Workshop Assembly & Line Tooling"),

            q("TTR-ENG-A2-003-Q8", "The maintenance crew _____ three new air filters into the paint booth yesterday.",
              {"A": "fitted", "B": "fit", "C": "were fit", "D": "fitting"}, "A",
              {"correct": "Regular past tense is 'fitted' (or 'fit'), but 'fitted' clearly signals past completion.",
               "wrong_B": "'fit' is ambiguous present.", "wrong_C": "Ungrammatical.", "wrong_D": "Participle alone cannot be verb."},
              "Czech 'Četa namontovala...'. Use Past Simple: 'fitted'.", "Workshop Assembly & Line Tooling"),

            q("TTR-ENG-A2-003-Q9", "The rear differential seal _____ during the rough-road durability test.",
              {"A": "leak", "B": "was leak", "C": "leaked", "D": "leaking"}, "C",
              {"correct": "Regular past tense is 'leaked'.",
               "wrong_A": "'leak' is present.", "wrong_B": "Ungrammatical.", "wrong_D": "Participle alone cannot be verb."},
              "Czech 'Těsnění teklo / propustilo olej'. Use Past Simple 'leaked'.", "Central Backbone Tube & Chassis R&D"),

            q("TTR-ENG-A2-003-Q10", "The quality engineer _____ the defective chassis back to welding station 2.",
              {"A": "send", "B": "sent", "C": "sended", "D": "was send"}, "B",
              {"correct": "Irregular past tense of 'send' is 'sent'.",
               "wrong_A": "'send' is present.", "wrong_C": "'sended' is non-existent irregular error.", "wrong_D": "Ungrammatical."},
              "Czech 'Inženýr poslal podvozek zpět'. Irregular verb: 'send $\\rightarrow$ sent'.", "Quality Assurance & Testing")
        ]
    }

    # -------------------------------------------------------------------------
    # TTR-ENG-A2-004: Chassis Geometry & Tool Locations: Prepositions of Place
    # -------------------------------------------------------------------------
    tests["TTR-ENG-A2-004"] = {
        "test_id": "TTR-ENG-A2-004",
        "title": "Chassis Geometry & Tool Locations: Prepositions of Place",
        "level": "A2",
        "category": "core",
        "workplace_track": "Central Backbone Tube & Chassis R&D",
        "estimated_time_minutes": 10,
        "description": "Specify exact spatial positions of driveshafts, brake lines, calipers, and safety switches using prepositions of place.",
        "learning_objectives": [
            "Use prepositions of place: under, inside, between, behind, above",
            "Give clear spatial directions on the truck assembly line",
            "Avoid typical Czech preposition interference"
        ],
        "questions": [
            q("TTR-ENG-A2-004-Q1", "The driveshaft runs directly _____ the central protective backbone tube.",
              {"A": "on", "B": "inside", "C": "between", "D": "onto"}, "B",
              {"correct": "The driveshaft is enclosed within the tube $\\rightarrow$ 'inside'.",
               "wrong_A": "'on' means on the exterior surface.", "wrong_C": "'between' requires two entities.", "wrong_D": "'onto' indicates motion toward surface."},
              "Czech 'Hnací hřídel běží uvnitř nosné roury'. Enclosed space uses 'inside'.", "Central Backbone Tube & Chassis R&D"),

            q("TTR-ENG-A2-004-Q2", "The mechanic is working _____ the truck chassis on the service pit.",
              {"A": "above", "B": "over", "C": "under", "D": "in"}, "C",
              {"correct": "Working beneath the vehicle $\\rightarrow$ 'under the chassis'.",
               "wrong_A": "'above' means on top/higher.", "wrong_B": "'over' means higher than.", "wrong_D": "'in' is incorrect for open chassis."},
              "Czech 'Mechanik pracuje pod podvozkem'. Spatial position beneath $\\rightarrow$ 'under'.", "Workshop Assembly & Line Tooling"),

            q("TTR-ENG-A2-004-Q3", "The auxiliary gearbox is mounted _____ the front axle and the rear bogie.",
              {"A": "between", "B": "among", "C": "under", "D": "through"}, "A",
              {"correct": "Positioned separating two distinct objects $\\rightarrow$ 'between'.",
               "wrong_B": "'among' is for three or more indistinct items.", "wrong_C": "'under' is beneath.", "wrong_D": "'through' indicates motion."},
              "Czech 'mezi přední nápravou a zadním podvozkem'. Two distinct reference points take 'between'.", "Central Backbone Tube & Chassis R&D"),

            q("TTR-ENG-A2-004-Q4", "Store all pneumatic torque wrenches _____ the red steel tool cabinet.",
              {"A": "to", "B": "on", "C": "at", "D": "in"}, "D",
              {"correct": "Enclosed storage container $\\rightarrow$ 'in the cabinet'.",
               "wrong_A": "'to' indicates movement.", "wrong_B": "'on' means on top of the cabinet roof.", "wrong_C": "'at' indicates general vicinity."},
              "Czech 'Uložte do skříně'. Enclosed storage uses 'in'.", "Workshop Assembly & Line Tooling"),

            q("TTR-ENG-A2-004-Q5", "The emergency stop button is situated on the wall directly _____ the operator station.",
              {"A": "between", "B": "inside", "C": "behind", "D": "under"}, "C",
              {"correct": "Positioned at the rear of the operator $\\rightarrow$ 'behind'.",
               "wrong_A": "'between' requires two points.", "wrong_B": "'inside' is enclosed.", "wrong_D": "'under' is beneath."},
              "Czech 'přímo za stanovištěm operátora'. Positioned at the rear $\\rightarrow$ 'behind'.", "Workshop Assembly & Line Tooling"),

            q("TTR-ENG-A2-004-Q6", "The fuel tank is secured _____ the right side of the central backbone tube.",
              {"A": "in", "B": "on", "C": "under", "D": "between"}, "B",
              {"correct": "Mounted on an exterior surface or side $\\rightarrow$ 'on the right side'.",
               "wrong_A": "'in' implies inside the tube.", "wrong_C": "'under' implies underneath the tube.", "wrong_D": "'between' requires two items."},
              "Czech 'na pravé straně'. English surface / side uses 'on the right side'.", "Central Backbone Tube & Chassis R&D"),

            q("TTR-ENG-A2-004-Q7", "The exhaust silencer is installed _____ the front cab and the cargo body.",
              {"A": "behind", "B": "inside", "C": "under", "D": "between"}, "D",
              {"correct": "Spatial position between two modules $\\rightarrow$ 'between the cab and the body'.",
               "wrong_A": "'behind' would omit the second reference point.", "wrong_B": "'inside' implies internal.", "wrong_C": "'under' implies underneath."},
              "Czech 'mezi kabinou a korbou'. Use 'between'.", "Central Backbone Tube & Chassis R&D"),

            q("TTR-ENG-A2-004-Q8", "Please place the calibrated torque certificate _____ the vehicle documentation folder.",
              {"A": "inside", "B": "on", "C": "over", "D": "under"}, "A",
              {"correct": "Placing documents into an enclosure $\\rightarrow$ 'inside the folder'.",
               "wrong_B": "'on' means on top of the cover.", "wrong_C": "'over' means hovering above.", "wrong_D": "'under' means beneath the folder."},
              "Czech 'Vložte dovnitř desek'. Use 'inside'.", "Quality Assurance & Testing"),

            q("TTR-ENG-A2-004-Q9", "The overhead crane hovers 5 meters _____ the chassis assembly line.",
              {"A": "under", "B": "through", "C": "above", "D": "between"}, "C",
              {"correct": "Higher vertical position without contact $\\rightarrow$ 'above the line'.",
               "wrong_A": "'under' means below.", "wrong_B": "'through' means passing across.", "wrong_D": "'between' requires two reference points."},
              "Czech '5 metrů nad linkou'. Vertical height without direct contact $\\rightarrow$ 'above'.", "Workshop Assembly & Line Tooling"),

            q("TTR-ENG-A2-004-Q10", "The brake fluid reservoir is located right _____ the master cylinder.",
              {"A": "between", "B": "next to", "C": "under", "D": "inside"}, "B",
              {"correct": "Adjacent position $\\rightarrow$ 'next to the master cylinder'.",
               "wrong_A": "'between' requires two objects.", "wrong_C": "'under' means beneath.", "wrong_D": "'inside' means internal."},
              "Czech 'hned vedle hlavního válce'. Adjacent position $\\rightarrow$ 'next to'.", "Central Backbone Tube & Chassis R&D")
        ]
    }

    # -------------------------------------------------------------------------
    # TTR-ENG-A2-005: Plant Warning Signs & Crane Safety: Can & Must
    # -------------------------------------------------------------------------
    tests["TTR-ENG-A2-005"] = {
        "test_id": "TTR-ENG-A2-005",
        "title": "Plant Warning Signs & Crane Safety: Can & Must",
        "level": "A2",
        "category": "core",
        "workplace_track": "Workshop Assembly & Line Tooling",
        "estimated_time_minutes": 10,
        "description": "Interpret shopfloor safety signs, overhead crane operating limits, and mandatory PPE rules using modal verbs.",
        "learning_objectives": [
            "Use modal 'must' for mandatory safety regulations",
            "Use 'must not' for strict prohibitions vs 'don't have to'",
            "Use 'can / can't' for crane and hoist weight capacities"
        ],
        "questions": [
            q("TTR-ENG-A2-005-Q1", "All visitors _____ wear safety boots and a high-visibility vest in the assembly plant.",
              {"A": "must to", "B": "must", "C": "can to", "D": "are"}, "B",
              {"correct": "Modal 'must' is followed directly by bare infinitive: 'must wear'.",
               "wrong_A": "'must to' is ungrammatical.", "wrong_C": "'can to' is ungrammatical.", "wrong_D": "'are' cannot pair with bare verb 'wear'."},
              "Czech 'Všichni musí nosit'. Never say *must to wear*. Use 'must wear'.", "Workshop Assembly & Line Tooling"),

            q("TTR-ENG-A2-005-Q2", "This overhead workshop crane _____ lift up to 15 metric tons safely.",
              {"A": "must to", "B": "is can", "C": "can", "D": "cans"}, "C",
              {"correct": "Capability modal 'can' takes no -s and takes bare infinitive: 'can lift'.",
               "wrong_A": "'must to' is ungrammatical.", "wrong_B": "Ungrammatical.", "wrong_D": "Modal verbs do not take 3rd person -s."},
              "Czech 'Jeřáb může zvednout'. Modal 'can' never takes -s: 'can lift'.", "Workshop Assembly & Line Tooling"),

            q("TTR-ENG-A2-005-Q3", "You _____ stand under a suspended load while the chassis is being transported!",
              {"A": "must not", "B": "don't have to", "C": "haven't to", "D": "needn't"}, "A",
              {"correct": "'Must not' expresses life-critical safety prohibition ('nesmíte').",
               "wrong_B": "'don't have to' means optional ('nemusíte'), which is a fatal error under a crane!", "wrong_C": "Ungrammatical.", "wrong_D": "'needn't' means lack of obligation."},
              "Czech 'Nesmíte stát pod břemenem' = 'must not stand'. Do not confuse with 'don't have to' (nemusíte).", "Workshop Assembly & Line Tooling"),

            q("TTR-ENG-A2-005-Q4", "Contractors _____ sign in at the security gate before entering the manufacturing zone.",
              {"A": "must to", "B": "are", "C": "can to", "D": "must"}, "D",
              {"correct": "Mandatory rule takes 'must + base verb': 'must sign in'.",
               "wrong_A": "'must to' is invalid.", "wrong_B": "'are' cannot pair with base verb 'sign in'.", "wrong_C": "'can to' is invalid."},
              "Czech 'Musí se zapsat'. Use 'must sign in'.", "Workshop Assembly & Line Tooling"),

            q("TTR-ENG-A2-005-Q5", "_____ we operate the overhead gantry crane without a certified signalman?",
              {"A": "Must", "B": "Do", "C": "Can", "D": "Are"}, "C",
              {"correct": "Permission/capability question takes 'Can we operate...'.",
               "wrong_A": "'Must we operate' asks about compulsion, not permission.", "wrong_B": "'Do we operate' asks about habitual routine.", "wrong_D": "'Are' requires continuous -ing."},
              "Czech 'Můžeme obsluhovat jeřáb bez...?'. Use 'Can we operate...'.", "Workshop Assembly & Line Tooling"),

            q("TTR-ENG-A2-005-Q6", "You _____ wear ear defenders in the stamping hall; the noise exceeds 90 dB.",
              {"A": "can", "B": "must", "C": "must to", "D": "have"}, "B",
              {"correct": "Mandatory safety rule takes 'must wear'.",
               "wrong_A": "'can' suggests optional choice.", "wrong_C": "'must to' is ungrammatical.", "wrong_D": "'have' requires 'to'."},
              "Czech 'Musíte nosit ochranu sluchu'. Mandatory rule takes 'must wear'.", "Workshop Assembly & Line Tooling"),

            q("TTR-ENG-A2-005-Q7", "The forklift truck _____ exceed 10 km/h inside the pedestrian crossway areas.",
              {"A": "must", "B": "can", "C": "doesn't have to", "D": "must not"}, "D",
              {"correct": "Strict prohibition takes 'must not exceed'.",
               "wrong_A": "'must' would mandate speeding.", "wrong_B": "'can' would permit speeding.", "wrong_C": "'doesn't have to' means optional."},
              "Czech 'Vysokozdvižný vozík nesmí překročit...'. Prohibition takes 'must not exceed'.", "Workshop Assembly & Line Tooling"),

            q("TTR-ENG-A2-005-Q8", "Employees _____ report all oil spills immediately to the environmental safety officer.",
              {"A": "must", "B": "must to", "C": "are", "D": "have"}, "A",
              {"correct": "Obligation modal 'must' is followed directly by bare infinitive: 'must report'.",
               "wrong_B": "'must to' is ungrammatical.", "wrong_C": "Ungrammatical.", "wrong_D": "'have' requires 'to'."},
              "Czech 'Zaměstnanci musí hlásit...'. Use 'must report'.", "Workshop Assembly & Line Tooling"),

            q("TTR-ENG-A2-005-Q9", "You _____ touch electrical control panels with wet hands under any circumstances.",
              {"A": "can", "B": "don't must", "C": "must not", "D": "needn't"}, "C",
              {"correct": "Prohibition takes 'must not'. Note that *don't must* does not exist in English.",
               "wrong_A": "'can' implies permission.", "wrong_B": "'don't must' is a frequent Czenglish grammatical error.", "wrong_D": "'needn't' indicates lack of necessity."},
              "Never say *don't must*. English prohibition is strictly 'must not'.", "Workshop Assembly & Line Tooling"),

            q("TTR-ENG-A2-005-Q10", "Only certified crane technicians _____ perform routine wire rope maintenance.",
              {"A": "can to", "B": "can", "C": "is can", "D": "must to"}, "B",
              {"correct": "Capability/authorization modal takes base form: 'can perform'.",
               "wrong_A": "'can to' is ungrammatical.", "wrong_C": "Ungrammatical.", "wrong_D": "'must to' is ungrammatical."},
              "Czech 'Pouze certifikovaní technici mohou provádět...'. Modal 'can' takes bare verb: 'can perform'.", "Workshop Assembly & Line Tooling")
        ]
    }

    # -------------------------------------------------------------------------
    # TTR-SALES-A2-002: Polite Email Requests to Foreign Dealers: Can, Could & Please
    # -------------------------------------------------------------------------
    tests["TTR-SALES-A2-002"] = {
        "test_id": "TTR-SALES-A2-002",
        "title": "Polite Email Requests to Foreign Dealers: Can, Could & Please",
        "level": "A2",
        "category": "core",
        "workplace_track": "International Sales & Customer Inquiries",
        "estimated_time_minutes": 10,
        "description": "Compose polite, clear email requests to international truck distributors regarding order confirmations and vehicle specs.",
        "learning_objectives": [
            "Use polite request modals: Could you please, Can you send",
            "Structure polite professional opening and closing phrases",
            "Avoid overly blunt imperative commands in customer communications"
        ],
        "questions": [
            q("TTR-SALES-A2-002-Q1", "Dear Mr. Schmidt, _____ you please send us the updated chassis delivery address?",
              {"A": "Can to", "B": "Could", "C": "Are", "D": "Do"}, "B",
              {"correct": "Polite email request formula takes 'Could you please + base verb': 'Could you please send'.",
               "wrong_A": "'Can to' is ungrammatical.", "wrong_C": "'Are' requires continuous -ing.", "wrong_D": "'Do' is not a polite request modal here."},
              "Czech 'Mohl byste nám prosím poslat...?'. Standard polite business inquiry: 'Could you please send us...'.", "International Sales & Customer Inquiries"),

            q("TTR-SALES-A2-002-Q2", "Please _____ the attached proforma invoice for the five military chassis units.",
              {"A": "finding", "B": "to find", "C": "find", "D": "finds"}, "C",
              {"correct": "Polite request with 'Please' takes base verb form: 'Please find'.",
               "wrong_A": "'-ing' cannot follow 'Please'.", "wrong_B": "Infinitive with 'to' cannot follow 'Please'.", "wrong_D": "'-s' form is incorrect."},
              "Czech 'V příloze naleznete...'. Standard formula: 'Please find the attached invoice'.", "International Sales & Customer Inquiries"),

            q("TTR-SALES-A2-002-Q3", "Could you confirm if the customer _____ right-hand drive or left-hand drive cabs?",
              {"A": "requires", "B": "require", "C": "is require", "D": "requiring"}, "A",
              {"correct": "Singular subject 'the customer' takes 3rd person -s: 'requires'.",
               "wrong_B": "'require' lacks 3rd person -s.", "wrong_C": "Ungrammatical.", "wrong_D": "Participle alone cannot be verb."},
              "Czech 'Zda zákazník požaduje...'. Singular customer takes '-s': 'requires'.", "International Sales & Customer Inquiries"),

            q("TTR-SALES-A2-002-Q4", "We _____ forward the full technical datasheet by 15:00 today.",
              {"A": "can to", "B": "are", "C": "do", "D": "can"}, "D",
              {"correct": "Capability/willingness modal takes bare verb: 'can forward'.",
               "wrong_A": "'can to' is ungrammatical.", "wrong_B": "'are' cannot pair with base verb 'forward'.", "wrong_C": "'do' is emphatic."},
              "Czech 'Můžeme přeposlat...'. Modal 'can' takes bare base verb without 'to': 'can forward'.", "International Sales & Customer Inquiries"),

            q("TTR-SALES-A2-002-Q5", "Please let me know if you _____ any further assistance with the tender documentation.",
              {"A": "are need", "B": "needs", "C": "need", "D": "needing"}, "C",
              {"correct": "Pronoun 'you' takes base verb 'need'.",
               "wrong_A": "Ungrammatical.", "wrong_B": "'needs' is 3rd person singular.", "wrong_D": "Participle alone cannot be verb."},
              "Czech 'pokud potřebujete jakoukoliv pomoc'. Standard email formula: 'if you need any assistance'.", "International Sales & Customer Inquiries"),

            q("TTR-SALES-A2-002-Q6", "_____ you like us to schedule a Teams video call with our chief suspension engineer?",
              {"A": "Do", "B": "Would", "C": "Could", "D": "Can"}, "B",
              {"correct": "Polite offer formula is 'Would you like [someone] to [verb]'.",
               "wrong_A": "'Do you like' asks about general preference, not an offer.", "wrong_C": "'Could you like' is ungrammatical.", "wrong_D": "'Can you like' is ungrammatical."},
              "Czech 'Přáli byste si, abychom naplánovali...?'. Polite offer takes 'Would you like us to schedule...'.", "International Sales & Customer Inquiries"),

            q("TTR-SALES-A2-002-Q7", "I look forward to _____ from you regarding the dealer agreement contract.",
              {"A": "hear", "B": "heard", "C": "be hear", "D": "hearing"}, "D",
              {"correct": "Prepositional idiom 'look forward to' must be followed by gerund (-ing): 'to hearing'.",
               "wrong_A": "'hear' is a frequent Czenglish error following 'to'.", "wrong_B": "'heard' is past tense.", "wrong_C": "Ungrammatical."},
              "Czech 'Těším se na vaši zprávu'. 'Look forward to' is a preposition $\\rightarrow$ requires '-ing': 'look forward to hearing from you'.", "International Sales & Customer Inquiries"),

            q("TTR-SALES-A2-002-Q8", "Could you please inform us when the bank transfer _____ completed?",
              {"A": "is", "B": "does", "C": "are", "D": "has"}, "A",
              {"correct": "Passive construction for completed state takes 'is completed'.",
               "wrong_B": "'does' is auxiliary for active verbs.", "wrong_C": "'are' is plural.", "wrong_D": "'has' requires past participle 'been completed'."},
              "Czech 'kdy bude převod dokončen'. Use 'when the transfer is completed'.", "International Sales & Customer Inquiries"),

            q("TTR-SALES-A2-002-Q9", "We are pleased to _____ you that the first three prototype trucks are ready for inspection.",
              {"A": "say", "B": "telling", "C": "inform", "D": "speech"}, "C",
              {"correct": "Formal business email formula: 'We are pleased to inform you that...'.",
               "wrong_A": "'say you' is ungrammatical without 'to'.", "wrong_B": "'-ing' cannot follow infinitive 'to'.", "wrong_D": "'speech' is a noun."},
              "Czech 'S potěšením vám oznamujeme'. Standard formula: 'pleased to inform you'.", "International Sales & Customer Inquiries"),

            q("TTR-SALES-A2-002-Q10", "Thank you for your inquiry; we will reply _____ your technical questions by Friday.",
              {"A": "at", "B": "to", "C": "on", "D": "for"}, "B",
              {"correct": "Verb 'reply' pairs strictly with preposition 'to': 'reply to your questions'.",
               "wrong_A": "'reply at' is incorrect.", "wrong_C": "'reply on' is a literal Czenglish error (*odpovědět na*).", "wrong_D": "'reply for' is incorrect."},
              "Czech 'odpovědět na dotazy'. Never say *reply on*. Always use 'reply TO your questions'.", "International Sales & Customer Inquiries")
        ]
    }

    # -------------------------------------------------------------------------
    # TTR-SALES-A2-003: Trade Fairs & Client Negotiations: Past Simple
    # -------------------------------------------------------------------------
    tests["TTR-SALES-A2-003"] = {
        "test_id": "TTR-SALES-A2-003",
        "title": "Trade Fairs & Client Negotiations: Past Simple",
        "level": "A2",
        "category": "core",
        "workplace_track": "International Sales & Customer Inquiries",
        "estimated_time_minutes": 10,
        "description": "Report trade fair meetings (IDET Brno, Eurosatory Paris) and past sales discussions with foreign partners.",
        "learning_objectives": [
            "Use Past Simple regular and irregular verbs (met, spoke, agreed, showed)",
            "Summarize past commercial negotiations and trade fair contacts",
            "Avoid present tense confusion when discussing past trade events"
        ],
        "questions": [
            q("TTR-SALES-A2-003-Q1", "Last week, our sales team _____ with delegates from the UAE defense ministry at IDET.",
              {"A": "meet", "B": "met", "C": "meeted", "D": "was meet"}, "B",
              {"correct": "Irregular past tense of 'meet' is 'met'.",
               "wrong_A": "'meet' is present tense.", "wrong_C": "'meeted' is invalid irregular morphology.", "wrong_D": "Ungrammatical."},
              "Czech 'Náš tým se setkal...'. Irregular verb: 'meet $\\rightarrow$ met'.", "International Sales & Customer Inquiries"),

            q("TTR-SALES-A2-003-Q2", "We _____ the prototype 8x8 chassis with the armored cab at Eurosatory in Paris.",
              {"A": "show", "B": "are show", "C": "showed", "D": "showing"}, "C",
              {"correct": "Regular past tense is 'showed'.",
               "wrong_A": "'show' is present.", "wrong_B": "Ungrammatical.", "wrong_D": "Participle alone cannot be verb."},
              "Czech 'Vystavovali jsme / předvedli jsme...'. Use Past Simple 'showed'.", "International Sales & Customer Inquiries"),

            q("TTR-SALES-A2-003-Q3", "The foreign client _____ keen interest in our swinging half-axle technology.",
              {"A": "expressed", "B": "express", "C": "was express", "D": "expressing"}, "A",
              {"correct": "Regular past tense is 'expressed'.",
               "wrong_B": "'express' is present.", "wrong_C": "Ungrammatical.", "wrong_D": "Participle alone cannot be verb."},
              "Czech 'Klient vyjádřil velký zájem'. Use Past Simple 'expressed'.", "International Sales & Customer Inquiries"),

            q("TTR-SALES-A2-003-Q4", "_____ the Polish dealer agree to the minimum annual order volume?",
              {"A": "Were", "B": "Do", "C": "Have", "D": "Did"}, "D",
              {"correct": "Past Simple questions take auxiliary 'Did' + base verb 'agree'.",
               "wrong_A": "'Were' cannot pair with bare verb 'agree'.", "wrong_B": "'Do' is present.", "wrong_C": "'Have' requires past participle 'agreed'."},
              "Czech 'Souhlasil polský dealer s...?'. In past questions, use 'Did the dealer agree...'.", "International Sales & Customer Inquiries"),

            q("TTR-SALES-A2-003-Q5", "The customer _____ our technical proposal because delivery time was too long.",
              {"A": "reject", "B": "was reject", "C": "rejected", "D": "rejecting"}, "C",
              {"correct": "Regular past tense is 'rejected'.",
               "wrong_A": "'reject' is present.", "wrong_B": "Ungrammatical.", "wrong_D": "Participle alone cannot be verb."},
              "Czech 'Zákazník zamítl naši nabídku'. Use Past Simple 'rejected'.", "International Sales & Customer Inquiries"),

            q("TTR-SALES-A2-003-Q6", "We _____ two commercial contracts with Scandinavian forestry operators yesterday.",
              {"A": "sign", "B": "signed", "C": "are signed", "D": "signing"}, "B",
              {"correct": "Regular past tense is 'signed'.",
               "wrong_A": "'sign' is present.", "wrong_C": "'are signed' is present passive.", "wrong_D": "Participle alone cannot be verb."},
              "Czech 'Včera jsme podepsali dvě smlouvy'. Use Past Simple 'signed'.", "International Sales & Customer Inquiries"),

            q("TTR-SALES-A2-003-Q7", "Why _____ the client request an extension on the tender submission deadline?",
              {"A": "does", "B": "is", "C": "was", "D": "did"}, "D",
              {"correct": "Past Simple question requires auxiliary 'did': 'Why did the client request...'.",
               "wrong_A": "'does' is present.", "wrong_B": "'is' is present.", "wrong_C": "'was' cannot pair with bare base verb 'request'."},
              "Czech 'Proč klient požádal o prodloužení?'. Use auxiliary 'did'.", "International Sales & Customer Inquiries"),

            q("TTR-SALES-A2-003-Q8", "Our export director _____ directly with the defense procurement minister in Warsaw.",
              {"A": "spoke", "B": "speak", "C": "speaked", "D": "was speak"}, "A",
              {"correct": "Irregular past tense of 'speak' is 'spoke'.",
               "wrong_B": "'speak' is present.", "wrong_C": "'speaked' is incorrect irregular morphology.", "wrong_D": "Ungrammatical."},
              "Czech 'Ředitel hovořil přímo s...'. Irregular verb: 'speak $\\rightarrow$ spoke'.", "International Sales & Customer Inquiries"),

            q("TTR-SALES-A2-003-Q9", "The dealer _____ not provide the required bank guarantee before the contract expired.",
              {"A": "was", "B": "is", "C": "did", "D": "does"}, "C",
              {"correct": "Past negative takes 'did not provide'.",
               "wrong_A": "'was not provide' is ungrammatical.", "wrong_B": "'is' is present.", "wrong_D": "'does' is present."},
              "Czech 'Dealer neposkytl záruku'. Use 'did not provide'.", "Commercial Contracts & Incoterms 2020"),

            q("TTR-SALES-A2-003-Q10", "At the Paris defense expo, we _____ over 50 qualified business leads.",
              {"A": "gather", "B": "gathered", "C": "are gather", "D": "gathering"}, "B",
              {"correct": "Regular past tense is 'gathered'.",
               "wrong_A": "'gather' is present.", "wrong_C": "Ungrammatical.", "wrong_D": "Participle alone cannot be verb."},
              "Czech 'Získali jsme přes 50 kontaktů'. Use Past Simple 'gathered'.", "International Sales & Customer Inquiries")
        ]
    }

    # -------------------------------------------------------------------------
    # TTR-SALES-A2-004: Truck Quantities, Weights & Prices: Numbers & Quantifiers
    # -------------------------------------------------------------------------
    tests["TTR-SALES-A2-004"] = {
        "test_id": "TTR-SALES-A2-004",
        "title": "Truck Quantities, Weights & Prices: Numbers & Quantifiers",
        "level": "A2",
        "category": "core",
        "workplace_track": "Commercial Contracts & Incoterms 2020",
        "estimated_time_minutes": 10,
        "description": "Accurately communicate payload capacities in metric tons, pricing per chassis unit, and order quantities in tenders.",
        "learning_objectives": [
            "Use quantifiers: many, much, a few, several, total",
            "State vehicle payload weights and pricing accurately in English",
            "Avoid common Czenglish number and pluralization errors"
        ],
        "questions": [
            q("TTR-SALES-A2-004-Q1", "The municipal fire department ordered _____ ten tactical 4x4 tanker chassis.",
              {"A": "a total of", "B": "a total", "C": "total of", "D": "totally"}, "A",
              {"correct": "Standard business quantifier phrase: 'a total of ten chassis'.",
               "wrong_B": "Lacks required preposition 'of'.", "wrong_C": "Lacks indefinite article 'a'.", "wrong_D": "'totally' is an adverb meaning completely."},
              "Czech 'celkem deset podvozků'. Standard commercial English idiom: 'a total of ten...'.", "Commercial Contracts & Incoterms 2020"),

            q("TTR-SALES-A2-004-Q2", "How _____ payload weight can the 8x8 heavy recovery vehicle carry off-road?",
              {"A": "many", "B": "much", "C": "far", "D": "long"}, "B",
              {"correct": "Uncountable noun 'weight' takes 'How much'.",
               "wrong_A": "'many' is for countable nouns.", "wrong_C": "'far' is distance.", "wrong_D": "'long' is duration/length."},
              "Czech 'Kolik váhy / nosnosti...?'. Uncountable nouns take 'How much weight'.", "Commercial Contracts & Incoterms 2020"),

            q("TTR-SALES-A2-004-Q3", "We have _____ spare military wheel rims in stock at the central warehouse.",
              {"A": "several", "B": "much", "C": "a little", "D": "any"}, "A",
              {"correct": "Plural countable noun 'wheel rims' takes 'several' in affirmative clauses.",
               "wrong_B": "'much' is for uncountable nouns.", "wrong_C": "'a little' is for uncountable nouns.", "wrong_D": "'any' is used in negative/interrogative."},
              "Czech 'Máme několik náhradních disků'. Countable plural takes 'several'.", "International Sales & Customer Inquiries"),

            q("TTR-SALES-A2-004-Q4", "The total contract value exceeds €2.5 _____ Euros for the complete fleet package.",
              {"A": "millions", "B": "million of", "C": "millions of", "D": "million"}, "D",
              {"correct": "When preceded by an exact number or decimal, 'million' does not take plural -s: '€2.5 million'.",
               "wrong_A": "*millions* with a numeral is incorrect.", "wrong_B": "'million of' is incorrect after numerals.", "wrong_C": "'millions of' is only used without exact numbers."},
              "Czech '2,5 milionu eur'. After numerals, never pluralize: '2.5 million Euros', NOT *2.5 millions*.", "Commercial Contracts & Incoterms 2020"),

            q("TTR-SALES-A2-004-Q5", "There are only _____ slots remaining in our Q3 assembly schedule for international orders.",
              {"A": "a little", "B": "much", "C": "a few", "D": "any"}, "C",
              {"correct": "Countable plural noun 'slots' takes 'a few' (small positive quantity).",
               "wrong_A": "'a little' is for uncountable nouns.", "wrong_B": "'much' is for uncountable nouns.", "wrong_D": "'any' is for negative/interrogative."},
              "Czech 'zbývá jen několik volných termínů'. Countable plural takes 'a few slots'.", "International Sales & Customer Inquiries"),

            q("TTR-SALES-A2-004-Q6", "The gross vehicle weight rating (GVWR) of this heavy dump truck is 38 _____ tons.",
              {"A": "metrics", "B": "metric", "C": "metrical", "D": "metre"}, "B",
              {"correct": "The adjective for metric units is 'metric': '38 metric tons'.",
               "wrong_A": "'metrics' is a plural noun (performance data).", "wrong_C": "'metrical' refers to poetic meter.", "wrong_D": "'metre' is a length unit."},
              "Czech '38 tun'. The standard technical phrase in international sales is 'metric tons'.", "Commercial Contracts & Incoterms 2020"),

            q("TTR-SALES-A2-004-Q7", "How _____ trucks does the municipal forestry department plan to order this year?",
              {"A": "much", "B": "many of", "C": "many", "D": "often"}, "C",
              {"correct": "Countable plural noun 'trucks' takes 'How many'.",
               "wrong_A": "'much' is for uncountable nouns.", "wrong_B": "'many of' is redundant before bare noun.", "wrong_D": "'often' asks about frequency."},
              "Czech 'Kolik nákladních vozidel...?'. Countable plural takes 'How many trucks'.", "International Sales & Customer Inquiries"),

            q("TTR-SALES-A2-004-Q8", "The distributor paid an initial deposit of 20 _____ upon signing the sales contract.",
              {"A": "percent", "B": "percents", "C": "percentages", "D": "percentage"}, "A",
              {"correct": "After a number, 'percent' never takes plural -s: '20 percent'.",
               "wrong_B": "*percents* is a common Czenglish error.", "wrong_C": "'percentages' is a plural noun.", "wrong_D": "'percentage' requires article 'a percentage'."},
              "Czech '20 procent'. After numerals, never say *percents*. Always say '20 percent'.", "Commercial Contracts & Incoterms 2020"),

            q("TTR-SALES-A2-004-Q9", "We received _____ inquiries from defense contractors in Southeast Asia this month.",
              {"A": "much", "B": "a little", "C": "numerous", "D": "any"}, "C",
              {"correct": "Countable plural noun 'inquiries' takes 'numerous' (= many).",
               "wrong_A": "'much' is for uncountable nouns.", "wrong_B": "'a little' is for uncountable nouns.", "wrong_D": "'any' is for negative/interrogative."},
              "Czech 'četné / mnoho poptávek'. Plural countable takes 'numerous inquiries'.", "International Sales & Customer Inquiries"),

            q("TTR-SALES-A2-004-Q10", "The base chassis price is €185,000, and customized armor plating _____ extra.",
              {"A": "costs", "B": "cost", "C": "is cost", "D": "costing"}, "A",
              {"correct": "Singular abstract/uncountable subject 'armor plating' takes 'costs' with 3rd person -s.",
               "wrong_B": "'cost' lacks 3rd person -s.", "wrong_C": "Ungrammatical.", "wrong_D": "Participle alone cannot be verb."},
              "Czech 'pancéřování stojí navíc'. Singular subject takes '-s': 'costs extra'.", "Commercial Contracts & Incoterms 2020")
        ]
    }

    # -------------------------------------------------------------------------
    # TTR-SALES-A2-005: Delivery Deadlines & Shipping Schedules: Prepositions of Time
    # -------------------------------------------------------------------------
    tests["TTR-SALES-A2-005"] = {
        "test_id": "TTR-SALES-A2-005",
        "title": "Delivery Deadlines & Shipping Schedules: Prepositions of Time",
        "level": "A2",
        "category": "core",
        "workplace_track": "Commercial Contracts & Incoterms 2020",
        "estimated_time_minutes": 10,
        "description": "Specify vehicle dispatch dates, shipping milestones, and factory handover deadlines using prepositions of time.",
        "learning_objectives": [
            "Use prepositions of time: in, on, at, by, within",
            "Distinguish deadline 'by Friday' from duration 'in two weeks'",
            "Communicate contract delivery dates without Czech interference"
        ],
        "questions": [
            q("TTR-SALES-A2-005-Q1", "All five chassis units will be ready for railway dispatch _____ October 24th.",
              {"A": "in", "B": "on", "C": "at", "D": "by the"}, "B",
              {"correct": "Specific calendar dates take preposition 'on': 'on October 24th'.",
               "wrong_A": "'in' is used for months or years without specific dates.", "wrong_C": "'at' is used for specific times of day.", "wrong_D": "'by the' is ungrammatical before date."},
              "Czech 'dne 24. října'. Specific dates take 'on': 'on October 24th'.", "Commercial Contracts & Incoterms 2020"),

            q("TTR-SALES-A2-005-Q2", "The customer requires final delivery _____ the end of the fourth quarter.",
              {"A": "at", "B": "in", "C": "by", "D": "on"}, "C",
              {"correct": "Deadline marker ('no later than') takes 'by': 'by the end of Q4'.",
               "wrong_A": "'at' indicates a point in time, not a deadline limit.", "wrong_B": "'in' means inside the period, not a strict deadline.", "wrong_D": "'on' is for days/dates."},
              "Czech 'nejpozději do konce 4. čtvrtletí'. Deadlines (no later than) take 'by'.", "Commercial Contracts & Incoterms 2020"),

            q("TTR-SALES-A2-005-Q3", "The international transport vessel departs from Hamburg port _____ 16:30.",
              {"A": "at", "B": "in", "C": "on", "D": "by"}, "A",
              {"correct": "Specific clock times take preposition 'at': 'at 16:30'.",
               "wrong_B": "'in' is for months/years.", "wrong_C": "'on' is for days/dates.", "wrong_D": "'by' indicates a deadline, not a scheduled departure time."},
              "Czech 'v 16:30'. Clock times take 'at'.", "Commercial Contracts & Incoterms 2020"),

            q("TTR-SALES-A2-005-Q4", "Production of the custom military tippers will commence _____ June 2027.",
              {"A": "at", "B": "on", "C": "by the", "D": "in"}, "D",
              {"correct": "Months and years without specific calendar days take 'in': 'in June 2027'.",
               "wrong_A": "'at' is for clock times.", "wrong_B": "'on' is for specific days.", "wrong_C": "'by the' is ungrammatical here."},
              "Czech 'v červnu 2027'. Months and years take 'in'.", "Commercial Contracts & Incoterms 2020"),

            q("TTR-SALES-A2-005-Q5", "The technical handover inspection will take place _____ Monday morning.",
              {"A": "in", "B": "at", "C": "on", "D": "by"}, "C",
              {"correct": "Days of the week and parts of specific days take 'on': 'on Monday morning'.",
               "wrong_A": "'in' is used for non-specific mornings ('in the morning'), but specific days take 'on'.", "wrong_B": "'at' is for clock times.", "wrong_D": "'by' indicates deadline."},
              "Czech 'v pondělí ráno'. Days of the week take 'on': 'on Monday morning'.", "International Sales & Customer Inquiries"),

            q("TTR-SALES-A2-005-Q6", "The client must submit formal acceptance documents _____ 30 calendar days of delivery.",
              {"A": "during", "B": "within", "C": "in between", "D": "at"}, "B",
              {"correct": "Time limit/window within which an action must happen takes 'within': 'within 30 days'.",
               "wrong_A": "'during' describes simultaneous action, not a deadline limit.", "wrong_C": "'in between' is spatial.", "wrong_D": "'at' is for exact points."},
              "Czech 'do 30 dnů / ve lhůtě 30 dnů'. Time window takes 'within 30 calendar days'.", "Commercial Contracts & Incoterms 2020"),

            q("TTR-SALES-A2-005-Q7", "The international sales office is closed _____ public holidays in the Czech Republic.",
              {"A": "in", "B": "on", "C": "at", "D": "by"}, "B",
              {"correct": "Holidays and named days take 'on': 'on public holidays'.",
               "wrong_A": "'in' is incorrect for holidays.", "wrong_C": "'at' is used for periods like 'at Christmas', but 'holidays' takes 'on'.", "wrong_D": "'by' indicates deadline."},
              "Czech 'o státních svátcích'. Plural holiday days take 'on public holidays'.", "International Sales & Customer Inquiries"),

            q("TTR-SALES-A2-005-Q8", "Please ensure the signed export declaration arrives _____ 17:00 tomorrow at the latest.",
              {"A": "by", "B": "in", "C": "on", "D": "to"}, "A",
              {"correct": "Deadline ('no later than') takes 'by': 'by 17:00 tomorrow'.",
               "wrong_B": "'in' expresses duration into the future.", "wrong_C": "'on' is for dates.", "wrong_D": "'to' indicates movement toward."},
              "Czech 'nejpozději do zítřejších 17:00'. Strict deadline takes 'by'.", "Commercial Contracts & Incoterms 2020"),

            q("TTR-SALES-A2-005-Q9", "The sea voyage from Antwerp to Alexandria typically takes _____ three weeks.",
              {"A": "in", "B": "around", "C": "at", "D": "on"}, "B",
              {"correct": "Approximation of duration takes 'around' (or 'about'): 'around three weeks'.",
               "wrong_A": "'in three weeks' means three weeks from now.", "wrong_C": "'at' is for clock times.", "wrong_D": "'on' is for days."},
              "Czech 'přibližně tři týdny'. Approximate duration takes 'around / about three weeks'.", "Commercial Contracts & Incoterms 2020"),

            q("TTR-SALES-A2-005-Q10", "The factory warranty coverage begins _____ the date of formal vehicle handover.",
              {"A": "at", "B": "on", "C": "in", "D": "from"}, "B",
              {"correct": "Preposition for dates/calendar days is 'on': 'on the date of handover' (or 'from the date', but 'on the date' specifies the effective start date).",
               "wrong_A": "'at' is for clock times.", "wrong_C": "'in' is for months/years.", "wrong_D": "'from' is informal compared to 'on the date of'."},
              "Czech 'dnem předání vozidla'. Formal effective date phrase: 'on the date of vehicle handover'.", "Commercial Contracts & Incoterms 2020")
        ]
    }

    return tests

print("Tatra tests defined.")
