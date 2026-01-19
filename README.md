🎓 Student Feedback Sentiment Analysis
AI & ML Workshop Feedback System

A Flask-based web application that collects and analyzes student feedback using Natural Language Processing (NLP) and Machine Learning.
The system automatically classifies feedback into Positive, Neutral, or Negative sentiment and presents insights through an admin dashboard with statistics and word clouds.

📌 Built for academic workshops, demos, and learning-focused deployments.

🌐 Live Demo

🏠 Home: https://student-feedback-analysis.onrender.com

📝 Give Feedback: https://student-feedback-analysis.onrender.com/student

📊 Admin Dashboard: https://student-feedback-analysis.onrender.com/admin

✨ Features
👨‍🎓 Student Module

Simple feedback form (mobile-friendly)

QR code access for instant submission

Natural language feedback input

Real-time sentiment prediction

🧑‍💼 Admin Module

Total feedback count

Positive / Neutral / Negative breakdown

Automatically generated word clouds

Clean and responsive dashboard UI

⚙️ System Highlights

Flask backend with clean routing

Pre-trained ML sentiment model

CSV-based storage (demo-friendly)

Render deployment ready

Fully responsive (desktop & mobile)

🛠️ Tech Stack
Layer	Technology
Backend	Flask (Python)
ML / NLP	scikit-learn
Data Handling	Pandas
Visualization	WordCloud, Matplotlib
Frontend	HTML, CSS
QR Code	qrcode, Pillow
Deployment	Render
📁 Project Structure
sentiment-feedback-app/
│
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

🚀 Getting Started (Local Setup)
1️⃣ Clone the Repository
git clone https://github.com/your-username/student-feedback-analysis.git
cd student-feedback-analysis

2️⃣ Create Virtual Environment
python -m venv venv

3️⃣ Activate Environment

Windows

venv\Scripts\activate


macOS / Linux

source venv/bin/activate

4️⃣ Install Dependencies
pip install -r requirements.txt

5️⃣ Run the App
python app.py


Open in browser:

http://127.0.0.1:5000

📦 Dependencies
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

🧠 How It Works

Students submit textual feedback

Feedback is preprocessed and vectorized

ML model predicts sentiment

Feedback is stored in CSV

Admin dashboard:

Computes sentiment statistics

Generates word clouds

Displays insights visually

⚠️ Notes & Limitations

Render uses an ephemeral filesystem

CSV data may reset on redeploy

Best suited for:

Academic projects

Workshops

Demonstrations

🔐 For production use, replace CSV with PostgreSQL.

☁️ Deployment (Render)

Build Command

pip install -r requirements.txt


Start Command

gunicorn app:app

🔮 Future Enhancements

Admin authentication

PostgreSQL database integration

Interactive analytics charts

Feedback export (PDF / Excel)

Workshop-wise feedback separation

Dark mode UI

👨‍💻 Author

Sai
AI & ML Workshop | Software Developer

Built for educational and academic purposes.

📜 License

This project is licensed for educational use.
You are free to fork, modify, and extend it for learning and academic demonstrations.
