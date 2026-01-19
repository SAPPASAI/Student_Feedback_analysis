import os
import joblib

# ---------- PATH SETUP ----------
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL_DIR = os.path.join(BASE_DIR, "model")

MODEL_PATH = os.path.join(MODEL_DIR, "sentiment_model.pkl")
VECTORIZER_PATH = os.path.join(MODEL_DIR, "vectorizer.pkl")

# ---------- LOAD MODEL ----------
model = joblib.load(MODEL_PATH)
vectorizer = joblib.load(VECTORIZER_PATH)

# ---------- PREDICTION ----------
def predict_sentiment(feedback: str):
    """
    Predict sentiment for a given feedback string
    """
    feedback = feedback.lower()
    vec = vectorizer.transform([feedback])
    prediction = model.predict(vec)[0]
    return prediction
