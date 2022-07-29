import numpy as np
import matplotlib.pyplot as plt
import cv2
import math
def hist(image):
	H = np.zeros(shape=(256, 1))
	s = image.shape
	for i in range(s[0]):
		for j in range(s[1]):
			k = image[i][j]
			H[k, 0] = H[k, 0] + 1 
	return H
	

space = cv2.imread('image.jpg')
#cv2.imshow('original', space)
#cv2.waitKey()
s = space.shape
graph = hist(space)
#plt.plot(graph)
#plt.show()
x = graph.reshape(1, 256)
y = np.array([])
y = np.append(y, x[0, 0])

for i in range(255):
	k = x[0, i + 1] + y[i]
	y = np.append(y, k)
y = np.round((y/(s[0]*s[1])) * 255)

for i in range(s[0]):
	for j in range(s[1]):
		k = space[i, j]
		space[i][j] = y[k]
cv2.imshow('equalize', space)
cv2.waitKey()
