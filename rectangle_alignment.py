import cv2
import numpy as np
import math

points = []
img = cv2.imread('Rectangle.jpg')

height, width, _ = img.shape

white_bg = np.ones((height, width, 3), dtype=np.uint8) * 255

def getpoints(event, x, y, flags, param):
    global img
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img, (x, y), 1, (255, 0, 0), -1)
        points.append([x, y])
        if len(points) == 4:
            getperspective()

    cv2.imshow('image', img)

def getperspective():
    global img, points, white_bg
    width = int(math.sqrt((points[1][0] - points[0][0])**2 + (points[1][1] - points[0][1])**2))
    height = int(math.sqrt((points[2][0] - points[0][0])**2 + (points[2][1] - points[0][1])**2))
    pts1 = np.float32(points)
    pts2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])
    matrix = cv2.getPerspectiveTransform(pts1, pts2)
    imgOutput = cv2.warpPerspective(img, matrix, (width, height))

    white_bg[points[0][1]:points[0][1]+height, points[0][0]:points[0][0]+width] = imgOutput
    
    cv2.imshow('output', white_bg)
    
    img = cv2.imread('Rectangle.jpg')
    points.clear()
    cv2.imshow('image', img)
    cv2.setMouseCallback('image', getpoints)

while True:
    cv2.imshow('image', img)
    cv2.setMouseCallback('image', getpoints)
    
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break
    elif key == ord('r'):
        img = cv2.imread('Rectangle.jpg')
        points.clear()
        cv2.imshow('image', img)
        cv2.setMouseCallback('image', getpoints)
    #enter d to save the output
    elif key == ord('d'):
        cv2.imwrite('output_alignment.jpg', white_bg)

cv2.destroyAllWindows()
