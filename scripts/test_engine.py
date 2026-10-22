import sys
sys.path.insert(0, "scripts")
from generators.diverse_question_engine import generate_module_questions

mod_b1_5 = {'test_id': 'TTR-ENG-B1-005', 'level': 'B1', 'workplace_track': 'Suspension, Half-Axles & CTIS Diagnostics'}
qs_b1_5 = generate_module_questions(mod_b1_5, 'tatra_eng')
print(f'TTR-ENG-B1-005 questions: {len(qs_b1_5)}')
for i, q in enumerate(qs_b1_5):
    print(f'  Q{i+1} [{q["correct_key"]}]: {q["prompt"][:65]}...')

mod_b1_16 = {'test_id': 'TTR-ENG-B1-016', 'level': 'B1', 'workplace_track': 'Vehicle Homologation & NATO STANAG Mobility'}
qs_b1_16 = generate_module_questions(mod_b1_16, 'tatra_eng')
print(f'TTR-ENG-B1-016 questions: {len(qs_b1_16)}')
for i, q in enumerate(qs_b1_16):
    print(f'  Q{i+1} [{q["correct_key"]}]: {q["prompt"][:65]}...')

# Check procedural module
mod_proc = {'test_id': 'BID-PUR-B1-001', 'level': 'B1', 'workplace_track': 'Cold-Chain Logistics & Temperature-Controlled Transport'}
qs_proc = generate_module_questions(mod_proc, 'bidfood_pur')
print(f'BID-PUR-B1-001 questions: {len(qs_proc)}')
for i, q in enumerate(qs_proc):
    print(f'  Q{i+1} [{q["correct_key"]}]: {q["prompt"][:65]}...')
