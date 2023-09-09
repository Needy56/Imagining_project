#Taking an imagePath and converting and saving it into grayscale.
import cv2
path=input("Enter the path of image you want to convert into grayscale\n") 
print("Your Entered path is ==",path)

# reading the image stored on the inputed path
img1=cv2.imread(path,1)
cv2.imshow("the Inputed image original one is",img1)
#converting original image into GrayScale
img2=cv2.imread(path,0)
cv2.imshow("the Inputed image original one is",img2)
print("To save the converted image press s")
# saving the images

k=cv2.waitKey(0)
if k==ord("s"):
    cv2.imwrite("D:\Wallpaper\outputnew.png",img2)
else:
    cv2.destroyAllWindows()