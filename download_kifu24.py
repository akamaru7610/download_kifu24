import settings
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

MY_DRIVER      = settings.MY_DRIVER
MY_DRIVER_WAIT = settings.MY_DRIVER_WAIT

def main():
    """
      将棋倶楽部２４棋譜検索から指定ユーザの棋譜をダウンロードします。
    """
    try:
        MY_DRIVER.get(settings.URL_SYOGI_CLUB_24)
        login_shogiclub24()

        for search_user_name in settings.SEARCH_USER_LIST:
            if search_user_name == "":
                continue
            download_kifu_file(search_user_name)

    # NOTE: Exception 指定は良くないらしい
    # TODO: 期待する例外を指定する
    except Exception as e:
        print("例外args:", e.args)
        MY_DRIVER.close()
        MY_DRIVER.quit()
    else:
        MY_DRIVER.close()
        MY_DRIVER.quit()

def login_shogiclub24():
    """
      棋譜検索にログインします。
    """
    MY_DRIVER.find_element_by_name(settings.ELEMENT_NAME_LOGIN_USER_NAME)\
        .send_keys(settings.LOGIN_USER_NAME)
    MY_DRIVER.find_element_by_name(settings.ELEMENT_NAME_LOGIN_PASSWORD)\
        .send_keys(settings.LOGIN_PASSWORD)
    MY_DRIVER.find_element_by_class_name(settings.ELEMENT_NAME_LOGIN_BUTTON)\
        .click()

def download_kifu_file(search_user_name):
    """
      引数:ユーザの棋譜ファイルをダウンロードします。
    """
    # 初期値(ログインユーザ)をクリアする
    MY_DRIVER.find_element_by_name(settings.ELEMENT_NAME_SEARCH_USER_NAME)\
        .clear()
    MY_DRIVER.find_element_by_name(settings.ELEMENT_NAME_SEARCH_USER_NAME)\
        .send_keys(search_user_name)
    # WARNNIG: 検索ボタンを押していないのに押したような動作をしているため、コメントアウト
    #          原因は調査していない
    # MY_DRIVER_WAIT.until(expected_conditions\
    #     .element_to_be_clickable((By.NAME, settings.ELEMENT_NAME_SEARCH_BUTTON)))
    MY_DRIVER.find_element_by_id(settings.ELEMENT_ID_DOWNLOAD_BUTTON)\
        .click()
    # ファイルのダウンロード完了待ちの設定
    # TODO: ファイル監視する実装があるので、対応したい
    sleep(15)

if __name__ == "__main__":
    main()

