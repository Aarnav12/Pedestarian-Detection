import cv2

img = cv2.imread('C:/Users/sapsl/Downloads/Whitehat jr Python/C106/Images/Father.jpg')

img = cv2.resize(img,(500,1000))

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

faceCascade = cv2.CascadeClassifier('C:/Users/sapsl/AppData/Local/Programs/Python/Python310/Lib/site-packages/cv2/data/haarcascade_frontalface_default.xml')

face = faceCascade.detectMultiScale(gray)

print(face)

for (x,y,w,h) in face:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)

cv2.imshow('Father',img)
cv2.waitKey(0)