"""
Test generators for missing Teva Engineering, Tapi Chemistry, and Teva IT modules.
"""

def get_teva_and_tapi_tests(q_helper):
    q = q_helper
    tests = {}

    # =========================================================================
    # TEVA ENGINEERING
    # =========================================================================

    # TEV-ENG-A2-002: Sterile Line Sensor Readings & Status: Present Simple
    tests["TEV-ENG-A2-002"] = {
        "test_id": "TEV-ENG-A2-002",
        "title": "Sterile Line Sensor Readings & Status: Present Simple",
        "level": "A2",
        "category": "core",
        "workplace_track": "Cleanroom HVAC Cascades & Differential Pressure",
        "estimated_time_minutes": 10,
        "description": "Report sterile vial filling line sensor readings, laminar flow velocities, and alarm states using Present Simple.",
        "learning_objectives": [
            "Use Present Simple 3rd person singular for instrument readouts",
            "State machine operational states with 'is / are'",
            "Avoid Czech word order transfer in affirmative instrument reports"
        ],
        "questions": [
            q("TEV-ENG-A2-002-Q1", "The differential pressure sensor on airlock 3 _____ a steady reading of 15 Pa.",
              {"A": "show", "B": "shows", "C": "showing", "D": "is show"}, "B",
              {"correct": "Singular subject 'sensor' takes 'shows' with 3rd person -s.", "wrong_A": "Lacks singular -s.", "wrong_C": "Participle alone cannot be verb.", "wrong_D": "Ungrammatical."},
              "Czech 'Senzor ukazuje'. Singular subject takes '-s': 'shows'.", "Cleanroom HVAC Cascades & Differential Pressure"),
            q("TEV-ENG-A2-002-Q2", "Laminar airflow velocity beneath the HEPA filter _____ within the 0.36 to 0.54 m/s specification.",
              {"A": "are", "B": "have", "C": "is", "D": "has"}, "C",
              {"correct": "Singular uncountable subject 'velocity' takes 'is'.", "wrong_A": "'are' is plural.", "wrong_B": "'have' cannot link to a predicate prepositional phrase.", "wrong_D": "'has' is incorrect for state."},
              "Czech 'Rychlost proudění je v normě'. 'Velocity' is singular $\\rightarrow$ 'is within specification'.", "Cleanroom HVAC Cascades & Differential Pressure"),
            q("TEV-ENG-A2-002-Q3", "The sterile vial filling machine _____ automatically when a fallen bottle is detected.",
              {"A": "stops", "B": "stop", "C": "is stop", "D": "stopping"}, "A",
              {"correct": "Singular subject 'machine' takes 'stops'.", "wrong_B": "Lacks -s.", "wrong_C": "Ungrammatical.", "wrong_D": "Participle cannot be verb."},
              "Czech 'Plnička se automaticky zastavuje'. Singular subject takes '-s': 'stops'.", "Sterile Compounding & Filling Line Automation"),
            q("TEV-ENG-A2-002-Q4", "_____ the SCADA monitoring system archive temperature logs every ten seconds?",
              {"A": "Is", "B": "Do", "C": "Are", "D": "Does"}, "D",
              {"correct": "Singular subject 'the system' takes auxiliary 'Does' in Present Simple questions.", "wrong_A": "'Is' requires continuous -ing.", "wrong_B": "'Do' is plural.", "wrong_C": "'Are' is plural."},
              "Czech 'Archivuje systém data každých deset sekund?'. Singular question takes 'Does the system archive...'.", "SCADA, PLC & Industrial Sensors"),
            q("TEV-ENG-A2-002-Q5", "Cleanroom technicians _____ glove integrity tests before entering Grade A aseptic zones.",
              {"A": "perform", "B": "performs", "C": "is perform", "D": "performing"}, "A",
              {"correct": "Plural subject 'technicians' takes base verb 'perform'.", "wrong_B": "'performs' is singular.", "wrong_C": "Ungrammatical.", "wrong_D": "Participle cannot be verb."},
              "Czech 'Technici provádějí...'. Plural subject takes base form without -s: 'perform'.", "Cleanroom HVAC Cascades & Differential Pressure"),
            q("TEV-ENG-A2-002-Q6", "The sterile transfer port _____ not unlock until differential pressure equalizes.",
              {"A": "is", "B": "does", "C": "do", "D": "has"}, "B",
              {"correct": "Singular negative Present Simple takes 'does not unlock'.", "wrong_A": "'is not unlock' is ungrammatical.", "wrong_C": "'do' is plural.", "wrong_D": "'has' cannot negate action verbs like this."},
              "Czech 'Port se neodemyká'. Use 'does not unlock'.", "Sterile Compounding & Filling Line Automation"),
            q("TEV-ENG-A2-002-Q7", "How often _____ the maintenance technician replace the peristaltic pump silicone tubing?",
              {"A": "is", "B": "do", "C": "are", "D": "does"}, "D",
              {"correct": "Singular technician subject takes auxiliary 'does': 'How often does the technician replace...'.", "wrong_A": "'is' cannot pair with bare verb 'replace'.", "wrong_B": "'do' is plural.", "wrong_C": "'are' is plural."},
              "Czech 'Jak často technik mění...?'. Question requires 'does the technician replace...?'.", "Sterile Compounding & Filling Line Automation"),
            q("TEV-ENG-A2-002-Q8", "The autoclave chamber temperature _____ steadily during the heating phase.",
              {"A": "rises", "B": "rise", "C": "is rise", "D": "rising"}, "A",
              {"correct": "Singular subject 'temperature' takes 'rises'.", "wrong_B": "Lacks singular -s.", "wrong_C": "Ungrammatical.", "wrong_D": "Participle alone cannot be verb."},
              "Czech 'Teplota v komoře stoupá'. Use 'rises' with 3rd person -s.", "Tablet Compression & Lyophilization Equipment"),
            q("TEV-ENG-A2-002-Q9", "Optical sensors on the conveyor belt _____ defective glass ampoules immediately.",
              {"A": "rejects", "B": "is reject", "C": "reject", "D": "rejecting"}, "C",
              {"correct": "Plural subject 'sensors' takes base verb 'reject'.", "wrong_A": "'rejects' is singular.", "wrong_B": "Ungrammatical.", "wrong_D": "Participle alone cannot be verb."},
              "Czech 'Optické senzory vyřazují...'. Plural subject takes base verb: 'reject'.", "Sterile Compounding & Filling Line Automation"),
            q("TEV-ENG-A2-002-Q10", "The cleanroom HVAC cascade _____ positive pressure from Grade B toward Grade C corridors.",
              {"A": "maintain", "B": "maintains", "C": "is maintain", "D": "maintaining"}, "B",
              {"correct": "Singular subject 'cascade' takes 'maintains'.", "wrong_A": "Lacks 3rd person -s.", "wrong_C": "Ungrammatical.", "wrong_D": "Participle alone cannot be verb."},
              "Czech 'Vzduchotechnická kaskáda udržuje...'. Singular subject takes '-s': 'maintains'.", "Cleanroom HVAC Cascades & Differential Pressure")
        ]
    }

    # TEV-ENG-A2-003: Yesterday's Machine Stoppages & Maintenance: Past Simple
    tests["TEV-ENG-A2-003"] = {
        "test_id": "TEV-ENG-A2-003",
        "title": "Yesterday's Machine Stoppages & Maintenance: Past Simple",
        "level": "A2",
        "category": "core",
        "workplace_track": "Sterile Compounding & Filling Line Automation",
        "estimated_time_minutes": 10,
        "description": "Report sterile filling line breakdowns, replacement of peristaltic pumps, and autoclave cycle resets using Past Simple.",
        "learning_objectives": [
            "Use Past Simple regular and irregular verbs (stopped, replaced, noticed, broke)",
            "Ask and answer simple past questions in maintenance deviation logs",
            "Avoid using present tense with past time adverbials"
        ],
        "questions": [
            q("TEV-ENG-A2-003-Q1", "Yesterday, the sterile capping machine _____ at 11:20 due to a jammed aluminum cap.",
              {"A": "stop", "B": "stopped", "C": "was stop", "D": "stopping"}, "B",
              {"correct": "Regular past tense is 'stopped' with doubled 'p'.", "wrong_A": "'stop' is present.", "wrong_C": "Ungrammatical.", "wrong_D": "Participle alone cannot be verb."},
              "Czech 'Včera se zařízení zastavilo'. Past Simple: 'stopped'.", "Sterile Compounding & Filling Line Automation"),
            q("TEV-ENG-A2-003-Q2", "The maintenance engineer _____ the worn peristaltic pump head in 20 minutes.",
              {"A": "replace", "B": "was replace", "C": "replaced", "D": "replacing"}, "C",
              {"correct": "Regular past tense is 'replaced'.", "wrong_A": "'replace' is present.", "wrong_B": "Ungrammatical.", "wrong_D": "Participle alone cannot be verb."},
              "Czech 'Inženýr vyměnil čerpadlo'. Use Past Simple 'replaced'.", "Sterile Compounding & Filling Line Automation"),
            q("TEV-ENG-A2-003-Q3", "The cleanroom operator _____ a pressure drop on the Grade B differential gauge.",
              {"A": "noticed", "B": "notice", "C": "was notice", "D": "noticing"}, "A",
              {"correct": "Regular past tense is 'noticed'.", "wrong_B": "'notice' is present.", "wrong_C": "Ungrammatical.", "wrong_D": "Participle alone cannot be verb."},
              "Czech 'Operátor si všiml poklesu tlaku'. Use Past Simple 'noticed'.", "Cleanroom HVAC Cascades & Differential Pressure"),
            q("TEV-ENG-A2-003-Q4", "_____ you calibrate the temperature sensor before starting the steam sterilization cycle?",
              {"A": "Were", "B": "Do", "C": "Have", "D": "Did"}, "D",
              {"correct": "Past Simple questions use auxiliary 'Did' + base verb 'calibrate'.", "wrong_A": "'Were' cannot pair with bare base verb.", "wrong_B": "'Do' is present.", "wrong_C": "'Have' requires past participle."},
              "Czech 'Zkalibroval jste senzor...?'. Use 'Did you calibrate...'.", "Tablet Compression & Lyophilization Equipment"),
            q("TEV-ENG-A2-003-Q5", "The autoclave heating element _____ during the sterilization phase yesterday afternoon.",
              {"A": "break", "B": "was break", "C": "broke", "D": "breaking"}, "C",
              {"correct": "Irregular past tense of 'break' is 'broke'.", "wrong_A": "'break' is present.", "wrong_B": "Ungrammatical.", "wrong_D": "Participle alone cannot be verb."},
              "Czech 'Topné těleso prasklo / porouchalo se'. Irregular verb: 'break $\\rightarrow$ broke'.", "Tablet Compression & Lyophilization Equipment"),
            q("TEV-ENG-A2-003-Q6", "The line technician _____ not reset the alarm before consulting the shift supervisor.",
              {"A": "was", "B": "did", "C": "does", "D": "is"}, "B",
              {"correct": "Past Simple negative takes 'did not reset'.", "wrong_A": "'was not reset' is passive.", "wrong_C": "'does' is present.", "wrong_D": "'is' is present."},
              "Czech 'Technik neresetoval alarm'. Use 'did not reset'.", "SCADA, PLC & Industrial Sensors"),
            q("TEV-ENG-A2-003-Q7", "Why _____ the SCADA server lose communication with PLC rack 4 yesterday?",
              {"A": "does", "B": "is", "C": "was", "D": "did"}, "D",
              {"correct": "Past question takes auxiliary 'did': 'Why did the server lose...'.", "wrong_A": "'does' is present.", "wrong_B": "'is' is present.", "wrong_C": "'was' cannot pair with bare verb 'lose'."},
              "Czech 'Proč server ztratil spojení?'. Question requires auxiliary 'did'.", "SCADA, PLC & Industrial Sensors"),
            q("TEV-ENG-A2-003-Q8", "We _____ a deviation report in the TrackWise system for the line stoppage.",
              {"A": "logged", "B": "log", "C": "were log", "D": "logging"}, "A",
              {"correct": "Regular past tense doubles the consonant: 'logged'.", "wrong_B": "'log' is present.", "wrong_C": "Ungrammatical.", "wrong_D": "Participle alone cannot be verb."},
              "Czech 'Zaznamenali jsme odchylku...'. Use Past Simple 'logged'.", "Cleanroom HVAC Cascades & Differential Pressure"),
            q("TEV-ENG-A2-003-Q9", "The sterile vial feeder bowl _____ 200 vials per minute before the jam occurred.",
              {"A": "feed", "B": "was feed", "C": "fed", "D": "feeding"}, "C",
              {"correct": "Irregular past tense of 'feed' is 'fed'.", "wrong_A": "'feed' is present.", "wrong_B": "Ungrammatical.", "wrong_D": "Participle alone cannot be verb."},
              "Czech 'Podavač podával 200 lahviček za minutu'. Irregular verb: 'feed $\\rightarrow$ fed'.", "Sterile Compounding & Filling Line Automation"),
            q("TEV-ENG-A2-003-Q10", "Quality assurance _____ the sterile batch after reviewing the autoclave chart records.",
              {"A": "release", "B": "released", "C": "is release", "D": "releasing"}, "B",
              {"correct": "Regular past tense is 'released'.", "wrong_A": "'release' is present.", "wrong_C": "Ungrammatical.", "wrong_D": "Participle alone cannot be verb."},
              "Czech 'Oddělení kvality propustilo šarži'. Use Past Simple 'released'.", "Cleanroom HVAC Cascades & Differential Pressure")
        ]
    }

    # TEV-ENG-A2-004: Cleanroom Airflow & Sensor Positions: Prepositions of Place
    tests["TEV-ENG-A2-004"] = {
        "test_id": "TEV-ENG-A2-004",
        "title": "Cleanroom Airflow & Sensor Positions: Prepositions of Place",
        "level": "A2",
        "category": "core",
        "workplace_track": "Cleanroom HVAC Cascades & Differential Pressure",
        "estimated_time_minutes": 10,
        "description": "Specify component positions inside laminar flow hoods, beneath HEPA filters, and between airlocks.",
        "learning_objectives": [
            "Use prepositions of place: under, inside, above, next to, between",
            "Give clear spatial directions in cleanroom suites and airlock cascades",
            "Avoid typical Czenglish preposition errors in sterile facility layouts"
        ],
        "questions": [
            q("TEV-ENG-A2-004-Q1", "Vial filling takes place directly _____ the Grade A unidirectional laminar airflow hood.",
              {"A": "on", "B": "under", "C": "between", "D": "over"}, "B",
              {"correct": "Beneath the laminar airflow hood $\\rightarrow$ 'under the hood'.", "wrong_A": "'on' means on top.", "wrong_C": "'between' requires two entities.", "wrong_D": "'over' means higher than."},
              "Czech 'přímo pod laminárním boxem'. Position beneath an airflow hood takes 'under'.", "Cleanroom HVAC Cascades & Differential Pressure"),
            q("TEV-ENG-A2-004-Q2", "Place the microbiological settle plates _____ the sterile filling enclosure.",
              {"A": "to", "B": "on", "C": "inside", "D": "under"}, "C",
              {"correct": "Enclosed sterile workspace $\\rightarrow$ 'inside the enclosure'.", "wrong_A": "'to' indicates movement.", "wrong_B": "'on' means on the exterior roof.", "wrong_D": "'under' means beneath the floor."},
              "Czech 'umístěte dovnitř boxu'. Enclosed interior takes 'inside'.", "Cleanroom HVAC Cascades & Differential Pressure"),
            q("TEV-ENG-A2-004-Q3", "The personal airlock is situated _____ the Grade C gowning room and the Grade B preparation area.",
              {"A": "between", "B": "among", "C": "under", "D": "through"}, "A",
              {"correct": "Separating two distinct cleanroom zones $\\rightarrow$ 'between'.", "wrong_B": "'among' is for three or more items.", "wrong_C": "'under' means beneath.", "wrong_D": "'through' indicates motion."},
              "Czech 'mezi šatnou třídy C a přípravnou třídy B'. Two distinct boundaries take 'between'.", "Cleanroom HVAC Cascades & Differential Pressure"),
            q("TEV-ENG-A2-004-Q4", "The magnehelic pressure gauge is mounted on the wall _____ the airlock entrance door.",
              {"A": "in", "B": "under", "C": "between", "D": "next to"}, "D",
              {"correct": "Adjacent position on the wall $\\rightarrow$ 'next to the door'.", "wrong_A": "'in' is internal.", "wrong_B": "'under' is on the floor.", "wrong_C": "'between' requires two doors."},
              "Czech 'hned vedle dveří'. Adjacent position takes 'next to'.", "Cleanroom HVAC Cascades & Differential Pressure"),
            q("TEV-ENG-A2-004-Q5", "The HEPA terminal filter units are installed in the ceiling _____ the sterile conveyor line.",
              {"A": "under", "B": "between", "C": "above", "D": "through"}, "C",
              {"correct": "Higher vertical position without contact $\\rightarrow$ 'above the line'.", "wrong_A": "'under' is beneath.", "wrong_B": "'between' requires two objects.", "wrong_D": "'through' indicates motion across."},
              "Czech 've stropě nad linkou'. Vertical position above $\\rightarrow$ 'above the line'.", "Cleanroom HVAC Cascades & Differential Pressure"),
            q("TEV-ENG-A2-004-Q6", "The emergency eye wash station is located _____ the entrance to the chemical preparation suite.",
              {"A": "under", "B": "near", "C": "between", "D": "inside of"}, "B",
              {"correct": "Proximity preposition $\\rightarrow$ 'near the entrance'.", "wrong_A": "'under' is beneath.", "wrong_C": "'between' requires two points.", "wrong_D": "'inside of' is redundant and clumsy."},
              "Czech 'poblíž vstupu'. Close proximity takes 'near'.", "Cleanroom HVAC Cascades & Differential Pressure"),
            q("TEV-ENG-A2-004-Q7", "Keep all sterile packaging materials _____ the stainless steel pass-through box.",
              {"A": "inside", "B": "under", "C": "on", "D": "through"}, "A",
              {"correct": "Enclosed container $\\rightarrow$ 'inside the pass-through box'.", "wrong_B": "'under' is beneath.", "wrong_C": "'on' means on the exterior roof.", "wrong_D": "'through' indicates movement."},
              "Czech 'uvnitř prokládacího boxu'. Enclosed interior takes 'inside'.", "Sterile Compounding & Filling Line Automation"),
            q("TEV-ENG-A2-004-Q8", "The return air grilles are installed in the wall near the floor _____ the filling table.",
              {"A": "behind", "B": "between", "C": "above", "D": "through"}, "A",
              {"correct": "Position at the rear $\\rightarrow$ 'behind the filling table'.", "wrong_B": "'between' requires two objects.", "wrong_C": "'above' is higher.", "wrong_D": "'through' indicates motion."},
              "Czech 'za plnicím stolem'. Position at the rear takes 'behind'.", "Cleanroom HVAC Cascades & Differential Pressure"),
            q("TEV-ENG-A2-004-Q9", "Never store empty transport carts _____ the fire exit door in the corridor.",
              {"A": "under", "B": "inside", "C": "in front of", "D": "between"}, "C",
              {"correct": "Blocking an exit $\\rightarrow$ 'in front of the fire exit door'.", "wrong_A": "'under' is beneath.", "wrong_B": "'inside' is internal.", "wrong_D": "'between' requires two doors."},
              "Czech 'před únikovými dveřmi'. Obstruction in front takes 'in front of'.", "Cleanroom HVAC Cascades & Differential Pressure"),
            q("TEV-ENG-A2-004-Q10", "The temperature data logger sensor is mounted _____ the middle rack of the incubator.",
              {"A": "to", "B": "on", "C": "under", "D": "at"}, "B",
              {"correct": "Mounted on a horizontal shelf surface $\\rightarrow$ 'on the middle rack'.", "wrong_A": "'to' indicates movement.", "wrong_C": "'under' means beneath the rack.", "wrong_D": "'at' is vague location."},
              "Czech 'na prostřední polici'. Surface position takes 'on'.", "Tablet Compression & Lyophilization Equipment")
        ]
    }

    # TEV-ENG-A2-005: Autoclave Cycles & Temperatures: Numbers & Measurements
    tests["TEV-ENG-A2-005"] = {
        "test_id": "TEV-ENG-A2-005",
        "title": "Autoclave Cycles & Temperatures: Numbers & Measurements",
        "level": "A2",
        "category": "core",
        "workplace_track": "Tablet Compression & Lyophilization Equipment",
        "estimated_time_minutes": 10,
        "description": "Communicate sterilizer temperatures in Celsius (121°C), cycle times in minutes, and steam pressure in bar.",
        "learning_objectives": [
            "State technical temperatures, pressures, and durations accurately in English",
            "Use prepositions with measurements: at 121°C, for 20 minutes, to 2.1 bar",
            "Avoid common Czenglish measurement phrasing mistakes"
        ],
        "questions": [
            q("TEV-ENG-A2-005-Q1", "The steam autoclave sterilizes surgical instruments _____ 121 degrees Celsius.",
              {"A": "in", "B": "at", "C": "on", "D": "with"}, "B",
              {"correct": "Specific operational temperatures take preposition 'at': 'at 121 degrees Celsius'.", "wrong_A": "'in' is incorrect for exact temperatures.", "wrong_C": "'on' is incorrect.", "wrong_D": "'with' is incorrect."},
              "Czech 'při 121 stupních Celsia'. Exact operating temperatures take 'at': 'at 121°C'.", "Tablet Compression & Lyophilization Equipment"),
            q("TEV-ENG-A2-005-Q2", "The sterilization holding phase must continue _____ exactly 20 minutes.",
              {"A": "during", "B": "in", "C": "for", "D": "since"}, "C",
              {"correct": "Duration of time takes preposition 'for': 'for 20 minutes'.", "wrong_A": "'during' is followed by an event noun ('during the cycle'), not a duration number.", "wrong_B": "'in' means after 20 minutes.", "wrong_D": "'since' indicates starting point in the past."},
              "Czech 'po dobu 20 minut'. Duration of time takes 'for': 'for 20 minutes'.", "Tablet Compression & Lyophilization Equipment"),
            q("TEV-ENG-A2-005-Q3", "The chamber pressure reaches _____ of 2.1 bar during the saturated steam cycle.",
              {"A": "a maximum", "B": "maximum", "C": "maximally", "D": "the maximally"}, "A",
              {"correct": "Noun phrase takes 'a maximum of 2.1 bar'.", "wrong_B": "Lacks required article 'a'.", "wrong_C": "'maximally' is an adverb.", "wrong_D": "Ungrammatical."},
              "Czech 'dosahuje maxima 2,1 bar'. Standard technical formula: 'reaches a maximum of 2.1 bar'.", "Tablet Compression & Lyophilization Equipment"),
            q("TEV-ENG-A2-005-Q4", "How _____ steam pressure is currently recorded inside the sterilization chamber?",
              {"A": "many", "B": "much of", "C": "much", "D": "many of"}, "C",
              {"correct": "Uncountable noun 'pressure' takes 'How much'.", "wrong_A": "'many' is for countable nouns.", "wrong_B": "'much of' is incorrect before bare noun.", "wrong_D": "'many of' is incorrect."},
              "Czech 'Kolik tlaku páry...?'. Uncountable nouns take 'How much steam pressure'.", "Tablet Compression & Lyophilization Equipment"),
            q("TEV-ENG-A2-005-Q5", "The cooling cycle brings the temperature down _____ room temperature (22°C).",
              {"A": "at", "B": "in", "C": "to", "D": "into"}, "C",
              {"correct": "Endpoint of a reduction or change takes preposition 'to': 'down to room temperature'.", "wrong_A": "'at' indicates fixed position, not endpoint of change.", "wrong_B": "'in' is incorrect.", "wrong_D": "'into' indicates physical entry."},
              "Czech 'ochlazuje na pokojovou teplotu'. Endpoint of temperature drop takes 'down to'.", "Tablet Compression & Lyophilization Equipment"),
            q("TEV-ENG-A2-005-Q6", "The autoclave door cannot be opened until the chamber pressure drops _____ 0.05 bar.",
              {"A": "under", "B": "below", "C": "down", "D": "beneath"}, "B",
              {"correct": "On numerical scales (temperature, pressure), lower value takes 'below': 'below 0.05 bar'.", "wrong_A": "'under' is common, but 'below' is the strictly preferred technical standard for scales.", "wrong_C": "'down' is an adverb.", "wrong_D": "'beneath' is spatial."},
              "Czech 'klesne pod 0,05 bar'. Measurements on a numerical scale use 'below'.", "Tablet Compression & Lyophilization Equipment"),
            q("TEV-ENG-A2-005-Q7", "The sterilizer holds _____ ten stainless steel trays per cycle.",
              {"A": "up", "B": "up of", "C": "to", "D": "up to"}, "D",
              {"correct": "Upper capacity limit takes 'up to': 'up to ten trays'.", "wrong_A": "'up' alone cannot express limit.", "wrong_B": "'up of' is invalid.", "wrong_C": "'to' alone is incomplete here."},
              "Czech 'až 10 nerezových táců'. Upper capacity limit takes 'up to ten trays'.", "Tablet Compression & Lyophilization Equipment"),
            q("TEV-ENG-A2-005-Q8", "The vacuum leak test takes approximately _____ and a half minutes to complete.",
              {"A": "seven", "B": "seventh", "C": "seven of", "D": "seventeen"}, "A",
              {"correct": "Cardinal number 'seven' pairs with 'seven and a half minutes'.", "wrong_B": "'seventh' is an ordinal number.", "wrong_C": "'seven of' is incorrect before 'and a half'.", "wrong_D": "'seventeen' is 17."},
              "Czech 'sedm a půl minuty'. Use cardinal number: 'seven and a half minutes'.", "Tablet Compression & Lyophilization Equipment"),
            q("TEV-ENG-A2-005-Q9", "The drying vacuum pulls the pressure down _____ negative 0.8 bar.",
              {"A": "on", "B": "in", "C": "to", "D": "at"}, "C",
              {"correct": "Reaching an endpoint takes 'to': 'down to negative 0.8 bar'.", "wrong_A": "'on' is incorrect.", "wrong_B": "'in' is incorrect.", "wrong_D": "'at' indicates current reading, not endpoint."},
              "Czech 'na minus 0,8 bar'. Endpoint of pull-down takes 'to negative 0.8 bar'.", "Tablet Compression & Lyophilization Equipment"),
            q("TEV-ENG-A2-005-Q10", "The temperature sensor has an accuracy tolerance of plus or minus 0.5 _____ Celsius.",
              {"A": "degree", "B": "degrees", "C": "degreeness", "D": "graded"}, "B",
              {"correct": "Plural noun 'degrees' follows decimals and numerals other than exactly 1: '0.5 degrees Celsius'.", "wrong_A": "'degree' is singular.", "wrong_C": "Non-existent word.", "wrong_D": "'graded' is past participle."},
              "Czech '0,5 stupně Celsia'. Decimals in English take plural 'degrees': '0.5 degrees Celsius'.", "Tablet Compression & Lyophilization Equipment")
        ]
    }

    return tests

print("Teva tests defined.")
