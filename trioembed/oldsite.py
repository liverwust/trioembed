from bs4 import BeautifulSoup
import requests


SOURCE_URL = "https://psutriangle.org/actives/"


class OldSiteEmbedder:
    """Embed the psutriangle.org Brotherhood page"""

    def __init__(self):
        self.url = SOURCE_URL

    def go(self):
        r = requests.get(self.url)
        soup = BeautifulSoup(r.text, 'html.parser')

        # section#content contains the undergraduate names and pictures in
        # a 900px-wide table with four columns
        body = soup.find('body')
        the_undergrads = soup.find('section', id='content').extract()
        # remove everything that comes before and after the content (page
        # header, footer, extra panes, etc.), and then restore
        # section#content all by itself
        body.clear()
        body.append(the_undergrads)

        return str(soup)
