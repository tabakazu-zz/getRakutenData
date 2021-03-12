from bs4 import BeautifulSoup
class Mybs4():
    #def __init__(self,html):
        #self.soup = BeautifulSoup ( html, "html.parser" )
    def set_html(self,html):
        self.soup=BeautifulSoup(html,"html.parser")

    def selectCSS(self,CSS):
        self._selectedItems=[n for n in self.soup.select(CSS)]
        return self._selectedItems

    def select_text(self, elem, CSS):
        ans = elem.select( CSS ).get_text ()
        if not ans == None:
            return ans
        else:
            return 'None'

    def select_one_text(self,elem,CSS):
        try:
            ans=elem.select_one(CSS).get_text()
            return ans
        except AttributeError:
            return 'None'

    def select_one_getAttribute(self,elem,CSS,attr):
        ans=elem.select_one(CSS).get(attr)
        if not ans==None:
            return ans
        else:
            return 'None'