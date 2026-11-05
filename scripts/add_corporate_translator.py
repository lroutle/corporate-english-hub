#!/usr/bin/env python3
"""
Adds the TikTok Corporate Translator & Buzzword Decoder to funny-english/index.html
and mirrors to funny_english.html:
- Mode 1: Corporate Speak -> Real English (The Savage Decoder) with Sarcasm Meter & Categories
- Mode 2: Raw Emotion -> Corporate Shield (The "How Do I Say Politely...?" Generator)
- Mode 3: The Email Sign-off Temperature Gauge (Interactive Passive-Aggressive Scale)
- Mode 4: Interactive Boardroom Decoder Quiz (5 items with instant scoring)
- Updates Master Portal index.html Card G2 with new badges and description.
"""

import sys
import json
import re
from pathlib import Path

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

ROOT = Path(__file__).resolve().parent.parent
funny_dir = ROOT / "funny-english"
target_html = funny_dir / "index.html"
mirror_html = ROOT / "funny_english.html"
index_html = ROOT / "index.html"

# -----------------------------------------------------------------------------
# 1. DATA DEFINITIONS (100% PURE ENGLISH)
# -----------------------------------------------------------------------------

CORP_PHRASES = [
    # Boundaries & Deflection
    {
        "phrase": "I encourage you to take the initiative on this.",
        "category": "boundaries",
        "category_label": "🛑 Setting Boundaries",
        "meter": "Spicy",
        "meter_val": 6,
        "meter_class": "spicy",
        "real": "Do not ask me to hold your hand through basic tasks.",
        "context": "Used when a colleague asks you how to do something that is literally their job description."
    },
    {
        "phrase": "I trust your judgment on this matter.",
        "category": "boundaries",
        "category_label": "🛑 Setting Boundaries",
        "meter": "Mild",
        "meter_val": 5,
        "meter_class": "mild",
        "real": "I do not care. Stop emailing me for permission to make minor routine decisions.",
        "context": "A polite way to refuse getting pulled into someone else's decision-making risk."
    },
    {
        "phrase": "Please feel free to take the lead on running with that.",
        "category": "boundaries",
        "category_label": "🛑 Setting Boundaries",
        "meter": "Hostile",
        "meter_val": 8,
        "meter_class": "hostile",
        "real": "You brought up this annoying, unnecessary idea in the meeting, so now you suffer the workload.",
        "context": "The classic punishment for volunteering an unprompted suggestion in front of management."
    },
    {
        "phrase": "Let's divide and conquer.",
        "category": "boundaries",
        "category_label": "🛑 Setting Boundaries",
        "meter": "Spicy",
        "meter_val": 7,
        "meter_class": "spicy",
        "real": "I will do the easy 5-minute part; you get the miserable 6-hour spreadsheet disaster.",
        "context": "Sounds collaborative, but almost always results in asymmetric workload distribution."
    },
    {
        "phrase": "I have limited bandwidth at the moment.",
        "category": "boundaries",
        "category_label": "🛑 Setting Boundaries",
        "meter": "Spicy",
        "meter_val": 6.5,
        "meter_class": "spicy",
        "real": "I am not doing this. Go away and leave me alone.",
        "context": "Borrowing computer networking terminology ('bandwidth') to sound technical instead of admitting you refuse to do extra work."
    },
    {
        "phrase": "I will let you run with this.",
        "category": "boundaries",
        "category_label": "🛑 Setting Boundaries",
        "meter": "Hostile",
        "meter_val": 8.5,
        "meter_class": "hostile",
        "real": "If this succeeds, I'll take credit; if it crashes catastrophically, it is 100% on you.",
        "context": "A classic middle-management move to delegate risk while preserving upside."
    },
    {
        "phrase": "Let me re-route you to [Colleague].",
        "category": "boundaries",
        "category_label": "🛑 Setting Boundaries",
        "meter": "Mild",
        "meter_val": 4,
        "meter_class": "mild",
        "real": "This is completely not my problem. Go bother someone else.",
        "context": "The professional hot-potato toss to prevent unwanted projects landing in your inbox."
    },

    # Passive-Aggressive Email War
    {
        "phrase": "Per my previous email...",
        "category": "passive",
        "category_label": "⚔️ Passive-Aggressive Fire",
        "meter": "Nuclear",
        "meter_val": 9.5,
        "meter_class": "nuclear",
        "real": "Can you actually read, or should I record an audio book for you?",
        "context": "The absolute king of corporate hostility. Used when you already answered their exact question in writing."
    },
    {
        "phrase": "As per our discussion earlier today...",
        "category": "passive",
        "category_label": "⚔️ Passive-Aggressive Fire",
        "meter": "Hostile",
        "meter_val": 7.5,
        "meter_class": "hostile",
        "real": "I am putting this in writing immediately so you cannot lie about it later.",
        "context": "Creating a paper trail right after a verbal meeting to lock the other person into their commitments."
    },
    {
        "phrase": "Correct me if I'm wrong, but...",
        "category": "passive",
        "category_label": "⚔️ Passive-Aggressive Fire",
        "meter": "Nuclear",
        "meter_val": 10,
        "meter_class": "nuclear",
        "real": "I know with 100% certainty that I am right, and I am about to publicly humiliate you with receipts.",
        "context": "Never used when someone is actually uncertain. Always introduces undeniable proof of someone's blunder."
    },
    {
        "phrase": "Help me understand your thought process here...",
        "category": "passive",
        "category_label": "⚔️ Passive-Aggressive Fire",
        "meter": "Hostile",
        "meter_val": 9,
        "meter_class": "hostile",
        "real": "What on earth were you thinking? This makes zero logical sense.",
        "context": "Disguises total disbelief and contempt behind a veneer of empathetic coaching."
    },
    {
        "phrase": "Just circling back on this.",
        "category": "passive",
        "category_label": "⚔️ Passive-Aggressive Fire",
        "meter": "Spicy",
        "meter_val": 6.5,
        "meter_class": "spicy",
        "real": "You have been ignoring me for a week and I haven't forgotten.",
        "context": "The polite reminder that will progressively escalate every 48 hours until you reply."
    },
    {
        "phrase": "Any updates on this?",
        "category": "passive",
        "category_label": "⚔️ Passive-Aggressive Fire",
        "meter": "Spicy",
        "meter_val": 7,
        "meter_class": "spicy",
        "real": "Why isn't this done yet? Stop stalling.",
        "context": "The 4-word email that triggers instant anxiety across office cubicles worldwide."
    },
    {
        "phrase": "Going forward, let's ensure we align on...",
        "category": "passive",
        "category_label": "⚔️ Passive-Aggressive Fire",
        "meter": "Hostile",
        "meter_val": 8,
        "meter_class": "hostile",
        "real": "Never make that stupid mistake ever again.",
        "context": "The executive reprimand disguised as collaborative forward-looking strategy."
    },
    {
        "phrase": "There appears to be a slight disconnect.",
        "category": "passive",
        "category_label": "⚔️ Passive-Aggressive Fire",
        "meter": "Spicy",
        "meter_val": 7.5,
        "meter_class": "spicy",
        "real": "You have completely misunderstood everything from day one.",
        "context": "Using the minimizer 'slight disconnect' to downplay a total operational catastrophe."
    },
    {
        "phrase": "Thanks for pointing that out!",
        "category": "passive",
        "category_label": "⚔️ Passive-Aggressive Fire",
        "meter": "Hostile",
        "meter_val": 8.5,
        "meter_class": "hostile",
        "real": "Nobody asked you, nobody cares, and you just wasted everybody's time with a minor pedantic detail.",
        "context": "The exclamation mark weaponized as a smile while grinding your teeth."
    },

    # Meeting Escapes & Small Talk
    {
        "phrase": "Let's take this offline.",
        "category": "meetings",
        "category_label": "☕ Meeting Escapes",
        "meter": "Hostile",
        "meter_val": 8,
        "meter_class": "hostile",
        "real": "Shut up immediately. You are embarrassing our department in front of the VP / client.",
        "context": "Used to shut down a rabbit hole or sensitive dispute during a large group presentation."
    },
    {
        "phrase": "Let's put a pin in that.",
        "category": "meetings",
        "category_label": "☕ Meeting Escapes",
        "meter": "Spicy",
        "meter_val": 7,
        "meter_class": "spicy",
        "real": "We will never speak of this idea again for the rest of human history.",
        "context": "A polite execution of an idea without having to bluntly say 'no'."
    },
    {
        "phrase": "Let's table this for now.",
        "category": "meetings",
        "category_label": "☕ Meeting Escapes",
        "meter": "Spicy",
        "meter_val": 7,
        "meter_class": "spicy",
        "real": "This idea is dead and buried. Moving on.",
        "context": "In US business, 'tabling' something means postponing or killing it (contrasting with UK where it means discussing it now)."
    },
    {
        "phrase": "I'll give you 10 minutes of your day back!",
        "category": "meetings",
        "category_label": "☕ Meeting Escapes",
        "meter": "Mild",
        "meter_val": 2,
        "meter_class": "mild",
        "real": "I am desperately trying to escape this pointless meeting before someone asks another question.",
        "context": "Framed as a benevolent philanthropic gift of time to attendees."
    },
    {
        "phrase": "Let's hop on a quick 5-minute call.",
        "category": "meetings",
        "category_label": "☕ Meeting Escapes",
        "meter": "Hostile",
        "meter_val": 8.5,
        "meter_class": "hostile",
        "real": "I refuse to type two sentences, so I am going to hijack 35 minutes of your afternoon.",
        "context": "The '5-minute call' that has never, in corporate history, lasted less than 30 minutes."
    },
    {
        "phrase": "Can everyone see my screen?",
        "category": "meetings",
        "category_label": "☕ Meeting Escapes",
        "meter": "Mild",
        "meter_val": 1,
        "meter_class": "mild",
        "real": "Please validate that technology is working so I don't talk to an empty void for 15 minutes.",
        "context": "The mandatory opening ritual of every Microsoft Teams and Zoom call on Earth."
    },
    {
        "phrase": "I think you're on mute.",
        "category": "meetings",
        "category_label": "☕ Meeting Escapes",
        "meter": "Mild",
        "meter_val": 1,
        "meter_class": "mild",
        "real": "You have been mouthing words to yourself like a goldfish for two whole minutes.",
        "context": "The universal phrase of the remote working era."
    },

    # Executive Jargon & Leadership Illusions
    {
        "phrase": "We need to do more with less this quarter.",
        "category": "executive",
        "category_label": "👔 Executive Jargon",
        "meter": "Nuclear",
        "meter_val": 9,
        "meter_class": "nuclear",
        "real": "We fired three people, and now you have their workload with zero pay increase.",
        "context": "Executive speak for cost-cutting while demanding the exact same or higher output."
    },
    {
        "phrase": "We are like a family here.",
        "category": "executive",
        "category_label": "👔 Executive Jargon",
        "meter": "Nuclear",
        "meter_val": 10,
        "meter_class": "nuclear",
        "real": "We expect unpaid overtime, weekend Slack replies, and emotional guilt trips.",
        "context": "The single biggest red flag in corporate recruiting and HR culture."
    },
    {
        "phrase": "It's a fast-paced, dynamic environment.",
        "category": "executive",
        "category_label": "👔 Executive Jargon",
        "meter": "Hostile",
        "meter_val": 8.5,
        "meter_class": "hostile",
        "real": "It is complete chaos, nothing is documented, and everyone is permanently overwhelmed.",
        "context": "Job description translation for zero structure, zero onboarding, and constant panic."
    },
    {
        "phrase": "A great learning and growth opportunity!",
        "category": "executive",
        "category_label": "👔 Executive Jargon",
        "meter": "Hostile",
        "meter_val": 8,
        "meter_class": "hostile",
        "real": "A miserable, unglamorous assignment that everyone senior successfully dodged.",
        "context": "Used to convince junior employees to take on thankless tasks without additional pay."
    },
    {
        "phrase": "Competitive salary package.",
        "category": "executive",
        "category_label": "👔 Executive Jargon",
        "meter": "Spicy",
        "meter_val": 7,
        "meter_class": "spicy",
        "real": "Completely average pay, but we have free tap water and fruit in the kitchen on Wednesdays.",
        "context": "Means the salary is competing with your monthly rent and barely winning."
    },
    {
        "phrase": "We are executing a strategic pivot.",
        "category": "executive",
        "category_label": "👔 Executive Jargon",
        "meter": "Hostile",
        "meter_val": 8.5,
        "meter_class": "hostile",
        "real": "Our previous 9-month plan failed catastrophically and leadership is panicking.",
        "context": "Rebranding an expensive failure as an intentional agile maneuver."
    },
    {
        "phrase": "Streamlining operational efficiencies.",
        "category": "executive",
        "category_label": "👔 Executive Jargon",
        "meter": "Nuclear",
        "meter_val": 9.5,
        "meter_class": "nuclear",
        "real": "Mass layoffs are imminent. Update your LinkedIn profile tonight.",
        "context": "The universal corporate euphemism for headcount reduction."
    },
    {
        "phrase": "Let's look at the optics of this.",
        "category": "executive",
        "category_label": "👔 Executive Jargon",
        "meter": "Spicy",
        "meter_val": 7.5,
        "meter_class": "spicy",
        "real": "It doesn't matter if this works or is true; how does it look on LinkedIn and to the board?",
        "context": "Prioritizing public relations and vanity metrics over actual operational reality."
    }
]

HOW_TO_SAY_ITEMS = [
    {
        "raw": "I already told you this last week and you clearly didn't read it.",
        "corp": "Re-attaching the timeline shared on Tuesday for ease of reference.",
        "trick": "By re-attaching the exact previous email with the timestamp visible, you prove they ignored you without using aggressive words."
    },
    {
        "raw": "Stop giving me impossible deadlines.",
        "corp": "To ensure this meets our quality standards, could you help clarify the priority order among current deliverables?",
        "trick": "Forces the requester to confront reality: if they want task B done, task A will have to wait."
    },
    {
        "raw": "That is 100% not my job.",
        "corp": "That falls outside of my current scope of responsibilities, but I can direct you to the team best equipped to handle that.",
        "trick": "Establishes a firm professional boundary while still appearing helpful by providing a redirect."
    },
    {
        "raw": "I am not working this weekend.",
        "corp": "I will be disconnected from email over the weekend, but will prioritize this first thing Monday morning.",
        "trick": "States disconnection as an established fact rather than a negotiation or an apology."
    },
    {
        "raw": "You're paying me for engineering, not manual administrative data entry.",
        "corp": "To maximize ROI on my technical bandwidth, let's explore automating or delegating these manual entries.",
        "trick": "Frames your refusal in financial terms that executives love: 'Return on Investment (ROI) of my expensive time'."
    },
    {
        "raw": "Stop emailing me at 9 PM on a Friday.",
        "corp": "Please note my standard working hours are 8am–5pm CET. I will review this upon my return to the office.",
        "trick": "Neutral, firm boundary setting that reminds the sender of professional boundaries."
    },
    {
        "raw": "I don't care at all. Just pick whatever.",
        "corp": "I defer to your operational expertise on this matter.",
        "trick": "Flutters their ego ('your expertise') while absolving you of all decision-making effort."
    },
    {
        "raw": "That is the dumbest proposal I have ever heard.",
        "corp": "That is certainly an interesting perspective; however, given our current strategic priorities, let's keep that on the backburner for now.",
        "trick": "Labels it 'interesting' before quietly pushing it into the corporate abyss where ideas go to die."
    },
    {
        "raw": "You messed this up, don't try to blame me.",
        "corp": "As flagged in my risk assessment email dated October 14th, this outcome was anticipated if the recommended mitigation steps were not taken.",
        "trick": "The ultimate corporate 'receipt'. Citing an exact date and email eliminates any possibility of scapegoating."
    },
    {
        "raw": "Stop micromanaging me and let me do my work.",
        "corp": "I have full visibility on this deliverable and will provide comprehensive updates during our scheduled weekly sync.",
        "trick": "Politely communicates: 'Stop checking in on me every 2 hours; you will hear from me on Friday'."
    },
    {
        "raw": "I have no idea what you are talking about.",
        "corp": "Could you provide additional background context to help me better understand the overarching objective?",
        "trick": "Instead of admitting confusion, you subtly imply their explanation was disorganized and incomplete."
    },
    {
        "raw": "That sounds like a 'you' problem, not a 'me' problem.",
        "corp": "I recommend liaising directly with your department lead to align on internal resource allocation.",
        "trick": "Kicks the ball entirely into their court without a shred of hostility."
    },
    {
        "raw": "Did you really think I wouldn't notice you didn't do it?",
        "corp": "Just following up to ensure this critical deliverable hasn't slipped through the cracks.",
        "trick": "Provides a face-saving exit ('slipped through the cracks') while letting them know you caught them."
    },
    {
        "raw": "I am completely burned out and taking a day off.",
        "corp": "I will be taking a personal day to recharge and will return with full capacity on Tuesday.",
        "trick": "Normalizes mental health and energy management as a business asset ('return with full capacity')."
    },
    {
        "raw": "I am not coming to your voluntary team-building event.",
        "corp": "Unfortunately, I have prior personal commitments and will be unable to attend, but hope everyone has a fantastic time!",
        "trick": "The airtight 'prior personal commitments' shield. No one can ask what they are without violating HR boundaries."
    }
]

SIGN_OFF_GAUGE = [
    {
        "sign": "Warm regards,",
        "temp": "🟢 Warm / Friendly (Level 1)",
        "meaning": "I actually like you and enjoy working together.",
        "vibe": "Genuine warmth. Rare in high-pressure finance or legal."
    },
    {
        "sign": "Best regards,",
        "temp": "🟡 Neutral / Professional (Level 2)",
        "meaning": "Standard business baseline. Everything is fine.",
        "vibe": "The white dress shirt of email closings. Cannot go wrong."
    },
    {
        "sign": "Best,",
        "temp": "🟠 Rushed / Executive (Level 3)",
        "meaning": "I am busy, self-important, and typing from an iPhone between flights.",
        "vibe": "Slightly brusque, but harmless. Standard Silicon Valley."
    },
    {
        "sign": "Regards,",
        "temp": "🔴 Cold War / Hostile (Level 4)",
        "meaning": "You have severely tested my patience. We are on the brink of conflict.",
        "vibe": "The loss of 'Best' is intentional. This is a verbal slap."
    },
    {
        "sign": "Thanks in advance,",
        "temp": "🚨 Mandatory Compliance (Level 5)",
        "meaning": "You do not have a choice. I have already assumed you will do this.",
        "vibe": "Preemptive psychological leverage. Closes any room for refusal."
    },
    {
        "sign": "[No sign-off, just a first name]",
        "temp": "💀 Silent Rage (Level 6)",
        "meaning": "Pure seething corporate fury. I cannot even bring myself to type a courteous word.",
        "vibe": "The digital equivalent of a death glare across a conference table."
    },
    {
        "sign": "Govern yourself accordingly,",
        "temp": "⚖️ Nuclear Legal Action (Level 7)",
        "meaning": "My attorneys are actively drafting the litigation filing. See you in court.",
        "vibe": "Official legal warfare. Only seen right before an injunction."
    }
]

BOARDROOM_QUIZ = [
    {
        "q": "1. In the middle of your presentation, the Vice President interrupts: 'Let's take this offline.' What does she really mean?",
        "options": [
            { "text": "A) Her Wi-Fi internet connection is unstable.", "correct": False },
            { "text": "B) Shut up immediately; you are derailing the meeting or exposing sensitive problems in front of clients.", "correct": True },
            { "text": "C) She wants to print out physical paper copies of your slides.", "correct": False }
        ],
        "explanation": "✓ 'Take this offline' is boardroom code for 'stop talking right now before you cause more damage'."
    },
    {
        "q": "2. You ask your project partner for data and he writes back: 'Per my previous email below...' What is his emotional state?",
        "options": [
            { "text": "A) Extremely polite and helpful.", "correct": False },
            { "text": "B) Confused about where the attachment is.", "correct": False },
            { "text": "C) Pure passive-aggressive fury that you asked something he already answered in writing.", "correct": True }
        ],
        "explanation": "✓ 'Per my previous email' is corporate for 'Can you actually read, or are you just lazy?'"
    },
    {
        "q": "3. The CEO opens the all-hands quarterly meeting: 'We need to do more with less this year.' What is the operational reality?",
        "options": [
            { "text": "A) Staff cuts or budget freezes have occurred, and remaining employees will shoulder the excess workload.", "correct": True },
            { "text": "B) Everyone is getting a 4-day working week.", "correct": False },
            { "text": "C) The company is adopting minimalist Scandinavian interior office furniture.", "correct": False }
        ],
        "explanation": "✓ 'Doing more with less' always means fewer people doing more work for the same salary."
    },
    {
        "q": "4. A supplier emails you: 'Would Thursday at 14:00 be convenient for our quarterly contract review?' How should you interpret the tone?",
        "options": [
            { "text": "A) Highly aggressive and demanding.", "correct": False },
            { "text": "B) Polite, standard, and accommodating for scheduling.", "correct": True },
            { "text": "C) Sarcastic.", "correct": False }
        ],
        "explanation": "✓ 'Convenient' is the proper professional word for scheduling meetings (never say 'Would Thursday be comfortable?')."
    },
    {
        "q": "5. You send a critical delivery status request and the British director signs off with just: 'Regards, Arthur'. What does the single word 'Regards' signal?",
        "options": [
            { "text": "A) Deep affection and friendship.", "correct": False },
            { "text": "B) He forgot to paste his email signature.", "correct": False },
            { "text": "C) Frustration, cold distance, and displeasure (the drop from 'Best regards' is deliberate).", "correct": True }
        ],
        "explanation": "✓ In British business correspondence, dropping 'Best' down to a bare 'Regards' is a calculated diplomatic chill."
    }
]

def main():
    print("=" * 60)
    print("IMPLEMENTING TIKTOK CORPORATE TRANSLATOR & BUZZWORD DECODER")
    print("=" * 60)

    content = target_html.read_text(encoding="utf-8")

    # 1. Update Navigation Tabs HTML
    old_tabs = '''    <div class="nav-tabs">
      <button class="tab-btn active" onclick="showTab('tab-subtext', this)">🇬🇧 British Subtext (14)</button>
      <button class="tab-btn" onclick="showTab('tab-spelling', this)">🔤 Spelling Chaos & "OUGH"</button>
      <button class="tab-btn" onclick="showTab('tab-eggcorns', this)">🥚 Eggcorns & Malapropisms</button>
      <button class="tab-btn" onclick="showTab('tab-contronyms', this)">🤯 Contronyms (12)</button>
      <button class="tab-btn" onclick="showTab('tab-phrasals', this)">⚡ Phrasal Verb Madness</button>
      <button class="tab-btn" onclick="showTab('tab-animals', this)">🐝 Bizarre Collective Nouns (16)</button>
      <button class="tab-btn" onclick="showTab('tab-headlines', this)">📰 Ambiguous Headlines (12)</button>
    </div>'''

    new_tabs = '''    <div class="nav-tabs">
      <button class="tab-btn active" onclick="showTab('tab-corporate', this)">📱 Corporate Translator (TikTok Edition)</button>
      <button class="tab-btn" onclick="showTab('tab-subtext', this)">🇬🇧 British Subtext (14)</button>
      <button class="tab-btn" onclick="showTab('tab-spelling', this)">🔤 Spelling Chaos & "OUGH"</button>
      <button class="tab-btn" onclick="showTab('tab-eggcorns', this)">🥚 Eggcorns & Malapropisms</button>
      <button class="tab-btn" onclick="showTab('tab-contronyms', this)">🤯 Contronyms (12)</button>
      <button class="tab-btn" onclick="showTab('tab-phrasals', this)">⚡ Phrasal Verb Madness</button>
      <button class="tab-btn" onclick="showTab('tab-animals', this)">🐝 Bizarre Collective Nouns (16)</button>
      <button class="tab-btn" onclick="showTab('tab-headlines', this)">📰 Ambiguous Headlines (12)</button>
    </div>'''

    if old_tabs in content:
        content = content.replace(old_tabs, new_tabs)
        print("  [OK] Updated nav-tabs: Added Corporate Translator as primary tab.")
    else:
        print("  [WARN] nav-tabs snippet not matched directly.")

    # 2. Add Tab Corporate HTML Container before Tab 1
    corporate_html = '''    <!-- ============================================================== -->
    <!-- TAB 0: TIKTOK CORPORATE TRANSLATOR & BUZZWORD DECODER          -->
    <!-- ============================================================== -->
    <div id="tab-corporate">
      <div class="section-desc" style="background: linear-gradient(135deg, #f5f3ff 0%, #ede9fe 100%); border-left: 6px solid var(--primary-dark);">
        <div style="display:flex; justify-content:space-between; align-items:flex-start; flex-wrap:wrap; gap:12px;">
          <div>
            <h2 style="color: var(--primary-dark); font-size: 1.6rem; display: flex; align-items: center; gap: 10px;">
              📱 The TikTok Corporate Translator: Corporate Speak ↔ Honest English
            </h2>
            <p style="color: #4c1d95; font-size: 0.98rem; max-width: 860px; margin-top: 6px;">
              Inspired by viral workplace creators (<em>Laura Whaley, Corporate Natalie</em>). Master the art of decoding polished boardroom passive-aggression, and learn how to translate your raw, unfiltered human frustration into bulletproof, HR-approved corporate shields.
            </p>
          </div>
          <span style="background: #7c3aed; color: #fff; font-size: 0.78rem; font-weight: 800; padding: 4px 12px; border-radius: 9999px; text-transform: uppercase; letter-spacing: 0.5px;">
            TikTok Inspired
          </span>
        </div>
      </div>

      <!-- Mode Selector Pills -->
      <div style="display: flex; gap: 10px; margin-bottom: 22px; flex-wrap: wrap;">
        <button class="corp-mode-btn active" id="btn-mode-savage" onclick="switchCorpMode('savage')">
          👔 Mode 1: Corporate → Honest English (The Savage Decoder)
        </button>
        <button class="corp-mode-btn" id="btn-mode-shield" onclick="switchCorpMode('shield')">
          🛡️ Mode 2: Raw Emotion → Corporate Shield ("How Do I Say Politely...?")
        </button>
        <button class="corp-mode-btn" id="btn-mode-gauge" onclick="switchCorpMode('gauge')">
          ✉️ Mode 3: Email Sign-Off Temperature Gauge
        </button>
        <button class="corp-mode-btn" id="btn-mode-quiz" onclick="switchCorpMode('quiz')">
          🎯 Mode 4: Boardroom Decoder Mini-Quiz
        </button>
      </div>

      <!-- ================= MODE 1: SAVAGE DECODER ================= -->
      <div id="corp-view-savage">
        <div class="controls-row" style="margin-bottom: 20px;">
          <input type="text" id="corp-search" class="search-input" placeholder="🔍 Search corporate phrase or real meaning (e.g. per my previous email, bandwidth, not my job)..." oninput="filterCorpPhrases()">
          
          <div class="filter-chips" style="margin-top: 10px; display: flex; gap: 8px; flex-wrap: wrap;">
            <button class="filter-chip active" onclick="filterCorpCategory('all', this)">All Categories (30+)</button>
            <button class="filter-chip" onclick="filterCorpCategory('boundaries', this)">🛑 Setting Boundaries</button>
            <button class="filter-chip" onclick="filterCorpCategory('passive', this)">⚔️ Passive-Aggressive Fire</button>
            <button class="filter-chip" onclick="filterCorpCategory('meetings', this)">☕ Meeting Escapes</button>
            <button class="filter-chip" onclick="filterCorpCategory('executive', this)">👔 Executive Jargon</button>
          </div>
        </div>

        <div id="corp-cards-grid" style="display: grid; grid-template-columns: repeat(auto-fill, minmax(min(100%, 340px), 1fr)); gap: 18px; margin-bottom: 40px;">
          <!-- Injected via JavaScript -->
        </div>
      </div>

      <!-- ================= MODE 2: THE CORPORATE SHIELD GENERATOR ================= -->
      <div id="corp-view-shield" style="display: none;">
        <div style="background: #ffffff; border: 1px solid var(--border); border-radius: var(--radius-lg); padding: 22px; margin-bottom: 24px;">
          <h3 style="font-size: 1.25rem; font-weight: 800; color: #1e293b; margin-bottom: 6px;">
            🛡️ The "How Do I Say Politely...?" Generator
          </h3>
          <p style="color: var(--text-muted); font-size: 0.92rem;">
            Click any raw, unfiltered human workplace frustration below to reveal the bulletproof corporate translation and the psychological trick that makes it HR-proof.
          </p>
        </div>

        <div style="display: flex; flex-direction: column; gap: 16px; margin-bottom: 40px;" id="shield-cards-container">
          <!-- Injected via JavaScript -->
        </div>
      </div>

      <!-- ================= MODE 3: SIGN-OFF TEMPERATURE GAUGE ================= -->
      <div id="corp-view-gauge" style="display: none;">
        <div style="background: #ffffff; border: 1px solid var(--border); border-radius: var(--radius-lg); padding: 22px; margin-bottom: 24px;">
          <h3 style="font-size: 1.25rem; font-weight: 800; color: #1e293b; margin-bottom: 6px;">
            ✉️ The Email Sign-Off Temperature Gauge: Passive-Aggression Calibration
          </h3>
          <p style="color: var(--text-muted); font-size: 0.92rem;">
            In English email correspondence, the closing sign-off is a finely tuned emotional barometer. Here is how native speakers decode what your sign-off actually signals:
          </p>
        </div>

        <div style="display: flex; flex-direction: column; gap: 14px; margin-bottom: 40px;" id="gauge-container">
          <!-- Injected via JavaScript -->
        </div>
      </div>

      <!-- ================= MODE 4: BOARDROOM DECODER QUIZ ================= -->
      <div id="corp-view-quiz" style="display: none;">
        <div class="quiz-box" style="margin-top: 0;">
          <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:20px;">
            <div>
              <h3 style="font-size: 1.3rem; color: var(--primary-dark); margin-bottom: 4px;">🎯 Boardroom Subtext Mini-Quiz</h3>
              <p style="font-size: 0.9rem; color: var(--text-muted);">Can you decode what native executives actually mean behind closed doors?</p>
            </div>
            <div id="corp-quiz-score" style="font-weight: 800; font-size: 1rem; color: var(--primary-dark); background: var(--primary-subtle); padding: 6px 16px; border-radius: 9999px;">
              Score: 0 / 5
            </div>
          </div>
          <div style="display: flex; flex-direction: column; gap: 18px;" id="corp-quiz-list">
            <!-- Injected via JavaScript -->
          </div>
        </div>
      </div>
    </div>
'''

    if 'id="tab-corporate"' not in content:
        content = content.replace('<div id="tab-subtext">', corporate_html + '\n    <div id="tab-subtext" style="display: none;">')
        print("  [OK] Injected Tab 0 (Corporate Translator) into HTML.")

    # 3. Inject CSS Styles for Corporate Translator
    corp_css = '''
    /* TikTok Corporate Translator Styles */
    .corp-mode-btn {
      background: #f1f5f9;
      border: 1px solid var(--border);
      color: #334155;
      font-size: 0.88rem;
      font-weight: 700;
      padding: 10px 18px;
      border-radius: var(--radius-md);
      cursor: pointer;
      transition: all 0.2s ease;
    }
    .corp-mode-btn:hover {
      background: #e2e8f0;
      color: var(--primary-dark);
    }
    .corp-mode-btn.active {
      background: var(--primary-dark);
      color: #ffffff;
      border-color: var(--primary-dark);
      box-shadow: 0 2px 4px rgba(109, 40, 217, 0.25);
    }

    .corp-card {
      background: #ffffff;
      border: 1px solid var(--border);
      border-radius: var(--radius-md);
      padding: 20px;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      box-shadow: var(--shadow-sm);
      transition: all 0.2s ease;
    }
    .corp-card:hover {
      border-color: var(--primary-light);
      box-shadow: var(--shadow-md);
      transform: translateY(-2px);
    }
    .corp-meter-badge {
      font-size: 0.72rem;
      font-weight: 800;
      text-transform: uppercase;
      padding: 3px 8px;
      border-radius: 9999px;
      letter-spacing: 0.5px;
    }
    .meter-mild { background: #dcfce7; color: #15803d; }
    .meter-spicy { background: #fef3c7; color: #b45309; }
    .meter-hostile { background: #fee2e2; color: #b91c1c; }
    .meter-nuclear { background: #fdf2f8; color: #be185d; border: 1px solid #fbcfe8; }

    .corp-phrase-text {
      font-size: 1.1rem;
      font-weight: 800;
      color: #1e1b4b;
      margin: 12px 0 10px 0;
      line-height: 1.4;
    }
    .corp-real-box {
      background: #f8fafc;
      border-left: 4px solid #ef4444;
      padding: 12px 14px;
      border-radius: 0 6px 6px 0;
      margin-top: 10px;
      font-size: 0.92rem;
      color: #0f172a;
    }
    .corp-real-label {
      font-size: 0.74rem;
      font-weight: 800;
      text-transform: uppercase;
      color: #dc2626;
      letter-spacing: 0.5px;
      margin-bottom: 4px;
      display: flex;
      align-items: center;
      gap: 4px;
    }
    .corp-context-note {
      font-size: 0.8rem;
      color: #64748b;
      margin-top: 8px;
      line-height: 1.4;
      font-style: italic;
    }

    /* Shield Cards */
    .shield-card {
      background: #ffffff;
      border: 1px solid var(--border);
      border-radius: var(--radius-lg);
      overflow: hidden;
      box-shadow: var(--shadow-sm);
      transition: all 0.2s ease;
    }
    .shield-header {
      padding: 16px 20px;
      background: #f8fafc;
      border-bottom: 1px solid var(--border);
      cursor: pointer;
      display: flex;
      justify-content: space-between;
      align-items: center;
    }
    .shield-header:hover {
      background: #f1f5f9;
    }
    .shield-body {
      display: none;
      padding: 20px 22px;
      background: #ffffff;
      animation: fadeIn 0.2s ease;
    }
    .shield-body.open { display: block; }
    .shield-quote-box {
      background: #ecfdf5;
      border: 1px solid #a7f3d0;
      border-left: 5px solid #10b981;
      padding: 14px 18px;
      border-radius: var(--radius-md);
      color: #065f46;
      font-size: 1rem;
      font-weight: 700;
      margin-bottom: 12px;
    }

    /* Gauge Card */
    .gauge-row {
      background: #ffffff;
      border: 1px solid var(--border);
      border-radius: var(--radius-md);
      padding: 16px 20px;
      display: flex;
      align-items: center;
      gap: 20px;
      box-shadow: var(--shadow-sm);
    }
    @media (max-width: 680px) {
      .gauge-row { flex-direction: column; align-items: flex-start; gap: 8px; }
    }
'''

    if '.corp-mode-btn' not in content:
        content = content.replace('</style>', corp_css + '\n  </style>')
        print("  [OK] Injected Corporate Translator CSS styles.")

    # 4. Inject JavaScript Data & Functions
    js_data = f'''
    // TikTok Corporate Translator Master Database
    const CORP_PHRASES_DATA = {json.dumps(CORP_PHRASES, indent=4, ensure_ascii=False)};
    const HOW_TO_SAY_DATA = {json.dumps(HOW_TO_SAY_ITEMS, indent=4, ensure_ascii=False)};
    const SIGN_OFF_DATA = {json.dumps(SIGN_OFF_GAUGE, indent=4, ensure_ascii=False)};
    const BOARDROOM_QUIZ_DATA = {json.dumps(BOARDROOM_QUIZ, indent=4, ensure_ascii=False)};
'''

    # Update showTab function in JS to support 'tab-corporate'
    old_show_tab = '''    function showTab(tabId, btn) {
      const tabs = ['tab-subtext', 'tab-spelling', 'tab-eggcorns', 'tab-contronyms', 'tab-phrasals', 'tab-animals', 'tab-headlines'];
      tabs.forEach(t => {
        const el = document.getElementById(t);
        if (el) el.style.display = (t === tabId) ? 'block' : 'none';
      });

      document.querySelectorAll('.tab-btn').forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
    }'''

    new_show_tab = '''    function showTab(tabId, btn) {
      const tabs = ['tab-corporate', 'tab-subtext', 'tab-spelling', 'tab-eggcorns', 'tab-contronyms', 'tab-phrasals', 'tab-animals', 'tab-headlines'];
      tabs.forEach(t => {
        const el = document.getElementById(t);
        if (el) el.style.display = (t === tabId) ? 'block' : 'none';
      });

      document.querySelectorAll('.tab-btn').forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
    }'''

    corp_js_funcs = '''
    // Corporate Translator Logic
    let currentCorpCat = 'all';
    let currentCorpQuery = '';
    let corpQuizAnswers = new Array(BOARDROOM_QUIZ_DATA.length).fill(null);

    function switchCorpMode(mode) {
      ['savage', 'shield', 'gauge', 'quiz'].forEach(m => {
        const v = document.getElementById(`corp-view-${m}`);
        const b = document.getElementById(`btn-mode-${m}`);
        if (v) v.style.display = (m === mode) ? 'block' : 'none';
        if (b) b.classList.toggle('active', m === mode);
      });
      if (mode === 'shield') renderShieldCards();
      if (mode === 'gauge') renderGaugeRows();
      if (mode === 'quiz') renderBoardroomQuiz();
    }

    function filterCorpCategory(cat, btn) {
      currentCorpCat = cat;
      document.querySelectorAll('#corp-view-savage .filter-chip').forEach(c => c.classList.remove('active'));
      btn.classList.add('active');
      renderCorpCards();
    }

    function filterCorpPhrases() {
      currentCorpQuery = document.getElementById('corp-search').value.toLowerCase().trim();
      renderCorpCards();
    }

    function renderCorpCards() {
      const grid = document.getElementById('corp-cards-grid');
      if (!grid) return;

      const filtered = CORP_PHRASES_DATA.filter(item => {
        if (currentCorpCat !== 'all' && item.category !== currentCorpCat) return false;
        if (currentCorpQuery) {
          const haystack = `${item.phrase} ${item.real} ${item.context}`.toLowerCase();
          if (!haystack.includes(currentCorpQuery)) return false;
        }
        return true;
      });

      if (filtered.length === 0) {
        grid.innerHTML = '<div style="grid-column:1/-1; padding:30px; text-align:center; color:#64748b;">No corporate phrases matched your search.</div>';
        return;
      }

      grid.innerHTML = filtered.map(item => `
        <article class="corp-card">
          <div>
            <div style="display:flex; justify-content:space-between; align-items:center;">
              <span style="font-size:0.75rem; font-weight:700; color:#6b21a8; background:#f3e8ff; padding:2px 8px; border-radius:4px;">
                ${item.category_label}
              </span>
              <span class="corp-meter-badge meter-${item.meter_class}">
                ${item.meter_val}/10 ${item.meter}
              </span>
            </div>
            <div class="corp-phrase-text">“${item.phrase}”</div>
            <div class="corp-real-box">
              <div class="corp-real-label">💥 What Native Speakers Actually Mean:</div>
              <div><strong>“${item.real}”</strong></div>
            </div>
          </div>
          <div class="corp-context-note">
            💡 ${item.context}
          </div>
        </article>
      `).join('');
    }

    function renderShieldCards() {
      const c = document.getElementById('shield-cards-container');
      if (!c || c.children.length > 0) return;

      c.innerHTML = HOW_TO_SAY_DATA.map((item, idx) => `
        <article class="shield-card">
          <div class="shield-header" onclick="toggleShieldCard(${idx})">
            <div>
              <span style="font-size:0.75rem; font-weight:800; color:#dc2626; text-transform:uppercase; letter-spacing:0.5px;">🤬 What You Want to Say (#${idx+1}):</span>
              <div style="font-size:1.05rem; font-weight:700; color:#1e293b; margin-top:2px;">“${item.raw}”</div>
            </div>
            <span style="font-size:1.2rem; color:#6d28d9; font-weight:800;">↓</span>
          </div>
          <div class="shield-body" id="shield-body-${idx}">
            <div class="shield-quote-box">
              🛡️ <strong>Bulletproof Corporate Shield:</strong><br>
              <div style="font-size:1.05rem; margin-top:4px;">“${item.corp}”</div>
            </div>
            <div style="font-size:0.85rem; color:#475569; background:#f8fafc; border:1px solid #e2e8f0; padding:10px 14px; border-radius:6px;">
              🧠 <strong>The Psychological Trick:</strong> ${item.trick}
            </div>
          </div>
        </article>
      `).join('');
    }

    function toggleShieldCard(idx) {
      const el = document.getElementById(`shield-body-${idx}`);
      if (el) el.classList.toggle('open');
    }

    function renderGaugeRows() {
      const c = document.getElementById('gauge-container');
      if (!c || c.children.length > 0) return;

      c.innerHTML = SIGN_OFF_DATA.map(item => `
        <div class="gauge-row">
          <div style="min-width:180px;">
            <strong style="font-size:1.15rem; color:#1e1b4b; font-family:monospace;">“${item.sign}”</strong>
            <div style="font-size:0.78rem; font-weight:700; margin-top:4px;">${item.temp}</div>
          </div>
          <div style="flex:1;">
            <div style="font-size:0.95rem; font-weight:700; color:#0f172a;">${item.meaning}</div>
            <div style="font-size:0.82rem; color:#64748b; margin-top:2px; font-style:italic;">${item.vibe}</div>
          </div>
        </div>
      `).join('');
    }

    function renderBoardroomQuiz() {
      const c = document.getElementById('corp-quiz-list');
      if (!c || c.children.length > 0) return;

      c.innerHTML = BOARDROOM_QUIZ_DATA.map((qItem, idx) => `
        <div class="quiz-question-card" id="corp-qcard-${idx}">
          <div class="question-prompt">${qItem.q}</div>
          <div class="options-grid">
            ${qItem.options.map((opt, optIdx) => `
              <button class="opt-btn" onclick="checkCorpQuiz(this, ${opt.correct}, 'corp-fb-${idx}', ${idx})">
                ${opt.text}
              </button>
            `).join('')}
          </div>
          <div id="corp-fb-${idx}" class="feedback-note">
            ${qItem.explanation}
          </div>
        </div>
      `).join('');
    }

    function checkCorpQuiz(btn, isCorrect, fbId, qIdx) {
      if (corpQuizAnswers[qIdx] !== null) return;
      corpQuizAnswers[qIdx] = isCorrect;

      const card = document.getElementById(`corp-qcard-${qIdx}`);
      const buttons = card.querySelectorAll('.opt-btn');
      buttons.forEach(b => {
        b.disabled = true;
        if (b.getAttribute('onclick').includes('true')) {
          b.classList.add('highlight-correct');
        }
      });

      const fb = document.getElementById(fbId);

      if (isCorrect) {
        btn.classList.add('is-correct');
        card.classList.add('correct');
        if (fb) fb.className = 'feedback-note show fb-ok';
      } else {
        btn.classList.add('is-wrong');
        card.classList.add('wrong');
        if (fb) fb.className = 'feedback-note show fb-bad';
      }

      const score = corpQuizAnswers.filter(a => a === true).length;
      document.getElementById('corp-quiz-score').innerText = `Score: ${score} / ${BOARDROOM_QUIZ_DATA.length}`;
    }

    // Auto-init Corporate cards on load
    document.addEventListener('DOMContentLoaded', () => {
      renderCorpCards();
    });
'''

    if 'const CORP_PHRASES_DATA =' not in content:
        content = content.replace('function showTab(tabId, btn) {', js_data + '\n' + corp_js_funcs + '\n' + old_show_tab)
        content = content.replace(old_show_tab, new_show_tab)
        print("  [OK] Injected Corporate Translator data and JavaScript logic.")

    # Write updated files
    target_html.write_text(content, encoding="utf-8")
    mirror_html.write_text(content, encoding="utf-8")
    print(f"  [OK] Successfully updated {target_html} ({len(content)} chars)")
    print(f"  [OK] Mirrored to {mirror_html}")

    # 5. Update index.html Card G2
    idx_content = index_html.read_text(encoding="utf-8")
    old_g2_desc = '''            <div class="suite-company">Universal Lesson Tool | 6 Pure English Humour Units</div>
            <p class="suite-desc">
              Pure English linguistic eye-openers: British Subtext Decoder (What Brits say vs mean), The 9 Sounds of 'OUGH' & Spelling Chaos, Eggcorns & Malapropisms ("Nip it in the butt"), Contronyms (words that mean their opposite), Phrasal Verb madness, and Ambiguous Headlines.
            </p>
            <div class="tier-pills">
              <span class="tier-pill pill-a2" style="background: #ede9fe; color: #6d28d9;">14 Subtext Decoders</span>
              <span class="tier-pill pill-b1" style="background: #fef3c7; color: #92400e;">9 'OUGH' Sounds</span>
              <span class="tier-pill pill-b2" style="background: #ccfbf1; color: #115e59;">12 Contronyms</span>
              <span class="tier-pill pill-sp" style="background: #fee2e2; color: #991b1b;">12 Crazy Headlines</span>
            </div>'''

    new_g2_desc = '''            <div class="suite-company">Universal Lesson Tool | 8 Pure English Units + TikTok Corporate Translator</div>
            <p class="suite-desc">
              Pure English linguistic eye-openers: <strong>TikTok Corporate Translator</strong> (Corporate Speak ↔ Honest English, "How Do I Say Politely...?", Sign-off Temperature Gauge), British Subtext Decoder, 9 Sounds of 'OUGH', Eggcorns &amp; Malapropisms, Contronyms, Phrasal Verbs, and Crash Blossom Headlines.
            </p>
            <div class="tier-pills">
              <span class="tier-pill pill-sp" style="background: #ede9fe; color: #6d28d9; border: 1px solid #c4b5fd;">📱 Corporate Translator (30+)</span>
              <span class="tier-pill pill-a2" style="background: #f1f5f9; color: #334155;">14 British Subtexts</span>
              <span class="tier-pill pill-b1" style="background: #fef3c7; color: #92400e;">9 'OUGH' Sounds</span>
              <span class="tier-pill pill-b2" style="background: #ccfbf1; color: #115e59;">12 Contronyms</span>
              <span class="tier-pill pill-sp" style="background: #fee2e2; color: #991b1b;">12 Crazy Headlines</span>
            </div>'''

    if old_g2_desc in idx_content:
        idx_content = idx_content.replace(old_g2_desc, new_g2_desc)
        index_html.write_text(idx_content, encoding="utf-8")
        print("  [OK] Updated Card G2 in index.html.")
    else:
        print("  [WARN] Card G2 snippet in index.html not matched directly.")

    print("\n" + "=" * 60)
    print("TIKTOK CORPORATE TRANSLATOR DEPLOYED SUCCESSFULLY!")
    print("=" * 60)

if __name__ == "__main__":
    main()
