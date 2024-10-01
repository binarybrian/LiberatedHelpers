import base64
import os
#import sys

#from util import pil_to_tensor, tensor_to_pil
from .util import tensor_to_pil

#from PIL import Image

class ImageExport:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "image": ("IMAGE",),
                "output_directory": ("STRING", {"default": ""}),
                "filename": ("STRING", {"default": "encoded_image.txt"}),
            }
        }

    RETURN_TYPES = ()
    FUNCTION = "process_image"
    CATEGORY = "Upscale Nodes/utility"
    OUTPUT_NODE = True

    def process_image(self, image, output_directory, filename):
        print(f"The type of the argument 'tensor' is: {type(image)}")

        pil_image = tensor_to_pil(image)
        image_bytes = pil_image.convert('RGB').tobytes()

        image_base64 = base64.b64encode(image_bytes).decode('utf-8')

        os.makedirs(output_directory, exist_ok=True)
        filepath = os.path.join(output_directory, filename)

        if not filepath.lower().endswith('.txt'):
            filepath += '.txt'

        try:
            with open(filepath, 'w') as file:
                file.write(image_base64)
            print(f"Encoded image saved to {filepath}")
        except Exception as e:
            print(f"Error saving encoded image file: {str(e)}")



# def main():
#     if len(sys.argv) != 2:
#         print("Usage: python script.py <image_path>")
#         sys.exit(1)
#
#     image_path = sys.argv[1]
#
#     try:
#         with Image.open(image_path) as img:
#             image_export = ImageExport()
#             tensor = pil_to_tensor(img)
#             image_export.process_image(tensor, "/qpool/temp/", 'encoded_image.txt')
#     except Exception as e:
#         print(f"Error processing image: {e}")
#         sys.exit(1)
#
# if __name__ == "__main__":
#     main()