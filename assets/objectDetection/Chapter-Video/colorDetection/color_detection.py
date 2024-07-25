# color_detection.py

import cv2
import numpy as np

def detect_traffic_light_color(roi):
    hsv = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)

    red_lower1 = np.array([0, 70, 50])
    red_upper1 = np.array([10, 255, 255])
    red_lower2 = np.array([170, 70, 50])
    red_upper2 = np.array([180, 255, 255])

    yellow_lower = np.array([20, 100, 100])
    yellow_upper = np.array([30, 255, 255])

    green_lower = np.array([40, 50, 50])
    green_upper = np.array([90, 255, 255])

    mask_red1 = cv2.inRange(hsv, red_lower1, red_upper1)
    mask_red2 = cv2.inRange(hsv, red_lower2, red_upper2)
    mask_red = cv2.add(mask_red1, mask_red2)

    mask_yellow = cv2.inRange(hsv, yellow_lower, yellow_upper)
    mask_green = cv2.inRange(hsv, green_lower, green_upper)

    red_count = cv2.countNonZero(mask_red)
    yellow_count = cv2.countNonZero(mask_yellow)
    green_count = cv2.countNonZero(mask_green)

    if red_count > yellow_count and red_count > green_count:
        return "vermelho"
    elif yellow_count > red_count and yellow_count > green_count:
        return "amarelo"
    elif green_count > red_count and green_count > yellow_count:
        return "verde"
    else:
        return "indefinido"

def describe_traffic_light_color(traffic_light_color, position):
    return f'semáforo {traffic_light_color} {position}'
