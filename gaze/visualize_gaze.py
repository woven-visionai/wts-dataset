import argparse
import json
import re
from pathlib import Path

import cv2
import numpy as np

def load_intrinsics(root: Path, cam_token: str):
    p = root / "camera_intrinsics" / f"{cam_token}.json"
    with open(p) as f:
        meta = json.load(f)[cam_token]
    fx, fy, cx, cy = meta["intrinsics"]
    K = np.array([[fx, 0, cx],
                  [0, fy, cy],
                  [0,  0,  1]], dtype=np.float32)
    dist = np.array(meta["distortion_coeffs"], dtype=np.float32)
    wh = tuple(meta["resolution"])
    return K, dist, wh, (fx, fy, cx, cy)

def draw_arrow(frame, start_xy, gaze_dir, L=150, use_fixed_length=False):
    if use_fixed_length:
        x, y, _ = gaze_dir
        magnitude = np.sqrt(x**2 + y**2)
        if magnitude < 1e-6:
            return
        norm_x = x / magnitude
        norm_y = y / magnitude
        end_x = int(start_xy[0] + norm_x * L)
        end_y = int(start_xy[1] + norm_y * L)
    else:
        x, y, z = gaze_dir
        scale = L / max(abs(z), 1e-6)
        end_x = int(start_xy[0] + x * scale)
        end_y = int(start_xy[1] + y * scale)

    cv2.arrowedLine(frame, start_xy, (end_x, end_y),
                    color=(0, 0, 255), thickness=3, tipLength=0.2)

def main(scene: str, split: str, show_head_dot: bool, no_undistort: bool, fixed_arrow_length: bool):
    root = Path(__file__).resolve().parent
    gaze_dir  = root / "3D_gaze" / split / scene
    head_dir  = root / "annotations/head" / split / scene
    video_dir = root / "videos" / split / scene / "overhead_view"
    out_dir   = root / "visualizations" / split / scene
    out_dir.mkdir(parents=True, exist_ok=True)

    for gfile in sorted(gaze_dir.glob("*_gaze.json")):
        m = re.search(r"(\d+\.\d+\.\d+\.\d+-\d+)_gaze\.json$", gfile.name)
        if not m:
            print(f"[SKIP] '{gfile.name}' – camera token not recognised")
            continue
        cam_dash = m.group(1)
        ip, idx  = cam_dash.split("-")
        cam_us   = f"{ip}_{idx}"

        hfile = head_dir / f"{scene}_{cam_us}_head.json"
        vfile = video_dir / f"{scene}_{cam_us}.mp4"
        print(f"Found gaze file: {gfile.name}")
        if not (hfile.exists() and vfile.exists()):
            print(f"[SKIP] missing head JSON or video file for {cam_dash}")
            if not hfile.exists(): print(f"  > Missing: {hfile}")
            if not vfile.exists(): print(f"  > Missing: {vfile}")
            continue

        try:
            K, dist, (W, H), _ = load_intrinsics(root, cam_dash)
        except FileNotFoundError:
            print(f"[SKIP] no intrinsics for {cam_dash}")
            continue

        gaze_anns = json.loads(gfile.read_text())["annotations"]
        head_anns = json.loads(hfile.read_text())["annotations"]
        N = min(len(gaze_anns), len(head_anns))
        if N == 0:
            print(f"[SKIIP] empty annotation list for {cam_dash}")
            continue

        cap = cv2.VideoCapture(str(vfile))
        if not cap.isOpened():
            print(f"[SKIP] cannot open video {vfile}")
            continue
        fps = cap.get(cv2.CAP_PROP_FPS) or 30
        fourcc = cv2.VideoWriter_fourcc(*"mp4v")

        out_path = out_dir / f"{gfile.stem[:-5]}_vis_head_origin.mp4"
        writer = cv2.VideoWriter(str(out_path), fourcc, fps, (W, H))

        print(f"[INFO] {scene} | {cam_dash}  →  {out_path.name}")
        
        frames_written = 0
        for i in range(N):
            gaze_dir_cam = gaze_anns[i]["gaze"]
            head_ann = head_anns[i]
            frame_id = head_ann["image_id"]
            original_head_coords = tuple(head_ann["head"])

            cap.set(cv2.CAP_PROP_POS_FRAMES, frame_id)
            ok, frame = cap.read()
            if not ok:
                print(f"  [WARN] Could not read frame {frame_id}. Stopping.")
                break
            
            if not no_undistort:
                processed_frame = cv2.undistort(frame, K, dist, None, K)
                points_to_undistort = np.array([[original_head_coords]], dtype=np.float32)
                undistorted_points = cv2.undistortPoints(points_to_undistort, K, dist, P=K)
                processed_head_coords = tuple(map(int, undistorted_points[0, 0]))
            else:
                processed_frame = frame
                processed_head_coords = tuple(map(int, original_head_coords))

            if show_head_dot:
                cv2.circle(processed_frame, center=processed_head_coords, radius=5, color=(0, 255, 0), thickness=-1)

            draw_arrow(processed_frame, processed_head_coords, gaze_dir_cam, use_fixed_length=fixed_arrow_length)
            writer.write(processed_frame)
            
            frames_written += 1

        cap.release()
        writer.release()
        print(f"  ✔ Wrote {frames_written} frames to the visualization file.\n")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("scene", help="scene ID, e.g. 20230922_12_CN7_T1")
    ap.add_argument("--split", default="train", choices=["train", "val"])
    ap.add_argument("--show-head-dot", action="store_true")
    ap.add_argument("--no-undistort", action="store_true")
    ap.add_argument("--fixed-arrow-length", action="store_true")
    args = ap.parse_args()
    main(args.scene, args.split, args.show_head_dot, args.no_undistort, args.fixed_arrow_length)