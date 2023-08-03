from bs4 import BeautifulSoup
import requests

url = "https://www.kadena.af.mil/Agencies/Local-Weather/"
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')
# print(soup.prettify())

with open('output.txt', 'w') as file:
    img_tags = soup.find_all('img')
    kore = img_tags[3].get('src')
    file.write(kore)





