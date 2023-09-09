# working with Color images
import cv2
img1=cv2.imread("D:\\Wallpaper\\durga.jpg",1)
print(img1)
img1=cv2.resize(img1,(1280,700)) # height and width
cv2.imshow("original",img1)
cv2.waitKey(4000)
cv2.destroyAllWindows()

# working with grayScale
import cv2
img2=cv2.imread("D:\\Wallpaper\\durga.jpg",0)
print(img2)
img2=cv2.resize(img2,(1280,700)) # height and width
cv2.imshow("Grayscale image",img2)
cv2.waitKey(4000)
cv2.destroyAllWindows()

#working with Unchanged (High saturation value)
import cv2
img3=cv2.imread("D:\\Wallpaper\\durga.jpg",-1)
print(img3)
img3=cv2.resize(img3,(1280,700)) # height and width
cv2.imshow("Grayscale image",img3)
cv2.waitKey(4000)
cv2.destroyAllWindows()

