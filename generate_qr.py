import qrcode
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_DIR = os.path.join(BASE_DIR, "static")

os.makedirs(STATIC_DIR, exist_ok=True)

url = "https://student-feedback-analysis.onrender.com/student"

qr = qrcode.make(url)
qr.save(os.path.join(STATIC_DIR, "feedback_qr.png"))

print("QR Code generated successfully!")
