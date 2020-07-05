from collections import Counter
import itertools
import re
import requests
from bs4 import BeautifulSoup


def read_url(url):
    print(f'\n{url}\n')
    data = requests.get(url).content
    soup = BeautifulSoup(data, "html5lib")
    body = soup.find('body')
    data = soup.body.text
    #TODO:fixing encoding and nested data problems
    # geting string between tow substrigs     
    return data
