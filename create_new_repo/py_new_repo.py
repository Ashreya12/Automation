import sys
from selenium import webdriver

name = sys.argv[1]

# Enter path to chromedriver.exe
browser = webdriver.Chrome(executable_path="path to chromedriver.exe")
browser.get('http://github.com/login')

login_user = browser.find_elements_by_xpath("//*[@id='login_field']")[0]
login_user.send_keys('username')  # Enter GitHub username
pass_user = browser.find_elements_by_xpath("//*[@id='password']")[0]
pass_user.send_keys('password')  # Enter GitHub password
login = browser.find_elements_by_xpath(
    "//*[@id='login']/form/div[3]/input[4]")[0]
login.click()
browser.get('https://github.com/new')
repo = browser.find_elements_by_xpath("//*[@id='repository_name']")[0]
repo.send_keys(name)
repo_button = browser.find_element_by_css_selector("button.first-in-line")
repo_button.submit()
# browser.quit()
