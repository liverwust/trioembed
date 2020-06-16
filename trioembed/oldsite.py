import requests
from bs4 import BeautifulSoup
from trioembed import BaseEmbedder


SOURCE_URL = "https://psutriangle.org/actives/"


class OldSiteEmbedder(BaseEmbedder):
    """Embed the psutriangle.org Brotherhood page.

    This overrides methods in BaseEmbedder, and should be used following the
    lifecycle sequence documented there.

    There are header and footer elements which need to be removed from this
    page. This is done by extracting the <section> with id=content from the
    middle of the page, promoting it to a top-level <body> element, and then
    removing everything outside of it.
    """

    def __init__(self, *args, **kwargs):
        super(OldSiteEmbedder, self).__init__(*args, **kwargs)
        self.url = SOURCE_URL

    def width(self):
        # this is a hard limit until i get reflow working properly
        if self.maxwidth == None:
            # oh boy!
            return 10000
        elif self.maxwidth < 778:
            raise ValueError("page must be at least 778 pixels wide")
        else:
            return self.maxwidth

    def height(self):
        if self.maxheight == None:
            # oh boy!
            return 10000
        else:
            # this should be properly calculated, but...
            return min(self.maxheight, 10000)

    def html(self):
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
