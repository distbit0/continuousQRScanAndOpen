import cv2
from pyzbar.pyzbar import decode
import subprocess
import time
from urllib.parse import urlparse

# Specify the Brave browser and Xed paths according to your system
brave_path = '/usr/bin/brave-browser-stable'
xed_path = '/usr/bin/xed'

def is_url(s):
    try:
        result = urlparse(s)
        return all([result.scheme, result.netloc])
    except ValueError:
        return False

def open_in_brave(url):
    subprocess.run([brave_path, url])

def open_in_xed(text):
    with open('/tmp/qr_code.txt', 'w') as f:
        f.write(text)
    subprocess.run([xed_path, '/tmp/qr_code.txt'])

# Initialize the webcam
cap = cv2.VideoCapture(0)
cap.set(3, 640)  # Width
cap.set(4, 480)  # Height

# List to store visited codes
visited_codes = []

while True:
    success, frame = cap.read()
    for barcode in decode(frame):
        data = barcode.data.decode('utf-8')
        if data not in visited_codes:
            visited_codes.append(data)
            print(f'Opening: {data}')
            if is_url(data):
                open_in_brave(data)
            else:
                open_in_xed(data)

