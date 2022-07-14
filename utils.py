import cv2 as cv
import numpy as np
import os

from datetime import datetime

def apply_kmeans(image):
    image_data = image.reshape((-1,3))
    image_data = np.float32(image_data)

    criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 10, 1.0)
    K=8

    result, label, center = cv.kmeans(
        image_data, 
        K, 
        None, 
        criteria, 
        10, 
        cv.KMEANS_RANDOM_CENTERS
    )

    center = np.uint8(center)
    result = center[label.flatten()]
    return result.reshape((image.shape))


def save(image):
    folder_name = 'output'
    filename = f'IMG{get_current_time()}'
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
    cv.imwrite(os.path.join(folder_name, filename+'.jpg'), image)


def get_current_time():
    now = datetime.now()
    formatted = now.strftime("%H%M%S%d%m%y")
    return str(formatted)
