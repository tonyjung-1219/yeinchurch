from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from PIL import Image

options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('window-size=1920x1080')
options.add_argument("disable-gpu")

# 유의: chromedriver를 위에서 받아준 
# chromdriver(windows는 chromedriver.exe)의 절대경로로 바꿔주세요!
driver = webdriver.Chrome('/home/tonyjung1219/vscodepython/chromedriver', chrome_options=options)

driver.get('https://yeinch.com/includes/social/login_page.php')
driver.implicitly_wait(3)
driver.get_screenshot_as_file('yeinchlogin_main.jpg')

driver.quit()
