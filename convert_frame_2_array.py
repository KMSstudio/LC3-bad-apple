import numpy as np
import cv2
import os
import time
import pickle

arr = []
for num in range(0, 6571, 3):
    res=""
    image = np.array(cv2.imread('./images/%06d.jpg'%num))
    H = len(image); W=len(image[0])
    for h in range(0, H//12*12, H//12):
        for w in range(0, W//16*16, W//16):
            res += '1' if image[h][w][0]>130 else '0'
    arr.append(res)

with open('./raw_array.pickle', 'wb') as fw:
    pickle.dump(arr, fw)