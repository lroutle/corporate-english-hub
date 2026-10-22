"""
Diverse Question Engine for Corporate English Assessment Ecosystem.
Generates pedagogically rigorous, non-repetitive, contrastive Czech-English test modules.
Guarantees 10 unique prompts per module with diverse grammar structures and balanced answer keys.
"""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(ROOT / "scripts"))

from generators.common import make_q, build_test_module, KEY_PATTERN

# -----------------------------------------------------------------------------
# BESPOKE HANDCRAFTED MODULES (TATRA ENGINEERING)
# -----------------------------------------------------------------------------
BESPOKE_MODULES = {}

# TTR-ENG-B1-005: Air Suspension Bellows Replacement: Sequence & Safety
BESPOKE_MODULES["TTR-ENG-B1-005"] = [
    ("TTR-ENG-B1-005-Q1",
     "Before loosening the lower air bellows retaining flange, the technician _____ the pneumatic suspension system to prevent explosive decompression.",
     {"A": "must to completely depressurize", "B": "must completely depressurize", "C": "must completely depressurizing", "D": "is must depressurize"},
     "B",
     {"correct": "Modal 'must' is directly followed by the bare infinitive verb 'depressurize' without 'to'.",
      "wrong_A": "'must to' is ungrammatical; modal verbs never take 'to'.",
      "wrong_C": "'must' cannot be followed by an '-ing' participle.",
      "wrong_D": "'is must' is completely ungrammatical in English."},
     "V angličtině se po způsobovém slovesu 'must' klade holý infinitiv bez 'to': 'must depressurize' (nikdy *must to*).",
     "Suspension, Half-Axles & CTIS Diagnostics"),

    ("TTR-ENG-B1-005-Q2",
     "Workshop safety protocol mandates that heavy-duty mechanical axle stands _____ securely beneath the backbone tube crossmember before anyone enters the pit.",
     {"A": "are positioning", "B": "position", "C": "be positioned", "D": "must to be positioned"},
     "C",
     {"correct": "The mandative subjunctive or passive construction following 'mandates that' requires 'be positioned'.",
      "wrong_A": "Active continuous 'are positioning' does not fit passive axle stands.",
      "wrong_B": "Axle stands do not position themselves actively.",
      "wrong_D": "'must to be' is ungrammatical; modal 'must' does not take 'to'."},
     "Pasivní vazba u bezpečnostních předpisů: stojany musí být umístěny ('be positioned'). Neživé předměty nejednají aktivně.",
     "Suspension, Half-Axles & CTIS Diagnostics"),

    ("TTR-ENG-B1-005-Q3",
     "The mechanic noticed an audible hiss around the auxiliary air valve _____ the bellow bladder was being inflated to operating height.",
     {"A": "while", "B": "during", "C": "for", "D": "since"},
     "A",
     {"correct": "'While' is a conjunction followed by a full continuous clause ('the bellow bladder was being inflated').",
      "wrong_B": "'During' is a preposition and must be followed by a noun phrase, not a clause with a finite verb.",
      "wrong_C": "'For' indicates duration of time, not concurrent background actions.",
      "wrong_D": "'Since' indicates a starting point in time or causation, not simultaneous events."},
     "Častá chyba: 'during' se pojí s podstatným jménem (during the test), zatímco s celou větou se slovesem se pojí spojka 'while' (while it was being inflated).",
     "Suspension, Half-Axles & CTIS Diagnostics"),

    ("TTR-ENG-B1-005-Q4",
     "After removing the top mounting bolts, inspect the upper vulcanized rubber bead _____ signs of ozone cracking or abrasive wear against the bump stop.",
     {"A": "to", "B": "at", "C": "against", "D": "for"},
     "D",
     {"correct": "The standard engineering collocation is 'inspect [something] for [defects/signs]'.",
      "wrong_A": "'inspect to' is incorrect phrasing for checking defects.",
      "wrong_B": "'inspect at' is non-standard in mechanical inspection.",
      "wrong_C": "'against' expresses opposition or contact, not the purpose of the inspection."},
     "Vazba 'inspect for defects' = zkontrolovat na přítomnost vad. Češi často nesprávně volí předložku 'on' nebo 'at'.",
     "Suspension, Half-Axles & CTIS Diagnostics"),

    ("TTR-ENG-B1-005-Q5",
     "If the replacement bellows does not seat properly on the lower swinging half-axle pedestal, the air fitting _____ cross-threaded.",
     {"A": "must to be", "B": "can to be", "C": "might be", "D": "is might"},
     "C",
     {"correct": "'Might be' correctly expresses technical possibility/deduction without ungrammatical 'to'.",
      "wrong_A": "'must to be' is ungrammatical.",
      "wrong_B": "'can to be' is ungrammatical in English.",
      "wrong_D": "'is might' is invalid syntax."},
     "Způsobová slovesa vyjadřující možnost (might, may, can, could) se nikdy nepojí s předložkou 'to': 'might be cross-threaded'.",
     "Suspension, Half-Axles & CTIS Diagnostics"),

    ("TTR-ENG-B1-005-Q6",
     "Never inflate a new air spring assembly beyond 0.5 bar _____ the axle shock absorber and upper retaining bracket are fully bolted down.",
     {"A": "by", "B": "until", "C": "during", "D": "since"},
     "B",
     {"correct": "'Until' indicates a condition or time limit that must occur before the prohibited action can change.",
      "wrong_A": "'by' denotes a deadline, not a temporal condition clause.",
      "wrong_C": "'during' cannot introduce a finite subordinate clause.",
      "wrong_D": "'since' indicates elapsed time from a past event or reason."},
     "'Until' = dokud ne / až do okamžiku, kdy. V angličtině po 'until' nenásleduje zápor: 'until they are fully bolted down'.",
     "Suspension, Half-Axles & CTIS Diagnostics"),

    ("TTR-ENG-B1-005-Q7",
     "The maintenance technician _____ the pneumatic quick-release coupling yesterday because the internal O-ring had dried out.",
     {"A": "has replaced", "B": "replaces", "C": "is replacing", "D": "replaced"},
     "D",
     {"correct": "The specific past time indicator 'yesterday' strictly requires Past Simple 'replaced'.",
      "wrong_A": "Present Perfect 'has replaced' cannot be used with finished past time expressions like 'yesterday'.",
      "wrong_B": "Present Simple expresses habitual routines, not a specific finished event.",
      "wrong_C": "Present Continuous expresses an action in progress right now."},
     "S příslovečným určením minulého času jako 'yesterday' se v angličtině striktně pojí minulý čas prostý (Past Simple: 'replaced'), nikoli předpřítomný čas.",
     "Suspension, Half-Axles & CTIS Diagnostics"),

    ("TTR-ENG-B1-005-Q8",
     "Tatra workshop manual TM-815 specifies that the mounting nuts _____ to 180 Nm using a calibrated torque wrench.",
     {"A": "should be tightened", "B": "should tighten", "C": "should to be tightened", "D": "are should tightened"},
     "A",
     {"correct": "Passive with modal 'should be tightened' correctly indicates how the nuts must be handled.",
      "wrong_B": "Active 'should tighten' is wrong; nuts cannot tighten themselves.",
      "wrong_C": "'should to be' is ungrammatical.",
      "wrong_D": "'are should' is invalid syntax."},
     "Trpný rod se způsobovým slovesem: 'should be tightened' (měly by být dotaženy). Vyhněte se činnému rodu u neživých součástek.",
     "Suspension, Half-Axles & CTIS Diagnostics"),

    ("TTR-ENG-B1-005-Q9",
     "To verify proper sealing after installation, apply soapy water solution _____ all pneumatic push-in airline fittings.",
     {"A": "into", "B": "towards", "C": "to", "D": "on top"},
     "C",
     {"correct": "The verb 'apply' collocates with preposition 'to': 'apply solution to fittings'.",
      "wrong_A": "'into' would mean introducing liquid inside the pressurized air lines, which causes contamination.",
      "wrong_B": "'towards' denotes general direction, not contact application.",
      "wrong_D": "'on top' is an incomplete prepositional phrase lacking 'of'."},
     "Vazba 'apply something to something' = aplikovat / nanést něco na něco. Do vnitřku vedení ('into') se roztok nesmí dostat.",
     "Suspension, Half-Axles & CTIS Diagnostics"),

    ("TTR-ENG-B1-005-Q10",
     "The truck cannot pass the workshop functional release inspection _____ the pneumatic leveling valve automatically restores ride height within 30 seconds.",
     {"A": "provided that", "B": "unless", "C": "if", "D": "as long as"},
     "B",
     {"correct": "'Unless' means 'except if' or 'if not', expressing the mandatory condition required for passing.",
      "wrong_A": "'provided that' would mean the truck cannot pass IF the valve works, which is illogical.",
      "wrong_C": "'if' creates an illogical negative outcome.",
      "wrong_D": "'as long as' also creates an inverted, illogical condition."},
     "'Unless' znamená 'pokud ne' (if not). Po 'unless' už v anglické větě nenásleduje další zápor.",
     "Suspension, Half-Axles & CTIS Diagnostics")
]

# TTR-ENG-B1-016: Prototype Test Track Rig Setup & Accelerometer Sensor Calibration
BESPOKE_MODULES["TTR-ENG-B1-016"] = [
    ("TTR-ENG-B1-016-Q1",
     "The test engineer noticed that the dynamic accelerometer _____ securely onto the backbone tube chassis before the high-speed gravel run began.",
     {"A": "was mounting", "B": "had been mounted", "C": "has mounted", "D": "didn't mount"},
     "B",
     {"correct": "Past Perfect Passive ('had been mounted') expresses an action completed prior to the past reference point 'began'.",
      "wrong_A": "Active continuous 'was mounting' does not fit passive sensor installation.",
      "wrong_C": "Present Perfect 'has mounted' cannot connect to a past narrative.",
      "wrong_D": "Active past simple 'didn't mount' is grammatically incorrect for passive equipment."},
     "Děj, který proběhl před jiným dějem v minulosti ('before the run began'), vyžaduje předminulý čas v trpném rodě: 'had been mounted'.",
     "Vehicle Homologation & NATO STANAG Mobility"),

    ("TTR-ENG-B1-016-Q2",
     "If the telemetry transceiver _____ signal with the base station on the Kopřivnice test polygon, the onboard logger stores raw vibration data internally.",
     {"A": "will lose", "B": "would lose", "C": "loses", "D": "lost"},
     "C",
     {"correct": "First conditional rule: Present Simple ('loses') in the conditional clause for real operational contingencies.",
      "wrong_A": "'will' cannot be used in a conditional if-clause.",
      "wrong_B": "'would' cannot be used in a real First Conditional.",
      "wrong_D": "Past tense 'lost' would conflict with present indicative 'stores'."},
     "Typická chyba: v podmínkové větě s 'if' se nesmí použít 'will' (*if it will lose*). Použijte přítomný čas: 'if it loses'.",
     "Vehicle Homologation & NATO STANAG Mobility"),

    ("TTR-ENG-B1-016-Q3",
     "During the 60 km/h Belgian block test, the suspension transducers registered severe vibrations _____ the rear swinging half-axles.",
     {"A": "across", "B": "into", "C": "onto", "D": "between of"},
     "A",
     {"correct": "'Across' appropriately describes vibrations distributed throughout or spanning the axle assembly.",
      "wrong_B": "'into' implies directional movement entering inside.",
      "wrong_C": "'onto' denotes motion to a surface.",
      "wrong_D": "'between of' is ungrammatical; 'between' does not take 'of'."},
     "Předložka 'across' vyjadřuje rozložení vibrací napříč polonápravami. Vyvarujte se chybné vazby *between of*.",
     "Vehicle Homologation & NATO STANAG Mobility"),

    ("TTR-ENG-B1-016-Q4",
     "To avoid electromagnetic noise interference from the alternator, all analog sensor cables _____ with grounded braided shielding.",
     {"A": "must to route", "B": "are routing", "C": "must route", "D": "must be routed"},
     "D",
     {"correct": "Passive with modal 'must be routed' correctly indicates cable routing requirements.",
      "wrong_A": "'must to route' is ungrammatical.",
      "wrong_B": "Cables do not route themselves actively.",
      "wrong_C": "Active voice 'must route' lacks an object and misassigns action to cables."},
     "Kabely musí být vedeny stíněním: 'must be routed'. Způsobové sloveso s trpným rodem 'be + příčestí minulé'.",
     "Vehicle Homologation & NATO STANAG Mobility"),

    ("TTR-ENG-B1-016-Q5",
     "The telemetry technician spent three hours yesterday _____ the multi-channel strain gauge amplifier before zero-point offset calibration.",
     {"A": "to fine-tune", "B": "fine-tune", "C": "fine-tuning", "D": "fine-tuned"},
     "C",
     {"correct": "The verb structure 'spend time doing something' requires the '-ing' gerund form: 'fine-tuning'.",
      "wrong_A": "'spend time to do' is ungrammatical in standard English.",
      "wrong_B": "Base form without '-ing' is incorrect after 'spend time'.",
      "wrong_D": "Past form cannot follow 'spend time'."},
     "Vazba 'spend time doing something' vyžaduje gerundium s koncovkou -ing: 'spent three hours fine-tuning' (nikoli *to fine-tune*).",
     "Vehicle Homologation & NATO STANAG Mobility"),

    ("TTR-ENG-B1-016-Q6",
     "Tatra prototype T-815-7 was driven over the 400 mm vertical obstacle _____ the dynamic wheel travel limits could be evaluated by optical cameras.",
     {"A": "in order", "B": "so that", "C": "because of", "D": "for"},
     "B",
     {"correct": "'So that' is a conjunction of purpose followed by a subject and modal verb clause ('the dynamic wheel travel limits could be evaluated').",
      "wrong_A": "'in order' requires 'to' + infinitive or 'that' + clause.",
      "wrong_C": "'because of' is followed by a noun phrase, not a clause with a finite verb.",
      "wrong_D": "'for' cannot introduce this purpose clause with modal 'could'."},
     "Účelová spojka 'so that' = aby (následovaná podmětem a způsobovým slovesem: 'so that limits could be evaluated').",
     "Vehicle Homologation & NATO STANAG Mobility"),

    ("TTR-ENG-B1-016-Q7",
     "When reviewing the accelerometer telemetry log, the validation engineer realized that the low-pass Butterworth filter _____ at 200 Hz instead of 500 Hz.",
     {"A": "was set", "B": "has set", "C": "is setting", "D": "had been set"},
     "D",
     {"correct": "Past Perfect Passive ('had been set') is required because the filter configuration occurred before the engineer 'realized' it.",
      "wrong_A": "Past simple does not clearly indicate priority before 'realized'.",
      "wrong_B": "Present perfect active is incorrect in voice and tense.",
      "wrong_C": "Present continuous does not fit completed past telemetry recording."},
     "Čeština používá v obou větách minulý čas. V angličtině vyžaduje děj předcházející minulému okamžiku předminulý čas: 'had been set'.",
     "Vehicle Homologation & NATO STANAG Mobility"),

    ("TTR-ENG-B1-016-Q8",
     "The NATO STANAG test protocol requires that each triaxial sensor _____ re-zeroed immediately after every heavy obstacle impact test.",
     {"A": "be", "B": "is", "C": "will be", "D": "must to be"},
     "A",
     {"correct": "The mandative subjunctive following 'requires that' uses the base form 'be' in formal technical documentation.",
      "wrong_B": "Indicative 'is' is informal and less appropriate in formal standard specifications.",
      "wrong_C": "Future 'will be' is incorrect after mandative 'requires that'.",
      "wrong_D": "'must to be' is ungrammatical."},
     "Subjunktiv po slovesech požadavku ('requires that each sensor be re-zeroed') používá základní tvar 'be', nikoli *is* nebo *will be*.",
     "Vehicle Homologation & NATO STANAG Mobility"),

    ("TTR-ENG-B1-016-Q9",
     "Why _____ the mobile DAQ (Data Acquisition) unit shut down unexpectedly during the cross-country trench crossing trial?",
     {"A": "has", "B": "was", "C": "did", "D": "does"},
     "C",
     {"correct": "Past Simple question with base verb 'shut down' requires auxiliary 'did': 'Why did the unit shut down?'.",
      "wrong_A": "'has' would require past participle and doesn't fit specific past event 'during the trial'.",
      "wrong_B": "'was' with 'shut down' would form a passive without subject-verb agreement or agent.",
      "wrong_D": "'does' is present tense, incompatible with completed trial."},
     "Tvoření otázek v minulém čase: tázací způsobové pomocné sloveso 'did' + podmět + základní tvar slovesa ('Why did the unit shut down?').",
     "Vehicle Homologation & NATO STANAG Mobility"),

    ("TTR-ENG-B1-016-Q10",
     "Unless the pneumatic tire pressure monitoring sensors are recalibrated for cold-weather conditions, the rolling resistance data _____ invalid.",
     {"A": "remains", "B": "will remain", "C": "would have remained", "D": "remained"},
     "B",
     {"correct": "First conditional result clause takes 'will + base verb' ('will remain') paired with present condition 'Unless... are recalibrated'.",
      "wrong_A": "Present simple in the main clause expresses timeless general truth rather than future predictive consequence.",
      "wrong_C": "Third conditional form conflicts with present conditional clause.",
      "wrong_D": "Past tense cannot serve as the main clause for a present condition."},
     "První kondicionál (First Conditional): Pokud je v podmínce přítomný čas (Unless sensors are...), v hlavní větě musí být budoucí čas: 'will remain'.",
     "Vehicle Homologation & NATO STANAG Mobility")
]

# -----------------------------------------------------------------------------
# DOMAIN LEXICONS & CONTEXT BANKS
# -----------------------------------------------------------------------------
DOMAIN_BANKS = {
    "tatra_eng": {
        "items": [
            ("the differential gear housing", "align with the central backbone tube", "tighten to 380 Nm", "assembled"),
            ("the swinging half-axle kingpin bearing", "lubricate with molybdenum grease", "inspect for free play", "lubricated"),
            ("the central tire inflation system (CTIS) rotary valve", "calibrate against pneumatic line pressure", "purge of condensed moisture", "calibrated"),
            ("the air suspension bellows assembly", "mount onto the rear chassis bracket", "test under 8 bar operating pressure", "installed"),
            ("the air-cooled V8 cylinder head gasket", "torque according to workshop manual TM-815", "check for exhaust soot blow-by", "torqued"),
            ("the transfer case planetary reduction gear", "engage smoothly under full mechanical load", "flush with synthetic gear oil", "inspected"),
            ("the dual-circuit pneumatic brake actuator", "regulate air pressure to NATO STANAG specs", "replace before road endurance trials", "serviced"),
            ("the hydraulic cabin tilt locking mechanism", "secure with dual mechanical safety latches", "bleed air from hydraulic lines", "locked"),
            ("the front wheel steering tie-rod ball joint", "measure for angular deflection runout", "adjust toe-in angle on the alignment rig", "adjusted"),
            ("the chassis backbone tube flange coupling", "weld under robotic shielding gas control", "verify by non-destructive ultrasonic scan", "welded")
        ],
        "operators": ["The assembly technician", "The quality inspector", "The chassis specialist", "The workshop mechanic", "The test track engineer"],
        "locations": ["in the Kopřivnice heavy assembly bay", "on the chassis assembly jig", "under the vehicle pit crossmember", "beside the dynamometer test stand"],
        "standards": ["Tatra technical standard CSN-815", "NATO STANAG 4569 mobility guidelines", "Kopřivnice quality manual QA-04", "ECE R13 brake regulation protocols"],
        "adverbs": ["carefully", "securely", "strictly", "routinely", "automatically"]
    },
    "tatra_sales": {
        "items": [
            ("the irrevocable confirmed Letter of Credit (L/C)", "issue through an accredited European tier-1 bank", "verify for documentary discrepancies", "confirmed"),
            ("the commercial export invoice and bill of lading", "endorse by the international shipping agent", "present before customs clearance in Hamburg", "endorsed"),
            ("the Incoterms 2020 DAP delivery milestone", "meet before the contractual penalty window", "coordinate with port terminal stevedores", "fulfilled"),
            ("the military fleet tender compliance matrix", "complete with full STANAG ballistic ratings", "sign by authorized corporate executives", "submitted"),
            ("the chassis knockdown (CKD) export container", "pack with desiccants for maritime shipping", "dispatch from Kopřivnice via rail freight", "inspected"),
            ("the international dealer warranty reimbursement", "audit against verified workshop hours", "credit to the distributor's account", "approved"),
            ("the defense offset joint venture agreement", "ratify by the sovereign ministry of defense", "formalize through legal corporate counsel", "negotiated"),
            ("the foreign exchange hedging forward contract", "lock in to mitigate crown-euro volatility", "execute through treasury department desk", "settled"),
            ("the pre-shipment vehicle inspection protocol", "certify by an independent classification society", "sign off at the manufacturing plant gate", "certified"),
            ("the demurrage and container storage surcharge", "dispute with the Mediterranean shipping line", "apportion between buyer and forwarding agent", "reconciled")
        ],
        "operators": ["The export sales manager", "The commercial director", "The international logistics coordinator", "The legal compliance counsel", "The tender bid specialist"],
        "locations": ["at the defense trade fair in Abu Dhabi", "in the international commercial contract", "during foreign ministerial bilateral meetings", "at the maritime container freight terminal"],
        "standards": ["Incoterms 2020 publication ICC 723", "Defense procurement directive DEF-2026", "International Chamber of Commerce arbitration rules", "EU export dual-use licensing guidelines"],
        "adverbs": ["formally", "promptly", "unilaterally", "diligently", "strictly"]
    },
    "tapi_eng": {
        "items": [
            ("the cleanroom differential pressure cascade", "maintain at 15 Pascals above ambient corridors", "log continuously into the SCADA historian", "validated"),
            ("the HEPA filter terminal ceiling diffuser", "test for aerosol penetration using Emery 3004", "certify according to ISO 14644 Class 5", "tested"),
            ("the Water for Injection (WFI) loop circulation pump", "run continuously at 80 degrees Celsius", "monitor for conductivity spikes below 1.1 uS/cm", "sanitized"),
            ("the automated autoclave chamber pressure vessel", "sterilize active equipment at 121 degrees Celsius", "calibrate temperature thermocouples annually", "calibrated"),
            ("the sterile filling peristaltic dosing pump", "dispense liquid active ingredients within +/- 0.5%", "prime with validated platinum-cured silicone tubing", "primed"),
            ("the lyophilizer condenser refrigeration circuit", "pull vacuum down to 0.05 millibar", "defrost via automated clean steam injection", "inspected"),
            ("the rotary tablet compression tooling punch", "polish to Ra 0.2 micron mirror surface finish", "measure for critical die pocket wear limits", "polished"),
            ("the HVAC air handling unit (AHU) pre-filter bank", "replace before pressure drop exceeds 250 Pa", "audit during scheduled plant shutdown windows", "replaced"),
            ("the SCADA PLC automated interlock safety loop", "prevent airlock doors from opening simultaneously", "backup to the encrypted secure cloud server", "configured"),
            ("the clean steam generator boiler blowdown valve", "purge dissolved solids from the evaporation tube", "test for non-condensable gas compliance", "serviced")
        ],
        "operators": ["The cleanroom facility engineer", "The GxP validation specialist", "The plant maintenance technician", "The automation PLC programmer", "The sterile operations supervisor"],
        "locations": ["inside the Grade A aseptic processing suite", "in the pharmaceutical utilities basement", "at the cleanroom secondary airlock boundary", "within the sterile packaging filling line"],
        "standards": ["EudraLex Volume 4 GMP Annex 1", "GAMP 5 computerized system guidelines", "ISO 14644-1 cleanroom classifications", "21 CFR Part 11 electronic records standards"],
        "adverbs": ["aseptically", "rigorously", "consistently", "meticulously", "automatically"]
    },
    "tapi_chem": {
        "items": [
            ("the high-performance liquid chromatograph (HPLC)", "equilibrate with 60:40 acetonitrile-water mobile phase", "verify system suitability peak tailing below 1.5", "equilibrated"),
            ("the jacketed glass batch synthesis reactor", "heat to 78 degrees Celsius under reflux conditions", "purge with dry nitrogen gas prior to charging", "purged"),
            ("the automated Karl Fischer coulometric titrator", "standardize using certified water standards", "check for drift rates below 5 micrograms per minute", "standardized"),
            ("the active pharmaceutical ingredient (API) crystallization tank", "seed with micronized crystals at 42 degrees Celsius", "cool at 0.5 degrees per minute ramp rate", "seeded"),
            ("the laboratory fume hood sash face velocity", "maintain above 0.5 meters per second", "certify with an automated hot-wire anemometer", "monitored"),
            ("the gas chromatography-mass spectrometry (GC-MS) column", "bake out overnight at 280 degrees Celsius", "tune using perfluorotributylamine (PFTBA)", "baked out"),
            ("the rotary vacuum paddle dryer cake", "sample under inert nitrogen blanket", "dry until residual solvent falls below 500 ppm", "sampled"),
            ("the analytical balance draft shield enclosure", "level using the internal optical spirit bubble", "calibrate using certified class E2 reference weights", "leveled"),
            ("the ultra-pure water polish cartridge", "rinse until resistivity reaches 18.2 megohm-cm", "replace when total organic carbon exceeds 500 ppb", "rinsed"),
            ("the thin layer chromatography (TLC) developing chamber", "saturate with solvent vapor for 30 minutes", "inspect under 254 nm ultraviolet light", "saturated")
        ],
        "operators": ["The analytical QC chemist", "The organic synthesis researcher", "The process development scientist", "The laboratory technician", "The quality assurance batch releaser"],
        "locations": ["inside the certified chemical fume hood", "in the API kilo-lab pilot plant", "at the analytical chromatography bench", "within the stability testing walk-in chamber"],
        "standards": ["European Pharmacopoeia (Ph. Eur.) monographs", "United States Pharmacopeia (USP <621>)", "ICH Q3A guideline on impurities in active substances", "Good Laboratory Practice (GLP) statutory standards"],
        "adverbs": ["analytically", "quantitatively", "precisely", "meticulously", "reproducibly"]
    },
    "tapi_it": {
        "items": [
            ("the Microsoft Entra ID privileged identity role", "protect with hardware FIDO2 multi-factor authentication", "audit monthly for dormant administrator accounts", "enforced"),
            ("the enterprise Azure virtual machine scale set", "provision across multiple availability zones", "scale automatically when CPU utilization exceeds 75%", "provisioned"),
            ("the next-generation firewall perimeter policy", "inspect encrypted TLS 1.3 traffic for malicious payloads", "block inbound SSH connections from foreign IP pools", "reconfigured"),
            ("the SAP S/4HANA enterprise database instance", "backup with point-in-time recovery logs", "failover seamlessly to the secondary disaster site", "migrated"),
            ("the Docker container Kubernetes cluster deployment", "isolate through Kubernetes network policies", "scan for critical CVE vulnerabilities before release", "scanned"),
            ("the Active Directory Group Policy Object (GPO)", "deploy to corporate workstations in staged rings", "enforce BitLocker 256-bit AES disk encryption", "deployed"),
            ("the ITIL Priority 1 critical incident ticket", "escalate to the senior engineering bridge within 15 minutes", "resolve within the four-hour customer SLA window", "escalated"),
            ("the enterprise Zero Trust endpoint security agent", "isolate compromised laptops from the local subnet", "update threat signatures every four hours", "isolated"),
            ("the virtual private network (VPN) gateway tunnel", "authenticate via corporate machine certificate", "terminate inactive remote sessions after 30 minutes", "authenticated"),
            ("the cloud infrastructure Terraform IaC template", "validate against security guardrails in the CI/CD pipeline", "commit to the protected main branch with peer approval", "validated")
        ],
        "operators": ["The cloud infrastructure architect", "The senior cybersecurity analyst", "The enterprise systems engineer", "The IT service desk specialist", "The DevOps platform engineer"],
        "locations": ["in the hybrid multi-cloud environment", "on the corporate Active Directory domain", "within the secure perimeter DMZ subnet", "at the global IT network operations center"],
        "standards": ["ISO/IEC 27001 information security standard", "NIST Cybersecurity Framework CSF 2.0", "CIS Benchmarks for hardened cloud platforms", "GDPR Article 32 technical security controls"],
        "adverbs": ["securely", "resiliently", "automatically", "promptly", "programmatically"]
    },
    "bidfood_pur": {
        "items": [
            ("the refrigerated container cold-chain data logger", "verify that core pulp temperature never exceeded -18 degrees Celsius", "download via USB interface before signing delivery notes", "verified"),
            ("the annual supplier master purchasing contract", "stipulate tiered volume rebate brackets and 60-day payment terms", "renegotiate prior to seasonal agricultural price fixing", "finalized"),
            ("the veterinary health import certificate (CHED-P)", "endorse by official state border veterinarians", "present to customs officers at the port of entry", "cleared"),
            ("the minimum order quantity (MOQ) pallet allocation", "optimize to minimize less-than-truckload (LTL) shipping surcharges", "confirm with the Dutch wholesale frozen food depot", "calculated"),
            ("the perishable fresh fish consignment lead time", "schedule for overnight transit to ensure 72-hour residual shelf life", "track in real time via GPS satellite telematics", "expedited"),
            ("the supplier quality non-conformance defect claim", "file within 24 hours of receiving thawed poultry cartons", "support with photographic evidence and core temperature logs", "submitted"),
            ("the eco-packaging transport film procurement order", "comply with the European Packaging and Packaging Waste Regulation (PPWR)", "ensure at least 35% post-consumer recycled polymer content", "ordered"),
            ("the commodity sunflower oil bulk contract", "hedge against international futures market fluctuations on Euronext", "settle through quarterly delivered forward contracts", "hedged"),
            ("the private label dairy co-packing agreement", "bind the manufacturer to strict recipe exclusivity and microbial limits", "audit annually against IFS Food safety standards", "ratified"),
            ("the distribution center warehouse cross-docking lane", "transfer perishable dairy pallets directly into outbound route vans", "clear within 45 minutes to preserve thermal integrity", "inspected")
        ],
        "operators": ["The senior procurement manager", "The wholesale category buyer", "The cold-chain logistics coordinator", "The incoming goods quality inspector", "The vendor relations specialist"],
        "locations": ["at the central Kralupy distribution hub", "in the cold storage cross-docking terminal", "at the border veterinary inspection post", "within the commercial purchasing office"],
        "standards": ["IFS Food Standard Version 8", "Incoterms 2020 international trade rules", "HACCP cold-chain temperature control regulations", "EU Regulation 178/2002 general food law"],
        "adverbs": ["promptly", "cost-effectively", "strictly", "consistently", "diligently"]
    },
    "bidfood_eng": {
        "items": [
            ("the two-stage industrial ammonia refrigeration compressor", "maintain suction pressure at 0.5 bar for spiral freezers", "overhaul shaft seals and oil separator filters annually", "overhauled"),
            ("the continuous cryogenic blast freezing tunnel", "drop food core temperatures from +65 to -18 degrees Celsius in 25 minutes", "defrost via hot ammonia gas injection twice per shift", "inspected"),
            ("the automated Clean-in-Place (CIP) caustic wash loop", "circulate 2% sodium hydroxide solution at 75 degrees Celsius", "flush with potable water until rinse water conductivity drops below 50 uS/cm", "sanitized"),
            ("the sanitary stainless steel pasteurizer flow diversion valve", "divert sub-temperature dairy liquids back to the raw balance tank", "test daily for automatic failsafe seat sealing", "tested"),
            ("the high-speed food packaging thermoformer line", "pull vacuum down to 5 mbar before nitrogen gas flushing", "synchronize modular conveyor belts with optical sensors", "synchronized"),
            ("the industrial steam boiler feedwater deaerator", "strip dissolved oxygen and carbon dioxide to prevent pipe corrosion", "dose with chemical oxygen scavenger and alkalinity builder", "calibrated"),
            ("the automated palletizing robotic cell safety interlock", "stop all axis motion instantly when the light curtain is broken", "reset manually only after physical area verification", "verified"),
            ("the compressed air desiccant refrigeration dryer", "maintain pressure dew point at minus 40 degrees Celsius", "purge coalescing oil mist filters every 2,000 running hours", "serviced"),
            ("the wastewater dissolved air flotation (DAF) separator", "skim coagulated fat, oil, and grease (FOG) into disposal hoppers", "dose polyaluminum chloride coagulant to clarify effluent", "monitored"),
            ("the ATEX-certified flour silo explosion relief vent", "relieve sudden overpressure safely to the building exterior", "inspect magnetic burst sensors and grounding straps monthly", "certified")
        ],
        "operators": ["The plant process engineer", "The industrial refrigeration technician", "The automation maintenance supervisor", "The food processing line operator", "The plant utilities engineer"],
        "locations": ["inside the central ammonia engine room", "along the automated food processing conveyor", "at the CIP sanitation chemical dosing station", "in the high-bay blast freezing warehouse"],
        "standards": ["EN 378 safety requirements for refrigerating systems", "IFS Food technical hygiene criteria", "EHEDG hygienic equipment design guidelines", "ATEX Directive 2014/34/EU for explosive atmospheres"],
        "adverbs": ["hygienically", "safely", "efficiently", "reliably", "automatically"]
    }
}

# -----------------------------------------------------------------------------
# DIVERSE QUESTION GENERATION BY LEVEL
# -----------------------------------------------------------------------------
def generate_diverse_a2_question(mod, q_idx, domain):
    qid = f"{mod['test_id']}-Q{q_idx+1}"
    target_k = KEY_PATTERN[q_idx % len(KEY_PATTERN)]
    bank = DOMAIN_BANKS[domain]
    
    item, action1, action2, part_v = bank["items"][q_idx % len(bank["items"])]
    operator = bank["operators"][q_idx % len(bank["operators"])]
    loc = bank["locations"][q_idx % len(bank["locations"])]
    adv = bank["adverbs"][q_idx % len(bank["adverbs"])]
    
    track = mod["workplace_track"]
    mod_num = int(mod["test_id"].split("-")[-1])
    
    # 10 completely distinct grammar questions per A2 test
    if q_idx == 0: # Modal verbs (must / have to)
        prompt = f"Before starting the shift, {operator.lower()} _____ {action1}."
        correct = "must"
        distractors = ["must to", "is must", "has must"]
        correct_exp = f"Modal 'must' is followed by the bare infinitive without 'to': 'must {action1.split()[0]}'."
        dist_exps = ["'must to' is ungrammatical; modals never take 'to'.", "'is must' is completely ungrammatical in English.", "'has must' is invalid verb phrasing."]
        cz_pt = "V angličtině se po způsobovém slovesu 'must' nikdy nepoužívá předložka 'to' (*must to* je hrubá chyba)."
        
    elif q_idx == 1: # Present Simple 3rd person singular -s
        prompt = f"Every morning, {operator.lower()} {adv} _____ {item} {loc}."
        v_base = action2.split()[0]
        v_3rd = v_base + "s" if not v_base.endswith(("s", "sh", "ch", "x", "o")) else v_base + "es"
        if v_base.endswith("y") and v_base[-2] not in "aeiou":
            v_3rd = v_base[:-1] + "ies"
        correct = v_3rd
        distractors = [v_base, v_base + "ing", "is " + v_base]
        correct_exp = f"Singular subject takes 3rd person singular Present Simple with '-s' ('{v_3rd}')."
        dist_exps = [f"Base form '{v_base}' lacks required 3rd person singular '-s'.", f"Participle '{v_base}ing' cannot act as finite verb without auxiliary.", f"'is {v_base}' is ungrammatical."]
        cz_pt = f"Ve 3. osobě jednotného čísla přítomného času prostého nezapomeňte na koncovku -s: '{v_3rd}'."
        
    elif q_idx == 2: # Preposition of Place
        prompt = f"The technician placed the diagnostic tool _____ the workbench {loc}."
        correct = "on"
        distractors = ["into", "under to", "between of"]
        correct_exp = "Preposition 'on' correctly denotes physical placement on a horizontal surface."
        dist_exps = ["'into' denotes motion entering inside an enclosed space.", "'under to' is an invalid double preposition.", "'between of' is ungrammatical; 'between' does not take 'of'."]
        cz_pt = "Čeština používá 'na stole' = 'on the workbench'. Dejte pozor na chybná spojení jako *between of*."
        
    elif q_idx == 3: # Past Simple with specific finished timestamp
        prompt = f"Yesterday during the handover, {operator.lower()} _____ {item}."
        v_past = part_v
        v_base = action1.split()[0]
        correct = v_past
        distractors = [v_base, "has " + v_past, "is " + v_base + "ing"]
        correct_exp = f"Specific past time adverbial 'yesterday' strictly requires Past Simple '{v_past}'."
        dist_exps = [f"Base form '{v_base}' lacks past tense inflection.", f"Present perfect 'has {v_past}' cannot accompany finished past time 'yesterday'.", "Present Continuous describes current actions, not yesterday's finished events."]
        cz_pt = "S příslovečným určením jako 'yesterday' se v angličtině striktně pojí minulý čas prostý (Past Simple), nikdy předpřítomný čas."
        
    elif q_idx == 4: # Quantifiers (some / any / much / many)
        prompt = f"Are there _____ spare gaskets left in the workshop storage cabinet?"
        correct = "any"
        distractors = ["some", "much", "an"]
        correct_exp = "'Any' is standard in questions inquiring about the existence or availability of items."
        dist_exps = ["'some' is typically reserved for affirmative statements or polite offers.", "'much' is only used with uncountable mass nouns, not plural 'gaskets'.", "'an' can only precede singular countable nouns beginning with a vowel sound."]
        cz_pt = "V běžných záporných větách a otázkách se pro 'nějaký / žádný' používá 'any', nikoli *some*."
        
    elif q_idx == 5: # Question formation with auxiliary (Do / Does / Did)
        prompt = f"_____ the maintenance technician inspect {item} every shift?"
        correct = "Does"
        distractors = ["Do", "Is", "Has"]
        correct_exp = "Singular 3rd person subject in Present Simple requires auxiliary 'Does'."
        dist_exps = ["'Do' is used for plural subjects (they, we, you) or 'I'.", "'Is' requires an '-ing' participle (Present Continuous), not a base verb.", "'Has' requires a past participle (Present Perfect)."]
        cz_pt = "V otázkách v přítomném čase se pro 3. osobu jednotného čísla používá pomocné sloveso 'Does': 'Does the technician inspect...?'."
        
    elif q_idx == 6: # Comparatives
        prompt = f"The newly calibrated unit runs significantly _____ than the older model."
        correct = "faster"
        distractors = ["more fast", "fastest", "as fast"]
        correct_exp = "One-syllable adjective 'fast' forms comparative with '-er': 'faster'."
        dist_exps = ["'more fast' is ungrammatical; short adjectives take '-er'.", "'fastest' is a superlative and requires 'the'.", "'as fast' requires 'as' ('as fast as'), not 'than'."]
        cz_pt = "Jednoslabičná přídavná jména tvoří 2. stupeň koncovkou -er (faster, cheaper), nikoli pomocí *more*."
        
    elif q_idx == 7: # Demonstratives (this, that, these, those)
        prompt = f"_____ new components on this table must be cataloged immediately."
        correct = "These"
        distractors = ["This", "That", "There"]
        correct_exp = "Plural noun 'components' located nearby requires plural demonstrative 'These'."
        dist_exps = ["'This' is singular and cannot modify plural 'components'.", "'That' is singular.", "'There' is an adverb of place or dummy pronoun, not a demonstrative determiner."]
        cz_pt = "Množné číslo pro věci blízko mluvčího je 'these' (tyto součástky), jednotné číslo je 'this' (tato součástka)."
        
    elif q_idx == 8: # Preposition of Motion
        prompt = f"The team transferred the heavy assembly _____ the testing bay."
        correct = "into"
        distractors = ["in to", "inside of", "onto to"]
        correct_exp = "'Into' expresses movement from the outside to the interior of a space."
        dist_exps = ["'in to' as two separate words is incorrect for directional movement.", "'inside of' is redundant and colloquial.", "'onto to' is an ungrammatical repetition."]
        cz_pt = "Směr dovnitř vyjadřuje předložka 'into' (přesunout do testovací haly = transferred into the bay)."
        
    else: # Polite requests (Could you please...)
        prompt = f"Could you please _____ the shift report before leaving today?"
        correct = "sign"
        distractors = ["to sign", "signing", "signed"]
        correct_exp = "Polite request with modal 'Could you please' is followed by the bare infinitive 'sign'."
        dist_exps = ["'to sign' is incorrect; modals do not take 'to'.", "Participle 'signing' cannot follow modal 'could'.", "Past tense 'signed' is ungrammatical after modal 'could'."]
        cz_pt = "Po zdvořilostní žádosti 'Could you please' následuje vždy základní tvar slovesa (bare infinitive) bez 'to'."

    opts = {target_k: correct}
    other_keys = [k for k in ["A", "B", "C", "D"] if k != target_k]
    exps = {"correct": correct_exp}
    for i, ok in enumerate(other_keys):
        opts[ok] = distractors[i]
        exps[f"wrong_{ok}"] = dist_exps[i]
        
    return make_q(qid, prompt, opts, target_k, exps, cz_pt, track)


def generate_diverse_b1_question(mod, q_idx, domain):
    qid = f"{mod['test_id']}-Q{q_idx+1}"
    target_k = KEY_PATTERN[q_idx % len(KEY_PATTERN)]
    bank = DOMAIN_BANKS[domain]
    
    item, action1, action2, part_v = bank["items"][q_idx % len(bank["items"])]
    operator = bank["operators"][q_idx % len(bank["operators"])]
    loc = bank["locations"][q_idx % len(bank["locations"])]
    adv = bank["adverbs"][q_idx % len(bank["adverbs"])]
    std = bank["standards"][q_idx % len(bank["standards"])]
    
    track = mod["workplace_track"]
    
    if q_idx == 0: # Past Simple vs Past Perfect (priority)
        prompt = f"Before the validation auditor arrived {loc}, {operator.lower()} noticed that {item} _____."
        correct = f"had been {part_v}"
        distractors = [f"was {part_v}", f"has been {part_v}", f"didn't {action1.split()[0]}"]
        correct_exp = f"Past Perfect Passive ('had been {part_v}') expresses an action completed prior to the past event 'arrived'."
        dist_exps = [f"Past Simple ('was {part_v}') fails to indicate precedence before past 'arrived'.", f"Present Perfect ('has been {part_v}') cannot anchor to a past narrative.", "Active negative is wrong in voice; technical equipment is acted upon passively."]
        cz_pt = "V angličtině vyžaduje děj předcházející jinému ději v minulosti předminulý čas (Past Perfect: 'had been...')."
        
    elif q_idx == 1: # First Conditional (If + present, will + base)
        prompt = f"If the operating parameter _____ above safe limits, the automated system immediately halts the cycle."
        v_base = action1.split()[0]
        correct = "rises"
        distractors = ["will rise", "would rise", "rose"]
        correct_exp = "First conditional if-clause requires Present Simple ('rises') for real operating conditions."
        dist_exps = ["Cannot use future modal 'will' inside the conditional if-clause.", "Cannot use 'would' in a real First Conditional.", "Past tense 'rose' creates an unreal conditional mismatched with present 'halts'."]
        cz_pt = "Zásadní pravidlo: v podmínkové větě po 'if' se nesmí použít 'will' (*If the parameter will rise* je hrubá chyba). Použijte přítomný čas: 'If the parameter rises'."
        
    elif q_idx == 2: # Time connectors: While vs During
        prompt = f"The maintenance specialist detected an irregular vibration _____ the equipment was running at maximum speed."
        correct = "while"
        distractors = ["during", "for", "since"]
        correct_exp = "'While' is a conjunction followed by a full finite clause ('the equipment was running')."
        dist_exps = ["'During' is a preposition and can only be followed by a noun phrase, never a clause with a verb.", "'For' expresses duration, not simultaneous background events.", "'Since' indicates a starting point in time or causation."]
        cz_pt = "Češi často pletou 'during' a 'while'. S celou větou se slovesem se pojí 'while' (while it was running), zatímco se samotným podstatným jménem se pojí 'during' (during the run)."
        
    elif q_idx == 3: # Passive voice with modals in SOPs
        prompt = f"According to {std}, {item} _____ at regular 500-hour operational intervals."
        v_base = action1.split()[0]
        correct = f"must be {part_v}"
        distractors = [f"must to be {part_v}", f"must {v_base}", f"are must {part_v}"]
        correct_exp = f"Passive with modal: 'must be {part_v}' correctly describes the technical maintenance requirement."
        dist_exps = ["'must to be' is ungrammatical; modal 'must' takes bare infinitive.", "Active voice is incorrect; equipment cannot service itself.", "'are must' is completely ungrammatical in English."]
        cz_pt = "Technické předpisy (SOP) vyžadují trpný rod se způsobovým slovesem: 'must be inspected' (musí být zkontrolováno)."
        
    elif q_idx == 4: # Present Perfect vs Past Simple (finished time)
        prompt = f"The engineering department _____ three comprehensive compliance audits since the beginning of this quarter."
        correct = "has conducted"
        distractors = ["conducted", "is conducting", "conducts"]
        correct_exp = "Time frame indicator 'since the beginning of this quarter' requires Present Perfect ('has conducted')."
        dist_exps = ["Past Simple cannot co-occur with 'since' connecting past to present.", "Present Continuous expresses action in progress, not completed tally.", "Present Simple expresses habitual routines, not accumulated achievements."]
        cz_pt = "Předložka 'since' (od té doby) striktně vyžaduje předpřítomný čas (Present Perfect: 'has conducted'), protože časové období pokračuje do přítomnosti."
        
    elif q_idx == 5: # Clauses of purpose: in order to / so that
        prompt = f"The parameters were recalibrated _____ the manufacturing line could achieve zero defect tolerance."
        correct = "so that"
        distractors = ["in order", "because of", "for to"]
        correct_exp = "'So that' is a conjunction of purpose followed by a subject and modal verb clause ('the line could achieve')."
        dist_exps = ["'in order' requires 'to' + infinitive or 'that' + clause.", "'because of' is followed by a noun phrase, not a clause with a finite verb.", "'for to' is completely ungrammatical in standard English."]
        cz_pt = "Účelová spojka 'so that' = aby (následovaná celou větou: 'so that the line could achieve')."
        
    elif q_idx == 6: # Phrasal verbs in technical contexts
        prompt = f"In the event of an unexpected pressure drop, the emergency system will _____ the main intake manifold."
        correct = "shut down"
        distractors = ["shut off to", "shutting down", "shut down of"]
        correct_exp = "Phrasal verb 'shut down' correctly means to halt or power off an operating mechanical system."
        dist_exps = ["'shut off to' is an ungrammatical combination.", "Participle 'shutting down' cannot follow future auxiliary 'will'.", "'shut down of' includes an unnecessary, ungrammatical preposition."]
        cz_pt = "Frázové sloveso 'shut down' (odstavit / vypnout zařízení). Po pomocném slovesu 'will' následuje základní tvar: 'will shut down'."
        
    elif q_idx == 7: # Relative pronouns (which / that / whose)
        prompt = f"The newly installed sensor, _____ measurement tolerance is within 0.01 mm, was imported from Germany."
        correct = "whose"
        distractors = ["which", "that", "of which"]
        correct_exp = "Possessive relative pronoun 'whose' correctly links the antecedent 'sensor' with its attribute 'measurement tolerance'."
        dist_exps = ["'which' cannot express possession without 'of'.", "'that' cannot be used in non-defining relative clauses set off by commas.", "'of which' would require different word order ('the measurement tolerance of which')."]
        cz_pt = "Přivlastňovací vztažné zájmeno 'whose' (jehož / jejíž tolerance) se v angličtině používá i pro neživé předměty a stroje."
        
    elif q_idx == 8: # Modals of deduction (must be / can't be / might be)
        prompt = f"The pressure gauge reads zero despite the compressor running, so the main seal _____ cracked."
        correct = "must be"
        distractors = ["must to be", "can to be", "is must"]
        correct_exp = "'Must be' expresses logical deduction based on clear physical evidence."
        dist_exps = ["'must to be' is ungrammatical.", "'can to be' is ungrammatical; modals never take 'to'.", "'is must' is invalid syntax."]
        cz_pt = "Logická dedukce (určitě je / musí být poškozeno): 'must be cracked'. Nikdy nepoužívejte *must to be*."
        
    else: # Unless vs If
        prompt = f"The production line cannot resume operation _____ the safety interlock circuit is fully reset."
        correct = "unless"
        distractors = ["if", "provided that", "as long as"]
        correct_exp = "'Unless' means 'if not' or 'except when', expressing the mandatory prerequisite for resumption."
        dist_exps = ["'if' would produce an illogical contradiction (cannot run IF reset).", "'provided that' creates the opposite, illogical meaning.", "'as long as' also creates an illogical condition."]
        cz_pt = "'Unless' znamená 'pokud ne' (if not). Po 'unless' už v anglické větě nenásleduje další zápor: 'unless the circuit is reset'."

    opts = {target_k: correct}
    other_keys = [k for k in ["A", "B", "C", "D"] if k != target_k]
    exps = {"correct": correct_exp}
    for i, ok in enumerate(other_keys):
        opts[ok] = distractors[i]
        exps[f"wrong_{ok}"] = dist_exps[i]
        
    return make_q(qid, prompt, opts, target_k, exps, cz_pt, track)


def generate_diverse_b2_question(mod, q_idx, domain):
    qid = f"{mod['test_id']}-Q{q_idx+1}"
    target_k = KEY_PATTERN[q_idx % len(KEY_PATTERN)]
    bank = DOMAIN_BANKS[domain]
    
    item, action1, action2, part_v = bank["items"][q_idx % len(bank["items"])]
    operator = bank["operators"][q_idx % len(bank["operators"])]
    loc = bank["locations"][q_idx % len(bank["locations"])]
    std = bank["standards"][q_idx % len(bank["standards"])]
    track = mod["workplace_track"]
    
    if q_idx == 0: # Inverted Third Conditional (Had + subject + past participle)
        prompt = f"_____ earlier during simulation, the catastrophic breakdown of {item} would have been avoided."
        correct = "Had the engineers detected the defect"
        distractors = ["If the engineers detected the defect", "Would the engineers have detected the defect", "Did the engineers detect the defect"]
        correct_exp = "Inverted Third Conditional 'Had the engineers detected...' correctly replaces 'If the engineers had detected...' in formal engineering discourse."
        dist_exps = ["'If the engineers detected' is Second Conditional (hypothetical present/future), incompatible with past 'would have been avoided'.", "'Would... have' cannot appear inside the conditional premise clause.", "'Did... detect' expresses a past question, not an unreal conditional condition."]
        cz_pt = "Ve formální technické angličtině se podmínka v minulosti často tvoří inverzí bez 'if': 'Had the engineers detected...' = 'Kdyby bývali inženýři zjistili...'. Do podmínky nikdy nepatří *would*."
        
    elif q_idx == 1: # Negative Inversion (Under no circumstances / Rarely)
        prompt = f"Under no circumstances _____ the secondary safety interlocks during live machine operation."
        correct = "should technicians bypass"
        distractors = ["technicians should bypass", "technicians must to bypass", "shall technicians to bypass"]
        correct_exp = "Negative phrase 'Under no circumstances' triggers subject-auxiliary inversion: 'should technicians bypass'."
        dist_exps = ["'technicians should bypass' lacks required subject-auxiliary inversion.", "'must to' is ungrammatical; modal 'must' does not take 'to'.", "'shall... to' is ungrammatical."]
        cz_pt = "Záporné úvodní fráze ('Under no circumstances', 'Rarely', 'Seldom') vyžadují převrácený slovosled (inverzi jako u otázky): 'Under no circumstances should technicians bypass...'."
        
    elif q_idx == 2: # Mixed Conditional (past cause, present result)
        prompt = f"If the preventative maintenance had been carried out properly last week, the system _____ erratic readings today."
        correct = "would not be showing"
        distractors = ["would not have shown", "will not show", "does not show"]
        correct_exp = "Mixed conditional: past unreal action ('had been carried out last week') with ongoing present result ('today') takes 'would not be showing'."
        dist_exps = ["'would not have shown' refers purely to past consequence, but adverbial 'today' anchors the result to the present.", "'will not show' is First Conditional, incompatible with past counterfactual condition.", "Indicative 'does not show' cannot express hypothetical consequence."]
        cz_pt = "Smíšený kondicionál (Mixed Conditional): minulá příčina spojená s přítomným následkem: 'If it had been done [minulost], it would not be showing [dnes]'."
        
    elif q_idx == 3: # Mandative Subjunctive in formal regulations
        prompt = f"Quality audit directives mandate that every facility _____ compliance with {std} without exception."
        correct = "demonstrate"
        distractors = ["demonstrates", "will demonstrate", "must to demonstrate"]
        correct_exp = "Mandative subjunctive after 'mandate that' requires the base verb form 'demonstrate' regardless of singular subject."
        dist_exps = ["Indicative 'demonstrates' with 3rd person -s violates mandative subjunctive syntax.", "Future 'will demonstrate' is incorrect after mandative 'mandate that'.", "'must to' is ungrammatical."]
        cz_pt = "Subjunktiv po formálních slovesech požadavku (mandate that, require that, insist that) vyžaduje základní tvar slovesa bez -s i u 3. osoby: 'mandate that every facility demonstrate'."
        
    elif q_idx == 4: # Participle clauses for conciseness
        prompt = f"_____ comprehensive non-destructive ultrasonic testing, the inspection team cleared {item} for immediate deployment."
        correct = "Having completed"
        distractors = ["After completed", "Have completed", "Being completed"]
        correct_exp = "Perfect active participle 'Having completed' correctly expresses an action finished prior to the main clause action 'cleared'."
        dist_exps = ["'After completed' is ungrammatical; 'after' requires an '-ing' participle or full clause.", "'Have completed' cannot act as an introductory participial phrase.", "'Being completed' is passive present, but the inspection team actively completed the testing."]
        cz_pt = "Předpřítomné participium (Having completed = poté, co dokončili) vyjadřuje předcházející děj před hlavní větou."
        
    elif q_idx == 5: # Concession clauses: Although vs In spite of / Notwithstanding
        prompt = f"_____ severe supply chain bottlenecks, the engineering team delivered the prototype on schedule."
        correct = "Notwithstanding"
        distractors = ["Although", "Even though", "Whereas"]
        correct_exp = "'Notwithstanding' is a formal preposition followed by a noun phrase ('severe supply chain bottlenecks')."
        dist_exps = ["'Although' is a conjunction and must be followed by a full clause with subject and verb.", "'Even though' requires a full clause.", "'Whereas' introduces a contrastive clause, not a prepositional phrase."]
        cz_pt = "'Notwithstanding' (navzdory / bez ohledu na) se pojí s podstatným jménem, zatímco spojky jako 'Although' a 'Even though' vyžadují celou větu se slovesem."
        
    elif q_idx == 6: # Complex passive reporting structures
        prompt = f"The failure rate of {item} is understood _____ by micro-fractures in the mounting alloy."
        correct = "to have been caused"
        distractors = ["to be caused", "having caused", "to cause"]
        correct_exp = "Perfect passive infinitive 'to have been caused' correctly attributes a past completed cause to a current condition."
        dist_exps = ["Present passive 'to be caused' fails to indicate past completion.", "Participle 'having caused' cannot follow passive reporting verb 'is understood'.", "Active infinitive 'to cause' is wrong in voice; failure rates do not cause themselves."]
        cz_pt = "Vazba 'is understood to have been caused' (má se za to, že bylo způsobeno) vyjadřuje minulý děj pomocí minulého infinitivu trpného."
        
    elif q_idx == 7: # Fronting with negative limiter: Only after
        prompt = f"Only after the second calibration cycle _____ the anomalous drift in sensor telemetry."
        correct = "did our technicians notice"
        distractors = ["our technicians noticed", "noticed our technicians", "have our technicians noticed"]
        correct_exp = "Limiting introductory phrase 'Only after...' triggers subject-auxiliary inversion with Past Simple: 'did our technicians notice'."
        dist_exps = ["'our technicians noticed' lacks the required subject-auxiliary inversion.", "'noticed our technicians' is archaic full inversion without auxiliary 'did'.", "Present perfect conflicts with the finished narrative event."]
        cz_pt = "Zdůrazňující úvodní vazba 'Only after...' vyžaduje inverzní slovosled s pomocným slovesem: 'Only after the cycle did technicians notice...'."
        
    elif q_idx == 8: # Epistemic stance & advanced modals
        prompt = f"Given the rigorous pre-flight inspections, the hydraulic failure _____ occurred without catastrophic external impact."
        correct = "cannot possibly have"
        distractors = ["must not have", "should not have", "may not have"]
        correct_exp = "'Cannot possibly have' expresses conclusive deduction of impossibility regarding a past event."
        dist_exps = ["'must not have' expresses deduction that something did not happen, but lacks impossibility nuance.", "'should not have' expresses unmet expectation or reproach, not impossibility.", "'may not have' expresses mere uncertainty, incompatible with 'conclusive'."]
        cz_pt = "Vyjádření naprosté nemožnosti v minulosti: 'cannot possibly have occurred' (rozhodně nemohlo dojít k...)."
        
    else: # Complex prepositional relative clause
        prompt = f"The international consortium signed an operational agreement, under the terms of _____ all patent rights remain protected."
        correct = "which"
        distractors = ["that", "whom", "what"]
        correct_exp = "Prepositional relative phrase 'under the terms of which' strictly takes 'which' when referring to an inanimate contract or agreement."
        dist_exps = ["'that' cannot follow a preposition in formal relative clauses.", "'whom' only refers to persons.", "'what' cannot function as a relative pronoun with an explicit antecedent."]
        cz_pt = "Po předložkách v rozvitých vztažných větách se pro věci a smlouvy používá výhradně 'which': 'under the terms of which' (podle jehož podmínek)."

    opts = {target_k: correct}
    other_keys = [k for k in ["A", "B", "C", "D"] if k != target_k]
    exps = {"correct": correct_exp}
    for i, ok in enumerate(other_keys):
        opts[ok] = distractors[i]
        exps[f"wrong_{ok}"] = dist_exps[i]
        
    return make_q(qid, prompt, opts, target_k, exps, cz_pt, track)


def generate_diverse_c1_question(mod, q_idx, domain):
    qid = f"{mod['test_id']}-Q{q_idx+1}"
    target_k = KEY_PATTERN[q_idx % len(KEY_PATTERN)]
    bank = DOMAIN_BANKS[domain]
    
    item, action1, action2, part_v = bank["items"][q_idx % len(bank["items"])]
    operator = bank["operators"][q_idx % len(bank["operators"])]
    std = bank["standards"][q_idx % len(bank["standards"])]
    track = mod["workplace_track"]
    
    if q_idx == 0: # Mandative Subjunctive in arbitration/executive mandates
        prompt = f"The international arbitral tribunal mandated that the respondent enterprise _____ full restitution for latent mechanical defaults."
        correct = "furnish"
        distractors = ["furnishes", "shall furnish", "must to furnish"]
        correct_exp = "High-register mandative subjunctive requires base form 'furnish' after 'mandated that'."
        dist_exps = ["Indicative 'furnishes' violates formal legal subjunctive syntax.", "'shall furnish' is indicative/modal, less standard than pure subjunctive in mandative clauses.", "'must to furnish' is completely ungrammatical in English."]
        cz_pt = "V mezinárodním právu a arbitrážních nálezech se po slovesech nařízení používá subjunktiv se základním tvarem: 'mandated that the respondent furnish'."
        
    elif q_idx == 1: # High-register negative inversion
        prompt = f"Seldom _____ witnessed such profound material degradation without prior ultrasonic acoustic warning."
        correct = "have our forensic metallurgists"
        distractors = ["our forensic metallurgists have", "did our forensic metallurgists had", "had our forensic metallurgists have"]
        correct_exp = "Negative adverb 'Seldom' triggers subject-auxiliary inversion: 'have our forensic metallurgists witnessed'."
        dist_exps = ["'our forensic metallurgists have' lacks required subject-auxiliary inversion.", "'did... had' is an ungrammatical double past.", "'had... have' is invalid auxiliary stacking."]
        cz_pt = "Záporné příslovce 'Seldom' na začátku věty vyžaduje přísnou inverzi pomocného slovesa a podmětu: 'Seldom have our experts witnessed...'."
        
    elif q_idx == 2: # Second Conditional Inversion (Were + subject + to + verb)
        prompt = f"_____ the sovereign ministry to repudiate the bilateral procurement treaty, international offset commitments would immediately trigger arbitration."
        correct = "Were"
        distractors = ["Had", "Should", "If were"]
        correct_exp = "Inverted Second Conditional with 'Were [subject] to [infinitive]' expresses formal hypothetical future contingency."
        dist_exps = ["'Had' forms a Third Conditional (past counterfactual), incompatible with 'to repudiate'.", "'Should' expresses tentative probability with bare infinitive, not 'to repudiate'.", "'If were' is redundant and ungrammatical."]
        cz_pt = "Inverze druhého kondicionálu v diplomatických smlouvách: 'Were the ministry to repudiate...' = 'Kdyby ministerstvo vypovědělo...'."
        
    elif q_idx == 3: # Deontic modality and indemnification
        prompt = f"Statutory covenants stipulate that intellectual property rights in respect of {item} _____ vested solely in the sovereign contracting authority."
        correct = "remain"
        distractors = ["remains", "will remain", "are remaining"]
        correct_exp = "Mandative subjunctive after 'stipulate that' takes base form 'remain'."
        dist_exps = ["Indicative 'remains' violates the subjunctive convention in statutory covenants.", "Future 'will remain' is non-standard in formal contract drafting.", "Continuous 'are remaining' cannot express permanent legal status."]
        cz_pt = "Smluvní ujednání (stipulate that) vyžadují základní tvar slovesa: 'stipulate that rights remain vested'."
        
    elif q_idx == 4: # Participial density in forensic inquiry
        prompt = f"_____ irreversible metallurgical micro-shear, the component fractured along the primary grain boundary."
        correct = "Having sustained"
        distractors = ["Sustaining", "Being sustained", "After sustained"]
        correct_exp = "Perfect active participle 'Having sustained' correctly expresses prior causal damage leading to subsequent fracture."
        dist_exps = ["Present participle 'Sustaining' implies simultaneous action rather than prior cause.", "Passive 'Being sustained' misassigns voice to the component.", "'After sustained' is ungrammatical syntax."]
        cz_pt = "Předpřítomné participium 'Having sustained' (utrpěvši nevratné poškození) vyjadřuje příčinu, která časově předcházela prasknutí."
        
    elif q_idx == 5: # Adversative concessions in governance
        prompt = f"The panel rejected the supplier's defense, _____ the catastrophic loss stemmed exclusively from improper operational maintenance."
        correct = "holding that"
        distractors = ["held that", "to hold that", "having held"]
        correct_exp = "Present participle 'holding that' functions as a supplementary clause expressing the legal rationale of the governing body."
        dist_exps = ["Past tense 'held that' cannot connect two main clauses without coordinating conjunction.", "Infinitive 'to hold that' implies purpose rather than contemporaneous legal holding.", "'having held' implies the holding occurred prior to the rejection."]
        cz_pt = "Právní formulace 'holding that...' (konstatujíc, že...) se v anglických soudních a arbitrážních nálezech používá pro odůvodnění rozhodnutí."
        
    elif q_idx == 6: # Counterfactual conditional synthesis
        prompt = f"Had timely notification of latent defect been served, compensatory damages _____ legally recoverable under Swiss federal law."
        correct = "would have been"
        distractors = ["would be", "had been", "will be"]
        correct_exp = "Third Conditional consequence clause requires 'would have been' to match past counterfactual premise 'Had notification been served'."
        dist_exps = ["'would be' refers to present result, but recovery relates to past arbitral award.", "'had been' is past perfect indicative, not a modal conditional consequence.", "'will be' is future indicative, completely incompatible with past counterfactual condition."]
        cz_pt = "Dokončený děj v minulém kondicionálu (Third Conditional): 'Had it been served, damages would have been recoverable'."
        
    elif q_idx == 7: # Fronting of prepositional phrase with inversion
        prompt = f"Foremost among the tribunal's findings _____ the persistent failure of senior management to enforce standard operating procedures."
        correct = "was"
        distractors = ["were", "has been", "did"]
        correct_exp = "Fronted prepositional phrase triggers subject-verb inversion; singular subject 'failure' requires singular verb 'was'."
        dist_exps = ["'were' incorrectly agrees with plural 'findings', but the real postposed subject is singular 'failure'.", "'has been' conflicts with the completed past narrative of the inquiry.", "'did' is an auxiliary that cannot function as a copula."]
        cz_pt = "Pozor na shodu podmětu s přísudkem při inverzi: 'Foremost among findings was the failure...' — podmět je jednotné číslo 'failure', proto sloveso musí být 'was' (nikoli *were*)."
        
    elif q_idx == 8: # Restrictive covenant formulas
        prompt = f"The multinational joint venture established a binding dispute mechanism, pursuant _____ all technical conflicts must be referred to ICC Paris."
        correct = "to which"
        distractors = ["of which", "for which", "in where"]
        correct_exp = "Formal legal phrase 'pursuant to' requires 'to which' when modifying the mechanism."
        dist_exps = ["'pursuant of' is incorrect legal English; 'pursuant' strictly takes 'to'.", "'for which' alters the meaning from legal conformance to purpose.", "'in where' is ungrammatical syntax."]
        cz_pt = "Právní vazba 'pursuant to which' (v souladu s nímž / na jehož základě) je ustálená formule mezinárodních smluv."
        
    else: # Executive strategic persuasion
        prompt = f"Unless the corporate steering committee _____ comprehensive capital reallocation by Q4, institutional market share will irreversibly erode."
        correct = "authorizes"
        distractors = ["will authorize", "would authorize", "shall to authorize"]
        correct_exp = "Conditional clause with 'Unless' requires Present Simple ('authorizes') in high-register executive projections."
        dist_exps = ["Future modal 'will' is prohibited inside the conditional 'Unless' clause.", "'would' creates an ungrammatical hypothetical mismatch with predictive 'will erode'.", "'shall to' is ungrammatical; modal 'shall' does not take 'to'."]
        cz_pt = "I na nejvyšší manažerské úrovni platí základní pravidlo: po spojce 'Unless' se nesmí použít 'will' (*Unless the committee will authorize*). Použijte přítomný čas: 'Unless the committee authorizes'."

    opts = {target_k: correct}
    other_keys = [k for k in ["A", "B", "C", "D"] if k != target_k]
    exps = {"correct": correct_exp}
    for i, ok in enumerate(other_keys):
        opts[ok] = distractors[i]
        exps[f"wrong_{ok}"] = dist_exps[i]
        
    return make_q(qid, prompt, opts, target_k, exps, cz_pt, track)


# -----------------------------------------------------------------------------
# MASTER QUESTION GENERATOR FOR ANY MODULE
# -----------------------------------------------------------------------------
def generate_module_questions(mod, domain):
    tid = mod["test_id"]
    
    # 1. If bespoke handcrafted questions exist for this module, use them!
    if tid in BESPOKE_MODULES:
        questions = []
        for q_data in BESPOKE_MODULES[tid]:
            qid, prompt, opts_dict, correct_key, exps_dict, cz_note, track = q_data
            q_obj = make_q(qid, prompt, opts_dict, correct_key, exps_dict, cz_note, track)
            questions.append(q_obj)
        return questions

    # 2. Otherwise generate 10 diverse, non-repetitive questions based on level
    lvl = mod["level"]
    questions = []
    for q_idx in range(10):
        if lvl == "A2":
            q = generate_diverse_a2_question(mod, q_idx, domain)
        elif lvl == "B1":
            q = generate_diverse_b1_question(mod, q_idx, domain)
        elif lvl == "B2":
            q = generate_diverse_b2_question(mod, q_idx, domain)
        else: # C1
            q = generate_diverse_c1_question(mod, q_idx, domain)
        questions.append(q)
        
    return questions
