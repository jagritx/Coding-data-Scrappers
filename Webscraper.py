from linkedin_scraper import Person, actions
from selenium import webdriver
from types import ClassMethodDescriptorType
from bs4 import BeautifulSoup
import requests
import time
import random
driver = webdriver.Chrome()


f = open("data.txt", "a")


email = "vchatur12345@gmail.com"
password = "chatur0987"


git = "jagritx"
hacker = "jagritx"
chef = "jagritx"

header = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_5_2) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.2 Safari/605.1.15',
}

gitstats = f'https://github-readme-stats.vercel.app/api?username={git}&count_private=true'
gitlangs = f'https://github-readme-stats.vercel.app/api/top-langs/?username={git}'
hackerrank = f'https://www.hackerrank.com/profile/{hacker}'
codechef = f'https://www.codechef.com/users/{chef}'

# linkedinscraper
actions.login(driver, email, password)
person = Person(
    "https://www.linkedin.com/in/jagritkamra/", driver=driver)

print(person, file=f)


# githup scraper
gitsource = requests.get(gitstats, headers=header).text
langsource = requests.get(gitlangs, headers=header).text


soup = BeautifulSoup(gitsource, 'lxml')
langsoup = BeautifulSoup(langsource, 'lxml')


countlist = []
langlist = []
if(soup.findAll('text', class_='stat')):
    for field in soup.findAll('text', class_='stat'):
        countlist.append(field.text)

if(langsoup.findAll('text', class_='lang-name')):
    for language in langsoup.findAll('text', class_='lang-name'):
        langlist.append(language.text)
print("Github stats", file=f)
print(countlist, file=f)
print("Github languages", file=f)
print(langlist, file=f)


# hackerrank scraper
hackersource = requests.get(hackerrank, headers=header).text
soup = BeautifulSoup(hackersource, 'lxml')

certificatelist = []
badgelist = []
badgedata = []
i = 0

if(soup.find('div', class_='hacker-certificates')):
    for certificates in soup.find('div', class_='hacker-certificates'):
        certificatelist.append(certificates.h2.text)

if(soup.find('div', class_='badges-list')):
    for badges in soup.find('div', class_='badges-list'):
        for bas in badges.find_all('svg', class_='badge-star'):
            i += 1
        badgedata.append(i)
        i = 0
        badgelist.append(badges.text)
print("Certificates", file=f)
print(certificatelist, file=f)
print("Badges", file=f)
print(badgelist, file=f)
print(badgedata, file=f)


# codechef scraper

chefsource = requests.get(codechef, headers=header).text
soup = BeautifulSoup(chefsource, 'lxml')

rating = 0
if (soup.find('div', class_='rating-number').text):
    rating = soup.find('div', class_='rating-number').text

ccrating = "Codechef:"+rating
print(ccrating, file=f)
print('\n', file=f)
print('\n', file=f)
