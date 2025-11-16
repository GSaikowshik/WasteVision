import streamlit as st
from streamlit_webrtc import webrtc_streamer, VideoTransformerBase, RTCConfiguration
from ultralytics import YOLO
import av
import os

# Set page title and icon
st.set_page_config(page_title="Waste Vision", page_icon="♻️")

# Use @st.cache_resource to load the model only once
@st.cache_resource
def load_yolo_model():
    """
    Loads the YOLOv8 model from the 'model/best.pt' file.
    This is cached so the model is not re-loaded on every interaction.
    """
    model_path = os.path.join('model', 'best.pt')
    if not os.path.exists(model_path):
        st.error("Model file 'model/best.pt' not found. Please make sure it's in the 'model' folder.")
        return None
    model = YOLO(model_path)
    return model

# Load the model
model = load_yolo_model()

# --- Main App Interface ---
st.title("♻️ Waste Vision")
st.write("This application uses a YOLOv8 model to detect and classify waste in real-time.")
st.write("Hold an item up to your webcam and click 'Start' to begin.")

# This class handles processing the video frames
class YOLOVideoTransformer(VideoTransformerBase):
    def recv(self, frame: av.VideoFrame) -> av.VideoFrame:
        """
        Receives a video frame, runs YOLO inference, and returns the annotated frame.
        """
        # Convert the frame to a numpy array (OpenCV format)
        img = frame.to_ndarray(format="bgr24")

        # Run YOLO inference
        # We use stream=True for efficiency, but only process one frame
        results_generator = model(img, stream=True, verbose=False) 
        
        # Get the first (and only) result and plot it
        r = next(results_generator)
        annotated_frame = r.plot() # r.plot() returns the frame with boxes/labels
        
        # Convert the (annotated) frame back to av.VideoFrame
        return av.VideoFrame.from_ndarray(annotated_frame, format="bgr24")

# --- Streamlit WEBRTC Component ---
# This starts the webcam feed and applies our YOLOVideoTransformer to each frame
if model:
    webrtc_streamer(
        key="waste-vision-demo",
        # This factory creates our video processor
        video_transformer_factory=YOLOVideoTransformer,
        # This configuration helps with deployment
        rtc_configuration=RTCConfiguration({
            "iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]
        }),
        # Constraints for the webcam
        # --- This is the line with the typo ---
        media_stream_constraints={"video": True, "audio": False},
        async_processing=True,
    )
else:
    st.warning("Model could not be loaded. Cannot start webcam stream.")