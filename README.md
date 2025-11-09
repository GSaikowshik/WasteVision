# Waste Vision: A Smart Waste Classification System
### Week 1: 30% Completion (The "Brain")
* [x] Set up GitHub repository.
* [x] Finalize dataset and project proposal.
* [x] Trained the core YOLOv8 model on the Kaggle dataset (see `notebooks/`).
* [x] Saved the trained model (`model/best.pt`) and validation results.

#### Training Results
* **Model:** YOLOv8-Nano
* **Epochs:** 75
* **mAP50-95:** 0.528 (from `results.png`)

![Training Results](images/results.png)
![Confusion Matrix](images/confusion_matrix.png)

### Week 2: 60% Completion (The "Eyes")
* [x] Created a local Python virtual environment.
* [x] Wrote `webcam_demo.py` to run the model on a live webcam using OpenCV.
* [x] Successfully tested the model in real-time.

#### Demo Video
*(You can upload your video file (e.g., `demo.mp4`) to a new `demo/` folder in your GitHub repo and link it here, or just have it ready to show.)*

#### How to Run the Demo
1.  Clone this repository.
2.  Create a virtual environment: `python -m venv venv`
3.  Activate it: `.\venv\Scripts\activate` (Windows) or `source venv/bin/activate` (Mac/Linux)
4.  Install requirements: `pip install -r requirements.txt`
5.  Run the demo: `python webcam_demo.py`