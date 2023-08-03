import requests

def download_image(url, filename):
    response = requests.get(url, stream=True)
    if response.status_code == 200:
        with open(filename, 'wb') as file:
            for chunk in response.iter_content(1024):
                file.write(chunk)
    else:
        print('Unable to download image.')
    
# You can call the function with an image url and filename
download_image('https://user-images.githubusercontent.com/25199092/140672104-9a688a21-92bd-400e-a874-93c2eb9a57c2.png', 'downloaded_image.jpg')



