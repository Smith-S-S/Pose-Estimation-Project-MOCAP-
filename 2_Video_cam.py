import cv2 
import numpy as np
# check once again..
cam_0 = cv2.VideoCapture(0)
cam_1 = cv2.VideoCapture(1)

while True:
    success_0, frame_0 = cam_0.read()
    success_1, frame_1 = cam_1.read()

    cv2.imshow("sm", frame_0)
    cv2.imshow("sm1", frame_1)

    key= cv2.waitKey(1)
    if key == 32:
        break





"""cam_0.release()
cam_1.release()
cv2.destroyAllWindows()"""
