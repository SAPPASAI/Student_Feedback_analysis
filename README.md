# 🎓 Student Feedback Sentiment Analysis

## AI & ML Workshop Feedback System

A **Flask-based web application** that collects and analyzes student feedback using  
**Natural Language Processing (NLP)** and **Machine Learning**.

The system automatically classifies feedback into **Positive**, **Neutral**, or **Negative**
sentiment and presents insights through an **admin dashboard** with statistics and word clouds.

> 📌 Built for academic workshops, demos, and learning-focused deployments.

---

## 🌐 Live Demo

- 🏠 **Home**  
  https://student-feedback-analysis.onrender.com

- 📝 **Give Feedback**  
  https://student-feedback-analysis.onrender.com/student

- 📊 **Admin Dashboard**  
  https://student-feedback-analysis.onrender.com/admin

---

## ✨ Features

### 👨‍🎓 Student Module
- Simple feedback form (mobile-friendly)
- QR code access for instant submission
- Natural language feedback input
- Real-time sentiment prediction

### 🧑‍💼 Admin Module
- Total feedback count
- Positive / Neutral / Negative sentiment breakdown
- Automatically generated word clouds
- Clean and responsive dashboard

### ⚙️ System Highlights
- Flask backend with clean routing
- Pre-trained Machine Learning model
- CSV-based storage (demo-friendly)
- Render-ready deployment
- Fully responsive UI

---

## 🛠️ Tech Stack

| Layer | Technology |
|------|------------|
| Backend | Flask (Python) |
| ML / NLP | scikit-learn |
| Data Handling | Pandas |
| Visualization | WordCloud, Matplotlib |
| Frontend | HTML, CSS |
| QR Code | qrcode, Pillow |
| Deployment | Render |

---

## 📁 Project Structure

```text
sentiment-feedback-app/
├── app.py
├── requirements.txt
├── Procfile
├── README.md
│
├── data/
│   └── collected_feedback.csv
│
├── model/
│   ├── sentiment_model.pkl
│   └── vectorizer.pkl
│
├── utils/
│   └── predict.py
│
├── static/
│   ├── style.css
│   ├── feedback_qr.png
│   ├── positive_wc.png
│   ├── neutral_wc.png
│   └── negative_wc.png
│
└── templates/
    ├── home.html
    ├── student.html
    ├── result.html
    └── admin.html

## 🚀 Getting Started (Local Setup)

Follow the steps below to run the project locally.

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/your-username/student-feedback-analysis.git
cd student-feedback-analysis
### 2️⃣ Create a Virtual Environment
bash
Copy code
python -m venv venv
### 3️⃣ Activate the Virtual Environment
Windows

bash
Copy code
venv\Scripts\activate
macOS / Linux

bash
Copy code
source venv/bin/activate
### 4️⃣ Install Dependencies
bash
Copy code
pip install -r requirements.txt
### 5️⃣ Run the Application
bash
Copy code
python app.py
Open your browser and visit:

cpp
Copy code
http://127.0.0.1:5000
### 📦 Dependencies
Flask

gunicorn

pandas

numpy

scikit-learn

joblib

matplotlib

wordcloud

qrcode

pillow

### 🧠 How It Works
Students submit textual feedback

Feedback is vectorized using a trained ML pipeline

Sentiment is predicted (Positive / Neutral / Negative)

Feedback is stored in a CSV file

Admin dashboard displays statistics and word clouds

### ⚠️ Notes & Limitations
Render uses an ephemeral filesystem

CSV data may reset on redeployment

Best suited for:

Academic projects

Workshops

Demonstrations

For production use, replace CSV storage with PostgreSQL.

### ☁️ Deployment (Render)
Build Command
bash
Copy code
pip install -r requirements.txt
Start Command
bash
Copy code
gunicorn app:app


### 📜 License
This project is licensed for educational use.
You are free to modify and extend it for learning and academic demonstrations.
