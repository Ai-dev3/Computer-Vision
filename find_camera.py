# My webcam is broken(camera 0), so this is to test what camera number I'm using.
# 
# AUTHOR: AIDEN ZHU

import cv2
camera_working = []

for i in range(5):
    camera = cv2.VideoCapture(i)
    success, frame = camera.read()

    if success:
        camera_working.append(i)

    camera.release()

print(f"working cameras:  {camera_working}")
        