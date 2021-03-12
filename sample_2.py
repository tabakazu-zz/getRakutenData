#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#https://hk29.hatenablog.jp/entry/2020/04/30/224711->再起的にhtml又はmhtmlで自動保存する
import os, sys
import requests
import xml.dom.minidom
import xml.etree.ElementTree as ET
from selenium import webdriver
# import codecs
import pyautogui  # GUI操作
import pyperclip  # クリップボード操作
import time


def get_url(myurl, target_str, file_name):  # xmlファイルからurlをゲッツする関数
    # 指定URLからデータをファイルに保存する
    res = requests.get ( myurl )
    with open ( file_name + '.xml', mode='w' ) as f:
        f.write ( res.text )

    # 保存したxmlファイルを読み込む
    dom = xml.dom.minidom.parse ( file_name + '.xml' )  # or xml.dom.minidom.parseString(xml_string)
    xml_string = dom.toprettyxml ()
    print ( xml_string )

    # XMLをパースする
    root = ET.fromstring ( xml_string )
    url_list = []
    for i, child in enumerate ( root ):
        # print(child.tag, child.attrib) # タグと属性の取得
        url = root[i][0].text  # 要素へのアクセス（url取得）
        url_list.append ( url )

    # urlに[target_str]があるものだけ残す
    url_list2 = [myurl for myurl in url_list if target_str in myurl]

    return url_list2


def save_html(options, myurl):  # Chromeブラウザで開いたwebページをファイルに保存する関数
    driver = webdriver.Chrome ( 'chromedriver.exe', chrome_options=options )
    driver.set_window_size ( 1024, 768 )
    driver.set_window_position ( 0, 0 )
    driver.get ( myurl )
    time.sleep ( 5 )

    # open 'Save as...' to save html and assets
    pyautogui.hotkey ( 'ctrl', 's' )
    time.sleep ( 1 )
    pyautogui.hotkey ( 'Home' )
    time.sleep ( 1 )
    # https://teratail.com/questions/79973
    # C:\Users\[USER]\Anaconda3\Lib\site-packages\pyautogui
    pyperclip.copy ( os.getcwd () )  # パスに日本語が入ってる場合の対策。クリップボードにコピー
    pyautogui.hotkey ( 'ctrl', 'v' )
    time.sleep ( 1 )
    pyautogui.typewrite ( '\\' )
    pyautogui.hotkey ( 'tab' )  # 「ファイルの種類」へ移動
    if save_file_type == 'mhtml':
        time.sleep ( 1 )
        pyautogui.press ( "down" )  # プルダウンを開く
        time.sleep ( 1 )
        pyautogui.press ( "up" )  #
        pyautogui.press ( "up" )  #
        pyautogui.press ( "down" )  # 「1つのファイル(*.mhtml)」を選択
        time.sleep ( 1 )
        pyautogui.hotkey ( 'enter' )  # 選択する
        time.sleep ( 1 )
    pyautogui.hotkey ( 'tab' )  # 「保存」へ移動
    pyautogui.hotkey ( 'enter' )  # 保存する
    time.sleep ( 6 )
    driver.close ()


def main():
    #      読み出すURL, 抽出したいURLに含まれる文字列, 保存するファイル名
    URL_list = get_url ( URL, 'month', 'sitemap' )  # 月別のurlリストをゲッツ

    for n, myurl in enumerate ( URL_list ):
        get_url_list = get_url ( myurl, 'entry', str ( n ) )  # 各記事のurlリストをゲッツする
        print ( get_url_list )

        options = webdriver.ChromeOptions ()
        options.add_experimental_option ( "prefs", {
            # "download.default_directory": r"./save_html",
            "download.prompt_for_download": False,
            "download.directory_upgrade": True,
            "safebrowsing.enabled": True
        } )
        for myurl_sub in get_url_list:  # 取得した月別サイトマップを巡回してwebページを保存する
            print ( myurl_sub )
            save_html ( options, myurl_sub )
            sys.exit ()  # 動作確認のためひとつだけDLする用。ループ一回目で強制終了


if __name__ == '__main__':
    URL = 'https://hk29.hatenablog.jp/sitemap.xml'
    save_file_type = 'mhtml'  # mhtml

    main ()