Evaluation Script
===================

Evaluate test set results for the AI City Challenge, Track 2.

## Description ##
This repository provides Python 3 support to evaluate metrics for the AI City Challenge, Track 2.

## Requirements ##
pip install -r requirements.txt

## Installation ##
To install pycocoevalcap and the pycocotools dependency (https://github.com/cocodataset/cocoapi), run:
```
pip install pycocoevalcap
```

## Test Usage ##
a test metrcis running script is provided for using as below. 
```
python metrics_test.py --pred <path_to_prediction_json>
```

Example with a toy test data:
```
python metrics_test.py --pred testdata/pred_identical.json
```

This example has prediction identical to the ground-truth, so it should give full score:
```
Pedestrian mean score over all data provided:
- bleu: 1.000
- meteor: 1.000
- rouge-l: 1.000
- cider: 10.000
Vehicle mean score over all data provided:
- bleu: 1.000
- meteor: 1.000
- rouge-l: 1.000
- cider: 10.000
Final mean score (range [0, 100]):
100.00
```

## Evaluate all validation set ##

please download our validation annotation and put it under the folder of `labels/gt`

Notice that for final evaluation of AIC challenge, `BDD_TC_5K` will be used for evaluation as well.
The score of the average of the WTS collected data (internal) and `BDD_TC_5K` (external) will be the final score.
The sample script is here for using:
```
python metrics_all.py --predictions_file <path_to_predictions_json> --ground_truth <path_to_ground_truth_folder>
```

The output for an example will be looks like below:
```
=== Results for internal videos ===
Pedestrian mean score over all data provided:
- bleu: 0.047
- meteor: 0.243
- rouge-l: 0.219
- cider: 0.203
Vehicle mean score over all data provided:
- bleu: 0.053
- meteor: 0.253
- rouge-l: 0.232
- cider: 0.213
mean score (range [0, 100]): 13.62
========================================
=== Results for external videos ===
Pedestrian mean score over all data provided:
- bleu: 0.041
- meteor: 0.237
- rouge-l: 0.217
- cider: 0.221
Vehicle mean score over all data provided:
- bleu: 0.039
- meteor: 0.243
- rouge-l: 0.223
- cider: 0.209
mean score (range [0, 100]): 13.03
========================================
Final mean score: 13.325083223918028
```

