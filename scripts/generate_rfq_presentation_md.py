import os

def generate_rfq_presentation_md():
    output_path = r"C:\tmp\00-Mycat\Engineering\Ford_CD4_Pedal_Pack_RFQ_Presentation_Content.md"
    print(f"Generating Ford RFQ Pack Presentation Content at: {output_path}...")

    # We will write the comprehensive markdown file directly
    content = """# Executive Slide Deck Content: Ford CD4 Pedal Box RFQ Package
## Complete Engineering Analysis, File Inventory & Supplier Execution Roadmap
### Vehicle Programs: Ford CD4.1 & CD4.2 (Mondeo, S-MAX, Galaxy, Edge) • PMT 3 Chassis Core Engineering

---

## Executive Summary & RFQ Package Overview

This document provides a slide-by-slide presentation deck that thoroughly breaks down the **Ford Motor Company Request for Quotation (RFQ) Pack** located at `C:\\tmp\\00-Mycat\\Engineering\\PEDAL-PACK`. 

The RFQ represents a formal commercial and technical sourcing package issued by **Ford Chassis Core Engineering (Merkenich / Cologne, Germany)** for the design, development, validation, and serial production of the **Clutch Pedal Box Assembly (LHD & RHD variants)** across the global **CD4 vehicle platform (CD4.1 and CD4.2)**.

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                        FORD CD4 PEDAL-PACK RFQ ARCHITECTURE                            │
├──────────────────────────┬─────────────────────────────────────────────────────────────┤
│ 1. CAD PACKAGING (33 STPs)│ 33 STEP models defining the full driver footwell DMU:       │
│                          │ Dash bulkhead, steering column kinematics, carpet, NVH,     │
│                          │ HVAC housing, wiring, crash envelope, foot zones, BOT switch│
├──────────────────────────┼─────────────────────────────────────────────────────────────┤
│ 2. CLUTCH PEDAL          │ Core statement of work and engineering standards:           │
│    ATTACHMENTS (10 Files)│ • Base Document ESOW (v20) - Master contractual scope       │
│                          │ • Attachment 9.0 (ESOW-PBOX-FD) - Specific pedal box rules  │
│                          │ • ES-PB (060602_ES_PB) - 66-page master DVP testing spec    │
│                          │ • BR-1119 (Clearance & ECE R35 layout standard)             │
│                          │ • BR-1127 (Dash deflection & pedal box stiffness standard)  │
│                          │ • CY-0002 (Pedal travel & effort curve standard)            │
│                          │ • SCCAF (Special Characteristics Alignment per FAP03-111)   │
│                          │ • crs_sim_data (Panther 2.0L Diesel hydraulic simulation)   │
│                          │ • 6G9T-11A152-AA & CAE Chassis Specific Attachment v7.7     │
├──────────────────────────┼─────────────────────────────────────────────────────────────┤
│ 3. GENERAL CORPORATE     │ Ford global procedural and compliance standards:           │
│    ATTACHMENTS (12 Files)│ • Att 01a (CAD C3PNG / Teamcenter Enterprise data release)  │
│                          │ • Att 01b (CAE Integration SOW & simulation requirements)   │
│                          │ • Att 02 (Failure Mode Avoidance / DFMEA v4.2 / P-Diagrams) │
│                          │ • Att 03 (Environmental / IMDS / WSS-M99P9999-A1 / RRR)     │
│                          │ • Att 04 (Global Regulatory Compliance & Type Approval)     │
│                          │ • Att 05 (Craftsmanship, Gap & Flush, Tactile Quality)      │
│                          │ • Att 06 (Design Feasibility Commitment Form 06)            │
│                          │ • Att 07 (Materials Engineering & WSS Specifications)       │
│                          │ • Att 08 (Web-Based Data Management & GSDB / Covisint)      │
│                          │ • Att 09 (Component Homologation & E-Marking)               │
│                          │ • Att 10 (Ford CyberAssurance SOW for Supplier IT/OT)       │
│                          │ • Directive E-108 (Global Parts Trademarks & Ford Oval)     │
├──────────────────────────┼─────────────────────────────────────────────────────────────┤
│ 4. COMMERCIAL CONTACTS   │ Ford Merkenich Chassis Core contacts:                       │
│    (Contact-Request docx)│ • Christina Kallas (Chassis Core Engineer)                  │
│                          │ • Steffen Schoenfuss (Chassis Core Supervisor)              │
│                          │ • Stefanie Reinert (Commercial Buyer)                       │
└──────────────────────────┴─────────────────────────────────────────────────────────────┘
```

---

## Master 20-Slide Presentation Structure

| Slide # | Slide Title | Module / Category | Target Time |
| :---: | :--- | :--- | :---: |
| **01** | Executive Title & Program Introduction | Executive Overview | 00:00 - 01:30 |
| **02** | RFQ Package Architecture: The 4 Core Information Pillars | Package Structure | 01:30 - 03:00 |
| **03** | Vehicle Program Scope: Ford CD4.1 & CD4.2 Architectures | Vehicle Platform | 03:00 - 04:30 |
| **04** | Subsystem Architecture: The Hydraulic Clutch Actuation Chain | Technical Integration | 04:30 - 06:00 |
| **05** | Master Contract: Base Document ESOW v20 Scope of Work | SOW Governance | 06:00 - 08:00 |
| **06** | Specific Pedal Box Deliverables: Attachment 9.0 (ESOW-PBOX-FD) | Component SOW | 08:00 - 09:30 |
| **07** | Master Engineering Testing Specification: ES-PB (060602_ES_PB) | DVP&R & Testing | 09:30 - 11:30 |
| **08** | Kinematics & Pedal Travel Standard: Ford CY-0002 | Operating Curves | 11:30 - 13:00 |
| **09** | Packaging & Clearance Envelopes Standard: Ford BR-1119 | DMU & Clearance | 13:00 - 14:30 |
| **10** | Structural Rigidity & Dash Deflection Standard: Ford BR-1127 | Deflection & NVH | 14:30 - 16:00 |
| **11** | Passive Safety & Crash Breakaway Mechanism | Crashworthiness | 16:00 - 17:30 |
| **12** | Quality & Special Characteristics Governance: SCCAF (FAP03-111) | Quality & Control Plans | 17:30 - 19:00 |
| **13** | 3D CAD DMU Packaging Environment: Primary Structural Interfaces | CAD Environment | 19:00 - 20:30 |
| **14** | Footwell Ergonomics & Secondary Trim Packaging Environment | Trim & Clearances | 20:30 - 22:00 |
| **15** | Electrical Subsystem Integration: Bottom-of-Travel (BOT) Switch | Electrical Controls | 22:00 - 23:30 |
| **16** | Corporate Engineering Attachments: CAD, CAE, FMA & Craftsmanship | Corporate SOW | 23:30 - 25:00 |
| **17** | Corporate Compliance Standards: Feasibility, Materials & Cyber | Homologation & Trademarks | 25:00 - 26:30 |
| **18** | Hydraulic Actuation Simulation: Panther 2.0L Diesel Case Study | CAE & Actuation | 26:30 - 28:00 |
| **19** | Supplier Launch Roadmap: Ford GPDS Gateways & Milestones | Gateway Execution | 28:00 - 29:30 |
| **20** | Quotation Checklist, Cost BOM & Technical Risk Assessment | Sourcing Summary | 29:30 - 30:00+ |

---

## Detailed Slide-by-Slide Content & Speaker Narration

### Slide 01: Executive Title & Program Introduction

* **Category:** Executive Overview • Slide 01 / 20
* **Target Timing:** 00:00 - 01:30
* **Visual Layout:** Premium obsidian/slate layout with dual Ford and Tier-1 supplier banner, vehicle platform callout badge (CD4.1 / CD4.2), and high-level commodity description card.
* **Core Slide Content:**
  * **Commodity Under Sourcing:** Clutch Pedal Box Assembly (LHD & RHD variants, manual transmission).
  * **Vehicle Program:** Ford CD4 Global Architecture (CD4.1 Mondeo/Fusion MCA & CD4.2 S-MAX, Galaxy, Edge).
  * **Issuing Entity:** Ford Motor Company, Chassis Core Engineering (Merkenich Technical Center, Cologne, Germany).
  * **Key Contacts:** Christina Kallas (Chassis Core Engineer), Steffen Schoenfuss (Chassis Core Supervisor), Stefanie Reinert (Commercial Buyer).
  * **Commercial Purpose:** Request for Information (RFI) / Request for Quotation (RFQ) for full-service Tier-1 design, virtual CAE validation, prototype delivery, hard tooling build, and Job 1 + 90 days serial launch support.
* **Technical Deep-Dive Callout:**
  > *The pedal box is a Class-A regulatory safety commodity. In modern vehicle architecture, it represents the critical ergonomic interface between driver intent and vehicle deceleration/propulsion, while functioning as a mandatory passive safety structure during high-speed frontal crash deceleration.*
* **Spoken Presenter Script (Speaker Notes):**
  > *"Good morning, team. Today we are conducting an exhaustive technical walkthrough of the Ford Motor Company RFQ package for the CD4 Clutch Pedal Box Module, located in our engineering repository. This sourcing pack was released by Ford Chassis Core Engineering out of the Merkenich Technical Center in Cologne, Germany. It encompasses both Left-Hand Drive and Right-Hand Drive pedal box variants for the CD4.1 and CD4.2 vehicle lines—which include the Ford Mondeo, S-MAX, Galaxy, and Edge. As a Tier-1 supplier, we are being asked to provide full-service engineering: from CATIA V5 CAD styling feasibility, kinematic over-center spring design, and explicit LS-DYNA crash simulation, all the way to production tooling construction, Cpk qualification, and Job 1 launch containment. Over the next thirty minutes, we will dissect every folder, standard, spreadsheet, and 3D CAD environment model contained in this pack so our cross-functional team can construct a winning technical and commercial proposal."*

---

### Slide 02: RFQ Package Architecture: The 4 Core Information Pillars

* **Category:** Package Structure • Slide 02 / 20
* **Target Timing:** 01:30 - 03:00
* **Visual Layout:** 4-column structured card architecture showing the primary folders: `CAD/`, `Clutch Pedal attachments/`, `General Attachments/`, and `Commercial Contacts`.
* **Core Slide Content:**
  * **Pillar 1: 3D CAD Packaging Repository (`CAD/`):** 33 native STEP models (~540 MB total) defining the complete spatial packaging volume in the driver footwell. Covers sheet metal bulkheads, steering columns, HVAC cases, carpet compression models, and crash deformation envelopes.
  * **Pillar 2: Commodity Technical Specifications (`Clutch Pedal attachments/`):** 10 critical documents including the Base ESOW, Attachment 9.0, the 66-page `ES_PB` test specification, Ford standards `BR-1119`, `BR-1127`, `CY-0002`, the SCCAF control plan alignment sheet, and Panther diesel hydraulic simulation data.
  * **Pillar 3: Ford Global Corporate Attachments (`General Attachments/`):** 12 mandatory governance documents governing C3PNG CAD release, CAE modeling guidelines, Failure Mode Avoidance (FMA/DFMEA v4.2), Environmental IMDS compliance, Craftsmanship, Materials, Homologation, Cybersecurity, and Trademark Directive E-108.
  * **Pillar 4: Commercial Terms & Communication (`Contact-Request docx`):** Official RFI contact channels, commercial buyer guidelines, confidentiality declarations, and quotation response timelines.
* **Technical Deep-Dive Callout:**
  > *An automotive RFQ is not merely a request for piece price; it is a legally binding statement of technical capabilities. Every general attachment represents an audited engineering gateway that must be passed before Part Submission Warrant (PSW) sign-off.*
* **Spoken Presenter Script (Speaker Notes):**
  > *"When approaching a Ford RFQ pack, it is essential to understand how the package is structured. Ford divides this sourcing pack into four distinct pillars. The first pillar is the CAD repository, containing thirty-three STEP models that define every millimeter of clearance in the vehicle environment. The second pillar contains the commodity-specific engineering requirements: the Base ESOW, Attachment 9, the 66-page pedal box testing specification, and critical Ford standards such as CY-0002 for pedal travel and BR-1127 for bulkhead stiffness. The third pillar comprises twelve corporate general attachments that dictate how we run our engineering organization—from CATIA V5 data release protocols in Teamcenter to IMDS material reporting and cybersecurity. Finally, the fourth pillar establishes commercial and technical lines of communication with the Ford Merkenich chassis team. Our quotation response must systematically address every requirement across all four pillars."*

---

### Slide 03: Vehicle Program Scope: Ford CD4.1 & CD4.2 Architectures

* **Category:** Vehicle Platform • Slide 03 / 20
* **Target Timing:** 03:00 - 04:30
* **Visual Layout:** Comparative platform matrix displaying CD4.1 vs. CD4.2 vehicle applications, body styles, plant locations, and packaging distinctions between Left-Hand Drive (LHD) and Right-Hand Drive (RHD).
* **Core Slide Content:**
  * **Platform Origin:** Ford Global CD-Segment Architecture (CD4) replacing EUCD/CD3. High-volume global platform designed for front-wheel drive and all-wheel drive transverse powertrains.
  * **CD4.1 Program Scope:** Mondeo / Fusion Mid-Cycle Action (MCA) 4-door saloon, 5-door hatchback, and estate wagon. Built at Valencia Assembly (Spain) and Hermosillo (Mexico).
  * **CD4.2 Program Scope:** S-MAX (Sports MPV), Galaxy (7-Seat MPV), and Edge (Mid-size Crossover / SUV). Higher seating H-point, altered dash cowl geometry, and heavier gross vehicle weight (GVW). Built at Valencia Assembly.
  * **Drivetrain Complexity:** 6-Speed Manual Transmission (MMT6) paired with Panther 2.0L EcoBlue Diesel and 1.5L/2.0L GTDI EcoBoost petrol engines.
  * **LHD vs. RHD Architectural Differences:**
    * *LHD:* Brake booster directly behind pedal box; direct straight-line pushrod actuation; tight clearance to steering intermediate shaft and left cowl side member (`LHD-41-SideL.stp`).
    * *RHD:* Cross-car brake transfer linkage; pedal box packages adjacent to HVAC distribution housing (`HVAC-CD4.1-RHD.stp`); unique clutch master cylinder (CMC) orientation.
* **Technical Deep-Dive Callout:**
  > *Because CD4.1 (Mondeo) and CD4.2 (S-MAX/Galaxy) have different cowl heights and seat H-points, the pedal box supplier must develop common bracket pressings or modular mounting tabs to maximize tooling reusability across both programs.*
* **Spoken Presenter Script (Speaker Notes):**
  > *"Slide 3 outlines the vehicle platform context. The CD4 architecture is Ford's flagship mid-size global vehicle platform. In this RFQ, we are quoting two distinct platform derivatives: CD4.1, which is the Mondeo saloon and estate, and CD4.2, which represents the S-MAX and Galaxy multi-purpose vehicles. Both platforms share common underbody pressings but differ significantly in dash cowl height, driver H-point, and instrument panel packaging. Furthermore, we must supply both Left-Hand Drive and Right-Hand Drive configurations. On LHD vehicles, the clutch pedal sits immediately inboard of the structural cowl side member, requiring tight clearance around the steering column. On RHD vehicles, the pedal box must package alongside the massive HVAC climate control housing. Our engineering objective is to design a common modular bracket architecture that satisfies both CD4.1 and CD4.2 in both LHD and RHD drive configurations with minimal unique tooling investment."*

---

### Slide 04: Subsystem Architecture: The Hydraulic Clutch Actuation Chain

* **Category:** Technical Integration • Slide 04 / 20
* **Target Timing:** 04:30 - 06:00
* **Visual Layout:** End-to-end schematic diagram showing the complete hydraulic actuation loop: Pedal Arm $\rightarrow$ Over-Center Spring $\rightarrow$ CMC $\rightarrow$ Hydraulic Line $\rightarrow$ In-Line Damper $\rightarrow$ CSC $\rightarrow$ Clutch Diaphragm Spring.
* **Core Slide Content:**
  * **System Actuation Loop:**
    1. *Driver Input:* Foot applies pedal effort onto pedal pad (target travel: 135 mm nominal).
    2. *Kinematic Modulation:* Over-Center Spring (OCS) reduces peak foot effort and provides tactile snap-over.
    3. *Clutch Master Cylinder (CMC):* FTE `3M51-7A543-AG` cylinder converts pedal arc into hydraulic displacement.
    4. *Hydraulic Line & In-Line Damper (ILD):* FTE frequency modulator attenuates high-frequency engine crankshaft torsional vibrations from entering the pedal box.
    5. *Concentric Slave Cylinder (CSC):* FTE `DG91-7A564-xx` aluminium slave cylinder inside MMT6 transmission bellhousing.
    6. *Clutch Cover & Disc:* LuK `HG91-7540-AA` diaphragm spring disengages engine torque.
  * **Supplier Interface Ownership (ESOW Section 5.1 & 5.4):**
    * *CMC to Pedal Box:* Mechanical snap-in bracket interface and tolerance stackup is **Tier-1 Pedal Box Supplier Responsibility**.
    * *CMC to Pedal Arm Pushrod:* Clevis/ball joint snap interface is **CMC Supplier Responsibility** (FTE Automotive).
    * *Serviceability Requirement:* The pedal box must allow unbolting/servicing of the CMC in dealership workshops without removing the complete instrument panel.
* **Technical Deep-Dive Callout:**
  > *The pedal box supplier does not manufacture the hydraulic master cylinder, but they own the mechanical interface, pushrod angularity, and structural mounting stiffness that dictates hydraulic efficiency and seal wear.*
* **Spoken Presenter Script (Speaker Notes):**
  > *"To design the pedal box, we must look at the entire hydraulic actuation chain. As shown on Slide 4, when the driver depresses the pedal pad, the pedal arm rotates on its low-friction pivot bushings, compressing the over-center spring. The pedal arm drives the pushrod into the Clutch Master Cylinder. Hydraulic fluid travels through a reinforced hose into an In-Line Damper—which filters out engine firing boom—and into the Concentric Slave Cylinder to disengage the LuK clutch cover. In this RFQ, Ford directly sources the master cylinder from FTE Automotive, but we as the pedal box supplier are fully responsible for the mechanical mounting interface, the pushrod trajectory angles, and the overall tolerance stackup. Furthermore, Ford strictly mandates that the CMC must be serviceable in the field without requiring technicians to remove the steering column or complete vehicle dashboard."*

---

### Slide 05: Master Contract: Base Document ESOW v20 Scope of Work

* **Category:** SOW Governance • Slide 05 / 20
* **Target Timing:** 06:00 - 08:00
* **Visual Layout:** 3-tier responsibility matrix showing Supplier Core Deliverables, Ford Shared Tasks, and Launch Milestone Commitments based on `Base Document_ESOW v20`.
* **Core Slide Content:**
  * **Contractual Status:** Corporate Engineering Statement of Work (ESOW Template v20, updated June 2016). Master binding agreement between Ford Chassis Engineering and Tier-1 Supplier.
  * **Core Supplier Scope of Work (Section 5.1):**
    * Complete design and development of LHD and RHD clutch pedal boxes with Over-Center Springs (OCS) and standard/decorative pads.
    * Development of 3D CAD models in CATIA V5, storing all releases into Teamcenter Enterprise (TCE) following C3PNG standards.
    * Delivery of finite element mesh models for vehicle-level crash simulations (LS-DYNA).
    * Topology optimization of pedal brackets to deliver maximum stiffness-to-weight ratio.
    * Compliance with all Ford generic System Design Specifications (SDS) and sign-off criteria.
    * Active concern resolution through Job 1 + 90 days and for Ongoing Product Development (OPD).
  * **Vehicle Quality Targets (Section 5.2):** Monitored through Global Quality Report System (GQRS), JD Power Initial Quality Study (IQS), and Automotive Warranty System (AWS).
  * **BOM & Data Governance (Section 2.1):** Full CAD-to-BOM alignment using Ford AVBOM and WERS (Worldwide Engineering Release System).
* **Technical Deep-Dive Callout:**
  > *Job 1 + 90 days commitment means the supplier's engineering team remains contractually on-site at Ford assembly plants (Valencia, Spain) for three months after serial production begins to resolve early warranty spikes.*
* **Spoken Presenter Script (Speaker Notes):**
  > *"Slide 5 details the master contract: the Base Document ESOW version 20. This document defines our legal and technical scope of supply. Ford places full-service responsibility on our shoulders. We must design both LHD and RHD pedal boxes, model all feature trees in CATIA V5, archive native CAD directly into Ford's Teamcenter Enterprise database, and provide detailed FEA meshes for vehicle-level crash simulation. Ford also expects us to utilize topology optimization to remove every unnecessary gram of mass from the bracket pressings while maintaining structural rigidity. Furthermore, our engineering responsibility does not end when production begins. Under Section 5.1, we are contractually required to support launch containment on-site through Job 1 plus 90 days, actively monitoring GQRS and warranty claim systems to ensure zero defects reach retail customers."*

---

### Slide 06: Specific Pedal Box Deliverables: Attachment 9.0 (ESOW-PBOX-FD)

* **Category:** Component SOW • Slide 06 / 20
* **Target Timing:** 08:00 - 09:30
* **Visual Layout:** Engineering checklist card highlighting production tooling tuning capabilities, switch flag angles, environmental standards, and prototype on-site support.
* **Core Slide Content:**
  * **Document Reference:** `060602_ESOW_PBOX_FD_ATT-9.pdf` (Revised Sep 26, 2016). Specific appendix to the Base ESOW controlling pedal box design, verification, and tooling.
  * **Mandatory Tooling Adjustment / Tuning Capability (Section 9.4):**
    * Supplier *must* design and build adjustment and tuning capability into all production stamping dies, injection moulds, and checking fixtures.
    * Allows fine-tuning of pedal height, lateral position, and switch trip points prior to Job 1 without recutting hard tooling.
  * **Switch Flag Angular Tolerance (Section 9.1):**
    * Angle from the center of the switch mounting hole through the actuation contact tip on the switch flag to the pedal pivot rotation axis must be held between **$-4^\circ$ and $-6^\circ$**.
  * **Interior Environmental & Odor Standards (Section 9.1):**
    * `WSS-M99P9999-A1`: Restricted Substance Management Standard (RSMS / IMDS).
    * `WSS-M99P2222-D1`: Performance, Vehicle Interior Environmental Quality (fogging & VOC emissions).
    * `FLTM BO 131-03`: Ford Laboratory Test Method for Interior Odor Evaluation.
  * **On-Site Prototype Build Support (Section 9.7):** Supplier resident engineering support required on-site at Ford prototype build events approximately **one week prior** to each build start date.
* **Technical Deep-Dive Callout:**
  > *Mandating adjustable tuning inserts in hard stamping dies protects both Ford and the supplier from multimillion-pound tooling scrap if styling changes the carpet thickness or the master cylinder pushrod stroke drifts during prototype builds.*
* **Spoken Presenter Script (Speaker Notes):**
  > *"Moving to Slide 6, we examine Attachment 9.0, which contains the specific engineering and tooling rules for pedal boxes. Section 9.4 contains a vital tooling directive: we are required to engineer adjustment and tuning capability into our production stamping dies and injection moulds prior to Job 1. This ensures that if pedal height or switch actuation points need calibration after physical prototype evaluation, we can adjust die inserts rather than scrapping expensive tooling. Section 9.1 also imposes strict geometric control over the electrical switch flag: the angle between the switch hole, the contact tip, and the pedal pivot axis must be held strictly between minus 4 and minus 6 degrees. Finally, because this assembly sits inside the passenger cabin, all plastics, lubricants, and coatings must comply with Ford's vehicle interior air quality standards, including fogging restrictions under WSS-M99P2222 and odor testing per FLTM BO 131-03."*

---

### Slide 07: Master Engineering Testing Specification: ES-PB (060602_ES_PB)

* **Category:** DVP&R & Testing • Slide 07 / 20
* **Target Timing:** 09:30 - 11:30
* **Visual Layout:** Comprehensive testing matrix table categorizing durability, structural abuse, climatic conditioning, and end-of-line verification tests from the 66-page `ES_PB` specification.
* **Core Slide Content:**
  * **Document Reference:** `060602_ES_PB_20160628.pdf` (66 Pages). Master Design Verification Plan (DVP) and Engineering Specification for Pedal Box Modules.
  * **Core Mechanical & Durability Test Matrix:**
    * *Life Cycle Durability Test (Section 3.1):* Minimum 500,000 to 1,000,000 full-stroke actuation cycles conducted across thermal extremes ($-40^\circ\text{C}$, $+23^\circ\text{C}$, and $+80^\circ\text{C}$).
    * *Clutch Structural Abuse Test (Section 3.6):* Pedal arm must withstand **$1,000\text{ N}$ static abuse force** applied directly to the pad along the actuation axis without fracture or permanent functional deformation. (Brake pedal requirement: $2,000\text{ N}$).
    * *Reverse Overload Test (Section 3.12):* Pedal arm must withstand **$500\text{ N}$ pull-back force** (reverse direction toward the driver) to simulate foot snagging under rapid release.
    * *Lateral Deflection Test (Section 3.7):* Static side load applied to pedal pad to evaluate bushing play and bracket torsional rigidity. Maximum allowable lateral free play: $<3\text{ mm}$ under load.
    * *Free Swing Test (Section 3.8):* Pedal must swing freely under gravity without stickiness or bushing binding throughout full angular sweep.
  * **Material Pre-Conditioning Protocol (Section 2.6):**
    * If composite/plastic components are used (e.g., glass-filled polyamide pedal arms), samples must undergo short-term heat, humidity, and cold cycling before structural testing.
  * **End-of-Line (EOL) 100% Production Verification (Section 2.9):** 100% automated inspection on assembly line verifying pivot pin retention, switch flag presence, spring rate, and date code stamping per Ford Directive E-108.
* **Technical Deep-Dive Callout:**
  > *The $1,000\text{ N}$ clutch structural abuse load represents an extreme panic condition (equivalent to a 100 kg load stomped onto the pedal pad). Plastic pedal arms must utilize ribbed PA66-GF30 or hybrid steel pressings to prevent structural yielding.*
* **Spoken Presenter Script (Speaker Notes):**
  > *"Slide 7 covers the technical bible of this RFQ: the 66-page Engineering Specification ES-PB. This document defines our Design Verification Plan and Report (DVP&R). The testing regime is uncompromising. Our pedal box must survive up to one million full actuation cycles in environmental chambers cycling from minus forty degrees Celsius to plus eighty degrees Celsius. In structural testing, the clutch pedal must survive a 1,000 Newton forward abuse load without yielding, and a 500 Newton reverse pull-back load without popping the pivot bushings or breaking the return stops. We also must conduct lateral deflection testing to guarantee that side loads do not cause the pedal to flex into the steering column or adjacent brake pad. Finally, Section 2.9 mandates that every single production pedal box that leaves our assembly line must pass 100% automated End-of-Line testing to verify switch flag position, spring retention, and laser date coding before shipment to Ford plants."*

---

### Slide 08: Kinematics & Pedal Travel Standard: Ford CY-0002

* **Category:** Operating Curves • Slide 08 / 20
* **Target Timing:** 11:30 - 13:00
* **Visual Layout:** Graphic curve representation showing Clutch Pedal Effort vs. Travel (mm), depicting the P5 Panther Diesel input curve, Over-Center Spring snap-over, hysteresis band, and clutch disengagement window.
* **Core Slide Content:**
  * **Standard Reference:** Ford Customized Requirement `CY-0002` (RQT-080000-008524, Rev 15, "Clutch Pedal Travel").
  * **Kinematic Travel Requirements (ESOW Section 5.4):**
    * *Nominal Pedal Travel:* **$135\text{ mm}$** total stroke from rest position to floor/carpet stop.
    * *Clutch Actuation Point 1 (CAP1):* Initial pushrod contact and master cylinder port cut-off.
    * *Clutch Actuation Point 2 (CAP2):* Full clutch disengagement point within nominal travel window.
  * **Over-Center Spring (OCS) Modulation:**
    * Over-center mechanical advantage: spring resists initial pedal motion, passes top-dead-center (snap-over point), and then aids driver depression to lower holding effort at bottom-of-travel.
    * Eliminates driver foot fatigue during extended traffic queueing.
  * **P5 Panther Diesel Engine Effort Curve (`crs_sim_data_out`):**
    * Peak pedal effort ($F_{pMax}$): **$113.4\text{ N}$** occurring at $93.4\text{ mm}$ travel ($68.3\%$ of stroke).
    * Hysteresis loop: Controlled return friction ensuring rapid pedal snap-back without sluggish return damping.
  * **Three Required CAD States:** All CAD models must formally represent three discrete kinematic positions:
    1. *Free Position (Rest):* Upper stop contact against bracket bumper.
    2. *Actuation Position (Disengagement):* Mid-travel clutch release point.
    3. *Bottom of Travel (BOT):* Fully depressed against carpet stop envelope.
* **Technical Deep-Dive Callout:**
  > *If the return spring force is too high, the pedal effort exceeds ergonomic limits ($>120\text{ N}$); if too low, the pedal fails to return rapidly during fast performance gear shifts. CY-0002 governs this precise balance.*
* **Spoken Presenter Script (Speaker Notes):**
  > *"Slide 8 focuses on pedal ergonomics and operating feel, governed by Ford Standard CY-0002. Total pedal travel is established at a nominal 135 millimeters. To optimize driver comfort, the clutch pedal incorporates an Over-Center Spring mechanism. As the driver pushes the pedal, the spring initially resists movement, but once it rotates past its center pivot, it snaps over and actively helps push the pedal down, reducing holding effort at the floor. In the Panther 2.0-liter diesel application, the peak pedal force is engineered to reach exactly 113.4 Newtons at 93.4 millimeters of stroke, or approximately 68% travel. Under the ESOW, Ford requires us to deliver our 3D CAD assemblies showing the pedal arm in three fully articulated states: the free rest position, the mid-travel actuation position, and the fully depressed bottom-of-travel position."*

---

### Slide 09: Packaging & Clearance Envelopes Standard: Ford BR-1119

* **Category:** DMU & Clearance • Slide 09 / 20
* **Target Timing:** 13:00 - 14:30
* **Visual Layout:** 3D spatial clearance diagram depicting the pedal pad coordinate layout, foot clearance ellipses, steering column dynamic sweep envelope, and ECE R35 regulatory spacing.
* **Core Slide Content:**
  * **Standard Reference:** Ford Customized Requirement `BR-1119` (RQT-060000-019108, Rev 8, "Clutch Pedal Clearance and Layout").
  * **Regulatory Compliance:** Aligns with European Regulation **ECE R35** (Uniform provisions concerning the approval of vehicles with regard to the arrangement of foot controls) and SAE J1100.
  * **Mandatory Clearance Envelopes in CAD:**
    * *Dynamic Steering Column Sweep:* Minimum **$15\text{ mm}$ dynamic clearance** to steering intermediate shafts, universal joints, and slip shafts (`Steeering cd41-lhd-rhd.stp`).
    * *Lateral Pedal Pad Separation:* Minimum **$50\text{ mm}$ lateral clearance** between clutch pedal pad edge and brake pedal pad edge to prevent simultaneous foot depression.
    * *Footrest / Left Cowl Clearance:* Minimum **$50\text{ mm}$ clearance** between clutch pedal pad and the left footrest / trimmed wheel arch (`LHD-41-SideL.stp`).
    * *Under-Instrument Panel Trim:* Minimum **$10\text{ mm}$ static clearance** to wiring harnesses, ducting, and structural cross-car beam members.
  * **CAD Deliverable Requirement:** Supplier must deliver the clutch pedal assembly in CATIA V5 with a **transparent swept volume envelope** representing dynamic lateral and longitudinal deflection under load per BR-1119.
* **Technical Deep-Dive Callout:**
  > *ECE R35 is a mandatory homologation requirement. A vehicle cannot be legally registered in Europe or North America if the lateral distance between clutch and brake pads fails regulatory minimums.*
* **Spoken Presenter Script (Speaker Notes):**
  > *"Slide 9 details packaging clearances governed by Ford Standard BR-1119 and European Regulation ECE R35. Driver footwells are among the most congested spatial environments in a modern car. We must maintain at least 50 millimeters of lateral separation between the clutch pedal pad and the brake pad, and 50 millimeters between the clutch pad and the left footrest, ensuring drivers with large winter footwear do not accidentally trap their feet. In addition, the pedal arm must clear the rotating steering column intermediate shaft by at least 15 millimeters throughout its entire swing arc. To prove feasibility in Ford's Digital Mockup reviews, BR-1119 requires us to model a transparent dynamic envelope in CATIA that shows the outer limits of pedal movement, including structural deflection under severe foot pressure."*

---

### Slide 10: Structural Rigidity & Dash Deflection Standard: Ford BR-1127

* **Category:** Deflection & NVH • Slide 10 / 20
* **Target Timing:** 14:30 - 16:00
* **Visual Layout:** Finite Element Analysis (FEA) deflection schematic showing the dash panel bulkhead mounting interface, load vectors, and dial-indicator deflection measurement points.
* **Core Slide Content:**
  * **Standard Reference:** Ford Customized Requirement `BR-1127` (RQT-060000-019420, Rev 4, "Dash Panel and Pedal Box Deflection during Clutch Operation").
  * **Engineering Objective:** Prevent sheet metal oil-canning, spongy pedal feel, loss of hydraulic stroke, and NVH acoustic transmission across the dash bulkhead.
  * **Deflection Limits Under Operating Load:**
    * When a **$400\text{ N}$ normal clutch actuation force** is applied, total longitudinal deflection of the master cylinder mounting face must remain below **$1.5\text{ mm}$**.
    * Total lateral deflection at the pedal pad must remain below **$3.0\text{ mm}$**.
  * **Structural Abuse Integrity:** Under **$1,000\text{ N}$ abuse load**, dash panel mounting studs and pedal bracket welds must exhibit zero tearing, zero cracking, and permanent plastic deformation must not exceed **$1.0\text{ mm}$**.
  * **Bushing Lash & Pivot Hysteresis:** Pivot bushings (PTFE/POM composite) must maintain zero perceptible free lash ($<0.2\text{ mm}$) to ensure solid perceived craftsmanship and eliminate pedal rattle under road vibration.
* **Technical Deep-Dive Callout:**
  > *If the dash bulkhead flexes excessively under pedal load, effective hydraulic fluid displacement is lost. The clutch slave cylinder fails to fully disengage, causing gear grinding and premature synchronizer wear in the transmission.*
* **Spoken Presenter Script (Speaker Notes):**
  > *"Slide 10 examines structural rigidity under Ford Standard BR-1127. When a driver presses the clutch pedal, reaction forces push backward directly against the vehicle dash bulkhead. If the pedal bracket or the dash sheet metal is too flexible, the firewall flexes like a diaphragm. This absorbs valuable pedal stroke, resulting in a spongy pedal feel and preventing the clutch from disengaging cleanly. BR-1127 establishes strict stiffness limits: under a standard 400 Newton operating force, deflection at the master cylinder mounting face cannot exceed 1.5 millimeters, and lateral pad deflection must stay under 3 millimeters. Under a 1,000 Newton panic load, the structure must absorb the energy without weld fracture or stud pull-out. Our bracket must incorporate structural swages, boxed flanges, or reinforcement gussets to meet these rigidity targets."*

---

### Slide 11: Passive Safety & Crash Breakaway Mechanism

* **Category:** Crashworthiness • Slide 11 / 20
* **Target Timing:** 16:00 - 17:30
* **Visual Layout:** Before-and-after crash sequence diagram illustrating frontal collision bulkhead intrusion, pedal box breakaway triggering, and rearward displacement decoupling.
* **Core Slide Content:**
  * **Safety Objective:** Mitigate severe driver lower limb injury (tibia index, ankle crushing, foot trapping) during high-speed frontal offset collisions (Euro NCAP $64\text{ km/h}$ ODB and US FMVSS 208).
  * **CAD Reference Models:** `cd41-LHD-Crash.stp` and `cd41-RHD-Crash.stp` (Crash intrusion vectors and knee clearance keep-out zones).
  * **Mandatory Crash Feature (ESOW Section 5.4):**
    * The pedal arm for both LHD and RHD *must* incorporate a crash breakaway or controlled deformation mechanism.
    * *Mechanism Operation:* During frontal impact, as the front wheel and subframe push the dash bulkhead rearward into the cabin, a mechanical trigger releases the pedal pivot or shears a sacrificial pin.
    * The pedal arm rotates downward and forward toward the floor, decoupling from the rearward intrusion of the firewall.
  * **Regulatory Criteria:** Residual rearward intrusion of the pedal pads must remain below regulatory thresholds ($<100\text{ mm}$ rearward displacement; zero upward vertical entrapment).
  * **CAE Simulation Deliverable:** Tier-1 supplier must provide validated LS-DYNA explicit finite element mesh models of the pedal box to Ford Crash Safety PMT to verify breakaway kinematics prior to physical sled testing.
* **Technical Deep-Dive Callout:**
  > *Pedal intrusion is one of the highest point deductions in Euro NCAP crash scoring. A failed breakaway mechanism can downgrade an entire vehicle from a 5-star to a 4-star safety rating.*
* **Spoken Presenter Script (Speaker Notes):**
  > *"Slide 11 addresses passive crash safety. In a severe frontal collision, vehicle engine blocks and suspension subframes are pushed rearward, causing the lower dash bulkhead to deform into the cabin. If the clutch pedal remained rigid, it would act as a ram, crushing the driver's feet and fracturing their lower tibia. Section 5.4 of the ESOW mandates that our pedal arm must feature an integrated crash breakaway system. When bulkhead intrusion forces exceed a calibrated threshold, the pivot bracket releases or fractures along a designed shear path, dropping the pedal arm down toward the floorpan away from the driver's feet. We must provide fully correlated LS-DYNA crash simulation models to Ford's safety team to prove the breakaway releases within milliseconds during digital 64 km/h offset crash testing."*

---

### Slide 12: Quality & Special Characteristics Governance: SCCAF (FAP03-111)

* **Category:** Quality & Control Plans • Slide 12 / 20
* **Target Timing:** 17:30 - 19:00
* **Visual Layout:** Special Characteristics cascade diagram linking Ford FAP03-111 procedure to DFMEA, SCCAF matrix, Supplier PFMEA, and Shop-Floor Control Plans.
* **Core Slide Content:**
  * **Document Reference:** `060602_SCCAF_PBOX_FD.xls` (Special Characteristics Communication and Agreement Form).
  * **Governing Procedure:** Ford Automotive Procedure **FAP03-111** (Agreement and Documentation of Product and Process Special Characteristics).
  * **Gateway Sign-Off Points:** Formal SCCAF sign-offs required at GPDS gateways: **UNV2** (Underbody Verification 2), **UPV2** (Upperbody Verification 2), and **PA** (Program Approval).
  * **Classification Hierarchy:**
    * *Critical Characteristics ($\nabla$ CC):* Failure Mode Severity **$S \ge 9$ or $10$**. Direct impact on vehicle safety, braking, or regulatory compliance (e.g., pivot pin retention, crash release triggering, structural weld integrity). Mandates inverted delta symbol ($\nabla$) on drawings, Control Plans, and $100\%$ automated poka-yoke verification ($C_{pk} \ge 1.67$).
    * *Significant Characteristics (SC):* Failure Mode Severity **$S = 5 \text{ to } 8$** combined with Occurrence **$O = 4 \text{ to } 10$**. Key features driving customer satisfaction, pedal effort, switch activation timing, and mounting hole true position ($C_{pk} \ge 1.33$).
    * *Operator Safety Characteristics:* Severity 9 or 10 relating to plant manufacturing and assembly personnel safety.
* **Technical Deep-Dive Callout:**
  > *The $\nabla$ (Inverted Delta) designation imposes strict legal liability. Every $\nabla$ CC identified in the SCCAF must have a direct, traceable statistical control plan on our factory floor audited during Ford PPAP.*
* **Spoken Presenter Script (Speaker Notes):**
  > *"Slide 12 covers quality governance under the SCCAF spreadsheet and Ford Procedure FAP03-111. In the automotive industry, quality control begins long before the factory floor. The SCCAF form is the formal bridge between our engineering DFMEA and manufacturing process control. It categorizes all product features into two tiers: Critical Characteristics, designated by Ford's famous Inverted Delta symbol, and Significant Characteristics. Any failure mode with a Severity rating of 9 or 10—such as pivot pin detachment or crash breakaway failure—is automatically classified as an Inverted Delta Critical Characteristic. This classification mandates that our production line must incorporate 100% automated mistake-proofing with statistical process capability Cpk of 1.67 or higher. Formal sign-off on the SCCAF is legally required at the UNV2 and Program Approval gateways."*

---

### Slide 13: 3D CAD DMU Packaging Environment: Primary Structural Interfaces

* **Category:** CAD Environment • Slide 13 / 20
* **Target Timing:** 19:00 - 20:30
* **Visual Layout:** CAD assembly exploded rendering showing the 33 STEP files grouped into Primary Bulkhead Interfaces, Steering Kinematics, Lower Fixings, and Side Cowls.
* **Core Slide Content:**
  * **Overview:** 33 STEP CAD models (~540 MB) provided in `CAD/` folder, modeling the exact geometry of Ford CD4.1 and CD4.2 driver footwells.
  * **Primary Structural Interface Models:**
    * *Bulkhead Mounting Surface:* `Dash-LHD.stp`, `Dash-RHD.stp`, `LHD-41-Dash.stp`, `RHD-41-Dash.stp` (Sheet metal firewall panels defining datum planes and mounting stud locations).
    * *CMC Master Cylinder Pass-Through:* `Dash-Hole.stp` (Stamping aperture through the dash panel where the master cylinder barrel and pushrod penetrate to the engine bay).
    * *Chassis Attachment Hardpoints:* `LHD-Lower-Fixing.stp`, `RHD-Lower-Fixing.stp` (Lower mounting bracket studs transferring pedal reaction forces into the structural floorpan crossmember).
    * *Structural Cowl Side Member:* `LHD-41-SideL.stp` (Deep-drawn inner body side structural stamping bounding the pedal box on the left).
  * **Steering Column Kinematic Envelopes:**
    * `Steeering cd41-lhd-rhd.stp` (48.3 MB) & `Steering cd42-lhd-rhd.stp` (38.6 MB).
    * Detailed models of steering column intermediate shafts, universal joints, and telescope/tilt adjustment ranges requiring dynamic clearance checks across all positions.
* **Technical Deep-Dive Callout:**
  > *Because the steering column telescopes toward the driver and tilts vertically, dynamic clearance sweeps must be calculated across the entire three-dimensional kinematic operating envelope, not just static nominal positions.*
* **Spoken Presenter Script (Speaker Notes):**
  > *"Slide 13 explores the 3D CAD packaging environment provided in the thirty-three STEP files. These models give us the exact digital twin of the vehicle footwell. The primary structural interfaces include the sheet metal dash bulkhead models for both LHD and RHD, which dictate our mounting stud coordinates and primary datum planes. The file Dash-Hole.stp defines the exact pass-through hole for the master cylinder pushrod, while the Lower-Fixing files specify where the lower bracket bolts into the underbody floor structure. Crucially, the steering column models—which total over 80 megabytes—show the full dynamic sweeps of the steering intermediate shaft and universal joints. Our CAD team must perform automated batch clash detection to ensure our pedal bracket maintains the required 15-millimeter clearance across all steering tilt and telescope adjustment ranges."*

---

### Slide 14: Footwell Ergonomics & Secondary Trim Packaging Environment

* **Category:** Trim & Clearances • Slide 14 / 20
* **Target Timing:** 20:30 - 22:00
* **Visual Layout:** Cross-sectional footwell diagram illustrating carpet compression, acoustic NVH heavy layers, HVAC housing proximity, and pedal pad target coordinates.
* **Core Slide Content:**
  * **Secondary Trim & Environmental CAD Models:**
    * *Molded Floor Carpet Assemblies:* `Carpet-LHD.stp`, `Carpet-RHD.stp`, `Carpet-LHD-RHD.stp` (64.2 MB). Represents uncompressed molded carpet contours and underlay foam padding directly beneath pedal travel.
    * *Acoustic NVH Insulation Barrier:* `NVH-cd41.stp` (32.3 MB) & `NVH-RHD-LHD-CD42.stp` (119.2 MB). Heavy-layer cast sound-deadening dash insulation pad sandwiched between the bracket and firewall.
    * *Climate Control Distribution Housing:* `HVAC-CD4.1-RHD.stp` (5.6 MB). Plastic heater core casing packaging tightly adjacent to the RHD pedal assembly.
  * **Ergonomic Foot Zone Envelopes (SAE J1100 / J1517):**
    * `CD41-LHD-FOOT-Zone.stp`, `CD41-RHD-FOOT-Zone.stp`, `LHD-42-Foot-zone.stp`, `RHD-42-Foot-zone.stp`.
    * Represents dynamic envelopes of the driver's shoe sole throughout pedal travel.
  * **Pedal Pad Geometry & Decorative Styling:**
    * `CD4.1-LHD-PAD.stp`, `CD4.1-RHD-PAD.stp`, `CD42-LHD-PAD.stp`, `CD42-RHD-PAD.stp` (Nominal rubber pedal pad contact faces).
    * `Decorative-Pad-LHD-CD41.stp` (3.8 MB) (Brushed aluminum sports pedal option with anti-slip rubber inserts).
* **Technical Deep-Dive Callout:**
  > *Carpet thickness tolerances ($\pm 3\text{ mm}$) directly affect bottom-of-travel stop coordinates. If the pedal hits compressed carpet before the master cylinder achieves full stroke, the clutch will drag.*
* **Spoken Presenter Script (Speaker Notes):**
  > *"On Slide 14, we review the secondary trim and ergonomic packaging environment. Beyond bare sheet metal, our pedal box interacts with complex interior trim. The CAD files include high-density scans of the molded floor carpets and acoustic NVH dash mats. In fact, the NVH insulation model alone is nearly 120 megabytes, representing the thick acoustic barrier between the driver and the engine bay. We must account for carpet compression under heavy foot pressure to ensure the pedal stop does not prematurely bottom out. The CAD pack also provides dynamic Foot-Zone models based on SAE J1100, which define the sweep of a 95th-percentile male shoe sole. Finally, Ford has included both standard rubber pads and decorative brushed-aluminum sports pads, which we must accommodate on the pedal arm without altering the pedal's underlying structural geometry."*

---

### Slide 15: Electrical Subsystem Integration: Bottom-of-Travel (BOT) Switch

* **Category:** Electrical Controls • Slide 15 / 20
* **Target Timing:** 22:00 - 23:30
* **Visual Layout:** Electrical switch packaging schematic showing the clutch pedal arm, switch flag actuation cam, electrical connector plug, and switch travel timing chart.
* **Core Slide Content:**
  * **Subsystem Purpose:** Bottom-of-Travel (BOT) clutch switch communicates directly with the Powertrain Control Module (PCM) and Body Control Module (BCM).
  * **Vehicle System Functions:**
    1. *Engine Starter Inhibit:* Prevents engine cranking unless clutch is fully depressed.
    2. *Stop-Start System:* Triggers automatic engine restart when clutch is depressed at traffic lights.
    3. *Adaptive Cruise Control:* Disengages cruise control upon initial pedal touch.
  * **CAD Reference Models:** `BOT-LHD-41.stp` & `BOT-RHD-41.stp` (5.5 MB each) (Switch housing envelope, mounting bayonet, harness connector).
  * **Electrical Harness Models:** `41-LHD-Electrical.stp` (40.8 MB) & `41-RHD-Electrical.stp` (13.6 MB) (Wire routing take-out points and harness clip hardpoints).
  * **Critical Actuation Parameters (ESOW Section 5.4 & Attachment 9.0):**
    * *Switch Actuation Point:* Nominal **$84\%$ of total pedal travel** (driven by vehicle driveability and gear engagement timing).
    * *Switch Flag Alignment:* Angle from switch mounting hole through contact tip to pedal pivot axis held strictly to **$-4^\circ \text{ to } -6^\circ$**.
    * *Electrical Responsibility Split:* Switch unit and wiring harness are direct Ford EESE (Electrical Electronic Systems Engineering) responsibility; mounting bracket, actuation flag, and mechanical timing are **Tier-1 Pedal Box Supplier Responsibility**.
* **Technical Deep-Dive Callout:**
  > *If the switch triggers too early ($<80\%$), the engine may restart while the clutch is partially engaged; if too late ($>88\%$), the driver will experience starter cranking hesitation. The 84% target requires tight tooling tolerances.*
* **Spoken Presenter Script (Speaker Notes):**
  > *"Slide 15 covers the electrical integration of the Bottom-of-Travel switch, or BOT switch. In modern vehicles, the clutch pedal is an electronic sensor trigger as well as a mechanical lever. The BOT switch feeds critical signals to the engine control unit for three key functions: starter motor inhibit, automatic engine stop-start restart, and cruise control cutoff. The files BOT-LHD-41 and BOT-RHD-41 give us the exact CAD geometry of the switch and its connector plug. Under Section 5.4 of the ESOW, the switch actuation point is strictly defined at 84% of total pedal travel. While Ford's electrical engineering team sources the switch itself, we are responsible for designing the mounting bracket and the integral switch flag on the pedal arm that trips the switch. Holding the switch trip point accurately throughout one million cycles demands high dimensional precision on our pivot bushings and switch flag cam surfaces."*

---

### Slide 16: Corporate Engineering Attachments: CAD, CAE, FMA & Craftsmanship (Att. 01a–05)

* **Category:** Corporate SOW • Slide 16 / 20
* **Target Timing:** 23:30 - 25:00
* **Visual Layout:** 5-segment engineering governance wheel summarizing Attachments 01a, 01b, 02, 03, 04, and 05.
* **Core Slide Content:**
  * **Attachment 01a — CAD Standards (C3PNG V3.6):**
    * Native CATIA V5 modeling following C3PNG corporate methodology.
    * Direct data integration into Ford Teamcenter Enterprise (TCE). Mandatory use of Ford seed files, standardized vehicle coordinate origins ($X, Y, Z$), and parametric feature tree hygiene.
  * **Attachment 01b & CAE Specific v7.7 — Digital CAE Integration:**
    * Finite element meshing compliant with Ford Global Chassis CAE Meshing Guideline (`00.00-C-602`).
    * Full material cards: true stress-strain curves, strain-life fatigue curves, Abaqus implicit/explicit decks, and rubber hyperelastic models (Mooney-Rivlin).
  * **Attachment 02 — Failure Mode Avoidance (FMA):**
    * Compliance with Ford FMEA Handbook v4.2. Mandatory Boundary Diagrams, Parameter Diagrams (P-Diagrams), and Design Verification Plans (DVP&R).
    * *Severity Discipline:* Any failure mode with Severity $S \ge 8$ mandates immediate design countermeasure and executive engineering review.
  * **Attachment 03 — Environmental & Recycling Targets:**
    * Mandatory submission into International Material Data System (IMDS).
    * Reusability, Recyclability, and Recoverability (RRR) per European Directive 2005/64/EC ($>85\%$ recyclable, $>95\%$ recoverable by mass). Compliance with `WSS-M99P9999-A1` restricted substance list.
  * **Attachment 05 — Craftsmanship & Perceived Quality:**
    * Perceived quality standards governing gap, flush, operating sound quality (squeak, rattle, click), and surface grain finish on driver-visible pedal components.
* **Technical Deep-Dive Callout:**
  > *Failing to upload valid IMDS chemical data in Attachment 03 will legally block production launch; Ford cannot sell the vehicle in the European Union without certified environmental material declarations.*
* **Spoken Presenter Script (Speaker Notes):**
  > *"Slide 16 details Ford's core engineering attachments. These documents define the digital and quality standards our engineering team must follow. Attachment 01a governs CAD delivery: all modeling must be native CATIA V5 archived directly in Ford's Teamcenter Enterprise system following strict C3PNG conventions. Attachment 01b and the Chassis CAE specific attachment govern finite element simulation, requiring validated Abaqus and LS-DYNA decks with full material strain-hardening curves. Attachment 02 enforces Ford's rigorous Failure Mode Avoidance process, requiring P-Diagrams and DFMEAs where any failure mode with a Severity of 8 or higher mandates an immediate design revision. Attachment 03 requires 100% material tracking in the IMDS system to meet European recycling laws, and Attachment 05 sets craftsmanship guidelines to eliminate squeaks, rattles, and clicks during pedal operation."*

---

### Slide 17: Corporate Compliance Standards: Feasibility, Materials & Cyber (Att. 06–10, E-108)

* **Category:** Homologation & Trademarks • Slide 17 / 20
* **Target Timing:** 25:00 - 26:30
* **Visual Layout:** Compliance verification matrix outlining Attachments 06, 07, 08, 09, 10, and Ford Directive E-108.
* **Core Slide Content:**
  * **Attachment 06 — Design Feasibility (Update Jun 2016):** Mandatory sign-off of Ford Design Feasibility Form 06. Tier-1 Supplier technical executive formally certifies that the proposed design can be manufactured at target line takt time and quality capability.
  * **Attachment 07 — Materials Engineering (Update Dec 2015):** Mandatory use of approved materials meeting Ford Worldwide Engineering Specifications (WSS). Enforces corrosion resistance (salt spray testing), polymer heat aging, and lubricant compatibility.
  * **Attachment 08 — Supplier Web-Based Data Management:** Mandates supplier connectivity and maintenance of Ford portals: Global Supplier Database (GSDB), Covisint, Ford Supplier Portal (FSP), and WERS.
  * **Attachment 09 — Component Homologation (General Attachment v1.3):** Establishes legal certification protocols for European E-marking, Conformity of Production (CoP) audits, and regulatory type-approval witness testing.
  * **Attachment 10 — Ford CyberAssurance SOW (Release V1.0):** Mandatory cybersecurity governance protecting supplier design servers, CAD data exchanges, and manufacturing shop-floor OT networks against cyber espionage and ransomware.
  * **Directive E-108 — Global Parts Trademarks:** Controls physical part markings: Ford Oval logo placement, 4-digit engineering part number font, supplier code, engineering revision level, and molded date clocks.
* **Technical Deep-Dive Callout:**
  > *Attachment 10 (CyberAssurance) reflects modern OEM supply chain protection. Ford audits Tier-1 CAD servers and PLM connections to prevent intellectual property leaks of upcoming vehicle platforms.*
* **Spoken Presenter Script (Speaker Notes):**
  > *"Slide 17 covers corporate compliance and legal attachments. Attachment 06 is our formal Design Feasibility commitment: by signing Form 06, we legally certify that the proposed pedal box can be manufactured to print at volume production rates. Attachment 07 governs approved materials, ensuring our polymer resins and corrosion coatings comply with Ford WSS specifications. Attachment 08 mandates our team's integration into Ford's web-based portals like Covisint and WERS. Attachment 09 governs legal component homologation and E-marking for international vehicle sales. Attachment 10 is Ford's CyberAssurance SOW, which requires us to maintain strict cybersecurity protocols on the CAD servers hosting Ford engineering data. Finally, Directive E-108 controls physical part markings, dictating the exact dimensions of the Ford Oval logo, part numbers, and date clocks molded into our components."*

---

### Slide 18: Hydraulic Actuation Simulation: Panther 2.0L Diesel Case Study

* **Category:** CAE & Actuation • Slide 18 / 20
* **Target Timing:** 26:30 - 28:00
* **Visual Layout:** Technical data sheet layout based on `crs_sim_data_out_18-May-2017_Panter.xlsx`, featuring the hydraulic circuit bill of materials, torque targets, and force-travel mathematical plots.
* **Core Slide Content:**
  * **Document Reference:** `crs_sim_data_out_18-May-2017_Panter.xlsx` (Clutch Release System Simulation Data Output v1.8, created May 18, 2017).
  * **Specific Vehicle & Powertrain Combination:** Ford CD4 Platform paired with the **Panther 2.0L EcoBlue Diesel Engine** and 6-Speed MMT6 Manual Transmission.
  * **Simulated Subsystem Bill of Materials:**
    * *Clutch Cover & Disc:* LuK `HG91-7540-AA-C2_TAC_LukSim.xlsx` (Self-adjusting clutch diaphragm spring).
    * *Concentric Slave Cylinder (CSC):* FTE `DG91-7A564-xx-FTE-MMT6-ALU.xlsx` (Aluminium CSC).
    * *Hydraulic Hose:* FTE Stiff Hydraulic Line (`Brake hose stiff FTE_01_157.xlsx`).
    * *In-Line Damper (ILD):* FTE Frequency Modulator (`ILD_Freq_Modulator_FTE.xlsx`).
    * *Clutch Master Cylinder (CMC):* FTE `3M51-7A543-AG-FTE-C346.xlsx`.
    * *Pedal Box Input File:* `xxxx-7B633-xx-CD4x-Panther_proposal_KSR Theoretical OCS Curve_RHD Average.xlsx`.
  * **Actuation Performance Simulation Results:**
    * *Peak Pedal Force ($F_{pMax}$):* **$113.37\text{ N}$** (Target: $<120\text{ N}$).
    * *Peak Force Travel Position:* **$93.38\text{ mm}$** ($68.29\%$ of total stroke).
    * *Total Nominal Travel:* **$135\text{ mm}$**.
    * *Torque Decoupling Metric ($T_{DP}$):* $0.3\text{ Nm}$ residual drag torque at disengagement.
* **Technical Deep-Dive Callout:**
  > *This simulation file confirms that KSR International submitted the baseline theoretical Over-Center Spring proposal for this program, establishing the mathematical benchmark that our design must achieve or surpass.*
* **Spoken Presenter Script (Speaker Notes):**
  > *"Slide 18 provides invaluable insight into Ford's hydraulic release simulation, extracted from the Panther diesel simulation spreadsheet. This data file models the complete hydraulic circuit for the new 2.0-liter Panther EcoBlue diesel engine. The bill of materials confirms the exact supplier interfaces: a LuK self-adjusting clutch, FTE aluminium concentric slave cylinder, FTE in-line vibration damper, and FTE master cylinder. The file models the pedal box using KSR International's theoretical over-center spring curve. The simulation proves out our target operating envelope: peak pedal force reaches 113.4 Newtons at 93.4 millimeters of stroke, well within Ford's ergonomic limit of 120 Newtons. This file gives our simulation engineers the exact input curves required to validate our kinematic CAD and spring selection before submitting our quotation."*

---

### Slide 19: Supplier Launch Roadmap: Ford GPDS Gateways & Milestones

* **Category:** Gateway Execution • Slide 19 / 20
* **Target Timing:** 28:00 - 29:30
* **Visual Layout:** Horizontal GPDS gateway chevron timeline linking Pre-Program, Design Freeze, Tooling Kick-Off, Prototype Fleets, PPAP, and Job 1.
* **Core Slide Content:**
  * **Program Management Framework:** Ford Global Product Development System (GPDS).
  * **Key Gateway Milestones & Supplier Deliverables:**
    1. *Strategic Intent (SI) & Confirmation (SC):* Initial packaging feasibility, kinematic clearance verification, and preliminary DFMEA submission.
    2. *Final Data Judgement (FDJ) / Design Freeze:* Absolute geometric freeze of CAD models in Teamcenter; formal approval of DFM; commitment point of no return for hard tooling.
    3. *Tooling Kick-Off (TKO):* Release of multimillion-pound capital expenditure for production stamping dies, injection moulds, and automated welding/assembly cells.
    4. *Verification Prototypes (VP Beta 0 & Beta 1):* Assembly and delivery of prototype pedal boxes for off-tool prototype vehicle builds and crash test sled fleets.
    5. *Tooling Tryout (TT):* First off-tool parts (100% CMM inspection, gauge tuning, initial dimensional verification).
    6. *Pilot Production (PP) & Pilot Series:* Run-at-rate production line verification at supplier manufacturing plant ($C_{pk} \ge 1.67$; Gage R&R $< 10\%$).
    7. *Mass Production 1 (MP1) & PSW Sign-Off:* Submission of all 18 PPAP elements; formal engineering sign-off on Part Submission Warrant (PSW).
    8. *Job 1 / Start of Production (SOP):* Serial volume production ramp-up at Ford assembly plants supported on-site through Job 1 + 90 days.
* **Technical Deep-Dive Callout:**
  > *In GPDS timing, missing the FDJ (Final Data Judgement) gateway delays the entire vehicle program by weeks, incurring massive financial penalties. Tooling cannot be cut until FDJ data is locked.*
* **Spoken Presenter Script (Speaker Notes):**
  > *"Slide 19 maps our execution roadmap across the Ford Global Product Development System, or GPDS. Automotive engineering is governed by strict stage-gate discipline. Our journey begins at Strategic Confirmation with packaging clash resolution. The most critical upstream milestone is FDJ, or Final Data Judgement—this is the design freeze gateway where our CATIA CAD models are locked in Teamcenter, triggering Tooling Kick-Off. During the VP prototype phases, we must supply physical off-tool prototype assemblies for Ford's vehicle test fleet and crash sled testing. Downstream, during Tooling Tryout and Pilot Production, we conduct capability studies on our production lines to prove Cpk greater than 1.67. Finally, at Mass Production 1, we submit all eighteen PPAP elements to achieve legal Part Submission Warrant sign-off prior to Job 1 volume ramp-up."*

---

### Slide 20: Quotation Checklist, Cost BOM & Technical Risk Assessment

* **Category:** Sourcing Summary • Slide 20 / 20
* **Target Timing:** 29:30 - 30:00+
* **Visual Layout:** Executive summary card divided into Commercial Cost BOM, Technical Risk Register, Tooling Investments, and Action Item Assignments.
* **Core Slide Content:**
  * **Commercial Quotation Breakdown:**
    * *Piece Cost BOM:* Stamped steel vs. moulded polymer bracket; pedal arm; pivot pin & bushings; over-center spring; rubber/decorative pads; hardware fasteners.
    * *Tooling Capital Investment (Capex):* Progressive stamping dies, composite injection moulds, assembly framing fixtures, 100% automated EOL test tester.
    * *Engineering & Development (D&D):* CATIA V5 CAD design, LS-DYNA crash CAE, prototype test builds, DVP&R laboratory test execution.
  * **Technical Risk Assessment & Mitigation:**
    * *Risk 1 (Packaging Congestion):* Tight clearance to steering shaft and HVAC case $\rightarrow$ *Mitigation: Early DMU sweeps using transparent envelopes per BR-1119.*
    * *Risk 2 (Dash Deflection):* Bulkhead flexing under 1000 N abuse load $\rightarrow$ *Mitigation: Topology-optimized bracket flanging per BR-1127.*
    * *Risk 3 (Crash Breakaway):* Inconsistent pivot release during offset crash $\rightarrow$ *Mitigation: Calibrated shear mechanism validated via dynamic LS-DYNA simulation.*
  * **Immediate Action Plan:**
    1. Complete kinematic synthesis of over-center spring curves in CATIA DMU.
    2. Validate Panther diesel hydraulic curves against CY-0002.
    3. Sign and execute Ford Design Feasibility Form 06.
    4. Submit complete commercial quotation pack to Stefanie Reinert by target deadline.
* **Technical Deep-Dive Callout:**
  > *Winning a Ford sourcing contract requires a balanced submission: an aggressive commercial piece price underpinned by an unassailable technical feasibility assessment.*
* **Spoken Presenter Script (Speaker Notes):**
  > *"To conclude our presentation on Slide 20, we summarize our quotation action plan and technical risk register. In our commercial submission to Stefanie Reinert, we must provide a detailed breakdown covering piece price, tooling capital, and D&D engineering costs. Our technical risk analysis highlights three critical focus areas: first, managing tight spatial clearances to the steering column using dynamic DMU envelopes; second, ensuring high structural stiffness to satisfy the BR-1127 dash deflection limits; and third, validating the crash breakaway mechanism in LS-DYNA to guarantee lower limb protection. By leveraging our deep experience across Ford platforms and following the exact requirements of this RFQ pack, our team is positioned to deliver a world-class, highly competitive engineering proposal. Thank you, and I look forward to your questions."*

---

## Complete RFQ Pack File Inventory & Technical Reference Table

The following master index provides a complete, itemized audit of every single file contained within the `C:\\tmp\\00-Mycat\\Engineering\\PEDAL-PACK` directory, detailing its engineering scope, format, and Tier-1 action required:

| # | Subdirectory | File Name | Size / Pages | Document Type / Standard | Engineering Purpose & Tier-1 Scope |
| :-: | :--- | :--- | :-: | :--- | :--- |
| **01** | `Root` | `Contact-Request for Information.docx` | 14 KB | Word Document | Ford Merkenich contact sheet: Chassis Core Engineer (Christina Kallas), Supervisor (Steffen Schoenfuss), Commercial Buyer (Stefanie Reinert). |
| **02** | `Clutch Pedal` | `Base Document_ESOW v20 updated jun2016-CD4-24May2017.pdf` | 14 Pages | Corporate ESOW Template | Master technical contract. Establishes CD4.1/CD4.2 scope, CAD/CAE deliverables, Job 1 + 90 days support, 135 mm stroke, crash feature, BOT switch. |
| **03** | `Clutch Pedal` | `060602_ESOW_PBOX_FD_ATT-9.pdf` | 5 Pages | Component SOW Appendix | Specific Pedal Box rules: Tooling tuning capability, switch flag angle ($-4^\circ$ to $-6^\circ$), WSS interior odor/fogging, on-site prototype support. |
| **04** | `Clutch Pedal` | `060602_ES_PB_20160628.pdf` | 66 Pages | Master Engineering Spec | Comprehensive DVP&R testing bible: Durability (1M cycles, $-40^\circ\text{C}$ to $+80^\circ\text{C}$), structural abuse (1000 N clutch / 2000 N brake), lateral play, EOL testing. |
| **05** | `Clutch Pedal` | `BR-1119.pdf` | 12 Pages | Ford Custom Standard | Clutch Pedal Clearance and Layout: ECE R35 pedal spacing ($50\text{ mm}$ to brake/footrest), steering shaft clearance ($15\text{ mm}$), transparent CAD envelopes. |
| **06** | `Clutch Pedal` | `BR-1127.pdf` | 42 Pages | Ford Custom Standard | Dash Panel and Pedal Box Deflection: Bulkhead rigidity limits ($<1.5\text{ mm}$ @ 400 N), lateral play ($<3\text{ mm}$), 1000 N abuse integrity. |
| **07** | `Clutch Pedal` | `CY-0002.pdf` | 23 Pages | Ford Custom Standard | Clutch Pedal Travel: Kinematic travel targets ($135\text{ mm}$ nominal), over-center spring snap-over, effort hysteresis, 3 required CAD articulation states. |
| **08** | `Clutch Pedal` | `060602_SCCAF_PBOX_FD.xls` | 165 KB | Excel Form | Special Characteristics Communication & Agreement Form (FAP03-111). Cascades Critical ($\nabla$ CC) and Significant (SC) characteristics to Control Plans. |
| **09** | `Clutch Pedal` | `crs_sim_data_out_18-May-2017_Panter.xlsx` | 1.8 MB | Excel Simulation | Hydraulic release simulation data for Panther 2.0L Diesel. LuK clutch, FTE slave/master cylinder, KSR pedal box proposal ($F_{pMax} = 113.4\text{ N}$). |
| **10** | `Clutch Pedal` | `CAE_specific_Chassis _ATTACHMENT_v77.pdf` | 2 Pages | Corporate SOW Appendix | Chassis CAE Specific Attachment: Global meshing guidelines (`00.00-C-602`), Abaqus material decks, rubber hyperelastic models, crash FEA timing. |
| **11** | `Clutch Pedal` | `6G9T-11A152-AA.pdf` | 1 Page | Engineering Drawing | Part print for EUCD/CD4 heritage clutch pedal bracket / switch stop bracket reference. |
| **12** | `General` | `01a CAD_C3PNG_V3_6 jun2016.pdf` | 8 Pages | Corporate Standard | CAD C3PNG standards: Native CATIA V5 modeling, Teamcenter Enterprise (TCE) release, seed files, global coordinate alignment. |
| **13** | `General` | `01b CAE_ ESOW_Attachment1b_2014-Mar_V2.pdf` | 6 Pages | Corporate Standard | CAE Integration SOW: Digital innovation, finite element mesh guidelines, structural and crash simulation boundary conditions. |
| **14** | `General` | `02 Failure Mode Avoidance Attachment 02 update dec2015.pdf` | 5 Pages | Corporate Standard | FMA Guidelines: Boundary diagrams, P-Diagrams, DFMEA v4.2 compliance, Severity $\ge 8$ mandatory redesign rule. |
| **15** | `General` | `03 Envionment_Recyc_attach 3_0 _LV_2014 July 25.pdf` | 9 Pages | Corporate Standard | Environmental & Recycling: IMDS material reporting, RRR Directive 2005/64/EC ($>85\%$ recyclability), `WSS-M99P9999-A1` restricted substances. |
| **16** | `General` | `04 Global Regulatory and Safety Compliance & Type Approval Attachment update jun2016.pdf` | 2 Pages | Corporate Standard | Regulatory compliance: ECE R35 (pedal spacing), ECE R12 (intrusion), FMVSS 124 (accelerator returnability), FMVSS 208/214 crash safety. |
| **17** | `General` | `05 ESOW_MSOW_Craftsmanship_Attachment5_v13_140318.pdf` | 3 Pages | Corporate Standard | Craftsmanship & Perceived Quality: Gaps, flushness, tactile feel, pedal pad alignment, squeak/rattle operating acoustic targets. |
| **18** | `General` | `06 Design Feasibility Attachment update jun2016.pdf` | 13 Pages | Corporate Standard | Design Feasibility Form 06: Formal Tier-1 executive engineering certification that part can be produced at volume capability. |
| **19** | `General` | `07 Materials Attachment 07 update dec2015.pdf` | 2 Pages | Corporate Standard | Materials Engineering: Approved material specifications (Ford WSS), plastic resins, steel alloys, salt spray corrosion protection. |
| **20** | `General` | `08 Supplier Ford Web Based Data Manage update jun2016.pdf` | 8 Pages | Corporate Standard | Web-Based Data Management: Supplier portal access via Covisint, Ford Supplier Portal (FSP), WERS, and GSDB administration. |
| **21** | `General` | `09 COMPONENT_HOMOLOGATION_GENERAL_ATTACHMENT_v1 3.pdf` | 2 Pages | Corporate Standard | Component Homologation: European E-marking, Conformity of Production (CoP) audits, regulatory test certification. |
| **22** | `General` | `10 Ford_CyberAssurance-SOW_ReleaseV1.0.pdf` | 16 Pages | Corporate Standard | Ford CyberAssurance SOW: Supplier cybersecurity governance, IT/OT network defense, CAD intellectual property protection. |
| **23** | `General` | `19-0108 DIRECTIVE E-108 GLOBAL PARTS TRADEMARKS.pdf` | 21 Pages | Corporate Standard | Directive E-108: Global Parts Trademarks, Ford Oval logo placement, engineering part numbering, supplier code, date clocks. |
| **24** | `CAD` | `41-LHD-Electrical.stp` | 40.8 MB | 3D STEP Model | CD4.1 LHD wiring harness routes, body harness take-outs, fuse box clearance. |
| **25** | `CAD` | `41-LHD-Steering.stp` | 13.3 MB | 3D STEP Model | CD4.1 LHD steering column lower shaft and universal joint packaging. |
| **26** | `CAD` | `41-RHD-Electrical.stp` | 13.6 MB | 3D STEP Model | CD4.1 RHD wiring harness routing and cross-car electrical packaging. |
| **27** | `CAD` | `41-RHD-Steering.stp` | 7.9 MB | 3D STEP Model | CD4.1 RHD steering column lower shaft clearance envelope. |
| **28** | `CAD` | `BOT-LHD-41.stp` | 5.5 MB | 3D STEP Model | CD4.1 LHD Bottom-of-Travel (BOT) switch geometry, connector, and mounting bayonet. |
| **29** | `CAD` | `BOT-RHD-41.stp` | 5.5 MB | 3D STEP Model | CD4.1 RHD Bottom-of-Travel (BOT) switch geometry and mounting interface. |
| **30** | `CAD` | `CD4.1-LHD-PAD.stp` | 1.2 MB | 3D STEP Model | CD4.1 LHD standard rubber pedal pad nominal contact face coordinates. |
| **31** | `CAD` | `CD4.1-RHD-PAD.stp` | 0.8 MB | 3D STEP Model | CD4.1 RHD standard rubber pedal pad nominal contact face coordinates. |
| **32** | `CAD` | `CD41-LHD-FOOT-Zone.stp` | 0.3 MB | 3D STEP Model | CD4.1 LHD dynamic driver foot clearance envelope per SAE J1100. |
| **33** | `CAD` | `CD41-RHD-FOOT-Zone.stp` | 0.4 MB | 3D STEP Model | CD4.1 RHD dynamic driver foot clearance envelope per SAE J1100. |
| **34** | `CAD` | `CD42-LHD-PAD.stp` | 0.8 MB | 3D STEP Model | CD4.2 LHD pedal pad nominal spatial location (S-MAX/Galaxy/Edge). |
| **35** | `CAD` | `CD42-RHD-PAD.stp` | 1.2 MB | 3D STEP Model | CD4.2 RHD pedal pad nominal spatial location (S-MAX/Galaxy/Edge). |
| **36** | `CAD` | `Carpet-LHD.stp` | 10.3 MB | 3D STEP Model | CD4 LHD molded floor carpet thickness and underlay contour under pedal travel. |
| **37** | `CAD` | `Carpet-RHD.stp` | 16.4 MB | 3D STEP Model | CD4 RHD molded floor carpet thickness and underlay contour under pedal travel. |
| **38** | `CAD` | `Carpet-LHD-RHD.stp` | 64.2 MB | 3D STEP Model | CD4 combined LHD and RHD master floor carpet assembly model. |
| **39** | `CAD` | `Dash-Hole.stp` | 2.0 MB | 3D STEP Model | Bulkhead / firewall pass-through aperture for master cylinder barrel and pushrod. |
| **40** | `CAD` | `Dash-LHD.stp` | 8.9 MB | 3D STEP Model | Master LHD dash bulkhead sheet metal stamping and mounting stud locations. |
| **41** | `CAD` | `Dash-RHD.stp` | 3.3 MB | 3D STEP Model | Master RHD dash bulkhead sheet metal stamping and mounting stud locations. |
| **42** | `CAD` | `Decorative-Pad-LHD-CD41.stp` | 3.8 MB | 3D STEP Model | CD4.1 LHD sports styling brushed aluminium decorative pedal pad model. |
| **43** | `CAD` | `HVAC-CD4.1-RHD.stp` | 5.6 MB | 3D STEP Model | CD4.1 RHD climate control distribution housing packaging envelope. |
| **44** | `CAD` | `LHD-41-Dash.stp` | 2.5 MB | 3D STEP Model | CD4.1 LHD dash panel detail section at pedal box mounting interface. |
| **45** | `CAD` | `LHD-41-SideL.stp` | 11.4 MB | 3D STEP Model | CD4.1 LHD structural cowl side member bounding pedal box on the left. |
| **46** | `CAD` | `LHD-42-Foot-zone.stp` | 0.2 MB | 3D STEP Model | CD4.2 LHD driver foot clearance zone envelope (S-MAX/Galaxy). |
| **47** | `CAD` | `LHD-Lower-Fixing.stp` | 4.5 MB | 3D STEP Model | LHD lower mounting studs and chassis floor reinforcement interface. |
| **48** | `CAD` | `NVH-cd41.stp` | 32.3 MB | 3D STEP Model | CD4.1 heavy-layer acoustic sound dampening barrier across dash panel. |
| **49** | `CAD` | `NVH-RHD-LHD-CD42.stp` | 119.2 MB | 3D STEP Model | CD4.2 master heavy-layer acoustic insulation barrier across firewall. |
| **50** | `CAD` | `RHD-41-Dash.stp` | 1.2 MB | 3D STEP Model | CD4.1 RHD dash panel detail section at pedal box mounting interface. |
| **51** | `CAD` | `RHD-42-Foot-zone.stp` | 0.2 MB | 3D STEP Model | CD4.2 RHD driver foot clearance zone envelope (S-MAX/Galaxy). |
| **52** | `CAD` | `RHD-Lower-Fixing.stp` | 0.7 MB | 3D STEP Model | RHD lower mounting studs and chassis floor reinforcement interface. |
| **53** | `CAD` | `Steeering cd41-lhd-rhd.stp` | 48.3 MB | 3D STEP Model | CD4.1 master steering column intermediate shaft and kinematic universal joints. |
| **54** | `CAD` | `Steering cd42-lhd-rhd.stp` | 38.6 MB | 3D STEP Model | CD4.2 master steering column intermediate shaft and kinematic universal joints. |
| **55** | `CAD` | `cd41-LHD-Crash.stp` | 1.1 MB | 3D STEP Model | CD4.1 LHD crash intrusion vectors, knee zones, and pedal breakaway clearance. |
| **56** | `CAD` | `cd41-RHD-Crash.stp` | 0.7 MB | 3D STEP Model | CD4.1 RHD crash intrusion vectors, knee zones, and pedal breakaway clearance. |

---

## Conclusion & Next Steps

This markdown document provides the complete presentation architecture and slide-by-slide text for review. To proceed, this content can be:
1. Reviewed and edited directly in this file.
2. Compiled into a widescreen PowerPoint presentation (.pptx) or interactive web deck.
3. Ingested directly into **Google NotebookLM** to generate modular slide decks or audio briefing podcasts via the `notebooklm` CLI.
"""

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"Successfully generated markdown presentation content ({len(content)} chars): {output_path}")

if __name__ == "__main__":
    generate_rfq_presentation_md()
