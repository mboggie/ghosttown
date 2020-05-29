#!/usr/bin/env python
from mechanize import Browser
from bs4 import BeautifulSoup

mech = Browser()
url = "http://www.biggestuscities.com/top-1000" # originally from: http://www.biggestuscities.com/top-1000
page = mech.open(url)

html = page.read()
soup = BeautifulSoup(html)
table = soup.find("table", 'table-condensed')

for row in table.findAll('tr')[0:]:
    col = row.findAll('td')
    rank = col[0].string
    city = col[1].find('a').text.split('\n')[0]
    state = col[2].find('a').text
    population = str(col[3].text.replace(',', ''))
    growth = col[4].text.replace(',', '')

    row = (rank, city, state, population, growth)
    sep = ','
    print (sep.join(row))