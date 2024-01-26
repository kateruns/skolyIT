import requests
from bs4 import BeautifulSoup
import pandas as pd

#adresa webu
url ="https://www.atlasskolstvi.cz/stredni-skoly?p=2&branchs=2087"

#request
r = requests.get(url)


#soup
data = BeautifulSoup(r.text, 'html.parser')

#print(data.prettify())

#  <div class="leftcol">
#      <ul class="schoollist cols1">
#       <li>
#        <a href="/ss440-integrovana-stredni-skola-technicka-a-ekonomicka-sokolov-prispevkova-organizace"><img alt="Integrovaná střední škola technická a ekonomická Sokolov, příspěvková organizace" src="/data/img/fotogalerie/ss/0440/logo/0440.png"/>
#         <h2>Integrovaná střední škola technická a ekonomická Sokolov, příspěvková organizace</h2>
#         <article> Jednoty 1620, 356 01 Sokolov </article>
#        </a>
#       </li>


#najít název školy na webu
div = data.find("div", class_="leftcol")
nazev = div.find_all('h2')
#print(nazev)

#najít adresy
adresa = div.find_all('article')
print(adresa)

#uděláme z prázdného seznamu seznam názvů škol
names = []
for i in nazev:
    name=i.text
    names.append(name)
print(names)


#uděláme z prázdného seznamu seznam adres
ads = []
for i in adresa:
    ad=i.text
    ads.append(ad)
print(ads)

#do tabulky
table = {
  "Název školy": names,
  "Adresa": ads
}

df=pd.DataFrame(table, index=pd.RangeIndex(start=1, stop=21, name='ID'))
print(df)


#tabulku do excelu, doinstalovat modul openpyxl, jinak nefunguje
df.to_excel("skolyIT.xlsx")
print("hotovo")