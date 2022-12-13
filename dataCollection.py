import cv2
from cvzone.HandTrackingModule import HandDetector
import numpy as np
import math
import time

cap = cv2.VideoCapture(0)
detector = HandDetector(maxHands=1)

offset = 20
imgSize = 300

counter = 0

while True:
    success, img = cap.read()
    hands, img = detector.findHands(img)
    if hands:
        hand = hands[0]
        x, y, w, h = hand['bbox']

        imgWhite = np.ones((imgSize, imgSize, 3), np.uint8) * 255
        imgCrop = img[y - offset:y + h + offset, x - offset:x + w + offset]

        imgCropShape = imgCrop.shape

        aspectRatio = h / w

        if aspectRatio > 1:
            k = imgSize / h
            wCal = math.ceil(k * w)
            imgResize = cv2.resize(imgCrop, (wCal, imgSize))
            imgResizeShape = imgResize.shape
            wGap = math.ceil((imgSize - wCal) / 2)
            imgWhite[:, wGap:wCal + wGap] = imgResize

        else:
            k = imgSize / w
            hCal = math.ceil(k * h)
            imgResize = cv2.resize(imgCrop, (imgSize, hCal))
            imgResizeShape = imgResize.shape
            hGap = math.ceil((imgSize - hCal) / 2)
            imgWhite[hGap:hCal + hGap, :] = imgResize

        cv2.imshow("ImageCrop", imgCrop)
        cv2.imshow("ImageWhite", imgWhite)

    cv2.imshow("Image", img)
    key = cv2.waitKey(1)
    
    if key == ord("a"):
        counter += 1
        cv2.imwrite(f'Data/A/Image_{time.time()}.jpg',imgWhite)
        print(counter)
    if key == ord("b"):
        counter += 1
        cv2.imwrite(f'Data/B/Image_{time.time()}.jpg',imgWhite)
        print(counter)
    if key == ord("c"):
        counter += 1
        cv2.imwrite(f'Data/C/Image_{time.time()}.jpg',imgWhite)
        print(counter)
    if key == ord("d"):
        counter += 1
        cv2.imwrite(f'Data/D/Image_{time.time()}.jpg',imgWhite)
        print(counter)
    if key == ord("e"):
        counter += 1
        cv2.imwrite(f'Data/E/Image_{time.time()}.jpg',imgWhite)
        print(counter)
    if key == ord("f"):
        counter += 1
        cv2.imwrite(f'Data/F/Image_{time.time()}.jpg',imgWhite)
        print(counter)
    if key == ord("g"):
        counter += 1
        cv2.imwrite(f'Data/G/Image_{time.time()}.jpg',imgWhite)
        print(counter)
    if key == ord("h"):
        counter += 1
        cv2.imwrite(f'Data/H/Image_{time.time()}.jpg',imgWhite)
        print(counter)
    if key == ord("i"):
        counter += 1
        cv2.imwrite(f'Data/I/Image_{time.time()}.jpg',imgWhite)
        print(counter)
    if key == ord("j"):
        counter += 1
        cv2.imwrite(f'Data/J/Image_{time.time()}.jpg',imgWhite)
        print(counter)
    if key == ord("k"):
        counter += 1
        cv2.imwrite(f'Data/K/Image_{time.time()}.jpg',imgWhite)
        print(counter)
    if key == ord("l"):
        counter += 1
        cv2.imwrite(f'Data/L/Image_{time.time()}.jpg',imgWhite)
        print(counter)
    if key == ord("m"):
        counter += 1
        cv2.imwrite(f'Data/M/Image_{time.time()}.jpg',imgWhite)
        print(counter)
    if key == ord("n"):
        counter += 1
        cv2.imwrite(f'Data/N/Image_{time.time()}.jpg',imgWhite)
        print(counter)
    if key == ord("o"):
        counter += 1
        cv2.imwrite(f'Data/O/Image_{time.time()}.jpg',imgWhite)
        print(counter)
    if key == ord("p"):
        counter += 1
        cv2.imwrite(f'Data/P/Image_{time.time()}.jpg',imgWhite)
        print(counter)
    if key == ord("q"):
        counter += 1
        cv2.imwrite(f'Data/Q/Image_{time.time()}.jpg',imgWhite)
        print(counter)
    if key == ord("r"):
        counter += 1
        cv2.imwrite(f'Data/R/Image_{time.time()}.jpg',imgWhite)
        print(counter)
    if key == ord("s"):
        counter += 1
        cv2.imwrite(f'Data/S/Image_{time.time()}.jpg',imgWhite)
        print(counter)
    if key == ord("t"):
        counter += 1
        cv2.imwrite(f'Data/T/Image_{time.time()}.jpg',imgWhite)
        print(counter)
    if key == ord("u"):
        counter += 1
        cv2.imwrite(f'Data/U/Image_{time.time()}.jpg',imgWhite)
        print(counter)
    if key == ord("v"):
        counter += 1
        cv2.imwrite(f'Data/V/Image_{time.time()}.jpg',imgWhite)
        print(counter)
    if key == ord("w"):
        counter += 1
        cv2.imwrite(f'Data/W/Image_{time.time()}.jpg',imgWhite)
        print(counter)
    if key == ord("x"):
        counter += 1
        cv2.imwrite(f'Data/X/Image_{time.time()}.jpg',imgWhite)
        print(counter)
    if key == ord("y"):
        counter += 1
        cv2.imwrite(f'Data/Y/Image_{time.time()}.jpg',imgWhite)
        print(counter)
    if key == ord("z"):
        counter += 1
        cv2.imwrite(f'Data/Z/Image_{time.time()}.jpg',imgWhite)
        print(counter)
    

    if key == ord(" "):
        break
cap.release()
cv2.destroyAllWindows()

    