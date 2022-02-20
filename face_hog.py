import cv2
import dlib
import os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__)) 
IMAGE_PATH = os.path.join(ROOT_DIR, 'images/people2.jpg')

image = cv2.imread(IMAGE_PATH)
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
detector = dlib.get_frontal_face_detector()
detections = detector(gray_image, 1)

for face in detections:
  l, t, r, b = face.left(), face.top(), face.right(), face.bottom()
  
  cv2.rectangle(image, (l, t), (r, b), (0,255,255), 2)
  
cv2.imshow('Img', image)
cv2.waitKey(0)