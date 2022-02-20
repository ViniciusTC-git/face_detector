import cv2
import os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__)) 
CASCADE_PATH = os.path.join(ROOT_DIR, 'cascade/haarcascade_frontalface_default.xml')
IMAGE_PATH = os.path.join(ROOT_DIR, 'images/people2.jpg')

image = cv2.imread(IMAGE_PATH)
image = cv2.resize(image, (800, 600))
detector = cv2.CascadeClassifier(CASCADE_PATH)
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
detections = detector.detectMultiScale(
  gray_image, 
  scaleFactor=1.1, 
  minNeighbors=1
)

for (x, y, w, h) in detections:
  cv2.rectangle(image, (x, y), (x + w, y + h), (0,255,0), 2)
  
cv2.imshow('Img', image)
cv2.waitKey(0)