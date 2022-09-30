import cv2 as cv

img = cv.imread('images/untitled.png')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

height, width, _ = img.shape
print('size:', height, width)

cutted_image = img[height//2:height, 0:width]

cv.imshow('Cropped', cutted_image)
cv.waitKey(0)