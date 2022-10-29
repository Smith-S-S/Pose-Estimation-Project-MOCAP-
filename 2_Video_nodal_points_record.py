import cv2
from cvzone.PoseModule import PoseDetector

model= PoseDetector()
model2= PoseDetector()



cam= cv2.VideoCapture("video/video1.mp4")
cam2= cv2.VideoCapture("video/video2.mp4")
position_list=[]
position_list2=[]

while True:
    success,img= cam.read()
    success2, img2 = cam2.read()
    img=model.findPose(img)
    img2 = model2.findPose(img2)
    lm_list, bbox_info= model.findPosition(img)
    lm_list2, bbox_info2 = model2.findPosition(img2)

    if bbox_info:
        lm_string= ""
        lm_string2 = ""
        for i in lm_list: # this i cantain the x,y,z values
            lm_string +=f'{i[1]},{img.shape[0]-i[2]},{i[3]},'
            "i[1] = 1st value x" \
            "for the y value opencv uses the top left value" \
            "but unity use bottom left" \
            "img.shape[0]==height of the frame" \
            "hight - y"
        position_list.append(lm_string)
        position_list.append((lm_string2))
    print(len(position_list))

    if bbox_info2:
        for i in lm_list2: # this i cantain the x,y,z values
            lm_string2 +=f'{i[1]},{img.shape[0]-i[2]},{i[3]},'
            position_list2.append((lm_string2))
        print(len(position_list2))



    cv2.imshow("smith",img)
    cv2.imshow("smiths", img2)

    key= cv2.waitKey(1)
    """if key == 32:
        break"""
    if key == ord("s"):
        with open("Animation1.txt","w") as f:
            f.writelines(["%s\n" % i for i in position_list])
        with open("Animation1.txt","w") as f:
            f.writelines(["%s\n" % i for i in position_list2])



