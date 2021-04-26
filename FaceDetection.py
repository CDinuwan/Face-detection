import cv2

face_cascade = cv2.CascadeClassifier("C:\\Users\\Chanuka Dinuwan\\Desktop\\Face Detection\\haarcascade_frontalface_default.xml")
img = cv2.imread("C:\\Users\\Chanuka Dinuwan\\Desktop\\Face Detection\\img.png")

gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray_img, scaleFactor=1.05, minNeighbors=5)

for x,y,z in faces:
    img=cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)

print(type(faces))
print(faces)

cv2.imshow('Face',img)
cv2.waitKey()
