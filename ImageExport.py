import base64
import io
import os
from PIL import Image

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
    FUNCTION = "encode_image"
    CATEGORY = "Liberated Nodes/Image"

    def encode_image(self, image: Image, output_directory: str, filename: str):
        # Convert image to bytes
        buffered = io.BytesIO()
        image.save(buffered, format=image.format)
        image_bytes = buffered.getvalue()

        # Encode bytes to base64
        image_base64 = base64.b64encode(image_bytes).decode('utf-8')

        os.makedirs(output_directory, exist_ok=True)
        filepath = os.path.join(output_directory, filename)

        # Ensure the filename ends with .csv
        if not filepath.lower().endswith('.txt'):
            filepath += '.txt'

        # Write base64 string to file
        try:
            with open(filepath, 'wb') as file:
                file.write(image_base64)
            print(f"Encoded image saved to {filepath}")
        except Exception as e:
            print(f"Error saving encoded image file: {str(e)}")

        return ()

    @classmethod
    def IS_CHANGED(cls, image, output_directory, filename):
        return float("NaN")