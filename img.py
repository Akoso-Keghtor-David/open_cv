import cv2

face_hear_cascade = cv2.CascadeClassifier('hearcascade_frontalface_')
image - cv2.imread('demo.jpg')
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

faces = cface_hear_cascade.detcteMultiScale(gray, 1,1,4)
for(x,y,w,h) in faces:
    cv2.rectangle(image,(x,y), (x+w, y+h), (0, 255, 0), 5)

cv2.im