# download_kifu24

## Overview
将棋倶楽部２４の棋譜検索から指定ユーザの棋譜をダウンロードします。

## Requirement
- macOS Catalina 10.15.7
- Python 3.9.5
- pip 21.1.1
- selenium 3.141.0
- google-chrome 91.0.4472.77
- chromedriver 90.0.4430.24

## Setup
python はインストールされている前提です。

1. git clone
```
git clone ...
cd download_kifu24
pip install -r requirements.txt
```

2. ChromeDriver をインストール
```
brew update
brew install selenium-server-standalone
brew install chromedriver --cask
```

## Usage
1. ログインユーザ設定<br>
環境変数 or .env ファイルで設定します。
- 環境変数で設定
  - ログインユーザ
    ```
    LOGIN_USER_NAME=testuser
    ```
  - パスワード
    ```
    LOGIN_PASSWORD=testpass
    ```

- .env ファイルで設定
  プロジェクトディレクトリに .env ファイルを作成します。<br>
  ファイルに記載してください。
    ```
    LOGIN_USER_NAME=testuser
    LOGIN_PASSWORD=testpass
    ```

2. ダウンロードユーザを設定<br>
search_users.txt にユーザを記載してください。
```
test1
test2
test3
```

3. 実行
```
python3 download_kifu24.py
```
Chrome が起動して処理します。  

# Description
不具合は修正予定なしです。<br>
軽い動作確認しかしていないです。<br>
私も使用続けるので、気になったら修正します。<br>

## Reference
整理したら書くかも

## Author
akamaru7610

## Licence
none

