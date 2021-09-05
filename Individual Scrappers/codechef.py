from types import ClassMethodDescriptorType
import selenium
from bs4 import BeautifulSoup
import requests
import time
import random

id = input("")
url = f'https://www.codechef.com/users/{id}'
header = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_5_2) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.2 Safari/605.1.15',
}
source = requests.get(url, headers=header).text
soup = BeautifulSoup(source, 'lxml')

rating = 0

rating = soup.find('div', class_='rating-number').text


ccrating = "Codechef:"+rating

f = open("data.txt", "a")
f.write(ccrating)
