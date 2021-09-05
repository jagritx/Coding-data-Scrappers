from linkedin_scraper import Person, actions
from selenium import webdriver
driver = webdriver.Chrome()

email = "vchatur12345@gmail.com"
password = "chatur0987"
# if email and password isnt given, it'll prompt in terminal
actions.login(driver, email, password)
person = Person(
    "https://www.linkedin.com/in/vipransh-agarwal", driver=driver)
print(person)
