import streamlit as st
import cv2
import tempfile
import numpy as np
from ultralytics import YOLO
from PIL import Image

# Title
st.title("🚘 Vehicle Type and Color Detection with YOLOv8")

# Upload video
uploaded_file = st.file_uploader("Upload a vehicle video (.mp4, .avi)", type=["mp4", "avi"])

# Load YOLOv8 model
model = YOLO("yolov8n.pt")  # You can use yolov8s.pt for better accuracy

# Color detection
def get_dominant_color(image):
    try:
        hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        avg_color = hsv.mean(axis=0).mean(axis=0)
        h = avg_color[0]

        if h < 10 or h > 160:
            return 'Red'
        elif 10 <= h < 35:
            return 'Yellow'
        elif 35 <= h < 85:
            return 'Green'
        elif 85 <= h < 130:
            return 'Blue'
        elif 130 <= h < 160:
            return 'Purple'
        else:
            return 'Unknown'
    except:
        return 'Unknown'

# Process video
if uploaded_file is not None:
    tfile = tempfile.NamedTemporaryFile(delete=False)
    tfile.write(uploaded_file.read())

    cap = cv2.VideoCapture(tfile.name)

    stframe = st.empty()
    frame_count = 0

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret or frame_count > 300:  # Limit to 300 frames
            break

        results = model(frame)[0]

        for box in results.boxes:
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            cls_id = int(box.cls[0])
            label = model.names[cls_id]
            cropped = frame[y1:y2, x1:x2]

            if cropped.size == 0:
                continue

            color = get_dominant_color(cropped)
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0,255,0), 2)
            cv2.putText(frame, f"{label}, {color}", (x1, y1 - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0,255,0), 2)

        # Convert to RGB and display in Streamlit
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        stframe.image(frame_rgb, channels="RGB", use_column_width=True)

        frame_count += 1

    cap.release()
    st.success("✅ Video processing complete!")
