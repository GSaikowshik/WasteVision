import cv2
from ultralytics import YOLO
import os

# --- SETTINGS ---
# Path to your trained model file (from Week 1)
MODEL_PATH = os.path.join('model', 'best.pt')

# Webcam index (0 is usually the built-in webcam)
WEBCAM_INDEX = 0 
# ------------------

print("Loading Waste Vision model...")

# Load your custom-trained YOLOv8 model
try:
    model = YOLO(MODEL_PATH)
except Exception as e:
    print(f"Error loading model from {MODEL_PATH}")
    print(f"Error: {e}")
    print("\nMake sure your 'best.pt' file is in a folder named 'model' inside your 'Waste-Vision' directory.")
    exit()

print("Model loaded successfully.")
print("Opening webcam...")

# Open the webcam
cap = cv2.VideoCapture(WEBCAM_INDEX)
if not cap.isOpened():
    print(f"Error: Could not open webcam at index {WEBCAM_INDEX}.")
    print("Try changing WEBCAM_INDEX to 1 if 0 doesn't work.")
    exit()

print("Webcam opened. Press 'q' to quit.")
print("-" * 30)

# Loop through the webcam frames
while True:
    # Read one frame from the webcam
    success, frame = cap.read()

    if success:
        # Run YOLOv8 inference on the frame
        # stream=True makes it more efficient for video
        results = model(frame, stream=True)

        # Loop through the detection results
        for r in results:
            # r.plot() draws all the boxes and labels on the frame
            annotated_frame = r.plot()

            # Display the annotated frame in a window
            cv2.imshow("Waste Vision Demo - Press 'q' to Quit", annotated_frame)

        # Check if the 'q' key is pressed to quit
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    else:
        # Break the loop if there's an error reading the frame
        break

# Release the webcam and close all windows
cap.release()
cv2.destroyAllWindows()
print("Demo finished.")