import numpy as np
import cv2
# Load a color image in grayscale
img = cv2.imread('OpenCV\download (1).jpeg',1)
# cv2.imshow('image',img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

resize=cv2.resize(img,(300,399))
# cv2.imwrite('new.jpeg',resize)
cv2.imshow('Resize:',resize)
