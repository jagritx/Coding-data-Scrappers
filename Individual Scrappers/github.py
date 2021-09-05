from types import ClassMethodDescriptorType
import selenium
from bs4 import BeautifulSoup
import requests
import time
import random

id = input("")
url = f'https://github-readme-stats.vercel.app/api?username={id}&count_private=true'
langurl = f'https://github-readme-stats.vercel.app/api/top-langs/?username={id}'
header = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_5_2) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.2 Safari/605.1.15',
}
source = requests.get(url, headers=header).text
langsource = requests.get(langurl, headers=header).text


soup = BeautifulSoup(source, 'lxml')
langsoup = BeautifulSoup(langsource, 'lxml')


countlist = []
langlist = []

for field in soup.findAll('text', class_='stat'):
    countlist.append(field.text)


for language in langsoup.findAll('text', class_='lang-name'):
    langlist.append(language.text)

print(countlist)
print(langlist)
