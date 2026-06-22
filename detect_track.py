
import cv2
from ultralytics import YOLO
from deep_sort_realtime.deepsort_tracker import DeepSort

            
VIDEO_SOURCE = 0           # 0 = webcam. Replace with "sample_video.mp4" for a file.
MODEL_PATH = "yolov8x.pt"  # Nano model — fastest, good for real-time
CONFIDENCE_THRESHOLD = 0.4
BOX_COLOR = (0, 0, 255)
TEXT_COLOR = (0, 255, 255)


def load_detector(model_path: str) -> YOLO:
    """Load the pre-trained YOLOv8 detector."""
    print(f"[INFO] Loading YOLOv8 model: {model_path}")
    return YOLO(model_path)


def load_tracker() -> DeepSort:
    """Initialize the Deep SORT tracker."""
    print("[INFO] Initializing Deep SORT tracker")
    return DeepSort(max_age=30)


def open_video_source(source) -> cv2.VideoCapture:
    """Open a webcam or video file and confirm it works."""
    cap = cv2.VideoCapture(source)
    if not cap.isOpened():
        raise RuntimeError(f"Could not open video source: {source}")
    print(f"[INFO] Video source opened: {source}")
    return cap


def detect_objects(model: YOLO, frame, conf_threshold: float) -> list:
    """Run YOLOv8 on a frame and return detections formatted for Deep SORT."""
    results = model(frame, verbose=False)[0]
    detections = []

    for box in results.boxes:
        conf = float(box.conf[0])
        if conf < conf_threshold:
            continue

        x1, y1, x2, y2 = map(int, box.xyxy[0])
        cls_id = int(box.cls[0])
        label = model.names[cls_id]
        width, height = x2 - x1, y2 - y1

        # Deep SORT expects [x, y, width, height]
        detections.append(([x1, y1, width, height], conf, label))

    return detections


def draw_tracks(frame, tracks):
    """Draw bounding boxes with tracking IDs and labels on the frame."""
    for track in tracks:
        if not track.is_confirmed():
            continue

        track_id = track.track_id
        x1, y1, x2, y2 = map(int, track.to_ltrb())
        label = track.get_det_class() or "object"

        cv2.rectangle(frame, (x1, y1), (x2, y2), BOX_COLOR, 2)
        cv2.putText(
            frame,
            f"ID {track_id} | {label}",
            (x1, max(y1 - 10, 0)),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.6,
            TEXT_COLOR,
            2,
        )
    return frame


def main():
    model = load_detector(MODEL_PATH)
    tracker = load_tracker()
    cap = open_video_source(VIDEO_SOURCE)

    print("[INFO] Starting detection + tracking. Press 'q' to quit.")

    try:
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                print("[INFO] No more frames to read. Exiting.")
                break

            detections = detect_objects(model, frame, CONFIDENCE_THRESHOLD)
            tracks = tracker.update_tracks(detections, frame=frame)
            frame = draw_tracks(frame, tracks)

            cv2.imshow("Object Detection + Tracking", frame)

            if cv2.waitKey(1) & 0xFF == ord("q"):
                print("[INFO] 'q' pressed. Exiting.")
                break

    finally:
        cap.release()
        cv2.destroyAllWindows()
        print("[INFO] Resources released. Done.")


if __name__ == "__main__":
    main()