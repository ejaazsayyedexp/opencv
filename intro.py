import cv2


smile_cascade = cv2.CascadeClassifier("./haarcascade_frontalface_alt2.xml")
video = cv2.VideoCapture(0,cv2.CAP_DSHOW)

a=1
while True:
    a+=1
    check,frame= video.read()
    #print(frame)
    newframe = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    #smile_cascade.detectMultiScale()
    faces = smile_cascade.detectMultiScale(newframe,1.05,5)
    for x,y,w,h in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,200),2)

    cv2.imshow("Capturing",frame)
    key = cv2.waitKey(1)
    if(key == ord('q')):
        break

print(a)
video.release()
cv2.destroyAllWindows()