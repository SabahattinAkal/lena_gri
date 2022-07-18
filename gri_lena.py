import cv2 
import numpy as np


# Görseli okuma ve ekranda gösterme

resim = cv2.imread("lena.png")
cv2.imshow("Orjinal Resim",resim)


#gri resmi ekranda gösterme

GriResim = resim[:,:,0]
cv2.imshow("Gri Resim",GriResim)
cv2.waitKey()