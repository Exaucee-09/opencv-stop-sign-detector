# 🛑 Stop Sign Detection and UART Integration Project

## 📌 Overview

This project implements a real-time stop sign detection system using a webcam and OpenCV in Python, designed to integrate with a microcontroller (Arduino) via UART for robotic control. The system detects stop signs in a live video feed, draws green bounding boxes around them, displays detection status, and captures snapshots when a stop sign is confirmed. When a stop sign is detected, the system is designed to send a `1` over UART for 3 seconds to stop the robot, then resume sending `0` to move forward. This submission includes the Python script, an optional Arduino sketch, and supporting files.

---

## 📁 Project Structure

- `detect.py`: Python script for stop sign detection using OpenCV. It processes webcam video, detects stop signs with a Haar cascade classifier, draws green bounding boxes, displays `"Stop Sign Detected"` or `"No Stop Sign"` on the feed, and saves snapshots when a stop sign is confirmed. Serial communication is disabled in this version for testing without Arduino hardware.

- `sketch.ino`: Optional Arduino sketch to control a robot with two DC motors via an H-bridge (e.g., L298N). It reads serial commands (`1` to stop, `0` to move) at 9600 baud and controls motor pins accordingly.

- `stop_sign_cascade.xml`: Haar cascade classifier file for stop sign detection. Sourced from [insert source, e.g., "a GitHub repository at https://github.com/example/stop-sign-cascade" or "trained using a custom dataset"].

- Snapshots (e.g., `stop_sign_20250620_112804.jpg`): Example images captured when stop signs are detected, included to demonstrate functionality.

---

## ⚙️ Requirements

### Software
- Python 3.x
- Python Libraries:
  - `opencv-python`: `pip install opencv-python`
  - `numpy`: `pip install numpy`
- Arduino IDE (optional, for testing `sketch.ino`)
- OpenCV-compatible webcam

### Hardware (Optional for UART Integration)
- Arduino board (e.g., Uno) with USB cable
- 2x DC motors + H-bridge motor driver (e.g., L298N)
- Wiring:
  - Motor A: Pins 7, 8, 9
  - Motor B: Pins 10, 11, 12

---

## 🛠️ Setup Instructions

### 🔍 Python Script: `detect.py`

1. Place `detect.py` and `stop_sign_cascade.xml` in the same directory.
2. Install dependencies:
   ```bash
   pip install opencv-python numpy
   ```
3. Connect your webcam and make sure it's detected by your system.
4. Run the script:
   ```bash
   python detect.py
   ```
5. Point your webcam at a printed or digital stop sign image.
6. Press `q` to quit the video stream.

#### Output
- Real-time video stream with:
  - Green bounding boxes around detected stop signs.
  - Status text:  
    - `"Stop Sign Detected"` (green)  
    - `"No Stop Sign"` (red)
- After **3 consecutive detections**, the text changes to:
  - `"Stop Sign Confirmed"` and a snapshot is saved.
- Snapshots saved in the format: `stop_sign_YYYYMMDD_HHMMSS.jpg`

---

### 🤖 Arduino Sketch (Optional): `sketch.ino`

1. Open `sketch.ino` in the Arduino IDE.
2. Connect the Arduino to your computer via USB.
3. Check and adjust motor wiring:
   - Motor A: Pins 7, 8, 9
   - Motor B: Pins 10, 11, 12
4. Upload the sketch to your Arduino board.
5. The Arduino listens for serial input:
   - `1` to stop motors
   - `0` to move forward

> ⚠️ Note: The Arduino code was not tested in this version due to unavailable hardware, but follows standard H-bridge and UART practices.

---

## 🧠 Haar Cascade

The `stop_sign_cascade.xml` file is sourced from [insert source or note if trained].

---

## 🧪 Testing Notes

### Detection
- The Python script uses stricter detection parameters (`scaleFactor=1.2`, `minNeighbors=8`) and requires 3 consecutive detections to confirm a stop sign, reducing false positives (e.g., garbage).
- Tested with a webcam in good lighting, using printed or on-screen stop sign images.
- False positives were minimized by adjusting detection thresholds.

### Snapshots
- Snapshots are taken only when a stop sign is confirmed, with unique filenames based on timestamps.
- Example snapshots are included to show successful detections.

### Serial Communication
- The provided Python script disables serial communication for testing without Arduino hardware.
- A version with serial communication (using `pyserial`) is available if hardware is acquired, sending `1` for 3 seconds on detection, then `0`.

### Arduino
- The sketch assumes a standard H-bridge setup with PWM speed control (`200/255`).
- Not tested due to unavailable hardware but follows standard motor control practices.

---

## ⚠️ Known Limitations

- Detection accuracy depends on the quality of `stop_sign_cascade.xml`. False positives may occur with a poorly trained cascade.
- Testing was limited to webcam input without Arduino hardware.
- Lighting and background clutter can affect detection; good lighting is recommended.

---

## 🚀 Future Improvements

- Train a custom Haar cascade with a larger dataset for better accuracy.
- Test with Arduino hardware to verify UART integration.
- Add real-time confidence scores for detections to further filter false positives.

---

## 📧 Contact

For questions or clarifications, please contact: **iturushimbabazipeace@gmail.com**
