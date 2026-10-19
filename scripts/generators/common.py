"""
Common utilities and constants for 400-module test generators.
"""

KEY_PATTERN = ["B", "C", "A", "D", "C", "B", "D", "A", "C", "B"]

def make_q(qid, prompt, options_dict, correct_key, explanations_dict, cz_note, track):
    """
    Creates a schema-compliant question object.
    options_dict: {"A": text, "B": text, "C": text, "D": text}
    correct_key: "A", "B", "C", or "D"
    explanations_dict: {"correct": text, "wrong_A": text, ...}
    cz_note: string with length >= 10
    track: workplace track string
    """
    options = [{"key": k, "text": options_dict[k]} for k in ["A", "B", "C", "D"]]
    
    # Ensure all distractor explanations are present
    for k in ["A", "B", "C", "D"]:
        if k != correct_key:
            wrong_k = f"wrong_{k}"
            if wrong_k not in explanations_dict or not explanations_dict[wrong_k].strip():
                explanations_dict[wrong_k] = f"Option {k} is incorrect in this technical context."

    if "correct" not in explanations_dict or not explanations_dict["correct"].strip():
        explanations_dict["correct"] = f"Option {correct_key} correctly satisfies the grammar and technical context."

    return {
        "id": qid,
        "prompt": prompt,
        "options": options,
        "correct_key": correct_key,
        "explanations": explanations_dict,
        "cz_learning_point": cz_note,
        "workplace_track": track
    }

def build_test_module(test_id, title, level, category, track, est_time, description, objectives, questions):
    """
    Creates a schema-compliant test module dictionary.
    """
    return {
        "test_id": test_id,
        "title": title,
        "level": level,
        "category": category,
        "workplace_track": track,
        "estimated_time_minutes": est_time,
        "description": description,
        "learning_objectives": objectives,
        "questions": questions
    }
