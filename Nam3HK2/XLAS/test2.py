import cv2 as cv2
import numpy as np
from matplotlib import pyplot as plt
img = cv2.imread('D:/Nam3HK2/XLAS/F95.png', 0)
threshval = 100; n = 255
retval, imB = cv2.threshold(img, threshval, n,
cv2.THRESH_BINARY)
# Taking a matrix as the kernel
kernel1 = np.ones((11,11), np.uint8)
kernel2 = np.ones((15,15), np.uint8)
kernel3 = np.ones((45,45), np.uint8)
img_dil1 = cv2.dilate(imB, kernel1, iterations=1)
img_dil2 = cv2.dilate(imB, kernel2, iterations=1)
img_dil3 = cv2.dilate(imB, kernel3, iterations=1)

plt.subplot(2,2,1),plt.axis('off')
plt.imshow(imB,cmap=plt.cm.gray)
plt.subplot(2,2,2),plt.axis('off')
plt.imshow(img_dil1,cmap=plt.cm.gray)
plt.subplot(2,2,3),plt.axis('off')
plt.imshow(img_dil2,cmap=plt.cm.gray)
plt.subplot(2,2,4),plt.axis('off')
plt.imshow(img_dil3,cmap=plt.cm.gray)