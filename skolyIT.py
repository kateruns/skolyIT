import requests
from bs4 import BeautifulSoup

#adresa webu
url ="https://www.atlasskolstvi.cz/stredni-skoly?p=2&branchs=2087"

#request
r = requests.get(url)
#print(r)

#soup
data = BeautifulSoup(r.text, 'html.parser')

#h2
table = data.find_all("h2")
print(table)