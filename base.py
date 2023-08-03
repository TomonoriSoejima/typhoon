import base64
import io
from PIL import Image

def convert_base64_to_image(base64_string, output_path):
    base64_data = base64_string.split(',')[1]
    image_data = base64.b64decode(base64_data)
    image = Image.open(io.BytesIO(image_data))
    image.save(output_path)

# example usage

with open('output.txt', 'r') as file:
    # Read the contents of the file
    content = file.read()

image_path=content
convert_base64_to_image(base64_string=image_path, output_path="output.png")
