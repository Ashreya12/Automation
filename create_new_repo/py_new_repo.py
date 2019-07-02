import sys
from selenium import webdriver

reponame = sys.argv[1]
username = sys.argv[2]
password = sys.argv[3]

browser = webdriver.Chrome(executable_path="C:\Drivers\chromedriver.exe")
browser.get('http://github.com/login')

login_user = browser.find_elements_by_xpath("//*[@id='login_field']")[0]
login_user.send_keys(username)
pass_user = browser.find_elements_by_xpath("//*[@id='password']")[0]
pass_user.send_keys(password)
login = browser.find_elements_by_xpath(
    "//*[@id='login']/form/div[3]/input[4]")[0]
login.click()
browser.get('https://github.com/new')
repo = browser.find_elements_by_xpath("//*[@id='repository_name']")[0]
repo.send_keys(reponame)
repo_button = browser.find_element_by_css_selector("button.first-in-line")
repo_button.submit()
# browser.quit()
