import os
import json

def generate_32_slides_html():
    out_path = r"C:\tmp\00-Mycat\Engineering\Automotive_Engineering_Presentation.html"

    # Define all 32 slides data:
    slides_data = [
        # SLIDE 1
        {
            "num": 1,
            "title": "From CAD Concept to Platform Leadership",
            "cat": "AUTOMOTIVE ENGINEERING MASTERY • 32-SLIDE RETROSPECTIVE",
            "time": "00:00 - 01:00",
            "type": "title"
        },
        # SLIDE 2
        {
            "num": 2,
            "title": "The Four Horizons of Automotive Responsibility",
            "cat": "CAREER EVOLUTION & SCOPE OF LEADERSHIP",
            "time": "01:00 - 02:00",
            "type": "horizons"
        },
        # SLIDE 3
        {
            "num": 3,
            "title": "Horizon 1 Deep-Dive: The CAD Designer Era",
            "cat": "GEOMETRY CREATION, PARAMETRICS & 2D RELEASE",
            "time": "02:00 - 03:00",
            "type": "cards_3",
            "col1": ("PARAMETRIC 3D SOLID & SURFACING", [("Parametric Feature Trees", "Building associative models in CATIA V4/V5 & NX capturing design intent."), ("Class-A to Class-B Offsets", "Translating studio clay scans into structural inner pressings with draft angles."), ("Master Section Development", "Cutting parametric cross-sections across A/B pillars and sills for spot-weld flange access.")]),
            "col2": ("PACKAGING & KINEMATICS", [("Kinematic Clearance Sweeps", "Dynamic sweeps of wheel jounce/rebound (+100/-80 mm), steering lock & snow chains."), ("SAE J826 H-Point Manikin", "Positioning 95th percentile male / 5th percentile female to establish SgRP & heel coordinates."), ("Vision Envelopes (SAE J941)", "Mapping driver eye ellipses to ensure regulatory direct and mirror field-of-view.")]),
            "col3": ("2D DETAILING & GD&T RELEASE", [("ASME Y14.5 & ISO 1101", "Creating unambiguous manufacturing drawings with Datum Reference Frames (DRFs)."), ("3-2-1 Locating Principle", "Constraining all 6 spatial degrees of freedom with primary, secondary, and tertiary datums."), ("Volkswagen RPS System", "Integrating standardized coordinate hole/pad target conventions across stamping assemblies.")])
        },
        # SLIDE 4
        {
            "num": 4,
            "title": "Horizon 2 Deep-Dive: The Project Engineer Era",
            "cat": "CROSS-FUNCTIONAL INTEGRATION, DFMEA & VIRTUAL CAE",
            "time": "03:00 - 04:00",
            "type": "cards_3",
            "col1": ("SUBSYSTEM OWNERSHIP", [("Cross-Functional Leadership", "Leading technical integration across BIW, Closures, Chassis subframes, and Exterior trim."), ("Interface Boundary Management", "Protecting physical and kinematic interfaces between Body, Closures, and Powertrain."), ("Supplier DFM Reviews", "Leading on-site feasibility reviews with Tier-1 stamping and injection mould tooling specialists.")]),
            "col2": ("DFMEA & ROBUSTNESS", [("Parameter Diagrams (P-Diagrams)", "Mapping signal inputs, control factors, and noise factors (thermal soak, aging, tolerances)."), ("Ford FMEA Handbook v4.2", "Enforcing strict Severity discipline: any failure mode with Severity >= 8 mandates redesign."), ("Special Characteristics Cascade", "Designating Critical Characteristics (∇ CC) for safety and Significant Characteristics (SC) for fit.")]),
            "col3": ("VIRTUAL CAE COORDINATION", [("Structural Rigidity (FEA)", "Aligning BIW torsional stiffness (18-28 kNm/°) and bending stiffness with vehicle dynamicists."), ("Dynamic Modal Decoupling", "Tuning body natural frequencies (>38-42 Hz) to decouple from engine idle boom (25-30 Hz)."), ("Crashworthiness (LS-DYNA)", "Interpreting explicit dynamic crash pulses, progressive rail folding, and survival cell integrity.")])
        },
        # SLIDE 5
        {
            "num": 5,
            "title": "Horizons 3 & 4: Project & Engineering Management",
            "cat": "PROGRAM GATEWAYS, MULTI-MILLION TOOLING & APQP GOVERNANCE",
            "time": "04:00 - 05:00",
            "type": "cards_2",
            "col1": ("HORIZON 3: PROJECT MANAGER", "Timing, Tooling Capital & Execution", [("OEM Gateway Governance", "Guiding vehicle programs through Ford GPDS (FDJ, VP, TT, PP, MP1) and VW PEP (DKM, VFF, PVS, SOP) gateways."), ("Tooling Capital Commitment", "Managing multimillion-pound hard tooling commitments; approving die construction at design freeze."), ("Prototype Fleet Delivery", "Orchestrating mule vehicles, Verification Prototypes (VP), crash test sleds, and extreme-weather test fleets."), ("Root-Cause Problem Solving", "Leading rapid issue containment and root-cause resolution using 8D methodologies and A3 reports.")]),
            "col2": ("HORIZON 4: ENGINEERING MANAGER", "Strategy, Organizational Quality & Mentorship", [("Platform Resource Strategy", "Allocating departmental engineering headcount and budgets across concurrent global vehicle architectures."), ("APQP & PSW Legal Sign-off", "Technical authority signing off on Design Verification Plans & Reports (DVP&R) and Part Submission Warrants (PSW)."), ("Architectural Migration to EV", "Steering engineering teams through the paradigm shift from ICE platforms to dedicated MEB electric skateboards."), ("Talent Mentorship & AI Tools", "Cultivating holistic engineering capability and driving adoption of generative AI topology optimization and surrogate CAE.")])
        },
        # SLIDE 6
        {
            "num": 6,
            "title": "The CAD Design Evolution: 1960s Drawing Boards to Generative AI",
            "cat": "HISTORICAL PROGRESSION OF AUTOMOTIVE DIGITAL DESIGN TOOLS",
            "time": "05:00 - 06:00",
            "type": "timeline"
        },
        # SLIDE 7
        {
            "num": 7,
            "title": "The CAD Paradigm Shift: 2D Drafting Tables to 3D Parametric Solids",
            "cat": "COMPARING ENGINEERING WORKFLOWS, DATA INTEGRITY & MANUFACTURING LINKAGES",
            "time": "06:00 - 07:00",
            "type": "comp_table",
            "rows": [
                ("GEOMETRIC DEFINITION", "Manual 2D Drafting / Early 2D CAD", "Independent 2D projections (plan, elevation, section). High risk of dimensional discrepancies between views when changes occurred.", "3D Parametric Solids (CATIA / NX)", "Single unified 3D solid model. 2D drawing views are live associative projections that automatically update when model changes."),
                ("DESIGN INTENT & MODIFICATIONS", "Manual 2D Drafting / Early 2D CAD", "No history or parametric constraints. Altering a wall thickness required manually erasing and redrawing every affected view.", "3D Parametric Solids (CATIA / NX)", "Explicit feature history tree (sketches, extrusions, fillets, drafts). Modifying a base parameter propagates instantly through child features."),
                ("INTERFERENCE & PACKAGING", "Manual 2D Drafting / Early 2D CAD", "Interference detected manually or discovered physically during prototype build bucks, costing weeks and thousands of pounds.", "3D Parametric Solids (CATIA / NX)", "Automated digital interference and clash detection across complete vehicle assemblies with live clearance measurements."),
                ("MASS & KINEMATIC SIMULATION", "Manual 2D Drafting / Early 2D CAD", "Mass and center-of-gravity estimated by hand calculation. Kinematics checked via physical cardboard overlays.", "3D Parametric Solids (CATIA / NX)", "Instantaneous calculation of mass, volume, and moments of inertia. Dynamic 3D simulation of suspension sweeps and closure arcs.")
            ]
        },
        # SLIDE 8
        {
            "num": 8,
            "title": "The Digital Mockup (DMU) & Packaging Revolution",
            "cat": "VIRTUAL VEHICLE ASSEMBLY, ERGONOMIC MANIKINS & KINEMATIC SWEEPS",
            "time": "07:00 - 08:00",
            "type": "cards_3",
            "col1": ("VIRTUAL FULL VEHICLE ASSEMBLY", [("Unified Global Coordinates", "Every component loaded into absolute vehicle zero space (X=front wheel center, Y=centerline, Z=rocker)."), ("Automated Nightly Clash Scans", "Batch collision algorithms scanning thousands of assemblies overnight to report hard, soft, and clearance clashing."), ("Elimination of Wooden Bucks", "Completely replacing expensive physical styling and packaging bucks with real-time digital DMU reviews.")]),
            "col2": ("OCCUPANT ERGONOMICS & VISIBILITY", [("Digital SAE J826 H-Point", "Virtual manikins representing 95th percentile male and 5th percentile female seated in digital CAD interiors."), ("Field-of-View Mapping (SAE J941)", "Projecting driver eye ellipses to verify regulatory forward sightlines through windshields and mirror blind spots."), ("Reach & Ingress Envelopes", "Evaluating steering wheel reach, pedal clearances, and head clearance during door ingress/egress.")]),
            "col3": ("DYNAMIC KINEMATIC SIMULATION", [("Suspension Travel Sweeps", "Dynamic multi-body sweeps verifying tire clearance across full jounce (+100 mm), rebound (-80 mm), and lock."), ("Closure Hinge & Latch Arcs", "Simulating door swing kinematics, check-arm detents, and latch catch engagement arcs in 3D virtual space."), ("Flexible Line Routing", "Simulating dynamic flex lines for brake hoses and wiring harnesses under continuous steering articulation.")])
        },
        # SLIDE 9
        {
            "num": 9,
            "title": "The Modern CAE & AI Frontier: Topology Optimization to Generative Design",
            "cat": "TRANSITIONING FROM MANUAL ITERATIVE CAD TO AI-DRIVEN GENERATIVE SYNTHESIS",
            "time": "08:00 - 09:00",
            "type": "cards_3",
            "col1": ("MANUAL PART OPTIMIZATION", [("Step 1: Baseline FEA", "Apply static loads and identify low-stress material zones in CAD."), ("Step 2: Manual CAD Removal", "Engineer manually cuts holes and fillets out of solid model in CAD."), ("Step 3: Remesh & Rerun", "Rerun FEA to check stiffness targets; repeated iteratively over weeks.")]),
            "col2": ("GENERATIVE DESIGN & TOPOLOGY", [("Boundary Conditions Only", "Define packaging design space, keep-out clearance zones, and multi-axis loads."), ("Algorithmic Material Growth", "Solver automatically removes non-contributing material, synthesizing organic load paths."), ("Mass & Stiffness Optimized", "Delivers 20-30% mass reduction with 10x faster turnaround than manual remodeling.")]),
            "col3": ("SURROGATE AI CRASH & TEXT-TO-CAD", [("Surrogate Crash Models", "Deep neural networks trained on historical LS-DYNA runs predicting crash pulses in milliseconds."), ("Text/Picture-to-CAD", "Emerging AI models converting descriptive requirements into parameterized 3D geometry."), ("Automated DFMEA Synthesis", "Ingesting warranty databases to automatically populate failure modes and controls.")])
        },
        # SLIDE 10
        {
            "num": 10,
            "title": "Ford European Small Car Foundations: BE91 (Fiesta) & BE146 (Ka)",
            "cat": "HIGH-VOLUME B & SUB-B SEGMENT ARCHITECTURE, SHEET METAL OPTIMIZATION & PACKAGING",
            "time": "09:00 - 10:00",
            "type": "cards_2",
            "col1": ("BE91 • FORD FIESTA (MK4)", "B-Segment High-Volume Hatchback", [("Aggressive Sheet Metal Consolidation", "Consolidating stamped inner structural panels to reduce overall piece count and assembly robot welds."), ("Stamping Blank Nesting Optimization", "Optimizing coil blank profiles to achieve >80% material utilization, minimizing scrap on high-speed press lines."), ("Front Crash Box Integration", "Integrating progressive deformation trigger indentations directly into the front longitudinal side rails."), ("High-Volume Manufacturing Efficiency", "Engineered for 60-second takt times across multiple European assembly plants (Dagenham, Cologne, Valencia).")]),
            "col2": ("BE146 • FORD KA", "Sub-B Segment Iconic City Car", [("Shared Platform Architecture", "Re-engineered the proven BE91 underbody floorpan while wrapping it in revolutionary 'New Edge' styling curves."), ("Tight Under-Hood Packaging", "Inventive packaging of cooling packs, steering columns, and suspension strut towers within a shortened front overhang."), ("Consolidated Bumper Substructures", "Pioneered integrated front and rear protective bumper structures, lowering low-speed repair costs."), ("Urban Agility & Mass Reduction", "Delivered agile urban handling while meeting European crash safety standards at minimum vehicle curb weight.")])
        },
        # SLIDE 11
        {
            "num": 11,
            "title": "Ford Emerging Markets & Dynamics: C195 (Ikon) & C170 (Focus Mk1)",
            "cat": "FROM RUGGED 3-BOX EMERGING MARKET PACKAGING TO MULTI-LINK HANDLING BENCHMARK",
            "time": "10:00 - 11:00",
            "type": "cards_2",
            "col1": ("C195 • FORD IKON", "Emerging Market 3-Box Saloon", [("Rugged Saloon Packaging", "Engineered a distinctive 3-box notchback boot on the B-car platform tailored for emerging markets (India, South Africa, S. America)."), ("Structural Boot Reinforcement", "Heavily reinforced rear parcel shelf, D-pillar gussets, and luggage floor to withstand severe road vibration and heavy payloads."), ("Rough-Road Chassis Upgrades", "Strengthened suspension subframe attachment hardpoints and increased ground clearance for punishing terrain."), ("Dust & Monsoon Sealing", "Engineered enhanced double-lip door and boot weatherstripping to prevent severe dust ingress and monsoon water intrusion.")]),
            "col2": ("C170 • FORD FOCUS (MK1)", "Benchmark Global Compact Platform", [("Control Blade Multi-Link Rear Suspension", "Pioneered the revolutionary multi-link rear suspension decoupled into trailing control blade and lateral links."), ("Zero Cabin Luggage Intrusion", "Packaged full multi-link kinematics within an ultra-low-profile subframe, maximizing square boot volume."), ("Torsional Rigidity Leadership", "High-stiffness Body-in-White isolating suspension bushing loads from passenger cabin resonance."), ("Redefining Compact Car Dynamics", "Set the global automotive benchmark for ride comfort, steering precision, and passive rear-wheel toe compliance.")])
        },
        # SLIDE 12
        {
            "num": 12,
            "title": "Ford Global D-Segment: CD132 (Mondeo Mk3) & EUCD Joint Platform",
            "cat": "BORON STEEL NODES, LASER BRAZING & MULTI-BRAND CROSS-OEM PLATFORM ARCHITECTURE",
            "time": "11:00 - 12:00",
            "type": "cards_2",
            "col1": ("CD132 • FORD MONDEO (MK3)", "D-Segment Executive Saloon & Estate", [("Pioneering Boron Steel Nodes", "Early introduction of ultra-high-strength boron steel in structural B-pillars and rocker nodes for side impact safety."), ("Laser-Brazed Roof Seams", "Pioneered automated laser brazing on the roof ditch, replacing black rubber mouldings with an aerodynamic seamless joint."), ("Dual-Subframe NVH Isolation", "Engineered fully isolated front and rear chassis subframes with hydraulic bushings to eliminate road harshness."), ("Deep-Draw Side Aperture Stampings", "Overcoming extreme draw depths and thinning limits on single-piece side outer body stampings.")]),
            "col2": ("EUCD • JOINT MULTI-BRAND ARCHITECTURE", "Shared Across Ford, Volvo & Land Rover", [("Multi-OEM Architectural Harmonization", "Joint platform engineering uniting Mondeo Mk4, S-MAX, Galaxy, Volvo S80/V70/XC60, and Freelander 2."), ("World-Class Safety Cage Integration", "Harmonizing Volvo's legendary passenger cell crash standards with Ford's high-speed volume manufacturing lines."), ("Deformable Crash Subframe", "Engineered lower subframe deformation kinematics to absorb kinetic energy and meet strict pedestrian impact criteria."), ("Transverse Powertrain Flexibility", "Accommodated 4-, 5-, and 6-cylinder transverse engines, dual-clutch transmissions, and AWD drivelines.")])
        },
        # SLIDE 13
        {
            "num": 13,
            "title": "Ford Global B-Car & SUV: B2E (Fiesta Mk6) & B2XX (EcoSport)",
            "cat": "HIGH-VOLUME GLOBAL PLATFORM FLEXIBILITY, RAISED SUV PACKAGING & TAILGATE ENGINEERING",
            "time": "12:00 - 13:00",
            "type": "cards_2",
            "col1": ("B2E • GLOBAL FIESTA (MK6)", "Global High-Volume B-Segment", [("Global Manufacturing Footprint", "Engineered for synchronized manufacturing across Europe, Asia, South America, and North America."), ("Hot-Stamped Boron Safety Cell", "Extensive hot-formed boron steel A-pillars, B-pillars, and rocker reinforcements achieving top safety ratings."), ("Hydroformed Front Subframe", "Hydroformed tubular front suspension subframe maximizing structural stiffness while cutting mass."), ("Electric Power Steering Packaging", "Pioneered early column-drive EPAS integration with optimized driver feedback.")]),
            "col2": ("B2XX • FORD ECOSPORT", "Compact Crossover / SUV Architecture", [("High Ground Clearance Packaging", "Raised ride height to >200 mm ground clearance, requiring revised suspension geometry and drive shaft angles."), ("Side-Hinged Tailgate Engineering", "Designed a unique side-hinged rear door carrying a full-size external spare wheel (>25 kg payload)."), ("Severe D-Pillar Structural Reinforcement", "Engineered heavy structural reinforcement brackets and forged hinges to eliminate door sag over rough terrain."), ("Dynamic Latch Fatigue & Sealing", "Multi-axis proving ground fatigue analysis to prevent latch rattle and water ingress under severe torsional racking.")])
        },
        # SLIDE 14
        {
            "num": 14,
            "title": "Volkswagen Modular Transverse Matrix: MQB-27 (A0) & MQB-37 (A1/A2)",
            "cat": "THE BAUKASTEN REVOLUTION: STANDARDIZED HARDPOINTS & UNPRECEDENTED GLOBAL SCALE",
            "time": "13:00 - 14:00",
            "type": "cards_2",
            "col1": ("MQB-27 (MQB A0)", "Subcompact Modular Platform (Polo / T-Cross)", [("Democratizing High-Tech Safety", "Integrated over 30% hot-formed boron steel into entry-level subcompacts, achieving 5-star Euro NCAP ratings."), ("RPS Datum System Standardization", "Full integration of Volkswagen's Referenzpunkt-System datum targets across multi-brand stamping plants."), ("Modular Cross-Car Beam", "Shared lightweight dashboard cross-car structure accommodating modular steering and HVAC units."), ("High Commonality Across Group", "Shared underbody components across VW Polo, T-Cross, SEAT Ibiza/Arona, and Škoda Fabia.")]),
            "col2": ("MQB-37 (MQB A1/A2)", "Core Global Platform (Golf / Tiguan / Passat)", [("The 'Fixed' Dimension", "Standardized uniform distance from pedal box to front wheel centerline across all vehicle lines."), ("Standardized 12° Engine Inclination", "Uniform engine tilt angles and exhaust routing allowed identical subframes across petrol, diesel, and hybrid."), ("Infinite Variable Dimensions", "Complete flexibility in wheelbase, track width, overhangs, and seating heights on identical framing bucks."), ("Industrial Efficiency Benchmark", "Reduced engineering hours by >30% while delivering unprecedented group manufacturing profitability.")])
        },
        # SLIDE 15
        {
            "num": 15,
            "title": "Volkswagen Electrification & Commercial: MEB Platform & T7 Multivan",
            "cat": "DEDICATED EV SKATEBOARD ARCHITECTURE & COMMERCIAL MIGRATION ONTO MODULAR CAR PLATFORMS",
            "time": "14:00 - 15:00",
            "type": "cards_2",
            "col1": ("MEB • ELECTRIC SKATEBOARD PLATFORM", "Dedicated BEV Matrix (ID.3 / ID.4 / ID. Buzz)", [("Structural Battery Pack Enclosure", "The high-voltage battery housing functions as an active underbody shear plate, increasing torsional stiffness past 30,000 Nm/°."), ("Multi-Cell Aluminium Crash Sills", "Massive extruded rocker sections engineered to absorb side pole impact before battery module intrusion."), ("Absence of Front ICE Load Path", "Front crumple zones redesigned with progressive rail accordion folding without reliance on engine block deceleration."), ("Flat Floor Interior Packaging", "Relocated HVAC unit forward into cowl area, creating D-segment interior cabin volume within a C-segment exterior footprint.")]),
            "col2": ("T7 MULTIVAN • MODULAR MPV", "Commercial Vehicle Migration to MQB", [("Migrating Van onto MQB Architecture", "Migrated Volkswagen's iconic commercial line onto passenger-car MQB foundations with car-like ride and handling."), ("Modular Floor Rail System", "Engineered flat floor rail tracks tested to extreme dynamic seatbelt pull loads (ECE R14) for sliding, removable seats."), ("Dual A-Pillar Structural Design", "Engineered dual A-pillar packaging with front quarter glass to maximize forward vision while ensuring roof crush strength."), ("Plug-In Hybrid Packaging", "Integrated high-voltage hybrid battery beneath the flat floor without encroaching on passenger cabin volume.")])
        },
        # SLIDE 16
        {
            "num": 16,
            "title": "Master Design-to-Manufacture Flowchart: Complete Automotive Lifecycle",
            "cat": "END-TO-END 12-STAGE INDUSTRIALIZATION ROADMAP FROM STYLING CONCEPT TO SERIAL SOP",
            "time": "15:00 - 16:30",
            "type": "flowchart_master"
        },
        # SLIDE 17
        {
            "num": 17,
            "title": "Design-to-Manufacture: Upstream Virtual Engineering",
            "cat": "PHASE 1: CONCEPT, PACKAGING, DFM, DFMEA & VIRTUAL CAE TO DESIGN FREEZE (FDJ / DKM)",
            "time": "16:30 - 17:30",
            "type": "flowchart_upstream"
        },
        # SLIDE 18
        {
            "num": 18,
            "title": "Design-to-Manufacture: Downstream Physical Industrialization",
            "cat": "PHASE 2: HARD TOOLING BUILD, TOOLING TRYOUT (TT), CAPABILITY STUDIES & PPAP / PSW SIGN-OFF",
            "time": "17:30 - 18:30",
            "type": "flowchart_downstream"
        },
        # SLIDE 19
        {
            "num": 19,
            "title": "Process 1: Initial 3D Design & Hardpoint Packaging",
            "cat": "PROCESS 1 OF 8 • PACKAGING & GEOMETRY ARCHITECTURE",
            "time": "18:30 - 19:30",
            "type": "cards_3",
            "col1": ("HARDPOINTS & ARCHITECTURE", [("Vehicle Coordinates", "Establishing absolute zero origins, front/rear wheel centers, cowl point, and ground clearance angles."), ("SAE J826 H-Point", "Positioning 95th percentile male / 5th percentile female manikins to define SgRP and heel point."), ("Vision & Glazing", "SAE J941 driver eye ellipse mapping ensuring regulatory vision through windshield and mirrors.")]),
            "col2": ("SURFACE FEASIBILITY (CLASS A TO B/C)", [("Offset Feasibility", "Translating styling clay scans into Class-B structural inners and Class-C non-visible brackets."), ("Flanging & Radii", "Modifying razor-sharp studio styling creases (<0.5 mm) to manufacturable stamping radii (>1.5 mm)."), ("Master Sections", "Cutting parametric cross-sections across pillars, sills, and headers to secure spot-weld flange access.")]),
            "col3": ("KINEMATIC DYNAMIC ENVELOPES", [("Suspension Sweeps", "Dynamic 3D swept volumes across full jounce (+100 mm), rebound (-80 mm), and steering lock."), ("Closure Kinematics", "Door and tailgate swing arcs with inclined hinge axes for natural gravity-assisted closure."), ("Weatherstrip Sealing", "Ensuring uniform 30-40% continuous seal compression around door apertures to stop wind noise.")])
        },
        # SLIDE 20
        {
            "num": 20,
            "title": "Process 2: Design for Manufacture (DFM) & Assembly (DFA)",
            "cat": "PROCESS 2 OF 8 • MANUFACTURING & ASSEMBLY FEASIBILITY",
            "time": "19:30 - 20:30",
            "type": "cards_3",
            "col1": ("SHEET METAL STAMPING DFM", [("Formability Limit (FLD)", "Assessing major vs. minor principal strain to eliminate tearing and wrinkling in die draws."), ("Minimum Punch Radii", "Enforcing internal punch radii >= 1.5t for mild steel, and >= 2.5-3.0t for advanced high-strength steels."), ("Springback Compensation", "Reverse-compensating tooling surfaces in CAD/CAM to counteract severe elastic recovery in AHSS.")]),
            "col2": ("INJECTION MOULDING DFM", [("Nominal Wall Thickness", "Maintaining uniform 2.5-3.0 mm walls on trims to avoid differential shrinkage and warpage."), ("Rib-to-Wall Ratios", "Limiting rib base thickness to 50-60% of adjacent wall (trib <= 0.6t) to eliminate sink marks."), ("Draft Angle Standards", "0.5°-1.0° on polished tools; minimum 1.5° per 0.025 mm texture grain depth to prevent scuffing.")]),
            "col3": ("DESIGN FOR ASSEMBLY (DFA)", [("Spot-Weld Flange Access", "Ensuring minimum 16-18 mm flange width for 16 mm robotic weld gun electrode tips."), ("Mistake-Proofing (Poka-Yoke)", "Asymmetrical mounting tabs preventing components from being installed inverted on the line."), ("Fastener Radial Clearance", "Minimum 35 mm clearance around bolt axes for multi-spindle automated nutrunners.")])
        },
        # SLIDE 21
        {
            "num": 21,
            "title": "Process 3: DFMEA & Robustness Linkages",
            "cat": "PROCESS 3 OF 8 • RISK MITIGATION & QUALITY ROBUSTNESS",
            "time": "20:30 - 21:30",
            "type": "cards_3",
            "col1": ("PARAMETER DIAGRAM (P-DIAGRAM)", [("Signal Input", "Driver command or system trigger (e.g., 40 N pull force on exterior door handle)."), ("Control Factors", "Design parameters: latch spring rate, cable stiffness, pivot mechanical advantage, alloy temper."), ("Noise Factors", "Uncontrollable disturbances: piece-to-piece tolerances, thermal extremes (-40°C to +85°C), seal icing, customer abuse.")]),
            "col2": ("RISK EVALUATION & FORD PHILOSOPHY", [("Severity (S 1-10)", "Ratings 9-10 indicate regulatory safety non-compliance. S >= 8 mandates redesign regardless of RPN."), ("Occurrence (O 1-10)", "Assesses failure mechanism probability based on design maturity and historical warranty."), ("Detection (D 1-10)", "Evaluates capability of DVP&R virtual simulations and physical rig tests to catch defects prior to freeze.")]),
            "col3": ("SPECIAL CHARACTERISTICS CASCADE", [("Critical Characteristics (∇ CC)", "Features affecting vehicle safety or regulatory compliance. Mandates ∇ symbol on CAD, drawings, and Control Plans."), ("Significant Characteristics (SC)", "Key features driving customer satisfaction, fit, flush, and major assembly interfaces."), ("PFMEA & Control Plan Link", "Every ∇ CC cascades directly to Process FMEA, poka-yoke gauging, and Cpk >= 1.67 statistical controls.")])
        },
        # SLIDE 22
        {
            "num": 22,
            "title": "Process 4: 2D Detailing & GD&T Architecture",
            "cat": "PROCESS 4 OF 8 • GEOMETRIC TOLERANCING ARCHITECTURE",
            "time": "21:30 - 22:30",
            "type": "cards_3",
            "col1": ("THE 3-2-1 LOCATING PRINCIPLE", [("Datum Reference Frame (DRF)", "Constraining all 6 spatial degrees of freedom (3 translations Tx, Ty, Tz and 3 rotations Rx, Ry, Rz)."), ("Primary Datum A (3 Points)", "Establishes the fundamental spatial plane; eliminates pitch, roll, and perpendicular translation."), ("Secondary Datum B & Tertiary C", "Datum B (2 points) constrains yaw and in-plane shift; Datum C (1 point) locks final stop.")]),
            "col2": ("VOLKSWAGEN RPS SYSTEM", [("Referenzpunkt-System", "VW's standardized coordinate datum targeting system applied across MQB, MEB, and commercial vehicles."), ("RPS Surface Pads (RPS-F)", "Precision-milled local pads on stamped panels functioning as repeatable CMM contact targets."), ("RPS 2-Way & 4-Way Holes", "Standardized round and slotted tooling holes (RPS-H) locating sub-assemblies in robotic welding bucks.")]),
            "col3": ("GEOMETRIC CONTROLS IN BIW", [("Profile of a Surface (|∩|)", "The universal geometric control for complex 3D stamped sheet metal and Class-A exterior skins."), ("True Position (⨁)", "Locating fastener clearance holes, suspension subframe attachment points, and hinge pins."), ("Maximum Material Condition (MMC)", "Utilizing bonus tolerances on clearance holes as hole size departs from minimum MMC boundary.")])
        },
        # SLIDE 23
        {
            "num": 23,
            "title": "Process 5: 1D Tolerance Stacks & 3D Variation Analysis",
            "cat": "PROCESS 5 OF 8 • DIMENSIONAL ENGINEERING & VARIATION SIMULATION",
            "time": "22:30 - 23:30",
            "type": "cards_3",
            "col1": ("1D TOLERANCE METHODS", [("Worst-Case Arithmetic (Twc)", "Twc = Σ |ti|. Assumes all parts simultaneously reach extreme dimensional limits. Overly conservative for mass production."), ("Root Sum of Squares (RSS)", "Trss = √(Σ ti²). Gaussian statistical model assuming independent normal distributions; ideal for high-volume lines (>200k/yr)."), ("Bender's Factor Correction", "Applying 1.3-1.5x multiplier to RSS to account for mean tooling wear and process drift over production lifetime.")]),
            "col2": ("3D MONTE CARLO VSA", [("Kinematic Simulation", "Running 5,000-10,000 virtual vehicle builds in VisVSA / 3DCS, modeling 6-DOF part variation and assembly sequences."), ("Exterior Gap & Flush", "Predicting hood-to-fender (3.5 ± 0.8 mm), door-to-door (4.0 ± 0.7 mm), and headlamp-to-bumper fitment."), ("Pareto Contribution Analysis", "Identifying the 'vital few' variables driving >70% of variation to target tooling investment precisely where it matters.")]),
            "col3": ("THERMAL EXPANSION DYNAMICS", [("Thermal Range (ΔT)", "Modeling structural expansion across -40°C arctic soak to +85°C high-ambient desert solar loading."), ("Material Mismatch (ΔL)", "Calculating expansion differentials between aluminium closures (α ≈ 23x10⁻⁶/K), steel BIW (α ≈ 12x10⁻⁶/K), and composites."), ("Weatherstrip Load Retention", "Verifying door seal compression remains within 30-40% across thermal extremes to prevent water leaks and wind hiss.")])
        },
        # SLIDE 24
        {
            "num": 24,
            "title": "Process 6: Finite Element Analysis (FEA) — Rigidity & NVH",
            "cat": "PROCESS 6 OF 8 • STRUCTURAL SIMULATION & ACOUSTICS",
            "time": "23:30 - 24:30",
            "type": "cards_3",
            "col1": ("STATIC RIGIDITY TARGETS", [("Torsional Rigidity (kNm/°)", "Targeting 18-28 kNm/° on ICE platforms; >30 kNm/° on MEB skateboard EV architectures."), ("Bending Stiffness (N/mm)", "Vertical rocker deflection control ensuring door latch alignment and preventing body sag under load."), ("Local Mount Stiffness", "Ensuring >10,000 N/mm at strut towers and subframe mounting nodes to deliver crisp steering feedback.")]),
            "col2": ("DYNAMIC NVH & MODAL FREQUENCIES", [("First Torsion Mode (>38-42 Hz)", "Decoupling BIW resonant torsion from engine 4-cylinder idle firing excitation (25-30 Hz at 750-900 RPM)."), ("First Bending Mode (>42-46 Hz)", "Decoupling vehicle body bending modes from suspension wheel-hop inputs (12-15 Hz)."), ("Acoustic Boom Prevention", "Preventing low-frequency cabin resonance that causes passenger ear pressure and fatigue.")]),
            "col3": ("FATIGUE & DURABILITY LIFE", [("Road Load Data (WFT)", "Multi-axis load time histories from Belgian cobblestones, pothole strikes, and curb impacts."), ("Miner's Rule Cumulative Damage", "Σ (ni / Ni) <= 1.0. Stress-life (S-N) and strain-life (ε-N) durability analysis across 150,000+ miles."), ("Spot-Weld & Adhesive Fatigue", "Evaluating nugget shear stresses; implementing continuous weld-bonding adhesive to cut stress peaks by 40%.")])
        },
        # SLIDE 25
        {
            "num": 25,
            "title": "Process 7: Structural Crashworthiness & EV Safety",
            "cat": "PROCESS 7 OF 8 • NON-LINEAR CRASH SIMULATION & SAFETY",
            "time": "24:30 - 25:30",
            "type": "cards_3",
            "col1": ("FRONTAL CRASH LOAD PATHS", [("Three Decoupled Paths", "Upper shotgun rail (25% energy), main longitudinal rail (55%), lower subframe extension (20%)."), ("Progressive Rail Collapse", "Hexagonal high-strength steel crash boxes with stamped trigger indentations creating uniform accordion crush."), ("Engine Block Kinematics", "Directing ICE block downward beneath passenger floorpan to prevent firewall penetration.")]),
            "col2": ("BORON SAFETY CELL (22MnB5)", [("Ultra-High-Strength Boron", "Hot-stamped at 900°C and quenched to martensitic microstructure with Rm > 1500 MPa."), ("Tailored Tempering B-Pillar", "1500 MPa martensite at upper B-pillar prevents head strike; 600-800 MPa ductile base creates controlled plastic hinge."), ("Boron Cross-Car Beams", "High-strength floor cross-members transferring side barrier impact across the underbody tunnel.")]),
            "col3": ("MEB EV BATTERY PROTECTION", [("Multi-Cell Aluminium Sills", "Massive extruded rocker sections engineered to absorb side pole impact before battery module intrusion."), ("Structural Battery Housing", "Heavy aluminium baseplate and internal web frame acting as an impenetrable survival cell."), ("Pyrofuse High-Voltage Disconnect", "Automatic pyrotechnic disconnect isolating 400V/800V battery pack within 2 milliseconds of impact.")])
        },
        # SLIDE 26
        {
            "num": 26,
            "title": "Process 8: APQP & Production Launch Governance",
            "cat": "PROCESS 8 OF 8 • LAUNCH GOVERNANCE & STATISTICAL QUALITY",
            "time": "25:30 - 26:30",
            "type": "cards_3",
            "col1": ("APQP 5-PHASE LIFECYCLE", [("Phase 1: Concept & Planning", "Translating Voice of Customer into target vehicle specifications and initial BOM."), ("Phase 2: Product Design", "CAD release, DFM/DFA, DFMEA, GD&T drawings, and DVP&R virtual verification."), ("Phase 3: Process Design", "Stamping die cutting, injection mould build, PFMEA, Control Plans, and packaging.")]),
            "col2": ("OEM GATEWAY SYNCHRONIZATION", [("Concept Freeze", "Ford Concept Approval (CA) ↔ VW Projektvereinbarung / Konzeptfreigabe."), ("Design Freeze (Hard Tooling)", "Ford Final Data Judgement (FDJ) ↔ VW Datenkontrollmodell (DKM). Hard tooling released."), ("Tooling Tryout (TT)", "First parts stamped from production dies ↔ VW Vorserie (VFF). Dimensional checks.")]),
            "col3": ("PPAP 18 ELEMENTS & CAPABILITY", [("Measurement Systems (MSA)", "Gage R&R < 10% mandatory for Critical Characteristics; 10-30% conditionally acceptable."), ("Process Capability (Cpk)", "Mandated Cpk >= 1.67 (5-sigma quality) for Critical Characteristics (∇ CC); Cpk >= 1.33 for standard."), ("Part Submission Warrant (PSW)", "The formal signed executive declaration certifying production readiness at rate with zero defects.")])
        },
        # SLIDE 27
        {
            "num": 27,
            "title": "Technical Case Study 1: The Multi-Link Packaging Triumph of Ford C170 Focus",
            "cat": "TECHNICAL CASE STUDY 1 • CHASSIS PACKAGING & VEHICLE DYNAMICS",
            "time": "26:30 - 27:15",
            "type": "cards_3",
            "col1": ("THE COMPACT CLASS CONUNDRUM", [("Twist-Beam Compromise", "Compact C-segment cars universally used cheap twist-beam rear axles, compromising ride quality and cornering stability."), ("The Multi-Link Barrier", "Traditional multi-link independent rear suspensions were considered too costly and intruded severely into boot luggage space."), ("Ford Dynamic Challenge", "Ford leadership demanded class-leading vehicle dynamics ('fun-to-drive') without compromising family luggage utility.")]),
            "col2": ("THE CONTROL BLADE SOLUTION", [("Decoupled Kinematics", "Longitudinal trailing arm (the flat stamped 'Control Blade') decoupled from short lateral camber/toe links."), ("Braking Compliance", "The thin vertical blade absorbed road longitudinal impact and braking torque while flexing laterally without binding."), ("Passive Rear-Wheel Steer", "Under lateral cornering forces, the elastomeric bushings induced passive toe-in, stabilizing the rear axle at speed.")]),
            "col3": ("ARCHITECTURAL IMPACT", [("Zero Boot Intrusion", "Packaged entire multi-link assembly within a compact subframe beneath the floor, preserving an immense square boot."), ("Class Benchmark for 20 Years", "The Control Blade architecture set the industry standard, copied by competitors across Europe and Asia."), ("Proof of Packaging Mastery", "Demonstrated that innovative geometric packaging delivers premium dynamics within high-volume cost constraints.")])
        },
        # SLIDE 28
        {
            "num": 28,
            "title": "Technical Case Study 2: Structural Safety Harmonization of Ford EUCD",
            "cat": "TECHNICAL CASE STUDY 2 • MULTI-BRAND PLATFORM HARMONIZATION",
            "time": "27:15 - 28:00",
            "type": "cards_3",
            "col1": ("THE MULTI-OEM CHALLENGE", [("Three Distinct Brands", "Developing a single shared platform for Ford (Mondeo/S-MAX), Volvo (S80/V70/XC60), and Land Rover (Freelander 2)."), ("Conflicting Philosophies", "Reconciling Volvo's unyielding passenger cell safety expectations with Ford's high-speed assembly line takt times."), ("Diverse Body Styles", "Accommodating saloons, estates, 7-seat MPVs, and all-wheel-drive SUVs across divergent curb weights.")]),
            "col2": ("THE STRUCTURAL SOLUTION", [("Multi-Tier Front Crash Rails", "Three decoupled front load paths absorbing energy at 64 km/h offset impacts while controlling deceleration pulses."), ("Deformable Crash Subframe", "Lower front subframe engineered to shear away and tilt the engine downward beneath the floor in severe impacts."), ("Hot-Stamped Boron Safety Cell", "Extensive hot-formed boron steel B-pillars and floor cross-members linking left and right rocker sills.")]),
            "col3": ("MANUFACTURING & MARKET SUCCESS", [("5-Star Euro NCAP Across Lines", "Every derivative vehicle on EUCD achieved 5-star Euro NCAP ratings, setting new executive segment safety benchmarks."), (">60% Underbody Commonality", "Shared over 60% of structural underbody pressings, unlocking massive global tooling and purchasing economies."), ("Proof of Cross-OEM Synergy", "Demonstrated that divergent engineering cultures can unite to produce world-class architectures.")])
        },
        # SLIDE 29
        {
            "num": 29,
            "title": "Technical Case Study 3: The Skateboard Revolution — MQB ICE vs. MEB EV",
            "cat": "TECHNICAL CASE STUDY 3 • ARCHITECTURAL COMPARISON",
            "time": "28:00 - 28:45",
            "type": "comp_table",
            "rows": [
                ("CRASH ENERGY MANAGEMENT", "Conventional ICE Architecture (MQB-37)", "Heavy engine block acts as rigid mass in frontal crash; front rails fold around engine while directing it downward beneath passenger floorpan.", "Dedicated EV Skateboard (MEB Platform)", "No rigid engine block allows longer progressive front rail crush; but high-voltage battery demands zero side-pole intrusion via extruded aluminium sills."),
                ("TORSIONAL RIGIDITY CONTRIBUTION", "Conventional ICE Architecture (MQB-37)", "Rigidity achieved via central floor exhaust tunnel, boxed rocker sills, and rear parcel shelf structure (typical: 20,000 - 24,000 Nm/°).", "Dedicated EV Skateboard (MEB Platform)", "Aluminium battery housing acts as massive underbody structural shear plate, increasing torsional rigidity past 30,000 Nm/° (+25% over ICE)."),
                ("CABIN SPACE & PACKAGING", "Conventional ICE Architecture (MQB-37)", "High dash cowl and central floor tunnel dividing passenger footwells; engine and cooling pack dictate front axle position.", "Dedicated EV Skateboard (MEB Platform)", "Completely flat cabin floor with zero exhaust tunnel; HVAC relocated forward into bulkhead; D-segment interior space in C-segment footprint.")
            ]
        },
        # SLIDE 30
        {
            "num": 30,
            "title": "Engineering Leadership & Capital Asset Governance",
            "cat": "EXECUTIVE MANAGEMENT & INNOVATION FRONTIER",
            "time": "28:45 - 29:15",
            "type": "cards_3",
            "col1": ("TOOLING ASSET GOVERNANCE", [("Managing 'Point of No Return'", "Rigorous technical reviews prior to Tooling Kick-Off (FDJ/DKM) preventing catastrophic late tooling rework."), ("High-Stakes Stamping Dies", "A single transfer die set for a side aperture outer costs $4M-$6M; requires zero tolerance for geometric errors."), ("Supplier Run-at-Rate Audits", "Leading on-site audits at supplier press shops to verify cycle takt time and dimensional stability.")]),
            "col2": ("PEOPLE & TEAM LEADERSHIP", [("Cross-Functional Harmony", "Uniting styling designers, body engineers, CAE simulation specialists, and assembly plant directors."), ("Mentoring Future Leaders", "Transforming junior CAD operators into holistic systems engineers who understand cost, tooling, and physics."), ("Codifying Lessons Learned", "Ensuring manufacturing launch defects and warranty feedback are written into future platform design guidelines.")]),
            "col3": ("STRATEGIC PLATFORM SCALABILITY", [("Cross-Brand Architecture", "Leveraging modular toolkits to maximize commonality across volume, commercial, and premium brands."), ("Bridging CAD to Serial SOP", "Maintaining relentless technical rigor from initial 3D sketch all the way to legal PSW signature."), ("Embracing Digital Disruption", "Leading engineering organizations into the future of electrified skateboards and generative AI CAE.")])
        },
        # SLIDE 31
        {
            "num": 31,
            "title": "Core Takeaways: Four Tenets of World-Class Automotive Engineering",
            "cat": "SYNTHESIS & EXECUTIVE REFLECTION",
            "time": "29:15 - 29:45",
            "type": "takeaways"
        },
        # SLIDE 32
        {
            "num": 32,
            "title": "Questions & Technical Discussion",
            "cat": "COLLABORATIVE EXCHANGE & DISCUSSION",
            "time": "29:45 - 30:00+",
            "type": "qa"
        }
    ]

    print(f"Total defined slides: {len(slides_data)}")

if __name__ == "__main__":
    generate_32_slides_html()
