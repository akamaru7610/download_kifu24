import os
from os.path import join, dirname
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from dotenv import load_dotenv

"""
  ドライバ設定
"""
MY_DRIVER = webdriver.Chrome('chromedriver')
MY_DRIVER.implicitly_wait(10)
MY_DRIVER_WAIT = WebDriverWait(MY_DRIVER, 10)

"""
  将棋倶楽部２４コア情報
"""
URL_SYOGI_CLUB_24 = 'https://www.shogidojo.net/shogi24kifu/'

"""
  棋譜検索ログイン画面の要素
"""
ELEMENT_NAME_LOGIN_USER_NAME = 'uname'
ELEMENT_NAME_LOGIN_PASSWORD  = 'pwd'
ELEMENT_NAME_LOGIN_BUTTON    = 'submit-button'

"""
  棋譜検索メイン画面の要素
"""
ELEMENT_NAME_SEARCH_USER_NAME = 'name1'
ELEMENT_NAME_SEARCH_BUTTON    = 'searchbtn'
ELEMENT_ID_DOWNLOAD_BUTTON    = 'dlBtn'

"""
  ログインユーザ情報
"""
load_dotenv(verbose=True)
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

LOGIN_USER_NAME = os.environ.get("LOGIN_USER_NAME")
LOGIN_PASSWORD  = os.environ.get("LOGIN_PASSWORD")

"""
  検索ユーザ情報
"""
SEARCH_USERS_FILE = './search_users.txt'
f = open(SEARCH_USERS_FILE, 'r')
SEARCH_USER_LIST = f.readlines()

