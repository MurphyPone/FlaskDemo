from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

# site to be scraped
url = 'https://www.dictionary.com/wordoftheday/'

# initialize/open web client
uClient = uReq(url)
page_html = uClient.read() # snag the HTML
uClient.close() # just like a scanner, close that stuff

page_soup = soup(page_html, "html.parser") # use bs4 to parse page_html using its "html.parser"

# find specific items containers to scrape
container = page_soup.findAll("div", {"class":"definition-box"})
word = container[0].strong.text

# get all definition
definitions = []
definitions_html = container[0].findAll("ol")
definitions_html = definitions_html[0].findAll("li")
for definition in definitions_html:
    definitions.append(definition.text)

# method which returns the packaged contents we want to send elsewhere
def getWord():
    result = [word]
    for defn in definitions:
        result.append(defn)
    return result
