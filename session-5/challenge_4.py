import random
import requests

from IPython import embed
from time import sleep
from bs4 import BeautifulSoup

BASE_URL = "http://sample-target-bucket-with-html-pages.s3-website-ap-southeast-1.amazonaws.com"

PAGES = ["group1/1.html",
         "group1/2.html",
         "group1/3.html",
         "group1/4.html",
         "group1/5.html"]

def debug_input_output(function):
    def wrapper(*args, **kwargs):
        print(f'[START: {function.__name__}]')
        output = function(*args, **kwargs)
        print(f'[END: {function.__name__}]')
        return output
    return wrapper

@debug_input_output
def delay(seconds):
    print(f"Sleeping for {seconds} second(s)")
    sleep(seconds)

def get_random_number():
    return random.randint(1,3)

@debug_input_output
def extract_html_content(target_url):
    print(f'Downloading HTML content of {target_url}')
    response = requests.get(target_url)
    return response.text

@debug_input_output
def extract_target_value_from_page(html_string):
    soup = BeautifulSoup(html_string, 'html.parser')
    div_elements = soup.find('div')
    return div_elements.get_text()

def main():
    for page in PAGES:
        target_page = BASE_URL + "/" + page
        htmls = extract_html_content(target_page)
        print(htmls)

        targets = extract_target_value_from_page(htmls)
        print(targets)

        delay(get_random_number())


if __name__ == "__main__":
    main()
