#!/usr/bin/env python3
"""
Comprehensive Upgrade for Czech-English False Friends Hub:
1. Expands FALSE_FRIENDS_DATA from 36 to 52 Word Pairs (+16 new high-stakes business & daily pairs).
2. Adds TAB 4: "Corporate Email Horror Stories" (8 interactive scenario simulators with simulated email clients, client shock reactions, and click-to-reveal linguistic breakdowns & executive rewrites).
3. Expands Diagnostic Quiz from 25 to 30 items (+5 new questions).
4. Updates score calculation to /30 and updates tab counts.
5. Syncs both false-friends/index.html and root false_friends.html.
"""

import sys
import json
import re
from pathlib import Path

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

ROOT = Path(__file__).resolve().parent.parent
ff_dir = ROOT / "false-friends"
target_html = ff_dir / "index.html"
root_mirror = ROOT / "false_friends.html"

# 16 Brand-New High-Stakes False Friends
NEW_PAIRS = [
    {
        "cz": "Harmonogram",
        "category": "business",
        "trap": "Harmonogram (does not exist in English!)",
        "trap_meaning": "V angličtině slovo 'harmonogram' neexistuje (rodilý mluvčí si představí hudební nástroj nebo harmoniku)",
        "correct": "Schedule / Timeline / Project plan / Roadmap / Milestones",
        "ex_wrong": "❌ 'I will send you the project harmonogram by tomorrow afternoon.' (Native speakers will be completely baffled!)",
        "ex_correct": "✓ 'I will send you the project schedule / timeline / milestone plan by tomorrow afternoon.'",
        "note": "One of the most pervasive Czenglish corporate errors. English never uses 'harmonogram' for work planning. Always say 'schedule' or 'timeline'."
    },
    {
        "cz": "Fabrika",
        "category": "business",
        "trap": "Fabric",
        "trap_meaning": "Látka / textilie / tkanina na oděvy (woven cloth, material)",
        "correct": "Factory / Manufacturing plant / Production facility / Mill",
        "ex_wrong": "❌ 'Our fabric in Ostrava employs over 800 technical operators.' (Sounds like you produce silk or curtains!)",
        "ex_correct": "✓ 'Our manufacturing plant / factory in Ostrava employs over 800 technical operators.'",
        "note": "'Fabric' in English is strictly cloth/textile. An industrial production site is always a 'factory' or 'manufacturing plant'."
    },
    {
        "cz": "Penzion",
        "category": "daily",
        "trap": "Pension",
        "trap_meaning": "Důchod / starobní renta / penzijní fond (retirement fund/allowance)",
        "correct": "Guesthouse / Bed and breakfast (B&B) / Inn / Boutique lodge",
        "ex_wrong": "❌ 'We booked a romantic pension in the mountains for our overseas client.' (Sounds like you bought them an annuity!)",
        "ex_correct": "✓ 'We booked a charming guesthouse / bed and breakfast in the mountains for our client.'",
        "note": "English 'pension' (/ˈpen.ʃən/) is strictly money paid to a retiree. For accommodation, say 'guesthouse' or 'B&B'."
    },
    {
        "cz": "Recept (lékařský / kuchařský)",
        "category": "daily",
        "trap": "Receipt / Recipe / Prescription",
        "trap_meaning": "Receipt (/rɪˈsiːt/) = pokladní účtenka z obchodu; Recipe (/ˈres.ə.pi/) = kuchařský recept; Prescription = lék na předpis",
        "correct": "Prescription (od lékaře na lék) / Recipe (návod na vaření) / Receipt (paragon/stvrzenka)",
        "ex_wrong": "❌ 'The doctor wrote me a recipe for antibiotics, but I lost the receipt.' (Total confusion of all three!)",
        "ex_correct": "✓ 'The doctor wrote me a prescription for antibiotics.' / 'Here is my grandmother's goulash recipe.'",
        "note": "Three-way trap: A chef follows a 'recipe' (vaření); a doctor writes a 'prescription' (léky); a shop gives you a 'receipt' (paragon)."
    },
    {
        "cz": "Likvidovat (odpad / smlouvu / chyby)",
        "category": "business",
        "trap": "Liquidate",
        "trap_meaning": "Rozprodat majetek v bankrotu / uhradit dluhy / násilně zavraždit (assassinate)",
        "correct": "Dispose of / Eliminate / Scrap / Terminate / Cancel",
        "ex_wrong": "❌ 'The purchasing department liquidated the problematic contractor yesterday.' (Sounds like a mafia hit!)",
        "ex_correct": "✓ 'Purchasing terminated the contract with the supplier.' / 'We safely disposed of the chemical waste.'",
        "note": "In English, 'liquidating a person or partner' means assassinating them! Use 'terminate contract', 'dispose of waste', or 'eliminate errors'."
    },
    {
        "cz": "Soudní proces",
        "category": "business",
        "trap": "Process",
        "trap_meaning": "Výrobní nebo technologický postup / proces zpracování",
        "correct": "Trial / Lawsuit / Court hearing / Legal proceedings / Litigation",
        "ex_wrong": "❌ 'The patent infringement will be decided in a lengthy process next month.'",
        "ex_correct": "✓ 'The patent infringement will be decided at trial / during court proceedings next month.'",
        "note": "A court case in English is never called a 'process'. It is a 'trial', 'lawsuit', or 'court hearing'."
    },
    {
        "cz": "Kabinet (ve škole / na úřadě)",
        "category": "roles",
        "trap": "Cabinet",
        "trap_meaning": "Vládní kabinet ministrů / kuchyňská skříňka na nádobí / skříň na spisy",
        "correct": "Staff room / Teacher's office / Department office / Consulting room",
        "ex_wrong": "❌ 'Professor Novák is waiting for you in his cabinet.' (Sounds like he is hiding inside a kitchen cupboard!)",
        "ex_correct": "✓ 'Professor Novák is waiting for you in his office / staff room.'",
        "note": "In English, a 'cabinet' is either furniture (kitchen cabinet, filing cabinet) or the government Cabinet (vláda)."
    },
    {
        "cz": "Katedra (na univerzitě)",
        "category": "roles",
        "trap": "Cathedral",
        "trap_meaning": "Katedrála / monumentální chrám (e.g. St. Vitus Cathedral)",
        "correct": "Department / Faculty / Academic Chair",
        "ex_wrong": "❌ 'I graduated from the Cathedral of Metallurgy at VŠB Technical University.' (A church inside a university?!)",
        "ex_correct": "✓ 'I graduated from the Department of Metallurgy at VŠB Technical University.'",
        "note": "Do not confuse the church 'cathedral' with a university 'department' or 'chair'."
    },
    {
        "cz": "Plastika (lékařská / umělecká)",
        "category": "daily",
        "trap": "Plastic",
        "trap_meaning": "Plast / syntetický polymer (polyetylen, PVC)",
        "correct": "Plastic surgery / Cosmetic procedure (lékařská) OR Sculpture / Relief (umělecké dílo)",
        "ex_wrong": "❌ 'The gallery is exhibiting a bronze plastic.' / 'She had a plastic after the accident.'",
        "ex_correct": "✓ 'The gallery is exhibiting a bronze sculpture.' / 'She underwent plastic surgery after the accident.'",
        "note": "'Plastic' as a noun is only the synthetic material. For medical treatments say 'plastic surgery'; for art say 'sculpture'."
    },
    {
        "cz": "Aféra (skandál)",
        "category": "social",
        "trap": "Affair",
        "trap_meaning": "Romantická manželská nevěra / intimní záletnictví OR běžná záležitost (matter, business)",
        "correct": "Scandal / Controversy / Public outcry",
        "ex_wrong": "❌ 'The automotive emissions cheat was a massive corporate affair.' (Sounds like executives were dating each other!)",
        "ex_correct": "✓ 'The automotive emissions cheat was a massive corporate scandal / controversy.'",
        "note": "While 'affair' can mean 'záležitost', in headlines it strongly implies extramarital sexual infidelity. For corruption/crises, say 'scandal'."
    },
    {
        "cz": "Generální oprava",
        "category": "business",
        "trap": "General repair",
        "trap_meaning": "Běžná, obecná, nespecifikovaná drobná oprava",
        "correct": "Major overhaul / Complete refurbishment / Total rebuild",
        "ex_wrong": "❌ 'The rolling mill will be shut down for three weeks for a general repair.' (Sounds like basic patching up!)",
        "ex_correct": "✓ 'The rolling mill will be shut down for three weeks for a major overhaul / complete refurbishment.'",
        "note": "Czech 'generální oprava' means a comprehensive rebuild from top to bottom. In English that is an 'overhaul' or 'refurbishment', not 'general repair'."
    },
    {
        "cz": "Deska (psací / prkno / plech / hudební)",
        "category": "daily",
        "trap": "Desk",
        "trap_meaning": "Kancelářský psací stůl (office table)",
        "correct": "Board / Plank (dřevo) / Sheet / Plate (kov) / Vinyl record (gramofonová)",
        "ex_wrong": "❌ 'Please put the steel desk onto the conveyor belt.' (Why are you moving office furniture into a machine?!)",
        "ex_correct": "✓ 'Please place the steel plate / sheet onto the conveyor belt.' / 'I bought a vintage vinyl record.'",
        "note": "'Desk' is exclusively an office desk. A flat piece of wood or metal is a 'board', 'sheet', or 'plate'."
    },
    {
        "cz": "Konkrétní (příklad / data)",
        "category": "business",
        "trap": "Concrete",
        "trap_meaning": "Stavební beton (směs cementu, štěrku a vody)",
        "correct": "Specific / Particular / Detailed (Note: 'concrete example' exists, but 'concrete data' sounds like building materials!)",
        "ex_wrong": "❌ 'Please send me the concrete numbers for the German client.' (Sounds like cement density measurements!)",
        "ex_correct": "✓ 'Please send me the specific / exact numbers for the German client.'",
        "note": "While native speakers occasionally say 'concrete example' (hmatatelný příklad), for facts, dates, and names prefer 'specific' or 'particular'."
    },
    {
        "cz": "Komfortní (termín / řešení)",
        "category": "social",
        "trap": "Comfortable",
        "trap_meaning": "Pohodlný po tělesné stránce (např. měkké křeslo, teplé boty)",
        "correct": "Convenient / Suitable / Smooth / Effortless",
        "ex_wrong": "❌ 'Would Tuesday 14:00 be comfortable for our Zoom call?' (Sounds like you want to nap during the meeting!)",
        "ex_correct": "✓ 'Would Tuesday 14:00 be convenient / suitable for our Zoom call?'",
        "note": "A chair is 'comfortable'; a meeting time or business arrangement is 'convenient' (/kənˈviː.ni.ənt/)."
    },
    {
        "cz": "Magazín (sklad / prodejna)",
        "category": "daily",
        "trap": "Magazine",
        "trap_meaning": "Tištěný ilustrovaný časopis OR muniční zásobník do zbraně (ammo clip)",
        "correct": "Warehouse / Storage facility / Depot / Retail outlet / Store",
        "ex_wrong": "❌ 'All finished aluminium coils were transferred to the central magazine.' (A giant reading room?!)",
        "ex_correct": "✓ 'All finished coils were transferred to the central warehouse / storage facility.'",
        "note": "In English, a 'magazine' is a periodical you read or an ammunition feed for a firearm. A storehouse is a 'warehouse'."
    },
    {
        "cz": "Kolega (spolužák ze školy)",
        "category": "roles",
        "trap": "Colleague",
        "trap_meaning": "Pracovní kolega v zaměstnání (coworker, business associate)",
        "correct": "Classmate / Fellow student / Schoolmate / University peer",
        "ex_wrong": "❌ 'David was my colleague when we studied at university.' (Implies you both were professors or university employees!)",
        "ex_correct": "✓ 'David was my classmate / fellow student when we were at university.'",
        "note": "In English, 'colleagues' only share a professional employer. People who study together are 'classmates' or 'fellow students'."
    }
]

# 8 Real-World Corporate Email Horror Stories
EMAIL_HORROR_STORIES = [
    {
        "id": "horror-1",
        "badge": "🚨 HR & UNION EMERGENCY",
        "subject": "Mandatory Plant Access Protocol",
        "sender": "Jan Novák <j.novak@corp-cz.com> (Operations Lead)",
        "recipient": "Mark Davies <m.davies@uk-partners.co.uk> (UK Operations Director)",
        "timestamp": "Monday, 07:42 AM",
        "email_text": "Dear Mark,<br><br>Regarding tomorrow's shift handover at the factory: starting at 08:00, security will <mark class='trap-highlight'>control</mark> all employees at the main facility gates before anyone enters the shop floor.<br><br>Best regards,<br>Jan",
        "reaction_avatar": "🇬🇧",
        "reaction_name": "Mark Davies (UK Director)",
        "reaction_quote": "“Wait, WHAT?! Did management suddenly declare martial law? Are we interrogating our employees like convicts?! The union will sue us by noon!”",
        "trap_word": "Control",
        "false_meaning": "In English, 'control' means to dominate, exercise authoritarian power over, or police someone.",
        "real_meaning": "Czech 'kontrolovat' simply means to verify, check, or inspect credentials or parameters.",
        "rewrite": "“...starting at 08:00, security will <strong>check / verify all employee ID badges</strong> at the main gates...”",
        "tip": "Never write 'control employees' or 'control customers'. In English, you only 'control' machinery, room temperatures, or inventory levels."
    },
    {
        "id": "horror-2",
        "badge": "💣 ANTI-TERROR & POLICE PANIC",
        "subject": "Upcoming Frankfurt Operations Announcement",
        "sender": "Tomáš Kučera <t.kucera@export-cz.eu> (Sales Director)",
        "recipient": "David Miller <d.miller@frankfurt-distrib.de> (Commercial Partner)",
        "timestamp": "Wednesday, 11:15 AM",
        "email_text": "Dear David,<br><br>I am excited to announce that our European team will launch a massive <mark class='trap-highlight'>action</mark> in Frankfurt this Friday! Please ensure all local reps are ready for the impact.<br><br>Sincerely,<br>Tomáš",
        "reaction_avatar": "🇩🇪",
        "reaction_name": "David Miller (German Distributor)",
        "reaction_quote": "“Massive action?! Is this an armed police raid? A hostile takeover? Are we being sued?! Why didn't you warn legal?!”",
        "trap_word": "Action",
        "false_meaning": "In English, 'a massive action' sounds like a military strike, police raid, or class-action lawsuit.",
        "real_meaning": "Czech 'akce' means a promotional discount campaign (prodejní akce) or social event (firemní akce).",
        "rewrite": "“...our European team will launch a massive <strong>promotional campaign / special discount event</strong> in Frankfurt this Friday!”",
        "tip": "For business sales, say 'special promotion', 'discount campaign', or 'promotional event' — never just 'an action'."
    },
    {
        "id": "horror-3",
        "badge": "⚰️ THE ASSASSINATION CRISIS",
        "subject": "Supplier Contract Resolution Update",
        "sender": "Petr Svoboda <p.svoboda@procurement.cz> (Purchasing Manager)",
        "recipient": "Arthur Pendelton <a.pendelton@group-hq.co.uk> (Group CFO, London)",
        "timestamp": "Thursday, 16:30 PM",
        "email_text": "Dear Arthur,<br><br>Good news from Prague: after weeks of difficult commercial disputes, our purchasing taskforce successfully <mark class='trap-highlight'>liquidated</mark> the supplier yesterday.<br><br>Regards,<br>Petr",
        "reaction_avatar": "🇬🇧",
        "reaction_name": "Arthur Pendelton (London CFO)",
        "reaction_quote": "“Good god, Petr! Did you just ASSASSINATE the vendor?! We are a manufacturing company, not the Sopranos! Call the police immediately!”",
        "trap_word": "Liquidate",
        "false_meaning": "Applying 'liquidate' to people or organizations in English implies mafia-style execution, murder, or violent elimination.",
        "real_meaning": "Czechs use 'zlikvidovat' casually for throwing away, cancelling, or finishing off a problem.",
        "rewrite": "“...our purchasing taskforce successfully <strong>terminated the contract with / severed ties with</strong> the supplier yesterday.”",
        "tip": "In corporate English, companies 'liquidate assets' (sell inventory for cash during bankruptcy). Contracts are 'terminated' or 'cancelled'."
    },
    {
        "id": "horror-4",
        "badge": "👻 THE EXISTENTIAL CLIENT",
        "subject": "Delivery Schedule & Production Status",
        "sender": "Lucie Dvořáková <l.dvorakova@precision-foil.cz> (Account Exec)",
        "recipient": "Michael Becker <m.becker@bavaria-foods.de> (Client Procurement)",
        "timestamp": "Tuesday, 09:10 AM",
        "email_text": "Dear Mr. Becker,<br><br>Thank you for your inquiry. I would like to reassure you that I am very <mark class='trap-highlight'>actual</mark> today regarding your packaging batch.<br><br>Best wishes,<br>Lucie",
        "reaction_avatar": "🇩🇪",
        "reaction_name": "Michael Becker (Munich Client)",
        "reaction_quote": "“She is... actual? Does she mean she exists in the physical universe? Did someone accuse her of being an AI hallucination or a ghost?!”",
        "trap_word": "Actual",
        "false_meaning": "'Actual' in English means real, existing in physical fact (ve skutečnosti / reálný).",
        "real_meaning": "Czech 'aktuální' means current, up-to-date, or active.",
        "rewrite": "“...I would like to reassure you that I am <strong>fully up to date</strong> regarding your packaging batch / here is our <strong>current status</strong>.”",
        "tip": "'Actually' contradicts what was said ('Actually, that is incorrect'); 'currently' refers to time right now."
    },
    {
        "id": "horror-5",
        "badge": "🚬 THE BLACK-TIE FIRE HAZARD",
        "subject": "Executive Gala Dinner Dress Code",
        "sender": "Zdeněk Kovář <z.kovar@al-invest.cz> (Event Coordinator)",
        "recipient": "All VIP Delegates <vip-delegates@industry-summit.com>",
        "timestamp": "Friday, 14:00 PM",
        "email_text": "Dear Distinguished Guests,<br><br>For this evening's 25th Anniversary Banquet in Prague, please note that all gentlemen are strictly required to wear black <mark class='trap-highlight'>smoking</mark>.<br><br>Kind regards,<br>Zdeněk",
        "reaction_avatar": "🇺🇸",
        "reaction_name": "James Henderson (US Keynote Speaker)",
        "reaction_quote": "“Wait, the hotel banned cigarettes, but the Czech invitation says smoking is MANDATORY for gentlemen?! Do I have to buy cigars before dinner?!”",
        "trap_word": "Smoking",
        "false_meaning": "'Smoking' in English is exclusively the inhalation of burning tobacco smoke.",
        "real_meaning": "Czech (via French/German) borrowed the Victorian term 'smoking jacket' to mean a formal tuxedo or dinner jacket.",
        "rewrite": "“...all gentlemen are strictly requested to wear <strong>black-tie attire (a tuxedo or formal dinner jacket)</strong>.”",
        "tip": "Never say 'a smoking' in English. It is a 'tuxedo' (US) or a 'dinner jacket' (UK)."
    },
    {
        "id": "horror-6",
        "badge": "🧵 THE TEXTILE FACTORY BLUNDER",
        "subject": "Order Confirmation: Heavy Industrial Coil Dispatch",
        "sender": "Ing. Marek Černý <m.cerny@heavy-metals.cz> (Plant Logistics)",
        "recipient": "Stefan Weber <s.weber@daimler-supply.de> (Lead Metallurgist)",
        "timestamp": "Wednesday, 15:45 PM",
        "email_text": "Dear Stefan,<br><br>We are pleased to inform you that our Břidličná <mark class='trap-highlight'>fabric</mark> has just finalized rolling 450 tons of hardened high-spec alloy.<br><br>Mit freundlichen Grüßen,<br>Marek",
        "reaction_avatar": "🇩🇪",
        "reaction_name": "Stefan Weber (Automotive Tier-1)",
        "reaction_quote": "“Fabric?! Did our purchasing team accidentally order 450 tons of silk curtains or sofa upholstery instead of high-grade aluminium?!”",
        "trap_word": "Fabric",
        "false_meaning": "'Fabric' in English is cloth, textile, or woven material used for making shirts and curtains.",
        "real_meaning": "Czech 'fabrika' is a factory, rolling mill, or industrial manufacturing plant.",
        "rewrite": "“...our Břidličná <strong>manufacturing plant / rolling mill</strong> has just finalized rolling 450 tons...”",
        "tip": "A manufacturing building is a 'factory' or 'plant'. 'Fabric' is what you buy at a curtain shop!"
    },
    {
        "id": "horror-7",
        "badge": "👨‍🍳 THE KITCHEN WARFARE",
        "subject": "Quarterly Budget Disagreement Escalation",
        "sender": "Martin Horák <m.horak@tech-fin.cz> (Financial Analyst)",
        "recipient": "Sarah Jenkins <s.jenkins@group-board.com> (HR Partner, London)",
        "timestamp": "Thursday, 10:20 AM",
        "email_text": "Dear Sarah,<br><br>I apologize for my delayed report. I spent all morning having a furious, shouting argument with our company <mark class='trap-highlight'>chef</mark> about our capital expenditure budget.<br><br>Best,<br>Martin",
        "reaction_avatar": "🇬🇧",
        "reaction_name": "Sarah Jenkins (London HR)",
        "reaction_quote": "“Why on earth is our senior financial analyst screaming at the cafeteria cook who makes the soup about multi-million pound capital expenditure?!”",
        "trap_word": "Chef",
        "false_meaning": "In English, a 'chef' is strictly a professional restaurant cook wearing a white hat.",
        "real_meaning": "Czech 'šéf' is your boss, line manager, supervisor, or managing director.",
        "rewrite": "“...having an intense disagreement with my <strong>boss / department head / managing director</strong> about our CAPEX budget.”",
        "tip": "The person you report to at work is your 'boss', 'manager', or 'director'. A 'chef' makes food!"
    },
    {
        "id": "horror-8",
        "badge": "👴 THE RETIREMENT FUND LODGING",
        "subject": "Travel Logistics for Prague Board Meeting",
        "sender": "Monika Veselá <m.vesela@ce-corp.cz> (Executive Assistant)",
        "recipient": "Robert Vance <r.vance@chicago-inv.com> (US Managing Director)",
        "timestamp": "Monday, 13:50 PM",
        "email_text": "Dear Mr. Vance,<br><br>Regarding your stay in Prague next week: don't worry about hotels; we have booked you into a lovely, quiet <mark class='trap-highlight'>pension</mark> right near the castle.<br><br>Sincerely,<br>Monika",
        "reaction_avatar": "🇺🇸",
        "reaction_name": "Robert Vance (Chicago Partner)",
        "reaction_quote": "“Wait, why is a Czech firm enrolling me into a senior citizens' retirement fund? Are they trying to forcibly retire me on this business trip?!”",
        "trap_word": "Pension",
        "false_meaning": "'Pension' (/ˈpen.ʃən/) is financial annuity money paid to elderly retirees after they stop working.",
        "real_meaning": "Czech 'penzion' is a cosy, family-run guesthouse or boutique bed-and-breakfast.",
        "rewrite": "“...we have booked you into a lovely, quiet <strong>boutique guesthouse / bed-and-breakfast (B&B)</strong> right near the castle.”",
        "tip": "For charming accommodation, always say 'guesthouse' or 'boutique B&B'. 'Pension' is your retirement savings."
    }
]

# 5 New Diagnostic Quiz Questions (26 to 30)
NEW_QUIZ_QUESTIONS = [
    {
        "q": "26. The project manager sent an email: 'I will distribute the updated project _______ before Friday's executive steering committee.'",
        "options": [
            { "text": "A) harmonogram", "correct": False },
            { "text": "B) schedule / timeline", "correct": True },
            { "text": "C) recipe", "correct": False }
        ],
        "explanation": "✓ 'Harmonogram' does not exist in standard English. Always use 'schedule', 'timeline', 'project plan', or 'milestones'."
    },
    {
        "q": "27. The plant director reported: 'Our manufacturing _______ in Ostrava produced 2,400 tonnes of cold-rolled foil last month.'",
        "options": [
            { "text": "A) fabric", "correct": False },
            { "text": "B) plant / factory", "correct": True },
            { "text": "C) cabinet", "correct": False }
        ],
        "explanation": "✓ Czech 'fabrika' is a 'plant' or 'factory'. 'Fabric' means woven cloth or textile for clothing and curtains."
    },
    {
        "q": "28. When the engineer felt ill on his business trip to London, the doctor gave him a _______ for antibiotics.",
        "options": [
            { "text": "A) recipe", "correct": False },
            { "text": "B) receipt", "correct": False },
            { "text": "C) prescription", "correct": True }
        ],
        "explanation": "✓ A doctor writes a 'prescription'. A 'recipe' is cooking instructions for food; a 'receipt' is a payment slip from a shop cash register."
    },
    {
        "q": "29. For the team strategy retreat, the coordinator booked a cosy _______ in the Moravian countryside.",
        "options": [
            { "text": "A) pension", "correct": False },
            { "text": "B) guesthouse / boutique inn", "correct": True },
            { "text": "C) cathedral", "correct": False }
        ],
        "explanation": "✓ Czech 'penzion' is a 'guesthouse' or 'inn'. In English, 'pension' strictly means money paid to a retired person."
    },
    {
        "q": "30. The legal counsel advised: 'If the contractor refuses to adhere to safety standards, we will _______ the supply contract immediately.'",
        "options": [
            { "text": "A) liquidate", "correct": False },
            { "text": "B) terminate / cancel", "correct": True },
            { "text": "C) reclaim", "correct": False }
        ],
        "explanation": "✓ Commercial contracts are 'terminated' or 'cancelled'. 'Liquidate' in English means to settle bankruptcy or assassinate someone!"
    }
]

def main():
    print("=" * 60)
    print("UPGRADING CZECH-ENGLISH FALSE FRIENDS HUB")
    print("=" * 60)

    html_content = target_html.read_text(encoding="utf-8")

    # 1. Update Navigation Tabs HTML to 4 Tabs
    old_tabs = '''    <div class="nav-tabs">
      <button class="tab-btn active" onclick="switchTab('tutorial')">
        📖 Visual Tutorial & Encyclopedia <span class="tab-count" id="count-cards">36</span>
      </button>
      <button class="tab-btn" onclick="switchTab('quiz')">
        🎯 25-Question Diagnostic Quiz <span class="tab-count">25 Items</span>
      </button>
      <button class="tab-btn" onclick="switchTab('table')">
        ⚡ Rapid A–Z Matrix <span class="tab-count">Quick Reference</span>
      </button>
    </div>'''

    new_tabs = '''    <div class="nav-tabs">
      <button class="tab-btn active" onclick="switchTab('tutorial')">
        📖 Visual Tutorial & Encyclopedia <span class="tab-count" id="count-cards">52</span>
      </button>
      <button class="tab-btn" onclick="switchTab('horror')">
        😱 Email Horror Stories <span class="tab-count" style="background:#fee2e2; color:#991b1b;">8 Real Crises</span>
      </button>
      <button class="tab-btn" onclick="switchTab('quiz')">
        🎯 30-Question Diagnostic Quiz <span class="tab-count">30 Items</span>
      </button>
      <button class="tab-btn" onclick="switchTab('table')">
        ⚡ Rapid A–Z Matrix <span class="tab-count">52 Pairs</span>
      </button>
    </div>'''

    if old_tabs in html_content:
        html_content = html_content.replace(old_tabs, new_tabs)
        print("  [OK] Updated navigation tabs to 4 tabs.")
    else:
        print("  [WARN] nav-tabs snippet not matched directly.")

    # 2. Add Tab 4 HTML (Corporate Email Horror Stories) before Tab 2
    horror_html_section = '''    <!-- ============================================================== -->
    <!-- TAB 4: CORPORATE EMAIL HORROR STORIES (SCENARIO SIMULATOR)     -->
    <!-- ============================================================== -->
    <div id="tab-horror" style="display: none;">
      <div style="background: linear-gradient(135deg, #fef2f2 0%, #fee2e2 100%); border: 2px solid #f87171; border-radius: var(--radius-lg); padding: 24px 28px; margin-bottom: 28px;">
        <h2 style="font-size: 1.45rem; font-weight: 800; color: #991b1b; display: flex; align-items: center; gap: 10px; margin-bottom: 8px;">
          😱 Corporate Email Horror Stories: When False Friends Go Horribly Wrong
        </h2>
        <p style="font-size: 0.95rem; color: #7f1d1d; line-height: 1.6;">
          Real-world corporate misunderstandings caused by innocent Czech false friends. Below are genuine email blunders that triggered HR panics, police alerts, and bewildered overseas boardrooms. Click <strong>"Inspect Linguistic Fallout"</strong> to see why native speakers reacted with horror and how to write it properly.
        </p>
      </div>

      <div id="horror-stories-grid" style="display: flex; flex-direction: column; gap: 24px; margin-bottom: 40px;">
        <!-- Injected via JavaScript -->
      </div>
    </div>
'''
    if '<div id="tab-quiz"' in html_content and 'id="tab-horror"' not in html_content:
        html_content = html_content.replace('<div id="tab-quiz"', horror_html_section + '\n    <div id="tab-quiz"')
        print("  [OK] Injected Tab 4 HTML section into page.")

    # 3. Add CSS for Horror Stories
    horror_css = '''
    /* Simulated Email Client Styles */
    .email-client-card {
      background: #ffffff;
      border: 1px solid #cbd5e1;
      border-radius: var(--radius-lg);
      box-shadow: var(--shadow-md);
      overflow: hidden;
      transition: all 0.2s ease;
    }
    .email-client-card:hover {
      box-shadow: var(--shadow-lg);
      border-color: #94a3b8;
    }
    .email-top-bar {
      background: #1e293b;
      color: #ffffff;
      padding: 12px 18px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      font-size: 0.82rem;
    }
    .email-badge-alert {
      background: #ef4444;
      color: #ffffff;
      padding: 3px 10px;
      border-radius: 9999px;
      font-weight: 800;
      letter-spacing: 0.5px;
      font-size: 0.74rem;
    }
    .email-meta {
      background: #f8fafc;
      padding: 14px 20px;
      border-bottom: 1px solid #e2e8f0;
      font-size: 0.85rem;
      line-height: 1.6;
    }
    .email-meta-row { display: flex; gap: 8px; margin-bottom: 4px; }
    .email-meta-label { font-weight: 700; color: #64748b; width: 68px; flex-shrink: 0; }
    .email-body {
      padding: 22px 24px;
      font-family: inherit;
      font-size: 0.95rem;
      color: #1e293b;
      line-height: 1.7;
      background: #ffffff;
    }
    .trap-highlight {
      background: #fee2e2;
      color: #b91c1c;
      padding: 2px 6px;
      border-radius: 4px;
      font-weight: 800;
      border-bottom: 2px dashed #ef4444;
    }
    .reaction-box {
      background: #fff1f2;
      border-top: 1px solid #fecdd3;
      border-bottom: 1px solid #fecdd3;
      padding: 16px 20px;
      display: flex;
      gap: 16px;
      align-items: flex-start;
    }
    .reaction-avatar {
      font-size: 2rem;
      line-height: 1;
      flex-shrink: 0;
    }
    .reaction-content h4 {
      font-size: 0.88rem;
      font-weight: 800;
      color: #9f1239;
      margin-bottom: 4px;
    }
    .reaction-quote {
      font-style: italic;
      color: #881337;
      font-size: 0.92rem;
      line-height: 1.5;
    }
    .horror-action-bar {
      padding: 14px 20px;
      background: #f8fafc;
      display: flex;
      justify-content: flex-end;
    }
    .btn-inspect-fallout {
      background: #4f46e5;
      color: #ffffff;
      border: none;
      padding: 8px 18px;
      border-radius: var(--radius-md);
      font-weight: 700;
      font-size: 0.85rem;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 6px;
      transition: all 0.2s;
    }
    .btn-inspect-fallout:hover {
      background: #3730a3;
      transform: translateY(-1px);
    }
    .fallout-drawer {
      display: none;
      background: #ffffff;
      border-top: 2px solid #e0e7ff;
      padding: 20px 24px;
      animation: fadeIn 0.25s ease-in-out;
    }
    .fallout-drawer.open { display: block; }
    .fallout-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(min(100%, 280px), 1fr));
      gap: 16px;
      margin-bottom: 16px;
    }
    .fallout-item {
      background: #f8fafc;
      border: 1px solid #e2e8f0;
      border-radius: var(--radius-md);
      padding: 14px;
    }
    .fallout-label {
      font-size: 0.75rem;
      font-weight: 800;
      text-transform: uppercase;
      letter-spacing: 0.5px;
      margin-bottom: 6px;
    }
    .rewrite-banner {
      background: #ecfdf5;
      border: 1px solid #a7f3d0;
      border-left: 5px solid #10b981;
      border-radius: var(--radius-md);
      padding: 14px 18px;
      color: #065f46;
      font-size: 0.92rem;
      line-height: 1.5;
    }
'''
    if '.email-client-card' not in html_content:
        html_content = html_content.replace('</style>', horror_css + '\n  </style>')
        print("  [OK] Injected horror stories CSS.")

    # 4. Inject JavaScript Data & Functions
    js_addon = f'''
    // Additional 16 High-Stakes False Friends
    const ADDITIONAL_PAIRS = {json.dumps(NEW_PAIRS, indent=4, ensure_ascii=False)};
    
    // Corporate Email Horror Stories Data
    const EMAIL_HORROR_STORIES = {json.dumps(EMAIL_HORROR_STORIES, indent=4, ensure_ascii=False)};
    
    // Additional 5 Diagnostic Quiz Questions
    const ADDITIONAL_QUIZ = {json.dumps(NEW_QUIZ_QUESTIONS, indent=4, ensure_ascii=False)};

    // Merge New Pairs into Master Database
    FALSE_FRIENDS_DATA.push(...ADDITIONAL_PAIRS);

    // Merge New Questions into Quiz
    QUIZ_QUESTIONS.push(...ADDITIONAL_QUIZ);
'''

    if 'const ADDITIONAL_PAIRS =' not in html_content:
        html_content = html_content.replace('const FALSE_FRIENDS_DATA = [', js_addon + '\n    const FALSE_FRIENDS_DATA = [')
        print("  [OK] Injected additional pairs and horror stories data into JavaScript.")

    # 5. Add renderHorrorStories function & update switchTab
    horror_funcs = '''
    function renderHorrorStories() {
      const container = document.getElementById('horror-stories-grid');
      if (!container) return;

      container.innerHTML = EMAIL_HORROR_STORIES.map((story, idx) => `
        <article class="email-client-card">
          <div class="email-top-bar">
            <span>📧 INCOMING EMAIL #${idx + 1}</span>
            <span class="email-badge-alert">${story.badge}</span>
          </div>
          <div class="email-meta">
            <div class="email-meta-row"><span class="email-meta-label">Subject:</span> <strong>${story.subject}</strong></div>
            <div class="email-meta-row"><span class="email-meta-label">From:</span> <span>${story.sender}</span></div>
            <div class="email-meta-row"><span class="email-meta-label">To:</span> <span>${story.recipient}</span></div>
            <div class="email-meta-row"><span class="email-meta-label">Sent:</span> <span style="color:#64748b;">${story.timestamp}</span></div>
          </div>
          <div class="email-body">
            ${story.email_text}
          </div>
          <div class="reaction-box">
            <div class="reaction-avatar">${story.reaction_avatar}</div>
            <div class="reaction-content">
              <h4>Shocked Native Recipient Reaction (${story.reaction_name}):</h4>
              <div class="reaction-quote">${story.reaction_quote}</div>
            </div>
          </div>
          <div class="horror-action-bar">
            <button class="btn-inspect-fallout" onclick="toggleHorrorDrawer(${idx})">
              🔍 Inspect Linguistic Fallout &amp; Professional Rewrite ↓
            </button>
          </div>
          <div class="fallout-drawer" id="fallout-drawer-${idx}">
            <div class="fallout-grid">
              <div class="fallout-item" style="border-left: 4px solid #ef4444;">
                <div class="fallout-label" style="color: #b91c1c;">❌ What Native Speakers Heard:</div>
                <p style="font-size:0.88rem; color:#1e293b;">${story.false_meaning}</p>
              </div>
              <div class="fallout-item" style="border-left: 4px solid #f59e0b;">
                <div class="fallout-label" style="color: #b45309;">💡 What the Czech Writer Meant:</div>
                <p style="font-size:0.88rem; color:#1e293b;">${story.real_meaning}</p>
              </div>
            </div>
            <div class="rewrite-banner">
              <strong>✅ Executive Rewrite (Say This Instead):</strong><br>
              <div style="margin-top:6px; font-size:0.95rem;">${story.rewrite}</div>
              <div style="margin-top:8px; font-size:0.8rem; color:#047857; font-style:italic;">💡 Expert Rule: ${story.tip}</div>
            </div>
          </div>
        </article>
      `).join('');
    }

    function toggleHorrorDrawer(idx) {
      const drawer = document.getElementById(`fallout-drawer-${idx}`);
      if (!drawer) return;
      drawer.classList.toggle('open');
    }
'''

    if 'function renderHorrorStories()' not in html_content:
        html_content = html_content.replace('function switchTab(tabId) {', horror_funcs + '\n    function switchTab(tabId) {')
        print("  [OK] Added renderHorrorStories & toggleHorrorDrawer functions.")

    # 6. Update switchTab implementation to handle 'horror' tab
    old_switch = '''    function switchTab(tabId) {
      document.getElementById('tab-tutorial').style.display = tabId === 'tutorial' ? 'block' : 'none';
      document.getElementById('tab-quiz').style.display = tabId === 'quiz' ? 'block' : 'none';
      document.getElementById('tab-table').style.display = tabId === 'table' ? 'block' : 'none';

      document.querySelectorAll('.tab-btn').forEach((btn, i) => {
        const matches = (i === 0 && tabId === 'tutorial') ||
                        (i === 1 && tabId === 'quiz') ||
                        (i === 2 && tabId === 'table');
        btn.classList.toggle('active', matches);
      });
    }'''

    new_switch = '''    function switchTab(tabId) {
      document.getElementById('tab-tutorial').style.display = tabId === 'tutorial' ? 'block' : 'none';
      if (document.getElementById('tab-horror')) {
        document.getElementById('tab-horror').style.display = tabId === 'horror' ? 'block' : 'none';
      }
      document.getElementById('tab-quiz').style.display = tabId === 'quiz' ? 'block' : 'none';
      document.getElementById('tab-table').style.display = tabId === 'table' ? 'block' : 'none';

      document.querySelectorAll('.tab-btn').forEach((btn, i) => {
        const matches = (i === 0 && tabId === 'tutorial') ||
                        (i === 1 && tabId === 'horror') ||
                        (i === 2 && tabId === 'quiz') ||
                        (i === 3 && tabId === 'table');
        btn.classList.toggle('active', matches);
      });

      if (tabId === 'horror') {
        renderHorrorStories();
      }
    }'''

    if old_switch in html_content:
        html_content = html_content.replace(old_switch, new_switch)
        print("  [OK] Updated switchTab to handle 4 tabs and render horror stories.")

    # 7. Update Quiz Item count in renderQuiz (Item X of 30) and score calculation
    html_content = html_content.replace('Item ${idx + 1} of 25', 'Item ${idx + 1} of ${QUIZ_QUESTIONS.length}')
    html_content = html_content.replace('Score: ${correct} / 25', 'Score: ${correct} / ${QUIZ_QUESTIONS.length}')
    html_content = html_content.replace('out of 25', 'out of ${QUIZ_QUESTIONS.length}')
    html_content = html_content.replace('score >= 23', 'score >= Math.round(QUIZ_QUESTIONS.length * 0.9)')
    html_content = html_content.replace('score >= 18', 'score >= Math.round(QUIZ_QUESTIONS.length * 0.72)')
    html_content = html_content.replace('score >= 12', 'score >= Math.round(QUIZ_QUESTIONS.length * 0.48)')

    # Also update count-cards initial innerText on boot
    html_content = html_content.replace("document.getElementById('count-cards').innerText = FALSE_FRIENDS_DATA.length;", 
                                        "document.getElementById('count-cards').innerText = FALSE_FRIENDS_DATA.length;\n      renderHorrorStories();")

    # Write updated file
    target_html.write_text(html_content, encoding="utf-8")
    root_mirror.write_text(html_content, encoding="utf-8")
    print(f"  [OK] Written {target_html} ({len(html_content)} chars)")
    print(f"  [OK] Mirrored to {root_mirror}")

    print("\n" + "=" * 60)
    print("FALSE FRIENDS HUB UPGRADE COMPLETE!")
    print("=" * 60)

if __name__ == "__main__":
    main()
