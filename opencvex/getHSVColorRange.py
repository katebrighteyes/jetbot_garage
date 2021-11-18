from OpenCV_Functions import *


def nothing(x):
    pass

imagePath = "./solidWhiteCurve.jpg"
image = imageRead(imagePath) 
#backup = imageCopy(image)

image_hsv = convertColor(image, cv2.COLOR_BGR2HSV)

#:wqimg = np.zeros((10, 10, 3), np.uint8)
cv2.namedWindow('image', cv2.WINDOW_GUI_EXPANDED)
cv2.createTrackbar('H1', 'image', 0, 360, nothing)
cv2.createTrackbar('S1', 'image', 0, 255, nothing)
cv2.createTrackbar('V1', 'image', 0, 255, nothing)
cv2.createTrackbar('H2', 'image', 0, 360, nothing)
cv2.createTrackbar('S2', 'image', 0, 255, nothing)
cv2.createTrackbar('V2', 'image', 0, 255, nothing)

cv2.setTrackbarPos('H1', 'image', 0)
cv2.setTrackbarPos('S1', 'image', 0)
cv2.setTrackbarPos('V1', 'image', 150)
cv2.setTrackbarPos('H2', 'image', 179)
cv2.setTrackbarPos('S2', 'image', 10)
cv2.setTrackbarPos('V2', 'image', 255)

while True:
	cv2.imshow('image', image)
	if cv2.waitKey(1) & 0xFF == 27:
		break
	h1 = cv2.getTrackbarPos('H1', 'image')
	s1 = cv2.getTrackbarPos('S1', 'image')
	v1 = cv2.getTrackbarPos('V1', 'image')
	h2 = cv2.getTrackbarPos('H2', 'image')
	s2 = cv2.getTrackbarPos('S2', 'image')
	v2 = cv2.getTrackbarPos('V2', 'image')

	#img1[:] = [h1, s1, v1]
	lower_hsv = np.array([h1, s1, v1])
	upper_hsv = np.array([h2, s2, v2])

	#img = convertColor(img1, cv2.COLOR_HSV2BGR)
	hls_region = splitColor(image_hsv, lower_hsv, upper_hsv)
	image = convertColor(hls_region, cv2.COLOR_HSV2BGR)

	#imageShow("image", output_hsv_region)

cv2.destroyAllWindows()
