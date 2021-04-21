#!/usr/bin/env python3
import requests, bs4

res = requests.get('https://notpurple.com')
res.raise_for_status()
noStarchSoup = bs4.BeautifulSoup(res.text, 'html.parser')
type(noStarchSoup)

elems = noStarchSoup.select('a')
elems2 = noStarchSoup.select('title')
print(elems)
print(elems2)
