import cv2
image=cv2.imread('lena.jpg',1)
cv2.imshow('image',image)
cv2.waitKey(10000)
cv2.imwrite('lena.png',image)
cv2.destroyWindow()