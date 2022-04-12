from __future__ import print_function
import cv2 as cv
import argparse

import pyautogui as pyautogui

parser = argparse.ArgumentParser(description='Code for Cascade Classifier tutorial.')
parser.add_argument('--face_cascade', help='Path to face cascade.', default='data/haarcascade_frontalface_default.xml')
parser.add_argument('--camera', help='Camera divide number.', type=int, default=0)
args = parser.parse_args()

face_cascade_name = args.face_cascade
face_cascade = cv.CascadeClassifier()

def detectAndDisplay(frame, x_wmax, y_wmax, x_wmin, y_wmin, x_vmax, y_vmax, x_vmin, y_vmin):
    #frame_gray = cv.flip(frame, 1)
    frame_gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    # -- Detect faces
    faces = face_cascade.detectMultiScale(frame_gray, 1.3, 5)

    sx = (x_vmax - x_vmin) / (x_wmax - x_wmin)
    sy = (y_vmax - y_vmin) / (y_wmax - y_wmin)

    for (x, y, w, h) in faces: #x, y, w, h pentru patratul care imi face fata
        #frame = cv.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 255), 3) #punctele pentru fata --> detectia fetei
        frame = cv.rectangle(frame, (x + int(w / 2), y + int(h / 2)), (x + int(w / 2), y + int(h / 2)), (0, 255, 0), 3)

        x_v = x_vmin + ((x - x_wmin) * sx)
        y_v = y_vmin + ((y - y_wmin) * sy)

        pyautogui.moveTo(x_v, y_v)
    cv.imshow('Capture - Face detection', frame)


def cameraView():
    # -- 1. Load the cascades
    if not face_cascade.load(cv.samples.findFile(face_cascade_name)):
        print('--(!)Error loading face cascade')
        exit(0)

    camera_device = args.camera
    # -- 2. Read the video stream
    cap = cv.VideoCapture(camera_device, cv.CAP_DSHOW)

    if not cap.isOpened:
        print('--(!)Error opening video capture')
        exit(0)

    while True:
        cap.set(cv.CAP_PROP_FRAME_WIDTH, 1920)
        cap.set(cv.CAP_PROP_FRAME_HEIGHT, 1080)
        ret, frame = cap.read()
        # currentPos = cap.get(cv.CAP_PROP_POS_FRAMES)
        # print(currentPos)

        x_wmax = 640
        y_wmax = 0
        x_wmin = 0
        y_wmin = 480

        x_vmax = 1920
        y_vmax = 0
        x_vmin = 0
        y_vmin = 1080

        # frame_w = cap.get(cv.CAP_PROP_FRAME_WIDTH)
        # frame_h = cap.get(cv.CAP_PROP_FRAME_HEIGHT)
        # print("latimea frame-ului este: ", frame_w)
        # print("inaltimea frame-ului este: ", frame_h)

        if frame is None:
            print('--(!) No captured frame -- Break!')
            break
        detectAndDisplay(frame, x_wmax, y_wmax, x_wmin, y_wmin, x_vmax, y_vmax, x_vmin, y_vmin)
        if cv.waitKey(10) == 27:
            break

if __name__ == '__main__':
    cameraView()