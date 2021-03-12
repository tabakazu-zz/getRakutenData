from bs4 import BeautifulSoup
from myClass.cl_getDriver import GetDriver_Selenium
from myClass.cl_Parse import Mybs4
from myClass.cl_dataclasses import ItemData
from dataclass_csv import DataclassWriter

class Main():
    def set_SearchWord(self,searchWord):
        self.searchWord=searchWord
    def set_URL(self,URL):
        self.URL=URL
    def start(self) -> object:
        myURL=self.URL
        sDriver = GetDriver_Selenium ()
        sDriver.getdriver (myURL)
        # print(html)
        soup = Mybs4 ()

        while True:
            itemDatas = []
            html = sDriver.get_PageSources ()
            soup.set_html(html)
            box=soup.selectCSS( 'div[class="dui-card searchresultitem"]')
            #soup = BeautifulSoup ( html, "html.parser" )
            #box = soup.select ( 'div[class="dui-card searchresultitem"]' )

            for elem in box:
            #itemtitle
                itemData=ItemData(
                    soup.select_one_text ( elem, "div[class='content title']>h2" ), #itemtitle
                    soup.select_one_getAttribute ( elem, "a", 'href' ), #url
                    soup.select_one_text ( elem, "div[class='content description price']" ), #price
                    soup.select_one_text(elem,'a[class="dui-rating-filter _link"]') # rate
                    )
                itemDatas.append ( itemData )
                """
                    itemtitle=soup.select_one_text(elem, "div[class='content title']>h2")
                    print(itemtitle)
                    #url
                    itemUrl=soup.select_one_getAttribute(elem,"a",'href')
                    print(itemUrl)
                    #price
                    itemPrice=soup.select_one_text(elem,"div[class='content description price']")
                    print(itemPrice)
                    #itemRate
                    itemRate=soup.select_one_text(elem,'a[class="dui-rating-filter _link"]')
                    print(itemRate)
                """



                    #print(itemDatas)

            with open(f"./rakuten_item_{self.searchWord}.csv","a") as f:
                w=DataclassWriter(f,itemDatas,ItemData)
                w.write()


            if sDriver.clickxpath ( "//a[@class='item -next nextPage']" ):
                pass
            else:
                break

        sDriver.QuitDriver ()

if __name__=="__main__":
    import sys
    args=sys.argv
    searchWord=args[1]
    url=args[2]
    main=Main()
    main.searchWord=searchWord
    #main.set_SearchWord('つや姫')
    main.set_URL(url)
    main.start()






