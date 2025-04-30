
import streamlit as st
import cv2
import numpy as np
import tempfile
import os
from pathlib import Path
from death_reason_screen_with_sensitivity import death_reason_screen
from multi_death_timeline import multi_death_timeline

def extract_key_frames(video_path, output_folder, frame_interval=30):
    os.makedirs(output_folder, exist_ok=True)
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        return "Error: Cannot open video file."
    frame_count = 0
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        if frame_count % frame_interval == 0:
            cv2.imwrite(os.path.join(output_folder, f"frame_{frame_count}.jpg"), frame)
        frame_count += 1
    cap.release()

def classify_scope_type(frame_path):
    frame = cv2.imread(frame_path)
    if frame is None:
        return "Error"
    height, width, _ = frame.shape
    hud_region = frame[height//3:2*height//3, width//3:2*width//3]
    gray = cv2.cvtColor(hud_region, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 50, 150)
    circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, dp=1.2, minDist=30,
                                param1=50, param2=30, minRadius=10, maxRadius=60)
    if circles is not None:
        return "Red Dot"
    lines = cv2.HoughLinesP(edges, 1, np.pi/180, threshold=50, minLineLength=20, maxLineGap=5)
    if lines is not None and len(lines) > 5:
        return "3x Scope"
    return "No Scope / Unknown"

def detect_game_mode_and_perspective(video_path, sample_frame_interval=30):
    cap = cv2.VideoCapture(video_path)
    frame_count = 0
    tdm_hud_match = 0
    fpp_match = 0
    tpp_match = 0
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret or frame_count > 300:
            break
        if frame_count % sample_frame_interval == 0:
            height, width = frame.shape[:2]
            top_bar = frame[:int(height * 0.1), int(width * 0.2):int(width * 0.8)]
            avg_color = np.mean(top_bar, axis=(0, 1))
            if avg_color[2] > 120 and avg_color[0] > 120:
                tdm_hud_match += 1
            center_area = frame[int(height * 0.4):int(height * 0.6), int(width * 0.45):int(width * 0.55)]
            edge_area = frame[int(height * 0.4):int(height * 0.6), int(width * 0.2):int(width * 0.35)]
            if np.std(edge_area) < np.std(center_area):
                fpp_match += 1
            else:
                tpp_match += 1
        frame_count += 1
    cap.release()
    game_mode = "TDM" if tdm_hud_match >= 1 else "Classic or Arena"
    perspective = "FPP" if fpp_match > tpp_match else "TPP"
    return game_mode, perspective

def main():
    st.title("🎮 AimPro AI by Sharan")
    st.subheader("Upload your BGMI clip for full AI coaching breakdown")

    uploaded_file = st.file_uploader("📤 Upload Gameplay Clip (.mp4 or .mov)", type=["mp4", "mov"])

    if uploaded_file is not None:
        with tempfile.NamedTemporaryFile(delete=False, suffix='.mp4') as tmp_file:
            tmp_file.write(uploaded_file.read())
            temp_video_path = tmp_file.name

        st.success("✅ Video uploaded successfully!")

        game_mode, perspective = detect_game_mode_and_perspective(temp_video_path)
        st.info(f"🗺️ Game Mode Detected: **{game_mode}**")
        st.info(f"👁️ Perspective: **{perspective}**")

        frames_folder = tempfile.mkdtemp()
        extract_key_frames(temp_video_path, frames_folder)
        first_frame_path = os.path.join(frames_folder, "frame_0.jpg")
        if os.path.exists(first_frame_path):
            scope_result = classify_scope_type(first_frame_path)
            st.info(f"🔍 Scope Detected: **{scope_result}**")

        # Show full death reason
        death_reason_screen()

        # Show multi-death breakdown timeline
        multi_death_timeline()

if __name__ == "__main__":
    main()
