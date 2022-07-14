import cv2 as cv
import numpy as np

import urllib.request

class UnsplashAPI:
    def __init__(self) -> None:
       pass

    @staticmethod
    def fetch_random_image(args:str='jet'):
        url = f'https://source.unsplash.com/random/?{args}'
        req = urllib.request.urlopen(url)

        # convert into a cv2 compatible object
        arr = np.asarray(bytearray(req.read()), dtype=np.uint8)
        image = cv.imdecode(arr, -1)

        return image if image is not None else None