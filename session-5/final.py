import random
import requests

from IPython import embed
from time import sleep
from bs4 import BeautifulSoup

BASE_URL = "http://sample-target-bucket-with-html-pages.s3-website-ap-southeast-1.amazonaws.com"


def delay(seconds):
    print(f"Sleeping for {seconds} second(s)")
    sleep(seconds)

def get_random_number():
    return random.randint(1,3)


def extract_html_content(target_url):
    print(f'Downloading HTML content of {target_url}')
    response = requests.get(target_url)
    return response.text



def main():
    delay(get_random_number())
    html_doc = extract_html_content(BASE_URL + '/group3/target.html')
    soup = BeautifulSoup(html_doc, 'html.parser')
    div_elements = soup.find_all('div', {'class': 'content_section_text'})
    target_div = div_elements[1]
    items = target_div.find('ul').find_all('li')
    for item in items:
        texts = item.get_text().replace('\n', '')
        text_lists = [text for text in texts.split(' ') if text]
        clean = ' '.join(text_lists)
        print(clean, '\n')

        delay(get_random_number())


if __name__ == "__main__":
    main()
