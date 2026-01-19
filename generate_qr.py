import qrcode

# Student feedback page URL
url = "http://192.168.2.150:5000/student"

qr = qrcode.make(url)
qr.save("static/feedback_qr.png")

print("QR Code generated successfully!")
