import cv2
import dlib

RTSP_IP = 'rtsp://192.168.15.2:8080/h264_ulaw.sdp'

cap = cv2.VideoCapture(RTSP_IP)
detector = dlib.get_frontal_face_detector()

while(1):
    ret, frame = cap.read()
    
    image = cv2.resize(frame, (800, 600))
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    detections = detector(gray_image, 1)

    for face in detections:
        l, t, r, b = face.left(), face.top(), face.right(), face.bottom()
        
        cv2.rectangle(image, (l, t), (r, b), (0,255,255), 2)
        
    cv2.imshow('Video', image)
    cv2.waitKey(1)