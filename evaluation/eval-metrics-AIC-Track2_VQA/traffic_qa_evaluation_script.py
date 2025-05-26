import json
import argparse

def load_json(path):
    with open(path, 'r') as f:
        return json.load(f)

def evaluate(ground_truth, user_responses):
    gt_dict = {entry['id']: entry['correct'].lower() for entry in ground_truth}
    user_dict = {entry['id']: entry['correct'].lower() for entry in user_responses}

    total = len(gt_dict)
    correct = 0
    wrong = 0
    missing = 0

    for qid, gt_answer in gt_dict.items():
        user_answer = user_dict.get(qid)
        if user_answer == gt_answer:
            correct += 1
        elif user_answer is not None:
            wrong += 1
        else:
            missing += 1
            

    accuracy = correct / total if total > 0 else 0.0

    return {"accuracy": accuracy, "correct": correct, "wrong": wrong, "missing": missing}

def main(gt_path, user_path):
    ground_truth = load_json(gt_path)
    user_responses = load_json(user_path)

    stats = evaluate(ground_truth, user_responses)

    print(f"Questions: {len(ground_truth)}  | Correct: {stats['correct']}  |  Wrong: {stats['wrong']}  |  Missing: {stats['missing']}")
    print(f"Accuracy: {stats['accuracy']:.2%}")
    

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Evaluate user responses against ground truth.")
    parser.add_argument("--gt", required=True, help="Path to ground truth JSON file")
    parser.add_argument("--user", required=True, help="Path to user response JSON file")
    args = parser.parse_args()

    main(args.gt, args.user)
