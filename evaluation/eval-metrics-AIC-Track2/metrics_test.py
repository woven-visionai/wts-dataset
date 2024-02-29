#!/usr/bin/python3
"""
Evaluate validation set result for the AI City Challenge, Track 2, 2024.
"""

import utils

from argparse import ArgumentParser
import glob
import json
import traceback


# Provide path to the ground truth directory that was downloaded.
# GROUND_TRUTH_DIR_PATH = ""
# Example using test data:
GROUND_TRUTH_DIR_PATH = "testdata/gt/"

def get_args():
    parser = ArgumentParser(add_help=False, usage=usage_msg())
    parser.add_argument('--help', action='help', help='Show this help message and exit')
    parser.add_argument("--pred", type=str, help="path to prediction json file")

    return parser.parse_args()


def usage_msg():
    return """ 
    
    python3 metrics_test.py --pred <path_to_prediction_json>

    See `python3 metrics_test.py --help` for more info.
    
    """


def usage(msg=None):
    """ Print usage information, including an optional message, and exit. """
    if msg:
        print("%s\n" % msg)
    print("\nUsage: %s" % usage_msg())
    exit()


# Read prediction json file that contains annotations of all scenarios. File format is specified in
# https://github.com/woven-visionai/wts-dataset/blob/main/README.md#evaluation.
def read_pred(pred_json_path):
    with open(pred_json_path) as f:
        data = json.load(f)

    return data


# Read ground truth json file for one scenario
def read_gt_one_scenario(gt_json_path):
    with open(gt_json_path) as f:
        data = json.load(f)

    return data["event_phase"]


# Read ground truth for all json files under gt_dir_path and return one dict containing all the annotation
def read_gt(gt_dir_path):
    gt_annotations = {}

    # read json files from GT directory and store in a dict
    for file_path in glob.iglob(gt_dir_path + '**/**.json', recursive=True):
        # skip vehicle view annotations since their captions are the same as overhead view
        if "vehicle_view" in file_path:
            continue

        # get scenario name from file path
        file_name = file_path.split("/")[-1]
        scenario_name = file_name.strip("_caption.json")

        # read annotation of this scenario
        gt_annotation = read_gt_one_scenario(file_path)
        gt_annotations[scenario_name] = gt_annotation

    return gt_annotations


# Compute metrics for one scenario and return a dict
def compute_metrics_scenario(pred_scenario: list, gt_scenario: list, scenario_name: str):

    pred_scenario_dict = utils.convert_to_dict(pred_scenario)
    gt_scenario_dict = utils.convert_to_dict(gt_scenario)

    metrics_ped_scenario_total = {
        "bleu":    0,
        "meteor":  0,
        "rouge-l": 0,
        "cider":   0,
    }
    metrics_veh_scenario_total = {
        "bleu":    0,
        "meteor":  0,
        "rouge-l": 0,
        "cider":   0,
    }
    num_segments = 0

    for segment, gt_segment_dict in gt_scenario_dict.items():
        if segment not in pred_scenario_dict:
            print(f"Segment captions missing for scenario {scenario_name}, segment number {segment}")
            # Skip adding score to this segment but still increment segment number since it is in GT
            num_segments += 1
            continue

        pred_segment_dict = pred_scenario_dict[segment]

        # compute caption metrics for this segment
        metrics_ped_segment_total = utils.compute_metrics_single(pred_segment_dict["caption_pedestrian"],
                                                                 gt_segment_dict["caption_pedestrian"])
        metrics_veh_segment_total = utils.compute_metrics_single(pred_segment_dict["caption_vehicle"],
                                                                 gt_segment_dict["caption_vehicle"])

        # add segment metrics total to scenario metrics total
        for metric_name, metric_score in metrics_ped_segment_total.items():
            metrics_ped_scenario_total[metric_name] += metric_score
        for metric_name, metric_score in metrics_veh_segment_total.items():
            metrics_veh_scenario_total[metric_name] += metric_score

        # increment segment count
        num_segments += 1

    return metrics_ped_scenario_total, metrics_veh_scenario_total, num_segments


def compute_metrics_overall(pred_all, gt_all):
    metrics_pedestrian_overall = {
        "bleu":    0,
        "meteor":  0,
        "rouge-l": 0,
        "cider":   0,
    }
    metrics_vehicle_overall = {
        "bleu":    0,
        "meteor":  0,
        "rouge-l": 0,
        "cider":   0,
    }
    num_segments_overall = 0

    for scenario_name, gt_scenario in gt_all.items():
        if scenario_name not in pred_all:
            print(f"Scenario {scenario_name} exists in ground-truth but not in predictions. "
                  f"Counting zero score for this scenario.")
            num_segments = len(gt_scenario)
            num_segments_overall += num_segments
            continue

        pred_scenario = pred_all[scenario_name]

        # Get total scores for this scenario (for pedestrian and vehicle separately; for each separate metric)
        # and number of segments
        metrics_ped_scenario_total, metrics_veh_scenario_total, num_segments = compute_metrics_scenario(pred_scenario, gt_scenario, scenario_name)

        # Accumulate metric and num_segments for this scenario to overall sum
        for metric_name, metric_score in metrics_ped_scenario_total.items():
            metrics_pedestrian_overall[metric_name] += metric_score
        for metric_name, metric_score in metrics_veh_scenario_total.items():
            metrics_vehicle_overall[metric_name] += metric_score
        num_segments_overall += num_segments

    return metrics_pedestrian_overall, metrics_vehicle_overall, num_segments_overall


def compute_mean_metrics(metrics_overall, num_segments_overall):
    metrics_mean = metrics_overall
    for metric_name in metrics_overall.keys():
        metrics_mean[metric_name] /= num_segments_overall

    return metrics_mean


def print_metrics(metrics_dict):
    for metric_name, metric_val in metrics_dict.items():
        print(f"- {metric_name}: {metric_val:.3f}")


if __name__ == '__main__':
    args = get_args()
    if not args.pred:
        print("Please specify --pred flag.")
        usage()

    try:
        # Read pred and gt to pred_all and gt_all, which will both look like:
        # {
        #     "<scenario-name-1>": [  # scenario name
        #         {
        #             "labels": [  # segment number, this is known information will be given
        #                 "0"
        #             ],
        #             "caption_pedestrian": "",  # caption regarding pedestrian
        #             "caption_vehicle": ""      # caption regarding vehicle
        #         },
        #         {
        #             ...
        #         }
        #     ]
        # },
        # {
        #     "<scenario-name-2>": [  # scenario name
        #         {
        #             ...
        #         },
        #     ]
        # }
        pred_all = read_pred(args.pred)
        gt_all = read_gt(GROUND_TRUTH_DIR_PATH)

        # Compute overall metrics (summed over all scenarios and segments)
        metrics_pedestrian_overall, metrics_vehicle_overall, num_segments_overall = compute_metrics_overall(pred_all,
                                                                                                            gt_all)
        # Compute average metrics
        metrics_pedestrian_mean = compute_mean_metrics(metrics_pedestrian_overall, num_segments_overall)
        metrics_vehicle_mean = compute_mean_metrics(metrics_vehicle_overall, num_segments_overall)

        print(f"Pedestrian mean score over all data provided:")
        print_metrics(metrics_pedestrian_mean)
        print(f"Vehicle mean score over all data provided:")
        print_metrics(metrics_vehicle_mean)

        # Compute average metrics over pedestrian and vehicle
        metrics_all_category_mean = {}
        for metric_name, ped_score in metrics_pedestrian_mean.items():
            veh_score = metrics_vehicle_mean[metric_name]
            metrics_all_category_mean[metric_name] = (ped_score + veh_score) / 2

        # TODO: take avg over 4 metrics after normalizing
        total = 0
        for metric_name, score in metrics_all_category_mean.items():
            if metric_name in ["bleu", "meteor", "rouge-l"]:
                total += score * 100
            elif metric_name == "cider":
                total += score * 10

        final_mean_score = total / 4

        print(f"Final mean score (range [0, 100]):\n{final_mean_score:.2f}")

    except Exception as e:
        print("Error: %s" % repr(e))
        traceback.print_exc()
