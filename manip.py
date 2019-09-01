print ("RELOAD SUCCESSFUL")
# set CONDA_DLL_SEARCH_MODIFICATION_ENABLE=1
# conda update freetype
# conda install opencv

K16 = 16384
K32 = 32768
scale = K16/10000

import numpy as np
import cv2

top = -10000
left = -10000
right = 10000
bottom = 10000
points = np.array([
        [-10000, -10000],
        [+10000, -10000],
        [+10000, +10000],
        [-10000, +10000],
    ], dtype = "float32")

flat = np.array([
        [-10000, -10000],
        [+10000, -10000],
        [+10000, +10000],
        [-10000, +10000],
    ], dtype = "float32")

"""
A->B
   |
   v
D<-C
"""

cal_pressed = 0
M = cv2.getPerspectiveTransform(points, points)

def trig(x, y, calibrate):
    global points, M, cal_pressed
    if calibrate and not cal_pressed:
        points = np.array([points[1], points[2], points[3], [x,y]], dtype = "float32")
        print ("Calibration point added: ", x, y)
        print ("Calibration = ", points)
        M = cv2.getPerspectiveTransform(points, flat)
    cal_pressed = calibrate
    q = np.float32([[x, y]]).reshape(-1, 1, 2)
    new_x, new_y = (cv2.perspectiveTransform(q, M)[0][0])
    new_x = (new_x * scale) + K16
    new_y = (new_y * scale) + K16
    new_x = min(new_x, K32)
    new_y = min(new_y, K32)
    new_x = max(0, new_x)
    new_y = max(0, new_y)
    return (int(new_x), int(new_y))