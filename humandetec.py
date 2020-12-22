import sys
import os 
try:
    import cv2
    import imutils
except Exception:
    os.system('pip install cv2 & pip install imutils')
    os.system('humandetec.py')
hg = cv2.HOGDescriptor()
hg.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())


img = sys.argv[1] #cv2.VideoCapture(0)

cv = cv2.imread(img)
#out = cv2.VideoWriter('output.avi', cv2.VideoWriter_fourcc(*'MJPG'), 15.,(640,480))

cv = imutils.resize(cv,width=min(400, cv.shape[1]))
regi, _ = hg.detectMultiScale(cv, winStride=(4, 4), padding=(4, 4), scale=1.05)
for (x,y,w,h) in regi:
    cv2.rectangle(cv, (x, y),(x + w, y + h), (0,0,255), 2)

cv2.imshow("Тело блять", cv)
cv2.waitKey(0)
cv2.destroyAllWindows()
