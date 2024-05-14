import numpy as np
import cv2

# 讀取圖像
image = cv2.imread("thumb-1920-1034708.jpg")
cv2.imshow("IMAGE", image)
cv2.imwrite("1.png", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 定義3x3的均值濾波器
mean_filter = np.array([[1/9, 1/9, 1/9],
                        [1/9, 1/9, 1/9],
                        [1/9, 1/9, 1/9]])

# 對圖像進行均值濾波
def apply_mean_filter(image):
    result = np.zeros_like(image)

    # 對圖像的每個像素進行遍歷
    for i in range(1, image.shape[0] - 1):
        for j in range(1, image.shape[1] - 1):
            # 初始化模糊後的像素值
            blurred_pixel = 0

            # 對3x3的鄰域進行遍歷，計算均值
            for k in range(-1, 2):
                for l in range(-1, 2):
                    blurred_pixel += image[i + k, j + l] * mean_filter[k + 1, l + 1]

            # 將計算得到的均值作為結果圖像的像素值
            result[i, j] = int(blurred_pixel + 0.5)  # 四捨五入取整數

    return result