#main
import cv2

import mediapipe as mp
import time
mpDraw=mp.solutions.drawing_utils


# now we creating the model
mp_pose= mp.solutions.pose
pose=mp_pose.Pose()
# true it keep on detect
# false .5 confidence detect and go to traking



# open cv is the library we use it for image processing
#mediapipe is frame work to do pose setimation

cap= cv2.VideoCapture(0)

previ_t=0

while True:
    success, img = cap.read()
    # our image in BGR
    #converting colours
    img_RGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

    result= pose.process(img_RGB)

    if result.pose_landmarks:
        mpDraw.draw_landmarks(img,result.pose_landmarks,mp_pose.POSE_CONNECTIONS)
        # here we created dots using the model and join by line

        #no we need to see the point of the positions
        # so we need to identify those pointd


# below code for the position circle------------------------
        for id, lm in enumerate(result.pose_landmarks.landmark):
            h,w,c = img.shape
            # c = channel
            print (id, lm)

            cx,cy= int(lm.x*w ), int(lm.y * h)
            # printing circle
            cv2.circle(img,(cx,cy),5,(0,255,0),cv2.FILLED)
            print()
   # ----------------------------------------------------------


    ct= time.time()
    fps = 1/(ct-previ_t)
    previ_t = ct


    cv2.putText(img,str(int(fps)),(70,80),cv2.FONT_HERSHEY_PLAIN,5,(0 ,255,0),10) # 70,50 ==orgin
    cv2.imshow("video", img)
    key=cv2.waitKey(1)
    if key==32:
        break

