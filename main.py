import cv2

img = cv2.imread("Assignment_image.png")
img = cv2.resize(img, None, fx = 0.5, fy = 0.5)

img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


row,col = img.shape

# for i in range(row):
#     for j in range(col):

        



cv2.imshow("image",img)
cv2.waitKey(0)