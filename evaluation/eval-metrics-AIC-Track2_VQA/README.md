Evaluation Script
===================

Evaluate validation set result for the AI City Challenge, Track 2, 2024.

## Description ##
This repository provides Python 3 support to evaluate Visual question Answers.


## Test Usage ##
a test metrcis running script is provided for using as below. 
```
python traffic_qa_evaluation_script.py --gt <path_to_ground_truth_json> --user <path_to_user_prediction_json>
```

Example with a toy test data:
```
python traffic_qa_evaluation_script.py --gt ./testdata/sample_ground_truth.json --user ./testdata/sample_user_output.json
```

This example has sample ground-truth and sample user output:

Evaluation script sample output:
```
Questions: 5  | Correct: 3  |  Wrong: 2  |  Missing: 0
Accuracy: 60.00%

```

## User Prediction Format ##

The script expects the following format from the user:

```
[
  {
    "id": "3c8c80e3-33f1-4133-a86c-1192c8a26159",
    "correct": "a"
  },
  ...
```

"id" represents question id in QA set.
"coorect" is the predicted label.


