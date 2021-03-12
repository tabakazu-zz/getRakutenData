import configparser
import logging.config
from myClass.cl_getDriver import GetDriver_Selenium
from myClass.cl_Parse import Mybs4
# TODO：楽天にログイン
# TODO；検索ワードで検索
# TODO:Data取得
# TODO:データ定義：DataClasses

#setting_config
config=configparser.ConfigParser()
config.read('./config.ini',encoding='utf-8') # パスの指定が必要です

#logging設定
logging.config.fileConfig('./logging.conf')
logger=logging.getLogger()

#ログイン処理
sDriver=GetDriver_Selenium()

sDriver.getdriver('https://www.rakuten.co.jp/')
loginbtnPath="//li[@class='section--1itbn'][2]/button[@class='button--laCfj type-primary--2_qVU size-xs--2sO5U size-xs-padding--SsiSC border-radius--3mPQW']/span[@class='text--1zvJD text-no-margin-right--3_FQT']"

sDriver.clickxpath(loginbtnPath)

sDriver.sendkey_xpath("//input[@id='loginInner_u']",config['Rakuten']['ACCESS_KEY'])
sDriver.sendkey_xpath("//td[@class='loginBoxValue']/input[@id='loginInner_p']",config['Rakuten']['ACCESS_PASS'])
sDriver.clickxpath("//div[@id='loginInner']/p[1]/input[@class='loginButton']")

#search_Word入力
searchWord="米"
sDriver.sendkey_xpath('//*[@id="common-header-search-input"]',searchWord)
sDriver.clickxpath('//div[@class="icon--2sY_j common-search--15EUB"]')

#スーパーSALE割引のクリック
sDriver.clickxpath("//form[@class='dui-form']/div[@class=' groupedfields']/div[@class='dui-list field'][1]/label[@class='item']/input")

while True:
    #テキスト取得
    html=sDriver.get_PageSources()
    mySoup=Mybs4()
    mySoup.set_html(html)
    itemlist=mySoup.selectCSS_text('div.dui-card')
    print(itemlist)


    if sDriver.clickxpath("//a[@class='item -next nextPage']"):
        pass
    else:
        break

sDriver.QuitDriver()