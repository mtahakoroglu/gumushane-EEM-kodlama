import cv2
import numpy as np

img1name = "20240528_144318.jpg"
img2name = "20240528_144324.jpg"
img1 = cv2.imread(img1name)
img2 = cv2.imread(img2name)
img1name, img1Extension = img1name.rsplit('.', 1)
img2name, img2Extension = img2name.rsplit('.', 1)
imgName, k = "", 0
while True:
    if img1name[k] == img2name[k]:
        imgName = f"{imgName}{img1name[k]}"
        k = k+1
    else:
        imgName = imgName[0:-1] # drop the last letter that is _
        break

h, w, c = img1.shape
img = np.zeros((h, 2*w, c), np.uint8)
img[:,0:w,:] = img1
img[:,w:2*w,:] = img2

# resize image to display on screen
s = 0.1
rimg = cv2.resize(img, (int(s*img.shape[1]), int(s*img.shape[0])), 0)
cv2.imshow("Merged image", rimg)
cv2.waitKey(0)
# save image
cv2.imwrite(f"{imgName}_merged_horizontally.jpg", img, [cv2.IMWRITE_JPEG_QUALITY, 20])