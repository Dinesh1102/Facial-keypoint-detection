# Facial-keypoint-detection


This project performs facial keypoint detection using a deep learning model. It uses a dataset from a Kaggle competition and provides both training and inference workflows.

---

## 🚀 Getting Started

### 1. Join the Kaggle Competition

- Go to the [Kaggle Facial Keypoint Detection competition](https://www.kaggle.com/competitions/facial-keypoints-detection) and **Join** the competition.

### 2. Download `kaggle.json`

- Navigate to your Kaggle [Account Settings](https://www.kaggle.com/account).
- Scroll down to the **API** section and click **Create New API Token**.
- This will download a file named `kaggle.json`.

---

## 🧪 Training (Using Google Colab)

1. Open the provided `.ipynb` notebook in **Google Colab**.
2. Upload your `kaggle.json` file in the notebook session.
3. Run all cells to train the model.

---

## 🔍 Inference (Local Setup)

### Step 1: Clone the Repository
`git clone https://github.com/Dinesh1102/Facial-keypoint-detection.git`
`cd Facial-keypoint-detection`

### Step 2: Create a conda environment
`conda create -n facial-keypoints python=3.11`
`conda activate facial-keypoints`

### Step 3: Install the requirements
`pip install -r requirements.txt`

### Step 4: Run interference
`python main.py`
