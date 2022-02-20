import cv2
import dlib
import os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__)) 
IMAGE_PATH = os.path.join(ROOT_DIR, 'images/people2.jpg')
MODEL_PATH =  os.path.join(ROOT_DIR, 'weights/mmod_human_face_detector.dat')
SCALE = 1

image = cv2.imread(IMAGE_PATH)
detector = dlib.cnn_face_detection_model_v1(MODEL_PATH)
detections = detector(image, SCALE)

for face in detections:
  l, t, r, b, c = face.rect.left(), face.rect.top(), face.rect.right(), face.rect.bottom(), face.confidence

  cv2.rectangle(image, (l, t), (r, b), (255, 255, 0), 2)

cv2.imshow('Img', image)
cv2.waitKey(0)
