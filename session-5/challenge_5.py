import random
import requests

from IPython import embed
from time import sleep
from bs4 import BeautifulSoup


BASE_URL = "https://sample-target-bucket-with-html-pages.s3-ap-southeast-1.amazonaws.com/group2/index.html"
base1 = "https://sample-target-bucket-with-html-pages.s3-ap-southeast-1.amazonaws.com"

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


def extract_html_content(target_url):
#     print(f'Downloading HTML content of {target_url}')
    response = requests.get(target_url)
    return response.text

# @debug_input_output
def extract_target_value_from_page(html_string):
    soup = BeautifulSoup(html_string, 'html.parser')
    l_elements = soup.find_all('a')
    a = []
    for i in l_elements:
        a += [i.get('href')]
    return a

def extract_target_value_from_page1(html_string):
    soup1 = BeautifulSoup(html_string, 'html.parser')
    div_elements = soup1.find('div')
    return div_elements.get_text()

def main():
    htmls = extract_html_content(BASE_URL)
    links = extract_target_value_from_page(htmls)
    for page in links:
        target_page = base1 + page
        print(target_page)



if __name__ == "__main__":
    main()
