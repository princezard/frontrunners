from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from bs4 import BeautifulSoup as bs
from PIL import Image
import requests
import time
import pandas as pd
import numpy as np
df = pd.read_csv('C:/Users/LEVEL51PC/Desktop/Essex/Frontrunner/premierleague/data_no_nan.csv')
df.drop(df.columns[0],axis=1,inplace=True)

def get_images(url:str) -> str:
    a=requests.get(url)
    content = bs(a.content)
    try:
        return content.select("div.articleImage img")[0]['src']
    except:
        return np.nan

def get_tags(url:str) -> str:
    a=requests.get(url)
    content = bs(a.content)
    try:    
        return content.select("div.articleImage img")[0]['alt']
    except:
        return np.nan

def clear_whitespaces(string:str) -> str:
    l = string.split(',')
    return ','.join([s.strip() for s in l])

# df['images_url'] = df['links_url'].apply(get_images)
# df['uncleaned_tags'] = df['links_url'].apply(get_tags)
# df['tags'] = df['uncleaned_tags'].apply(strip_list)
# df.to_csv('data.csv')
# df=pd.read_csv('C:/Users/LEVEL51PC/Desktop/Essex/Frontrunner/premierleague/data.csv')
# df.drop(df.columns[0],axis=1,inplace=True)
# df.dropna(inplace=True)
# df.to_csv('C:/Users/LEVEL51PC/Desktop/Essex/Frontrunner/premierleague/data_no_nan.csv')
