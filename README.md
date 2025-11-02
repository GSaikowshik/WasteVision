# Waste Vision: A Smart Waste Classification System

**Internship Project for Edunet Foundation**
**By: Gandikota Sai Kowshik**

## Project Description

Waste Vision is an intelligent, real-time waste classification system. It uses a state-of-the-art Convolutional Neural Network (YOLOv8) to detect and classify items from a live webcam feed. The final goal is to create a physical "smart bin" prototype using a Raspberry Pi that can automatically identify and sort waste to improve recycling accuracy.

## 1. Problem Statement

The goal of this project is to combat the problem of improper waste sorting, which leads to recyclable materials ending up in landfills. We will build a "smart bin" that uses a camera and a CNN to automatically identify different types of waste, helping to automate and improve recycling efficiency.

## 2. Methodology

This project will use a real-time object detection model (YOLOv8) trained on a public dataset. The final system will run on a Raspberry Pi, which will use the model's output to identify waste and provide real-time feedback.

## 3. Dataset

* **Dataset:** [Garbage Detection – 6 Waste Categories](https://www.kaggle.com/datasets/viswaprakash1990/garbage-detection)
* **Classes to be Detected:**
    * BIODEGRADABLE
    * CARDBOARD
    * GLASS
    * METAL
    * PAPER
    * PLASTIC

## 4. Weekly Progress

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
