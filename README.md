<div id="top" align="center">

<p align="center">
  <img src="assets/images/overview.png">
</p>

**WTS:A Pedestrian-Centric Traffic Video Dataset for Fine-grained Spatial-Temporal Understanding**

Dataset download [**link**](https://docs.google.com/forms/u/1/d/e/1FAIpQLSe6eshgQQyf1wZmJkgnqsoDaFb_h-673qG7VHPxapkhh30_Gw/viewform?usp=send_form) (serves as official source for [`AI City Challenge 2024 Track2 @ CVPR2024`](https://www.aicitychallenge.org/2024-challenge-tracks/))
</div>

<div id="top" align="center">
  
[![License](https://img.shields.io/badge/License-wts_terms%20-blue)](#licenseandcitation)
[![](https://img.shields.io/badge/Latest%20release-v1.0-yellow)](#datastructure)
[![Project](https://img.shields.io/badge/Project-website%20-green)](https://woven-visionai.github.io/wts-dataset-homepage/)
</div>

## News and Updates</a>

### News <a name="news"></a>
- **`Note:`** for the purpose of joining the AI City Challenge Track2 2024, please make sure you fill up the [form](https://docs.google.com/forms/d/e/1FAIpQLSdOVC33d-R23PCuBdSsmo08e-98HiDLykhIIAzryjzjYoilVQ/viewform) from AIC as well.

- **`[2024/02/23]`** updated the [evaluation script](https://github.com/woven-visionai/wts-dataset/tree/main/evaluation/eval-metrics-AIC-Track2) for AIC Track2 evaluatin system submission.

- **`[2024/02/22]`** AIC challenge Track2 Test data released and [evaluation](https://www.aicitychallenge.org/2024-evaluation-system/) is open !

- **`[2024/02/22]`** BBox of whole train/val of dataset are updated! Please download it from privided dropbox or google drive link to your email.

- **`[2024/01/31]`** updated with the [evaluation script](https://github.com/woven-visionai/wts-dataset/tree/main/evaluation/eval-metrics-AIC-Track2) for AIC Track2.
- **`[2024/01/22]`** [AI City Challenge 2024 Track2](https://www.aicitychallenge.org/2024-challenge-tracks/) opened.
- **`[2024/01/22]`** WTS dataset released.
- **`[2024/01/21]`** WTS dataset [project page](https://woven-visionai.github.io/wts-dataset-homepage/) released.

### Update List <a name="update"></a>

- [x] List of views used as main reference during annotation. (2024/01/23)
- [x] First frame annotated bbox for each segment. (2024/02/22)
- [x] Generated bbox for target pedesrian and vehicle. (2024/02/22)
- [x] Evaluation code. (2024/02/23)
- [ ] 3D Gaze annotation release.
- [ ] Dataset arXiv paper. 

## WTS Dataset <a name="introduction"></a>

The [Woven Traffic Safety (WTS) Dataset](https://woven-visionai.github.io/wts-dataset-homepage/) from [Woven by Toyota, Inc.](https://woven.toyota/en/), is designed to emphasize detailed behaviors of both vehicles and pedestrians within a variety of staged traffic events including accidents.
Comprising over 1.2k video events across over 130 distinct traffic scenarios, WTS integrates diverse perspectives from vehicle ego and fixed overhead cameras in a vehicle-infrastructure cooperative environment.
Each event in WTS is enriched with comprehensive textual descriptions of the observed behaviors and contexts.
For diverse experimental purposes, we also provide the same detailed textual description annotations for approximately 4.8k publicly sourced pedestrian-related traffic videos from BDD100K for external use as training/test resources, etc.

## Features and Comparison <a name="feature"></a>

WTS provides the largest number of videos with long fine-grained video descriptions with 3D spatial information in the traffic domain.
<p align="center">
  <img src="assets/images/comparison.png" width="800">
</p>

## Dataset Structure <a name="datastructure"></a>
we have two kinds of video data provided for use:
- Collected real-world WTS data including traffic accidents.
- Filtered pedestrian-centric videos from [BDD100K](https://www.vis.xyz/bdd100k/) data with our WTS annotations as `BDD_PC_5K`

**Video Data**

All collected WTS video data are stored under the `videos` folder. 
For the multiple-view videos, part of the scenarios will proceed across the views.
We also provide the bbox annotations for the target pedestrian and vehicle for selecting the target video once needed. 
```
videos
├── train
│   ├── 20230707_12_SN17_T1  ##scenario index
│   │   ├── overhead_view    ##different overhead view about the scenario
│   │   │   ├── 20230707_12_SN17_T1_Camera1_0.mp4
│   │   │   ├── 20230707_12_SN17_T1_Camera2_3.mp4
│   │   │   ├── 20230707_12_SN17_T1_Camera3_1.mp4
│   │   │   └── 20230707_12_SN17_T1_Camera4_2.mp4
│   │   └── vehicle_view  ##vehicle ego-view about the scenario
│   │       └── 20230707_12_SN17_T1_vehicle_view.mp4
│   ├── 20230707_15_SY4_T1
│   │   ├── overhead_view
│   │   │   ├── 20230707_15_SY4_T1_Camera1_0.mp4
│   │   │   ├── 20230707_15_SY4_T1_Camera2_1.mp4
│   │   │   └── 20230707_15_SY4_T1_Camera3_2.mp4
│   │   └── vehicle_view
│   │       └── 20230707_15_SY4_T1_vehicle_view.mp4
...
```
All pedestrian-related videos from BDD are stored under `external` folder:
```
external/
└── BDD_PC_5K
    ├── videos
    │   ├── train
        │   ├── video1004.mp4
        │   ├── video1006.mp4
        │   ├── video1009.mp4
        │   ├── video100.mp4
        │   ├── video1015.mp4
...
```

**Annotation**

Two kinds of annotations now are available. 
- BBox for the target pedestrian and vehicle.
- Description for the traffic scenario focuses on the `location, attention, behavior, context` regarding the pedestrian and vehicle.
- 3D Gaze of the pedestrian

Will update the 3D Gaze and Location annotations for use (stay tuned).

Notice that the videos from overhead and vehicle in the same scneario index folder will share the same caption.
```
annotations
├──caption/
  ├── train
  │   ├── 20230707_12_SN17_T1 ##scenario index
  │   │   ├── overhead_view   
  │   │   │   └── 20230707_12_SN17_T1_caption.json   ##caption shared by multiple views
  │   │   └── vehicle_view   
  │   │       └── 20230707_12_SN17_T1_caption.json   ##caption is the same as overhead view, only timestamp is for vehicle view for finding the same segment.
  │   ├── 20230707_15_SY4_T1
  │   │   ├── overhead_view
  │   │   │   └── 20230707_15_SY4_T1_caption.json
  │   │   └── vehicle_view
  │   │       └── 20230707_15_SY4_T1_caption.json
...
```
Caption JSON format:
```
{
    "id": 722,
    "overhead_videos": [ ## caption related videos
        "20230707_8_SN46_T1_Camera1_0.mp4",
        "20230707_8_SN46_T1_Camera2_1.mp4",
        "20230707_8_SN46_T1_Camera2_2.mp4",
        "20230707_8_SN46_T1_Camera3_3.mp4"
    ],
    "event_phase": [
        {
            "labels": [
                "4"  ##segment number
            ],
            "caption_pedestrian": "The pedestrian stands still on the left side behind the vehicle, ...",  ##caption for pedestrian during the segment
            "caption_vehicle": "The vehicle was positioned diagonally to ...",  ##caption for vehicle during the segment
            "start_time": "39.395",  ##start time of the segment in seconds, 0.0 is the starting time of the given video.
            "end_time": "44.663"     ##end time of the segment in seconds
        },
...
```

BBox annotations for the first frame of each segment in the video, notice that not all videos have the bbox as there are some views that can not cover the pedestrian or vehicle.
```
annotations
├── bbox_annotated ##bbox for the first frame of each segment
│   ├── pedestrian  ##bbox for pedestrian and vehicle respectively 
│   │   ├── train
│   │   │   ├── 20230707_12_SN17_T1
│   │   │   │   └── overhead_view
│   │   │   │       ├── 20230707_12_SN17_T1_Camera1_0_bbox.json  ##bbox for per video
│   │   │   │       ├── 20230707_12_SN17_T1_Camera2_3_bbox.json
│   │   │   │       ├── 20230707_12_SN17_T1_Camera3_1_bbox.json
│   │   │   │       └── 20230707_12_SN17_T1_Camera4_2_bbox.json
...
```
BBox annotations for the whole frames generated by the video object tracking method for each segment in the video:
```
annotations
├── bbox_generated  ##bbox for the whole frame of each segment
│   ├── pedestrian  ##bbox for pedestrian and vehicle respectively
│   │   ├── train
│   │   │   ├── 20230707_12_SN17_T1
│   │   │   │   └── overhead_view
│   │   │   │       ├── 20230707_12_SN17_T1_Camera1_0_bbox.json  ##bbox for per video
│   │   │   │       ├── 20230707_12_SN17_T1_Camera2_3_bbox.json
│   │   │   │       ├── 20230707_12_SN17_T1_Camera3_1_bbox.json
│   │   │   │       └── 20230707_12_SN17_T1_Camera4_2_bbox.json
...
```
BBox format follows COCO format, you could use our `frame_extraction` script to reproduce the frames with `image_id`.
```
{
    "annotations": [
        {
            "image_id": 904, ## frame ID
            "bbox": [
                1004.4933333333333, ## x_min 
                163.28666666666666, ## y_min
                12.946666666666667, ## width
                11.713333333333333  ## height
            ],
            "auto-generated": false,  ##human annotated frame
            "phase_number": "0"
        },
        {
            "image_id": 905,
            "bbox": [
                1007.1933333333333,
                162.20666666666668,
                12.946666666666667,
                11.713333333333333
            ],
            "auto-generated": true,  ##generated bbox annotation for the frame
            "phase_number": "0"
        },
...
```

For BDD, each caption annotations correspond with one video for use.
The annotation format is the same as our collected data caption annotations.
```
external/
└── BDD_PC_5K
    ├── annotations
    │   ├── train
    │   │   ├── video1004_caption.json
    │   │   ├── video1006_caption.json
    │   │   ├── video1009_caption.json
    │   │   ├── video100_caption.json
    │   │   ├── video1015_caption.json
...
```

3D Gaze is also provided for each camera for a given dates and the structure is shown below:

```
annotations
├── 3D_gaze
│   ├── pedestrian  ## 3D gaze is only provided for the pedestrian
│   │   ├── train
│   │   │   ├── 20230922_1_SN2_T1
│   │   │   │   └── overhead_view
│   │   │   │       ├── 20230922_1_SN2_T1_192.168.0.11-1_gaze.json  ## Gaze per camera video 
│   │   │   │       ├── 20230922_1_SN2_T1_192.168.0.12-2_gaze.json
│   │   │   │       └── 20230922_1_SN2_T1_192.168.0.28-3_gaze.json
...
```
Gaze annotation follows the similar structure as BBox, as shown below. The gaze (x, y, z) is in overhead camera coordinates in OpenGL axis convention (x to the right, y up, and z backward). `image_id` refers to the frame number in the overhead video.

```
{
    "annotations": [
        {
            "image_id": 0, ## frame ID
            "gaze": [
                0.7267333451506679, ## x
                0.27087537465994793, ## y
                -0.6312568142259175 ## z
            ],
        },
        {
            "image_id": 1,
            "gaze": [
                0.7267333451506679,
                0.27087537465994793,
                -0.6312568142259175
            ],
        },
...
```

## Data Preparation

- Our BBox annotation is frame-based, you could use the below script to extract the frame to align the ID in our annotations.
```
python script/frame_extraction.py
```

- The caption annotations are shared with the videos in the same scenario folders in WTS collected video part.
We provide a list of which camera views are mainly used as a reference during the annotation, thuss which views are covered well of the whole scenarios in 
`view_used_as_main_reference.csv` as below format. Users could feel free to use it.
```
<Scene,Viewpoint1_video_name,Viewpoint2_video_name,Viewpoint3_video_name,...>  ##maximum to 4 views
20230707_4_CN35_T1,20230707_4_CN35_T1_Camera3_0.mp4,20230707_4_CN35_T1_Camera4_1.mp4
20230707_8_SN46_T1,20230707_8_SN46_T1_Camera2_1.mp4,20230707_8_SN46_T1_Camera2_2.mp4
20230707_9_SN1_T1,20230707_9_SN1_T1_Camera2_1.mp4,20230707_9_SN1_T1_Camera2_2.mp4
```

## Evaluation

We provide the validation set for the video2text task with a given segment duration.
Video and its GT of the validation set are stored following the same structure as `train` under `val` folders.

For our collected data in WTS, the inference results are required to be provided per scenario. 
Users could feel free to use the multi-view videos in the same scenario folders for validation purposes, 
as well as multi-view videos in `train` for training purposes.
For `BDD_PC_5K`, each video has its caption GT in `train` and `val`, and validation will be done per video.

Regarding `AI City Challenge 2024 Track2`, the evaluation script is provided under `evaluation/`, notice that only caption annotations will be used for the challenge.
Submission(model output) format is defined as:
```
{
    "20230707_12_SN17_T1": [  ##scneario index for multiple view situations OR video name for single view of "BDD_PC_5K".
        {
            "labels": [  ##segment number, this is known information will be given
                "4"
            ],
            "caption_pedestrian": "",  ##caption regarding pedestrian 
            "caption_vehicle": ""      ##caption regarding vehicle
        },
        {
            "labels": [
                "3"
            ],
            "caption_pedestrian": "",
            "caption_vehicle": ""
        },
        {
            "labels": [
                "2"
            ],
            "caption_pedestrian": "",
            "caption_vehicle": ""
        },
        {
            "labels": [
                "1"
            ],
            "caption_pedestrian": "",
            "caption_vehicle": ""

        },
        {
            "labels": [
                "0"
            ],
            "caption_pedestrian": "",
            "caption_vehicle: ""
        }
    ]

    "20231013_105827_normal_192.168.0.14_1_event_2": [  ##scneario index for multiple view situations OR video name for single view "BDD_PC_5K".
        {
            "labels": [  ##segment number, this is known information will be given
                "4"
            ],
            "caption_pedestrian": "",  ##caption regarding pedestrian 
            "caption_vehicle": ""      ##caption regarding vehicle
        },
        {
            "labels": [
                "3"
            ],
            "caption_pedestrian": "",
            "caption_vehicle": ""
        },
        {
            "labels": [
                "2"
            ],
            "caption_pedestrian": "",
            "caption_vehicle": ""
        },
        {
            "labels": [
                "1"
            ],
            "caption_pedestrian": "",
            "caption_vehicle": ""

        },
        {
            "labels": [
                "0"
            ],
            "caption_pedestrian": "",
            "caption_vehicle: ""
        }
    ]
    
    "video3334": [  ##scneario index for multiple view situations OR video name for single view "BDD_PC_5K".
        {
            "labels": [  ##segment number, this is known information will be given
                "4"
            ],
            "caption_pedestrian": "",  ##caption regarding pedestrian 
            "caption_vehicle": ""      ##caption regarding vehicle
        },
        {
            "labels": [
                "3"
            ],
            "caption_pedestrian": "",
            "caption_vehicle": ""
        },
        {
            "labels": [
                "2"
            ],
            "caption_pedestrian": "",
            "caption_vehicle": ""
        },
        {
            "labels": [
                "1"
            ],
            "caption_pedestrian": "",
            "caption_vehicle": ""

        },
        {
            "labels": [
                "0"
            ],
            "caption_pedestrian": "",
            "caption_vehicle": ""
        }
    ]
}
```

Note:
1. Please submit one JSON file that includes results for ALL videos in the test set. Otherwise, you will get warning saying counting zero score for missing videos.
2. In your submissin, please make sure all video segments that the dataset annotation specified have both "caption_pedestrian" an "caption_vehicle" keys existing. Otherwise, you will get KeyError saying the key is not found.

## Annotation Manner <a name="licenseandcitation"></a>

will be updated with the arXiv paper soon.

## License and Citation <a name="licenseandcitation"></a>
Please refer to our license from WTS dataset [homepage](https://woven-visionai.github.io/wts-dataset-homepage/)

Please consider citing our project if you find WTS dataset is helpful for your works.
```BibTeX
@article{WTS2024,
title = {WTS: A Pedestrian-Centric Traffic Video Dataset for Fine-grained Spatial-Temporal Understanding},
author = {Quan Kong and Yuki Kawana and Rajat Saini and Ashutosh Kumar and Jingjing Pan and Ta Gu and Yohei Ozao and Balazs Opra and David C. Anastasiu and Yoichi Sato and Norimasa Kobori},
year = {2024},
url = {https://github.com/woven-visionai/wts-dataset}
}
```
