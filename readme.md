# 🧠 Face Recognition System

## 📌 Project Overview

This project implements a face recognition system using deep learning and modern web technologies. The system consists of three main components:

- 🧬 A **Deep Learning model** for face recognition  
- 🔌 A **Flask backend API** for inference  
- 🎥 A **React frontend** with webcam integration  

---

## 🏗️ Technical Architecture

### 1. Deep Learning Model

- **Base Model:** [Xception](https://keras.io/api/applications/xception/) (from Keras Applications)  
- **Pre-trained Weights:** ImageNet  
- **Fine-Tuning Approach:**
  - Transfer learning from ImageNet weights  
  - Custom classification head for face recognition  
  - Fine-tuned on a personal face dataset (Because of the sensitivity of this - I Didn't add my dataset. But all the scripts that you need in order to achieve the same results have been added to the project)
  - you need to create this folder structure for your training - data/train
  - you need to create 2 folders in the above for your binary classification. The model would use alphabetical order to determine the class that is false and true.

---

### 2. Backend (Flask)

- **Framework:** Flask  
- **Key Features:**
  - RESTful API endpoints  
  - Image processing pipeline  
  - Model inference service  
  - Error handling and input validation  

---

### 3. Frontend (React + Vite)

- **Framework:** React with [Vite](https://vitejs.dev/) for fast development  
- **Key Features:**
  - Real-time webcam integration  
  - Image capture and preprocessing  
  - Communication with Flask API  
  - Interactive UI for face recognition results  

---

## 📂 Project Structure (Optional)

