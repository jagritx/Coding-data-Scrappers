from types import ClassMethodDescriptorType
import selenium
from bs4 import BeautifulSoup
import requests
import time
import random

id = input("")
url = f'https://www.hackerrank.com/{id}?h_r=internal-search&hr_r=1'
header = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_5_2) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.2 Safari/605.1.15',
}
source = requests.get(url, headers=header).text
soup = BeautifulSoup(source, 'lxml')

certificatelist = []
badgelist = []
badgedata = []
i = 0

if(soup.find('div', class_='hacker-certificates')):
    for certificates in soup.findAll('h2', class_='certificate-heading'):
        certificatelist.append(certificates.text)

if(soup.find('div', class_='badges-list')):
    for badges in soup.find('div', class_='badges-list'):
        for bas in badges.find_all('svg', class_='badge-star'):
            i += 1
        badgedata.append(i)
        i = 0
        badgelist.append(badges.text)

print(certificatelist)
print(badgelist)
print(badgedata)
