import trioembed


class NaiveEmbedder(trioembed.BaseEmbedder):
    """Don't do any fancy heightxwidth calculations; just use the max"""

    def width(self):
        return self.maxwidth

    def height(self):
        return self.maxheight

    def html(self):
        # https://en.wikipedia.org/wiki/XHTML_Basic
        return """<?xml version="1.0" encoding="UTF-8"?>
               <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML Basic 1.1//EN"
               "http://www.w3.org/TR/xhtml-basic/xhtml-basic11.dtd">
               <html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en">
               <head>
               <title>Hello</title>
               </head>
               <body>
               <p>Hello <a href="http://example.org/">world</a>.</p>
               </body>
               </html>
               """


