import cv2
import time
import numpy as np
from datetime import datetime

# Load the Haar cascade classifier for stop sign detection
cascade_path = "stop_sign_cascade.xml"
stop_cascade = cv2.CascadeClassifier(cascade_path)

if stop_cascade.empty():
    print("Error: Could not load cascade classifier")
    exit(1)

# Initialize webcam
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Error: Could not open webcam")
    exit(1)

# Variables for stop sign detection timing
stop_detected = False
stop_time = 0
STOP_DURATION = 3  # Duration to simulate stop signal (in seconds)
snapshot_taken = False  # Flag to ensure snapshot is taken only once per detection
detection_count = 0  # Counter for consecutive detections
DETECTION_THRESHOLD = 3  # Number of consecutive frames to confirm detection

try:
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: Failed to capture frame")
            break

        # Convert frame to grayscale for detection
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Detect stop signs with stricter parameters
        stop_signs = stop_cascade.detectMultiScale(
            gray,
            scaleFactor=1.2,  # Increased to reduce false positives
            minNeighbors=8,   # Increased for stricter detection
            minSize=(50, 50),
            flags=cv2.CASCADE_SCALE_IMAGE
        )

        # Draw green rectangles and text around detected stop signs
        for (x, y, w, h) in stop_signs:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 3)  # Thicker green box
            cv2.putText(frame, 'Stop Sign', (x, y-10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

        # Check if stop sign is detected
        current_time = time.time()
        if len(stop_signs) > 0:
            detection_count += 1  # Increment detection counter
            if detection_count >= DETECTION_THRESHOLD and not stop_detected:
                stop_detected = True
                stop_time = current_time
                print("Stop sign confirmed, would send 1")
                # Take snapshot when stop sign is confirmed
                if not snapshot_taken:
                    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                    snapshot_filename = f"stop_sign_{timestamp}.jpg"
                    cv2.imwrite(snapshot_filename, frame)
                    print(f"Snapshot saved as {snapshot_filename}")
                    snapshot_taken = True
                # Display confirmation text
                cv2.putText(frame, 'Stop Sign Confirmed', (10, 60),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            # Display detection status
            cv2.putText(frame, 'Stop Sign Detected', (10, 30),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        else:
            detection_count = 0  # Reset counter if no detection
            # If stop sign was previously detected, check if 3 seconds have passed
            if stop_detected and (current_time - stop_time) >= STOP_DURATION:
                stop_detected = False
                snapshot_taken = False  # Reset snapshot flag
                print("Resuming, would send 0")
            elif not stop_detected:
                print("No stop sign, would send 0")
            # Display no detection status
            cv2.putText(frame, 'No Stop Sign', (10, 30),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

        # Display the frame
        cv2.imshow('Stop Sign Detection', frame)

        # Break loop on 'q' key press
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

except KeyboardInterrupt:
    print("Program terminated by user")
except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Cleanup
    cap.release()
    cv2.destroyAllWindows()
    print("Resources released, program ended")