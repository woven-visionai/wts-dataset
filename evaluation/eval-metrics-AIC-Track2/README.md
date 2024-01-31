Evaluation Script
===================

Evaluate validation set result for the AI City Challenge, Track 2, 2024.

## Description ##
This repository provides Python 3 support to evaluate metrics for the AI City Challenge, Track 2.

## Requirements ##
pip install -r requirements.txt

## Installation ##
To install pycocoevalcap and the pycocotools dependency (https://github.com/cocodataset/cocoapi), run:
```
pip install pycocoevalcap
```

## Usage ##
```
python3 metrics.py --pred <path_to_prediction_json>
```

Example with a toy test data:
```
python metrics.py --pred testdata/pred_identical.json
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
