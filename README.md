
# 🎯 Real-Time Object Detection & Tracking

![Python](https://img.shields.io/badge/Python-3.11-blue?style=flat-square&logo=python)
![YOLOv8](https://img.shields.io/badge/Model-YOLOv8-purple?style=flat-square)
![OpenCV](https://img.shields.io/badge/OpenCV-Computer%20Vision-green?style=flat-square&logo=opencv)
![DeepSORT](https://img.shields.io/badge/Tracking-Deep%20SORT-orange?style=flat-square)
![Status](https://img.shields.io/badge/Status-Working-brightgreen?style=flat-square)

> Detect objects in real time, then track each one with a persistent ID
> as it moves across the frame — powered by YOLOv8 and Deep SORT.

---

## 🎬 What This Project Does

Most detection scripts find objects frame by frame with no memory —
every object gets treated as brand new each time. This project goes
further: it **detects AND tracks**, assigning each object a unique ID
that stays consistent as it moves, leaves, and re-enters the frame.

Point it at your webcam or a video file, and watch it label every
person, car, or object in real time with a bounding box, class name,
and tracking ID.

---

## 🧠 How It Works

```
Video Frame
    │
    ▼
┌──────────────────────────────┐
│  Step 1 — YOLOv8 Detection   │   Finds objects in the current frame
│  Returns: boxes + labels     │   (person, car, dog, etc.) with confidence
└──────────────────────────────┘
    │
    ▼
┌──────────────────────────────┐
│  Step 2 — Confidence Filter  │   Discards detections below the
│  Threshold: 0.4              │   confidence threshold (reduces noise)
└──────────────────────────────┘
    │
    ▼
┌──────────────────────────────┐
│  Step 3 — Deep SORT Tracking │   Matches this frame's detections to
│  Assigns persistent IDs      │   objects tracked in previous frames
└──────────────────────────────┘
    │
    ▼
┌──────────────────────────────┐
│  Step 4 — Draw & Display     │   Renders boxes, labels, and IDs
│  Real-time output window     │   directly onto the video feed
└──────────────────────────────┘
```

---

## 📁 Project Structure

```
object-detection-project/
│
├── detect_track.py       # Main script — detection + tracking
├── yolov8n.pt             # Pre-trained YOLOv8 model (auto-downloaded)
├── requirements.txt       # Python dependencies
└── README.md              # You are here
```

---

## 🛠️ Tech Stack

| Component | Purpose |
|---|---|
| **YOLOv8** (`ultralytics`) | Real-time object detection |
| **OpenCV** (`opencv-python`) | Video capture, frame processing, display |
| **Deep SORT** (`deep-sort-realtime`) | Multi-object tracking with persistent IDs |

---

## ⚙️ Installation

### 1. Clone or download this project
```bash
git clone https://github.com/your-username/object-detection-project.git
cd object-detection-project
```

### 2. (Recommended) Create a virtual environment
```bash
python -m venv venv
venv\Scripts\activate        # Windows
source venv/bin/activate     # macOS/Linux
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

Or install manually:
```bash
pip install ultralytics opencv-python deep-sort-realtime
```

---

## ▶️ Usage

### Run with webcam (default)
```bash
python detect_track.py
```

### Run with a video file
Open `detect_track.py` and change:
```python
VIDEO_SOURCE = 0
```
to:
```python
VIDEO_SOURCE = "sample_video.mp4"
```
Then run the same command:
```bash
python detect_track.py
```

Press **`q`** at any time to quit.

---

## 🎛️ Configuration

All key settings are at the top of `detect_track.py` — no need to dig through the code:

```python
VIDEO_SOURCE = 0              # 0 = webcam, or path to a video file
MODEL_PATH = "yolov8n.pt"     # YOLOv8 model size (n/s/m/l/x)
CONFIDENCE_THRESHOLD = 0.4    # Minimum confidence to display a detection
BOX_COLOR = (0, 255, 0)       # Bounding box color (BGR format)
TEXT_COLOR = (0, 255, 0)      # Label text color (BGR format)
```

### YOLOv8 Model Options

| Model | Speed | Accuracy | Best For |
|---|---|---|---|
| `yolov8n.pt` | ⚡ Fastest | Lower | Real-time webcam on a normal PC |
| `yolov8s.pt` | Fast | Better | Balanced performance |
| `yolov8m.pt` | Medium | Good | Higher accuracy needs |
| `yolov8l.pt` / `yolov8x.pt` | Slow | Best | GPU-equipped systems |

---

## 📊 Sample Output

```
[INFO] Loading YOLOv8 model: yolov8n.pt
[INFO] Initializing Deep SORT tracker
[INFO] Video source opened: 0
[INFO] Starting detection + tracking. Press 'q' to quit.
[INFO] 'q' pressed. Exiting.
[INFO] Resources released. Done.
```

On screen, each detected object is displayed as:
```
┌─────────────────────┐
│  ID 3 | person       │
└─────────────────────┘
```
The **ID stays the same** as the object moves — that's the tracking part working.

---

## 🔍 Detection vs. Tracking — What's the Difference?

| | Detection Only | Detection + Tracking (this project) |
|---|---|---|
| Identifies objects per frame | ✅ | ✅ |
| Draws bounding boxes | ✅ | ✅ |
| Remembers object identity across frames | ❌ | ✅ |
| Assigns persistent ID numbers | ❌ | ✅ |
| Useful for counting unique objects | ❌ | ✅ |

---

## 🚀 Possible Improvements

- [ ] Save output video to a file instead of just displaying it
- [ ] Add an FPS counter overlay
- [ ] Filter detections to specific classes only (e.g. people only)
- [ ] Add a counting system for objects crossing a line
- [ ] Deploy as a web app using Streamlit or Flask
- [ ] Support multiple camera inputs simultaneously

---

## ❗ Troubleshooting

| Error | Fix |
|---|---|
| `ModuleNotFoundError: No module named 'cv2'` | Run `pip install opencv-python` |
| `ModuleNotFoundError: No module named 'ultralytics'` | Run `pip install ultralytics` |
| Webcam doesn't open | Try `VIDEO_SOURCE = 1` instead of `0` |
| Slow performance | Switch to `yolov8n.pt` (fastest model) |
| Model download fails | Check internet connection (only needed on first run) |

---

## 📄 License

This project is open for educational and personal use.
Feel free to fork, modify, and build on it.




