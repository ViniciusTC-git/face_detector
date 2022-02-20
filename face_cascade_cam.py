import cv2
import os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__)) 
CASCADE_PATH = os.path.join(ROOT_DIR, 'cascade/haarcascade_frontalface_default.xml')
RTSP_IP = 'rtsp://192.168.15.2:8080/h264_ulaw.sdp'

cap = cv2.VideoCapture(RTSP_IP)
detector = cv2.CascadeClassifier(CASCADE_PATH)

while(1):
    ret, frame = cap.read()
    
    image = cv2.resize(frame, (800, 600))
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    detections = detector.detectMultiScale(gray_image)
    
    for (x, y, w, h) in detections:
        cv2.rectangle(image, (x, y), (x + w, y + h), (0,255,0), 2)
  
    cv2.imshow('Video', image)
    cv2.waitKey(1)