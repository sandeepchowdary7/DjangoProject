import selenium
import time
from selenium.webdriver.common.keys import Keys
import requests

driver = selenium.webdriver.Chrome('chromedriver')

driver.get('https://www.instagram.com/accounts/login/?source=auth_switcher')
time.sleep(3)

user = driver.find_element_by_name('username')
pasword = driver.find_element_by_name('password')

user.send_keys('rosaconndev')
time.sleep(1)
pasword.send_keys('gond2lupt-co1BASS')
time.sleep(1)
pasword.send_keys(Keys.RETURN)
time.sleep(3)
first_not_now_btn = driver.find_element_by_xpath("//*[text()='Not Now']")
first_not_now_btn.click()
time.sleep(3)
second_not_now_btn = driver.find_element_by_xpath("//*[text()='Not Now']")
second_not_now_btn.click()

# users = ["natarajan_jayaprakash", "narendramodi", "virat.kohli"]
users = ["natarajan_jayaprakash", "narendramodi"]

for user in users:
    driver.get('https://www.instagram.com/' + user + '/')
    time.sleep(2)
    followButton = driver.find_element_by_css_selector('button')
    followButton.click()

    img_src = driver.find_element_by_xpath('//div/img').get_attribute("src")
    print('img:', img_src)

    r = requests.get(img_src)

    fp = open('image.jpg', 'wb')  # it has to be `bytes` mode
    fp.write(r.content)  # it has to be `r.content, not `r.text`
    fp.close()

# driver.close()
