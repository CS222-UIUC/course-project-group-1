import time
import os

from PIL import Image, ImageFilter
from nudenet import NudeClassifier

classifier = NudeClassifier()


class ImageProcessor:
    @staticmethod
    def process(image: Image) -> Image:
        # Blurring the image
        image_path = 'temp_{}.jpeg'.format(time.time())
        image.save(image_path)
        if classifier.classify(image_path)[image_path]['unsafe'] > 0.5:
            processed_image = image.filter(ImageFilter.GaussianBlur(radius=10))
        else:
            processed_image = image
        os.remove(image_path)
        return processed_image
    
