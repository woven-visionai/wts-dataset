<div id="top" align="center">

<p align="center">
  <img src="assets/images/overview.png">
</p>

**WTS:A Pedestrian-Centric Traffic Video Dataset for Fine-grained Spatial-Temporal Understanding**

Dataset download [**link**](https://docs.google.com/forms/u/1/d/e/1FAIpQLSe6eshgQQyf1wZmJkgnqsoDaFb_h-673qG7VHPxapkhh30_Gw/viewform?usp=send_form) (serves as official source for [`AI City Challenge Track2`](https://www.aicitychallenge.org/2024-challenge-tracks/))
</div>

<div id="top" align="center">
  
[![License](https://img.shields.io/badge/License-wts_terms%20-blue)](#licenseandcitation)
[![](https://img.shields.io/badge/Latest%20release-v1.0-yellow)](#datastructure)
[![Project](https://img.shields.io/badge/Project-website%20-green)](https://woven-visionai.github.io/wts-dataset-homepage/)
</div>

## News and Updates</a>

### News <a name="news"></a>
- **`[2025/06/13]`** All data (including videos, captions, VQA, 3D gaze, and bbox) are **up-to-date**.

- **`[2025/05/21]`** AIC challenge Track2 Test data for **ICCV 2025** is released and [evaluation](https://eval.aicitychallenge.org/aicity2025/login) is open!
  
- **`[2024/07/25]`** WTS dataset is accepted by ECCV24! Updated arXiv [paper](https://arxiv.org/abs/2407.15350)! 

- **`[2024/06/30]`** AI City Challenge 2024 is finished this year! Please directly require the WTS dataset from this [form](https://docs.google.com/forms/d/e/1FAIpQLSe6eshgQQyf1wZmJkgnqsoDaFb_h-673qG7VHPxapkhh30_Gw/viewform)

- **`[2024/02/23]`** Updated the [evaluation script](https://github.com/woven-visionai/wts-dataset/tree/main/evaluation/eval-metrics-AIC-Track2) for AIC Track2 evaluatin system submission.

- **`[2024/02/22]`** AIC challenge Track2 Test data for ECCV 2024 is released and [evaluation](https://www.aicitychallenge.org/2024-evaluation-system/) is open !

- **`[2024/02/22]`** BBox of whole train/val of dataset are updated! Please download it from provided dropbox or google drive link to your email.

- **`[2024/01/31]`** updated with the [evaluation script](https://github.com/woven-visionai/wts-dataset/tree/main/evaluation/eval-metrics-AIC-Track2) for AIC Track2.
- **`[2024/01/22]`** [AI City Challenge 2024 Track2](https://www.aicitychallenge.org/2024-challenge-tracks/) opened.
- **`[2024/01/22]`** WTS dataset released.
- **`[2024/01/21]`** WTS dataset [project page](https://woven-visionai.github.io/wts-dataset-homepage/) released.

### Update List <a name="update"></a>

- [x] List of views used as main reference during annotation. (2024/01/23)
- [x] First frame annotated bbox for each segment. (2024/02/22)
- [x] Generated bbox for target pedesrian and vehicle. (2024/02/22)
- [x] Evaluation code. (2024/02/23)
- [x] 3D Gaze annotation release. (2024/07/17)
- [x] Dataset arXiv paper. 

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

## Dataset Download

1. Please **submit request** through [Google Form](https://docs.google.com/forms/u/1/d/e/1FAIpQLSe6eshgQQyf1wZmJkgnqsoDaFb_h-673qG7VHPxapkhh30_Gw/viewform?usp=send_form) first.
2. You will get a DropBox link and a Google Drive link. They have identical content, so you can choose **either one**.
3. For the Google Drive, in case you do not have access, **request on Google Drive** and it will be approved manually as long as you have completed Step 1.


## Dataset Overview

### Internal and External Datasets
As described in our [paper](https://arxiv.org/abs/2407.15350), the dataset consists of 2 parts:
1. **Internal dataset:**

    Real-world WTS data including traffic accidents. We collected them **from scratch**.

2. **External dataset:**

    Based on [BDD100K](https://www.vis.xyz/bdd100k/) data, we filtered out pedestrian-centric videos. We call it `BDD_PC_5K`.


### Videos, Caption and VQA
This challenge consists of **2 tasks**:
- Captioning task
- VQA task

Therefore, for the **train/val split**, we provide these data:
- Videos
- Ground-truth **captions**
- Ground-truth **VQA**


### Additional metadata
Additionally, we provide additional **metadata** at our best effort:
- Bbox (of the target pedestrian and the vehicle)
  - We provide 2 variations:
    - bbox_annotated (i.e. human annotations of the first frame of each phase only)
    - bbox_generated (i.e. including above, and generated bboxes of the following frames using Track-Anything)
- 3D Gaze and 2D head position of the pedestrian.


Note: It's **optional** for you to utilize these additional metadata for your algorithm.

<p>&nbsp;</p>

Above forms our WTS dataset.

<p>&nbsp;</p>

## Dataset File Structure
To help you navigate through the downloaded files, here we list the **folder link of each part** of data.

### Train/val split
  - Internal dataset
    - [Video](https://drive.google.com/file/d/1U_cpSGMD8BKr6WZJKwBfFljEPm2g-EVm/view?usp=drive_link)
    - [Caption](https://drive.google.com/file/d/1JhBTxusph_1I1BhGaA8Ykx7EowcuK370/view?usp=drive_link)
    - [VQA](https://drive.google.com/file/d/1qejf0VO33v-Rm-8X4-leKclgakoLJY1w/view?usp=drive_link)
    - [bbox_annotated](https://drive.google.com/file/d/1HLmzMapqRJLyM5Ema5oWrJBktZ2iGbLa/view?usp=drive_link)
    - [bbox_generated](https://drive.google.com/file/d/1PJZlgluyxCjgkrfVTnXK24FupDYEEyB0/view?usp=drive_link)
    - [3D Gaze](https://drive.google.com/file/d/1744aqEwUuOFGyCVHNtthsAZtHf7ekEbG/view?usp=drive_link)
    - [Head](https://drive.google.com/file/d/1tX1LGONFvkgFLWWUX31eyN6YkhpK-1nW/view?usp=drive_link)

      
  - External dataset
    - [Video](https://drive.google.com/file/d/1EJgLslKvyKMUyPC-aWR8YpzNZRBUu-gg/view?usp=drive_link)
    - [VQA, Caption, and Bbox](https://drive.google.com/file/d/1rzExQcjkuV3_C4WtDBRWHBwBiRnBzxtO/view?usp=drive_link)


### Public Test split
- For both internal & external datasets:
  - [Videos and phase start/end timestamps](https://drive.google.com/file/d/1f32teoQ4OWLCe7AHisHvkTH3woQ3x768/view?usp=drive_link)
  - [Bbox](https://drive.google.com/file/d/1y8BANRcuf1wgHS7DvNwae0HhXjjrem0E/view?usp=drive_link)
  - [VQA](https://drive.google.com/file/d/1ArrB4r100958xbFewJXRar77VnWECFIp/view?usp=drive_link)


## Video Data Structure

All collected WTS video data are stored under the `videos` folder. 
Some scenarios have multiple-view videos.

```
videos
├── train
│   ├── 20230707_12_SN17_T1  ##scenario index
│   │   ├── overhead_view    ##different overhead views of the scenario
│   │   │   ├── 20230707_12_SN17_T1_Camera1_0.mp4
│   │   │   ├── 20230707_12_SN17_T1_Camera2_3.mp4
│   │   │   ├── 20230707_12_SN17_T1_Camera3_1.mp4
│   │   │   └── 20230707_12_SN17_T1_Camera4_2.mp4
│   │   └── vehicle_view  ##vehicle ego-views of the scenario
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

## Annotation Data Format and Structure

### Caption

Note that the videos from overhead_view and vehicle_view in the same scenario folder will share the same caption.

```
annotations
├──caption/
  ├── train
  │   ├── 20230707_12_SN17_T1 ##scenario index
  │   │   ├── overhead_view   
  │   │   │   └── 20230707_12_SN17_T1_caption.json   ##captions are shared by multiple views
  │   │   └── vehicle_view   
  │   │       └── 20230707_12_SN17_T1_caption.json   ##captions are the same as overhead view. Only timestamp may be different, in order to find the same phase in the vehicle view video.
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

<p>&nbsp;</p>

### BBox 
BBox annotations for the first frame of each segment in the video. Note that not all videos have the bbox metadata, as there are some views that cannot cover the pedestrian or vehicle. Also, when the first-frame bbox for a phase is too small, we do not generate tracked bbox for that phase.

Human-Annotated Bboxes
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

Generated Bboxes
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

For BDD, each caption annotations correspond with one video.
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
<p>&nbsp;</p>


### Gaze and Head Position
See the [Gaze README](gaze/README.md).

<p>&nbsp;</p>

### VQA

```
annotations
├── vqa
│   └── train
│   │   ├── 20230707_8_SN46_T1
│   │   │   ├── environment ## contains QA about environment
│   │   │   │      ├── 20230707_8_SN46_T1.json  
│   │   │   └── overhead_view ## contains QA about overhead view
│   │   │   │      ├── 20230707_8_SN46_T1.json  
│   │   │   └── vehicle_view ## contains QA about vehicle view
│   │   │   │      ├── 20230707_8_SN46_T1.json
│   │   ├── 
...
│   └── val
│   │   ├── 20230707_9_SN1_T1
│   │   │   ├── environment 
│   │   │   │      ├── 20230707_9_SN1_T1.json  
│   │   │   └── overhead_view
│   │   │   │      ├── 20230707_9_SN1_T1.json  
│   │   │   └── vehicle_view
│   │   │   │      ├── 20230707_9_SN1_T1.json
```

VQA follows the following format

QA for environment follows the format:

```
[
    {
        "id": 722,
        "overhead_videos": [
            "20230707_8_SN46_T1_Camera1_0.mp4",
            "20230707_8_SN46_T1_Camera2_1.mp4",
            "20230707_8_SN46_T1_Camera2_2.mp4",
            "20230707_8_SN46_T1_Camera3_3.mp4"
        ],
        "environment": [
            {
                "question": "What is the road inclination in the scene?",
                "a": "Steep downhill",
                "b": "Level",
                "c": "Gentle downhill",
                "d": "Steep uphill",
                "correct": "b"
            },
            ...
```

QA for overhead/vehicle QA follows the format:

```
[
    {
        "id": 722,
        "overhead_videos": [
            "20230707_8_SN46_T1_Camera1_0.mp4",
            "20230707_8_SN46_T1_Camera2_1.mp4",
            "20230707_8_SN46_T1_Camera2_2.mp4",
            "20230707_8_SN46_T1_Camera3_3.mp4"
        ],
        "event_phase": [
            {
                "start_time": "39.395",
                "end_time": "44.663",
                "labels": [
                    "avoidance"
                ],
                "conversations": [
                    {
                        "question": "What is the orientation of the pedestrian's body?",
                        "a": "Same direction as the vehicle",
                        "b": "Diagonally to the left, in the opposite direction to the vehicle",
                        "c": "Perpendicular to the vehicle and to the right",
                        "d": "Diagonally to the right, in the same direction as the vehicle",
                        "correct": "c"
                    },
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

## Evaluation of Captioning Task

We provide the validation set for the video2text task with a given segment duration.
Video and its GT of the validation set are stored following the same structure as `train` under `val` folders.

For our collected data in WTS, the inference results are required to be provided per scenario. 
Users could feel free to use the multi-view videos in the same scenario folders for validation purposes, 
as well as multi-view videos in `train` for training purposes.
For `BDD_PC_5K`, each video has its caption GT in `train` and `val`, and validation will be done per video.

Regarding `AI City Challenge Track2`, the evaluation script is provided under `evaluation/eval-metrics-AIC-Track2/`, notice that only caption annotations will be used for the challenge.
Submission(model output) format is defined as:
```
{
    "20230707_12_SN17_T1": [  ##scenario index for multiple view situations OR video name for single view of "BDD_PC_5K".
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

    "20231013_105827_normal_192.168.0.14_1_event_2": [  ##scenario index for multiple view situations OR video name for single view "BDD_PC_5K".
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
    
    "video3334": [  ##scenario index for multiple view situations OR video name for single view "BDD_PC_5K".
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
2. In your submission, please make sure all video segments that the dataset annotation specified have both "caption_pedestrian" an "caption_vehicle" keys existing. Otherwise, you will get KeyError saying the key is not found.


## Evaluation of Visual Question Answering Task

The evaluation script for VQA task is located here: 
```
evaluation/eval-metrics-AIC-Track2_VQA/traffic_qa_evaluation_script.py
```

The evaluation script expects the following format:
```
[
  {
    "id": "3c8c80e3-33f1-4133-a86c-1192c8a26159",
    "correct": "a"
  },
  ...
  
  where id is the question id in test set and correct is the predicted option label.
```

Refer [this](https://github.com/woven-visionai/wts-dataset/blob/main/evaluation/eval-metrics-AIC-Track2_VQA/README.md) for more details.

Note:
1. Missing predictions for QAs are counted as zero score.


## Annotation Manner <a name="licenseandcitation"></a>

Our annotation pipeline:
<img width="896" alt="image" src="https://github.com/user-attachments/assets/63fa5f89-662c-455c-ac6a-9f06223d009c" />



## License and Citation <a name="licenseandcitation"></a>
Please refer to our license from WTS dataset [homepage](https://woven-visionai.github.io/wts-dataset-homepage/)

Please consider citing our paper if you find WTS dataset is helpful for your works.
```BibTeX
@misc{kong2024wtspedestriancentrictrafficvideo,
      title={WTS: A Pedestrian-Centric Traffic Video Dataset for Fine-grained Spatial-Temporal Understanding}, 
      author={Quan Kong and Yuki Kawana and Rajat Saini and Ashutosh Kumar and Jingjing Pan and Ta Gu and Yohei Ozao and Balazs Opra and David C. Anastasiu and Yoichi Sato and Norimasa Kobori},
      year={2024},
      eprint={2407.15350},
      archivePrefix={arXiv},
      primaryClass={cs.CV},
      url={https://arxiv.org/abs/2407.15350}, 
}
```
