from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from bs4 import BeautifulSoup as bs
from PIL import Image
import requests
import time

driver_path = 'C:\Program Files (x86)\chromedriver.exe'
brave_path = 'C:\Program Files\BraveSoftware\Brave-Browser\Application/brave.exe'
option = webdriver.ChromeOptions()
option.binary_location = brave_path
# option.add_argument("--incognito") OPTIONAL
# option.add_argument("--headless") OPTIONAL

# Create new Instance of Chrome
driver = webdriver.Chrome(executable_path=driver_path, chrome_options=option)

r = driver.get("https://www.premierleague.com/news")
wait = WebDriverWait(driver, 10)
wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"._2hTJ5th4dIYlveipSEMYHH.BfdVlAo_cgSVjDUegen0F.js-accept-all-close")))
time.sleep(3)
driver.find_element_by_css_selector("._2hTJ5th4dIYlveipSEMYHH.BfdVlAo_cgSVjDUegen0F.js-accept-all-close").click()

SCROLL_PAUSE_TIME = 0.75

# Get scroll height
last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    print(len(driver.find_elements_by_css_selector("span.image.thumbCrop-news-list img")))
    if len(driver.find_elements_by_css_selector("span.image.thumbCrop-news-list img")) >= 1000:
        driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.HOME)
        break
    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Wait to load page
    time.sleep(SCROLL_PAUSE_TIME)

    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height

# r = requests.get("https://www.premierleague.com/news")
webpage = bs(r.content)

images = webpage.select("span.image.thumbCrop-news-list img")
images_url = [image['src'] for image in images]

for i in range(len(images_url)):
    try:
        img = Image.open(requests.get(images_url[i],stream=True).raw)
        img.save(f"pic_{i+1}.jpg")
    except Exception as e:
        print("Picture Index:",i)
        print(e)