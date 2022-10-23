import cv2

vid = cv2.VideoCapture('C:/Users/sapsl/Downloads/Whitehat jr Python/C106/Video/walking.avi')
faceCascade = cv2.CascadeClassifier('C:/Users/sapsl/AppData/Local/Programs/Python/Python310/Lib/site-packages/cv2/data/haarcascade_fullbody.xml')
# img = cv2.resize(img,(500,500))
while True:
    ret,frame=vid.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    

    face = faceCascade.detectMultiScale(gray,1.2,3)

    print(face)

    for (x,y,w,h) in face:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)

    cv2.imshow('Pedestrian',frame)
    cv2.waitKey(100)