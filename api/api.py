import base64
import io

from flask import Flask
from flask_restful import Resource, Api, reqparse
from PIL import Image

from image_processor import ImageProcessor


def decode_image(encoded_image: str) -> Image:
    """
    Decodes image data from a request
    :param encoded_image: image data from a request
    :return: decoded PIL image
    """
    image_data = base64.b64decode(encoded_image)
    image = Image.open(io.BytesIO(image_data))
    return image


def encode_image(image: Image) -> str:
    """
    Encodes image data to a request
    :param image: image data from a request
    :return: encoded PIL image
    """
    buffered = io.BytesIO()
    image.save(buffered, format="JPEG")
    img_bytes = base64.b64encode(buffered.getvalue())
    return img_bytes.decode('utf-8')


class ImageResource(Resource):
    def get(self, img: str):
        decoded_image = decode_image(img.replace('-', '/'))
        processed_image = ImageProcessor.blur(decoded_image)
        encoded_image = encode_image(processed_image)

        return {'image': encoded_image}


class CleanSurfApi(Flask):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.api = Api(self)
        self.image_processor = ImageProcessor()

        self.api.add_resource(ImageResource, '/image/<string:img>')

    def run(self, *args, **kwargs):
        super().run(*args, **kwargs)


if __name__ == '__main__':

    app = CleanSurfApi(__name__)
    app.run(debug=True)


