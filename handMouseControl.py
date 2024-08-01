from sys import stdout
from math import hypot
from pynput.mouse import Button, Controller as MouseController
from time import time, sleep
from screeninfo import get_monitors
import numpy as np
import cv2
from handTrackerModule import handDetector

mymouse = MouseController()

monitor = get_monitors()[0]
wScr = monitor.width
hScr = monitor.height

wCam, hCam = 640, 480
framReduction = 150
smoothening = 3

pLoc = [0,0]
cLoc = [0,0]
# wCam, hCam = 1280, 720

cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)

pTime = 0
cTime = 0

detector = handDetector(detectionConfidence=0.85)

maxX = 747
maxY = 610

tipIds = [4, 8, 12, 16, 20]

press = False
while True:
    success, img = cap.read()
    img = detector.findHands(img)
    lmList = detector.findPosition(img, draw=False)

    cv2.rectangle(img, (framReduction, framReduction), (wCam-framReduction, hCam-framReduction), (51, 190, 232), 2)
    if len(lmList) != 0:
        indexFinger = lmList[8][1], lmList[8][2]
        thumb = lmList[4][1], lmList[4][2]
        knuckle = lmList[6][1], lmList[6][2]

        cv2.circle( img, indexFinger, 15, (51, 190, 232), cv2.FILLED)
        cv2.circle( img, thumb, 15, (51, 190, 232), cv2.FILLED)

        fingers = detector.fingersUp(img)

        if sum(fingers) != 0:
            if fingers[1] and not fingers[2]:
                moved = (np.interp(indexFinger[0], (framReduction, wCam-framReduction), (0, wScr)), np.interp(indexFinger[1], (framReduction, hCam-framReduction), (0, hScr)))

                cLoc[0] = pLoc[0] + (moved[0] - pLoc[0])/smoothening
                cLoc[1] = pLoc[1] + (moved[1] - pLoc[1])/smoothening

                mymouse.position = (wScr-cLoc[0], cLoc[1])
                pLoc = cLoc

            if fingers[1]:
                length = hypot(thumb[0]-knuckle[0], thumb[1]-knuckle[1])
                if length < 15:
                    if not press:
                        press = True
                        mymouse.press(Button.left)
                else:
                    if press:
                        press = False
                        mymouse.release(Button.left)

        stdout.flush()
        if not press:
            print(f"\rNot pressed {fingers}", end="")
        else:
            print(f"\rPressed     {fingers}", end="")



    cTime = time()
    fps = 1/(cTime - pTime)
    pTime = cTime

    cv2.putText(img, f"FPS: {int(fps)}", (40, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (51, 190, 232), 3)
    cv2.imshow("Img", img)
    cv2.waitKey(1)