from setuptools import setup

setup(
   name='face_detector',
   version='1.0',
   description='face detection with different computer vision techniques',
   author='Vinicius Teixeira',
   author_email='viniteixeira2@hotmail.com',
   packages=['face_detector'], 
   install_requires=[
    'opencv-python>=4.5.5.62', 
    'dlib>=19.23.0'
   ], 
)