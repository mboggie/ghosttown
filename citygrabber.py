#!/usr/bin/env python
import json
from mechanize import Browser
from bs4 import BeautifulSoup

mech = Browser()
url = "http://www.biggestuscities.com/top-1000" # originally from: http://www.biggestuscities.com/top-1000
page = mech.open(url)

html = page.read()
soup = BeautifulSoup(html)
#print(soup.table.prettify())
table = soup.find("table", 'table-condensed')
blob = []
for row in table.findAll('tr')[0:]:
    col = row.findAll('td')
    if col:
        rank = col[0].string.strip()
        city = col[1].find('a').text.strip()
        state = col[2].find('a').text.strip()
        pop = str(col[3].text.replace(',', '')).strip()
        #growth = col[4].span.text.strip()

        line = '{{"number" : {0}, "city": "{1}", "state" : "{2}", "pop" : {3}}}'.format(rank, city, state, pop)
        #print(line)
        blob.append(line)
        #list.append(entry)

print("[")
sep = ",\n"
print(sep.join(blob))
print("]")