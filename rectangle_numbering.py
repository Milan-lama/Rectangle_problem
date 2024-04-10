import cv2
import numpy as np
import math

points = []
length = []
img = cv2.imread('Rectangle.jpg')

def getpoints(event, x, y, flags, param):
    global img
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img, (x, y), 1, (255, 0, 0), -1)
        points.append([x, y])
        if len(points) == 3:
            distance = int(math.sqrt((points[1][0] - points[0][0])**2 + (points[1][1] - points[0][1])**2))
            length.append([distance,points[2]])
            points.clear()

    cv2.imshow('image', img)

def assignOrder():
    sorted_data = sorted(length, key=lambda x: x[0])
    for i in range(len(sorted_data)):
        cv2.putText(img, str(i+1), (sorted_data[i][1][0], sorted_data[i][1][1]), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)



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
    #enter d to assign number and save the output
    elif key == ord('d'):
        assignOrder()
        cv2.imwrite('output_numbering.jpg', img)

        

cv2.destroyAllWindows()
