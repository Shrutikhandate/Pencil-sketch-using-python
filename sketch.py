import cv2 as cv

image = cv.imread("C:\\Users\\Akash\\Desktop\\Python Coding\\image.png")
cv.imshow("Image",image )
gray_image =cv.cvtColor(image,cv.COLOR_BGR2GRAY)
inverted = 255-gray_image
blur = cv.GaussianBlur(inverted ,(21,21),0)
invertedBlur = 255-blur
sketch = cv.divide(gray_image , invertedBlur, scale= 256.0)
cv.imwrite("sketch.jpg" ,sketch)
cv.imshow("sketch",sketch)
cv.waitKey(0)
