import cv2
import dlib
import os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__)) 
MODEL_PATH =  os.path.join(ROOT_DIR, 'weights/mmod_human_face_detector.dat')
RTSP_IP = 'rtsp://192.168.15.2:8080/h264_ulaw.sdp'
SCALE = 1

cap = cv2.VideoCapture(RTSP_IP)
detector = dlib.cnn_face_detection_model_v1(MODEL_PATH)

while(1):
    ret, frame = cap.read()
    
    image = cv2.resize(frame, (800, 600))
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    detections = detector(gray_image, SCALE)

    for face in detections:
        l, t, r, b, c = face.rect.left(), face.rect.top(), face.rect.right(), face.rect.bottom(), face.confidence

        cv2.rectangle(image, (l, t), (r, b), (255, 255, 0), 2)
  
    cv2.imshow('Video', image)
    cv2.waitKey(1)