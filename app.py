from flask import Flask, render_template, request
from utils.predict import predict_sentiment
import pandas as pd
import os
from datetime import datetime
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import re
from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS

app = Flask(__name__)

# This file is ONLY for collected feedback (not training data)
FEEDBACK_FILE = "data/collected_feedback.csv"

# Create feedback file only once if it does not exist
if not os.path.exists(FEEDBACK_FILE):
    df_init = pd.DataFrame(columns=[
        "Timestamp",
        "Combined_Feedback",
        "Sentiment"
    ])
    df_init.to_csv(FEEDBACK_FILE, index=False)

# ---------------- HOME PAGE ------------------
@app.route("/")
def home():
    return render_template("home.html")

# ---------------- STUDENT PAGE ------------------
@app.route("/student")
def student_page():
    return render_template("student.html")

# ---------------- SUBMIT FEEDBACK ----------------
@app.route("/submit", methods=["POST"])
def submit_feedback():

    answers = [
        request.form["q1"],
        request.form["q2"],
        request.form["q3"],
        request.form["q4"],
        request.form["q5"]
    ]

    # Combine all answers into one feedback text
    combined_feedback = ". ".join(answers)

    # Predict sentiment using trained model
    sentiment = predict_sentiment(combined_feedback)

    # Append feedback (DO NOT overwrite)
    df = pd.read_csv(FEEDBACK_FILE)
    df.loc[len(df)] = [
        datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        combined_feedback,
        sentiment
    ]
    df.to_csv(FEEDBACK_FILE, index=False)

    return render_template(
        "result.html",
        feedback=combined_feedback,
        sentiment=sentiment
    )

# ---------------- ADMIN PAGE ----------------
@app.route("/admin")
def admin_dashboard():
    import re
    from wordcloud import WordCloud
    from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS

    df = pd.read_csv(FEEDBACK_FILE)

    # Handle empty feedback case
    if df.empty:
        return render_template(
            "admin.html",
            total=0,
            positive=0,
            neutral=0,
            negative=0
        )

    # ---------------- SENTIMENT COUNTS ----------------
    sentiment_counts = df["Sentiment"].value_counts()

    total = len(df)
    positive = sentiment_counts.get("Positive", 0)
    neutral = sentiment_counts.get("Neutral", 0)
    negative = sentiment_counts.get("Negative", 0)

    # ---------------- TEXT CLEANING ----------------
    def clean_text(text):
        text = text.lower()
        text = re.sub(r"[^a-z\s]", "", text)
        words = [w for w in text.split() if len(w) > 3]
        return " ".join(words)

    # ---------------- STOPWORDS ----------------
    common_stopwords = set(ENGLISH_STOP_WORDS)

    extra_stopwords = {
        "the", "was", "were", "but", "and", "to", "of",
        "very", "more", "most", "some", "many", "much",
        "not", "too", "also", "still", "overall"
    }

    domain_stopwords = {
        "workshop", "training", "session", "sessions",
        "ai", "ml", "machine", "learning",
        "algorithm", "algorithms",
        "program", "course", "classes",
        "trainer", "instructor",
        "concept", "concepts"
    }

    all_stopwords = common_stopwords.union(extra_stopwords).union(domain_stopwords)

    # ---------------- WORD CLOUD GENERATION ----------------
    for sentiment in ["Positive", "Neutral", "Negative"]:

        sentiment_text = " ".join(
            df[df["Sentiment"] == sentiment]["Combined_Feedback"]
            .astype(str)
            .apply(clean_text)
        )

        if sentiment_text.strip():
            wc = WordCloud(
                width=400,
                height=300,
                background_color="white",
                stopwords=all_stopwords,
                collocations=False
            ).generate(sentiment_text)

            wc.to_file(f"static/{sentiment.lower()}_wc.png")

    # ---------------- RENDER ADMIN PAGE ----------------
    return render_template(
        "admin.html",
        total=total,
        positive=positive,
        neutral=neutral,
        negative=negative
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
