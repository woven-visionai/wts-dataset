<div id="top" align="center">

<p align="center">
  <img src="assets/images/overview.png">
</p>

**WTS:A Pedestrian-Centric Traffic Video Dataset for Fine-grained Spatial-Temporal Understanding**

Dataset download [**link**](TBA) (serves as official source for [`AI City Challenge Track2 @ CVPR2024`](TBA))
</div>

<div id="top" align="center">
  
[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](#licenseandcitation)
[![](https://img.shields.io/badge/Latest%20release-v1.0-yellow)](#gettingstarted)

</div>

## WTS Dataset <a name="highlight"></a>

The [Woven Traffic Safety (WTS) Dataset](https://woven-visionai.github.io/wts-dataset-homepage/) is designed to emphasize detailed behaviors of both vehicles and pedestrians within a variety of staged traffic events including accidents.
Comprising over 1.2k video events across over 255 distinct traffic scenarios, WTS integrates diverse perspectives from vehicle ego and fixed overhead cameras in a vehicle-infrastructure cooperative environment.
Each event in WTS is enriched with comprehensive textual descriptions of the observed behaviors and contexts.
For diverse experimental purposes, we also provide the same detailed textual description annotations for approximately 4.8k publicly sourced pedestrian-related traffic videos from BDD100K for external use as training resource, etc.

### Dataset structure
we have two kinds of video data provided for use:
- Collected real-world WTS data including traffic accidents.
- Filtered pedestrian-centric [BDD]([/docs/data_prep_nus.md](https://www.vis.xyz/bdd100k/)https://www.vis.xyz/bdd100k/) data with out WTS annotations.

**Video Data**

All collected WTS video data are stored under the `videos` folder. 
For the multiple-view videos, part of the scenarios will proceed across the views.
We provide the bbox annotations for the target pedestrian and vehicle for selecting the target video once needed. 
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
└── BDD_TC_5K
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

Plan to update the 3D Gaze and Location annotations for use, please keep watching!

Caption annotations for each scenario, notice that multi-view videos share the same caption:
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
        "20230707_8_SN46_T1_Camera2(2)_1.mp4",
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
            "start_time": "39.395",  ##start time of the segment
            "end_time": "44.663"     ##end time of the segment
        },
...
```

BBox annotations for the first frame of each segment in the video:
```
annotations
├── bbox_first ##bbox for the first frame of each segment
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
BBox format are following COCO format, you could use our `frame_extraction` script to reproduce the frames with `image_id`.
```
{
    "annotations": [
        {
            "image_id": 904,
            "bbox": [
                1004.4933333333333,
                163.28666666666666,
                12.946666666666667,
                11.713333333333333
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

For BDD,
```
external/
└── BDD_TC_5K
    ├── annotations
    │   ├── train
    │   │   ├── video1004_caption.json
    │   │   ├── video1006_caption.json
    │   │   ├── video1009_caption.json
    │   │   ├── video100_caption.json
    │   │   ├── video1015_caption.json
...
```
