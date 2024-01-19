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

The [Woven Traffic Safety (WTS) Dataset](TBA) is designed to emphasize detailed behaviors of both vehicles and pedestrians within a variety of staged traffic events including accidents.
Comprising over 1.2k video events across over 255 distinct traffic scenarios, WTS integrates diverse perspectives from vehicle ego and fixed overhead cameras in a vehicle-infrastructure cooperative environment.
Each event in WTS is enriched with comprehensive textual descriptions of the observed behaviors and contexts.
For diverse experimental purposes, we also provide the same detailed textual description annotations for approximately 4.8k publicly sourced pedestrian-related traffic videos from BDD100K for external use as training resource, etc.

### Dataset structure
we have two kinds of video data provided for using:
- Collected real-world WTS data including traffic accidents.
- Filtered pedestrian-centric [BDD](https://www.vis.xyz/bdd100k/) data with WTS caption annotations.

**Video Data**, all collected WTS video data are stored under the videos folder. 
```
videos
├── train
│   ├── 20230707_12_SN17_T1  ##scenario index
│   │   ├── overhead_view  ##different overhead view about the scenario
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
For WTS collected data,
```
annotations
├── bbox
│   ├── pedestrian
│   │   ├── train
│   │   │   ├── 20230707_12_SN17_T1
│   │   │   │   └── overhead_view
│   │   │   │       ├── 20230707_12_SN17_T1_Camera1_0_bbox.json
│   │   │   │       ├── 20230707_12_SN17_T1_Camera2_3_bbox.json
│   │   │   │       ├── 20230707_12_SN17_T1_Camera3_1_bbox.json
│   │   │   │       └── 20230707_12_SN17_T1_Camera4_2_bbox.json
│   │   │   ├── 20230707_15_SY4_T1
│   │   │   │   └── overhead_view
│   │   │   │       ├── 20230707_15_SY4_T1_Camera1_0_bbox.json
│   │   │   │       ├── 20230707_15_SY4_T1_Camera2_1_bbox.json
│   │   │   │       └── 20230707_15_SY4_T1_Camera3_2_bbox.json
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
