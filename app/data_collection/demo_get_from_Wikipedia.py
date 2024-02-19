# install these two libraries
# pip3 install requests
# pip3 install BeautifulSoup

import requests
from bs4 import BeautifulSoup

names = dict()

response = requests.get(
	url="https://en.wikipedia.org/wiki/List_of_wealthiest_Americans_by_net_worth",
)
soup = BeautifulSoup(response.content, 'html.parser')

name_elements = soup.css.select('.mw-content-ltr.mw-parser-output table tr td:nth-of-type(2) a')

for name_element in name_elements:
    print(name_element.string)

