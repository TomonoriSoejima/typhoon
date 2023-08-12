
## Okinawa Weather Scraper

This script is designed to scrape weather images from `https://www.kadena.af.mil/Agencies/Local-Weather/`, analyze the images for specific text patterns indicating weather conditions, and then send the relevant notifications using the LINE Notify API.

### Features:

1. Web scraping using `BeautifulSoup`.
2. Image conversion from Base64 to PNG.
3. Text detection from images using `Google Cloud Vision API`.
4. Sending notifications through LINE Notify API.

### How to Setup:

1. Install the required Python packages:
    
    ```bash
    pip3 install beautifulsoup4 requests pillow google-cloud-vision
    ```
    
2. Ensure you have setup Google Cloud SDK and have `vision_v1.ImageAnnotatorClient()` credentials configured.
3. Set your LINE token in your environment. It will be used to send notifications.
    
    ```bash
    export LINE_TOKEN='your_token_here'
    ```
    

### Usage:

Run the script using Python:

```bash
python3 all.py
```

### Functions:

1. `convert_base64_to_image(base64_string, output_path)`: Converts a base64 encoded image to a PNG file.
2. `detect_text(path)`: Detects text from an image using Google Cloud Vision API and searches for specific text patterns related to Okinawa's weather conditions.
3. `line_notify(msg)`: Sends the detected text and additional predefined information as a message to the LINE Notify API.

### Note:

* This script currently targets a specific image on the web page (`img_tags[3]`). Ensure the image of interest remains at this index.
* It specifically looks for the pattern `"OKINAWA IS CURRENTLY IN"` in the text annotations and sends notifications accordingly.

### Disclaimer:

The website structure or the specific image index might change over time. It is advisable to periodically check the script's functionality. Ensure you have the necessary permissions to scrape data from the mentioned website. This script is for educational purposes only.

### License:

MIT (or any appropriate license you want to put)

### Contributing:

If you have suggestions to improve the script or find any issues, feel free to contribute or open an issue.

### Credits:

[Your Name / Your Organization / or leave it blank if you prefer]

* * *

Remember, always make sure that you're allowed to scrape a website by checking its `robots.txt` file or its terms of service. This README is designed to be both informative and user-friendly. Adjustments can be made as per specific requirements or additional details.
