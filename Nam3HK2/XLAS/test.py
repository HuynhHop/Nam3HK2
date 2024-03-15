# # import cv2
# # import numpy as np
# # import matplotlib.pyplot as plt
# # def conv(image, kernel):
# #     return cv2.filter2D(image, -1, kernel)
# # path=r'D:\Nam3HK2\XLAS\anh-gai-k5-1.jpg'
# # img=cv2.imread(path)
# # # cv2.imshow('Load Image', img)
# # k=np.ones((5,5))/25
# # r,g,b=cv2.split(img)
# # B=conv(b,k)
# # G=conv(g,k)
# # R=conv(r,k)
# # imgC=np.array(cv2.merge((R,G,B)),dtype='uint8')
# # plt.imshow(img)
# # plt.show()
# # plt.imshow(imgC)

# import cv2
# import numpy as np
# import matplotlib.pyplot as plt
# def conv(A, k):
#     # return cv2.filter2D(image, -1, kernel)
#     kh,kw=k.shape
#     h,W=A.shape
#     B=np.ones((h,W))
#     for i in range(0,h-kh+1):
#         for j in range(0,W-kw+1):
#             sA=A[i:i+kh,j:j+kw]
#             B[i,j]=np.sum(k*sA)
#     B=B[0:h-kh+1,0:W-kw+1]
#     return B

# path = r'D:\Nam3HK2\XLAS\anh-gai-k5-1.jpg'
# img = cv2.imread(path)
# k = np.ones((5, 5), np.float32) / 25
# b, g, r = cv2.split(img)
# B = conv(b, k)
# G = conv(g, k)
# R = conv(r, k)
# imgC = cv2.merge((R, G, B))
# plt.imshow(img)
# plt.show()
# plt.imshow(imgC)

import cv2
import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import convolve
from scipy.ndimage import median_filter, maximum_filter, minimum_filter

plt.rcParams.update({'font.size': 5})

# Hàm convolution cho ảnh không gian với ảnh gray hoặc ảnh màu
def Conv(img, k):
    Out = np.zeros_like(img)
    if img.ndim > 2:
        for i in range(3):
            Out[:, :, i] = convolve(img[:, :, i], k)
    else:
        Out = convolve(img, k)
    return Out

def Gausskernel(l=5, sig=1.5):
    s = round((l - 1) / 2)
    ax = np.linspace(-s, s, l)
    gauss = np.exp(-np.square(ax) / (2 * (sig**2)))
    kernel = np.outer(gauss, gauss)
    return kernel / np.sum(kernel)

def MedianFilter(img, size=3):
    if img.ndim > 2:
        return np.stack([median_filter(img[:, :, i], size=size) for i in range(3)], axis=-1)
    else:
        return median_filter(img, size=size)

def MaxFilter(img, size=3):
    if img.ndim > 2:
        return np.stack([maximum_filter(img[:, :, i], size=size) for i in range(3)], axis=-1)
    else:
        return maximum_filter(img, size=size)

def MinFilter(img, size=3):
    if img.ndim > 2:
        return np.stack([minimum_filter(img[:, :, i], size=size) for i in range(3)], axis=-1)
    else:
        return minimum_filter(img, size=size)

img = cv2.imread(r'D:\Nam3HK2\XLAS\anh-gai-k5-1.jpg', cv2.IMREAD_COLOR)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

plt.figure(figsize=(10, 8), dpi=100)

# Original image
subf = plt.subplot(2, 3, 1)
plt.imshow(img)
plt.axis('off')
subf.set_title("Original image")

# Mean filter
k = np.ones((11, 11)) / (11 * 11)
imgOutMean = Conv(img, k)
subf = plt.subplot(2, 3, 2)
plt.imshow(imgOutMean)
plt.axis('off')
subf.title.set_text('Box filter')

# Gaussian filter
gauss_kernel = Gausskernel(l=11, sig=1.5)
imgOutGauss = Conv(img, gauss_kernel)
subf = plt.subplot(2, 3, 3)
plt.imshow(imgOutGauss)
plt.axis('off')
subf.title.set_text('Gaussian filter')

# Median filter
imgOutMedian = MedianFilter(img, size=3)
subf = plt.subplot(2, 3, 4)
plt.imshow(imgOutMedian)
plt.axis('off')
subf.title.set_text('Median filter')

# Max filter
imgOutMax = MaxFilter(img, size=3)
subf = plt.subplot(2, 3, 5)
plt.imshow(imgOutMax)
plt.axis('off')
subf.title.set_text('Max filter')

# Min filter
imgOutMin = MinFilter(img, size=3)
subf = plt.subplot(2, 3, 6)
plt.imshow(imgOutMin)
plt.axis('off')
subf.title.set_text('Min filter')

plt.tight_layout()
plt.show()