#!/usr/bin/python3
"""
Evaluate validation set result for the AI City Challenge, Track 2, 2024.
"""

import os
import glob
import json
import utils
import warnings
import traceback

from argparse import ArgumentParser

def get_args():
    parser = ArgumentParser(add_help=False, usage=usage_msg())
    parser.add_argument('--help', action='help', help='Show this help message and exit')
    parser.add_argument("--predictions_file", type=str, help="path to predictions file", required=True)
    parser.add_argument("--ground_truth", type=str, default="labels/gt", help="path to ground truth json files")

    return parser.parse_args()


def usage_msg():
    return """ 
    
    python3 metrics_all.py --predictions_file <path_to_predictions_json> --ground_truth <path_to_ground_truth_folder>

    See `python3 metrics_all.py --help` for more info.
    
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
    for file_path in glob.iglob(gt_dir_path + '/**/**.json', recursive=True):
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

# Filter internal or external data.
# If internal is True, keep internal data.
# If internal is False, keep external data.
def filter_internal_or_external_data(data, internal):
    filtered_data = {}
    for key, value in data.items():
        if (internal and key.startswith("2023")) or (not internal and key.startswith("video")):
            filtered_data[key] = value

    return filtered_data


def filter_data_with_video_list(data, video_list):
    filtered_data = {}
    for key, value in data.items():
        if key in video_list:
            filtered_data[key] = value
    return filtered_data


# Evaluate either internal or external dataset. If video_list is provided, only evaluate on this subset.
def evaluate_one_dataset(predictions_file, ground_truth_dir_path, internal):
    try:
        # Read pred and gt to pred_all and gt_all, which will both look like:
        # {
        #     "<scenario-name-1>": [  # scenario name for multiple view or video file name for single view of BDD_TC_5K
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
        pred_all = read_pred(predictions_file)
        gt_all = read_gt(ground_truth_dir_path)

        # Only evaluate internal or external data at one time
        pred_all = filter_internal_or_external_data(pred_all, internal)

        with warnings.catch_warnings():
            warnings.simplefilter("ignore")

            # Compute overall metrics (summed over all scenarios and segments)
            metrics_pedestrian_overall, metrics_vehicle_overall, num_segments_overall = compute_metrics_overall(pred_all,
                                                                                                                gt_all)
            # Compute average metrics
            metrics_pedestrian_mean = compute_mean_metrics(metrics_pedestrian_overall, num_segments_overall)
            metrics_vehicle_mean = compute_mean_metrics(metrics_vehicle_overall, num_segments_overall)

        # Compute average metrics over pedestrian and vehicle
        metrics_all_category_mean = {}
        for metric_name, ped_score in metrics_pedestrian_mean.items():
            veh_score = metrics_vehicle_mean[metric_name]
            metrics_all_category_mean[metric_name] = (ped_score + veh_score) / 2

        total = 0
        for metric_name, score in metrics_all_category_mean.items():
            if metric_name in ["bleu", "meteor", "rouge-l"]:
                total += score * 100
            elif metric_name == "cider":
                total += score * 10

        mean_score = total / 4

        
        print(f"=== Results for {'internal' if internal else 'external'} videos ===")
        print(f"Pedestrian mean score over all data provided:")
        print_metrics(metrics_pedestrian_mean)
        print(f"Vehicle mean score over all data provided:")
        print_metrics(metrics_vehicle_mean)
        print(f"mean score (range [0, 100]): {mean_score:.2f}")
        print("=="*20)

    except Exception as e:
        if mr:
            print('{"error": "%s"}' % repr(e))
        else:
            print("Error: %s" % repr(e))
        traceback.print_exc()
        exit()

    return metrics_all_category_mean, mean_score



if __name__ == '__main__':
    args = get_args()

    gt_internal = f'{args.ground_truth}/annotations'
    gt_external = f'{args.ground_truth}/external/BDD_PC_5K/annotations'
    if not os.path.exists(gt_internal) or not os.path.exists(gt_external):
        if args.mr:
            print('{"error": "Internal or external ground truth labels missing."}')
        else:
            print("Error: Internal or external ground truth labels missing.")
        exit()

    # evaluate internal videos
    metrics_all_category_mean_internal, mean_score_internal = evaluate_one_dataset(
        args.predictions_file,
        gt_internal,
        internal=True,
    )
    # evaluate external videos
    metrics_all_category_mean_external, mean_score_external = evaluate_one_dataset(
        args.predictions_file,
        gt_external,
        internal=False,
    )

    final_score_overall = (mean_score_internal + mean_score_external) / 2

    results = {f'{k}_i':v for k,v in metrics_all_category_mean_internal.items()}
    results.update({f'{k}_e':v for k,v in metrics_all_category_mean_external.items()})
    results['s2'] = final_score_overall
   
    print("Final mean score: " + str(final_score_overall))

