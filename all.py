from bs4 import BeautifulSoup
import requests
import base64
import io
import os
from PIL import Image
from google.cloud import vision_v1

def convert_base64_to_image(base64_string, output_path):
    base64_data = base64_string.split(',')[1]
    image_data = base64.b64decode(base64_data)
    image = Image.open(io.BytesIO(image_data))
    image.save(output_path)

def detect_text(path):
    client = vision_v1.ImageAnnotatorClient()
    with open(path, 'rb') as image_file:
        content = image_file.read()
    image = vision_v1.Image(content=content)
    response = client.text_detection(image=image)
    texts = response.text_annotations
    result = []
    for text in texts:
        lines = text.description.split('\n')
        for i in range(len(lines)):
            if "OKINAWA IS CURRENTLY IN" in lines[i]:
                result.append(lines[i])  # append the target line to the result list
                if i+1 < len(lines):
                    result.append(lines[i+1])  # append the next line to the result list
                return result

    if response.error.message:
        raise Exception(
            '{}\nFor more info on error messages, check: '
            'https://cloud.google.com/apis/design/errors'.format(
                response.error.message))

def line_notify(msg):
    token = os.environ['LINE_TOKEN']
    url = 'https://notify-api.line.me/api/notify'
    headers = {'Authorization': 'Bearer ' + token}
    
    # Join array elements into a single string with line breaks
    msg.append("\n")
    msg.append("台風コンディション1,1C,1E,1R, を発令している場合、休校です。\n")
    msg.append("Condition 1(normal) 12時間以内に 50ノットの突風の可能性\n")
    msg.append("Condition 1C (caution) 35-49ノットかそれ以上の強風\n")
    msg.append("Condition 1E (emergency) 50ノットかそれ以上の強風\n")
    msg.append("Condition 1R (recovery) 引き続き自宅待機\n")
    
    msg = '\n'.join(msg)
    
    payload = {'message': msg}
    r = requests.post(url, headers=headers, params=payload)
    return r.status_code



# Scraping the image
url = "https://www.kadena.af.mil/Agencies/Local-Weather/"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
img_tags = soup.find_all('img')
base64_string = img_tags[3].get('src')

# Converting the base64 string to image
output_path = "output.png"
convert_base64_to_image(base64_string=base64_string, output_path=output_path)

# Detecting the text in the image
line_notify(detect_text(output_path))


