import cv2
img1=cv2.imread("D:\\Wallpaper\\durga.jpg",1)
print(img1)
img1=cv2.resize(img1,(1280,700)) # height and width
cv2.imshow("original",img1)
cv2.waitKey()
cv2.destroyAllWindows()

import cv2
img1=cv2.imread("D:\\Wallpaper\\durga.jpg",0)
print(img1)
img1=cv2.resize(img1,(1280,700)) # height and width
cv2.imshow("original",img1)
cv2.waitKey()
cv2.destroyAllWindows()
