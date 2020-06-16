import json


class BaseEmbedder:
    """Abstract base class for Embedders.

    An Embedder converts the markup obtained from a particular page to a
    "rich"-type oEmbed response. Depending on the expected content, subclasses
    may add or subtract certain page elements, introduce new stylesheets or
    scripts, and so on.

    Do not instantiate this class directly but use its subclasses. Follow this
    lifecycle sequence:
    1) instantiate a subclass, which usually requires HTTPS response text
    2) assign values to x.maxwidth and x.maxheight based on the oEmbed request
       (which will have been provided as URL query / GET attributes)
       Note: None is an acceptable value, but only if *both* W and H are None
    3) call x.respond(), which will provide a JSON text block ready to be sent
       back to the consumer

    Subclasses should respect self.maxwidth and self.maxheight, which are
    provided by the oEmbed consumer as absolute bounds on the space available.
    These are considered to be infinite if None. Subclasses should override
    these instance methods:

    width() --  calculate the actual width required to properly display the
                embedded page
    height() -- same, but for height
    html() -- provide the XHTML 1.0 Basic markup which will be provided

    See: https://www.oembed.com/
    """

    def __init__(self):
        self._got_maxwidth, self._got_maxheight = False, False
        self._maxwidth, self._maxheight = None, None

    @property
    def maxwidth(self):
        if self._got_maxwidth:
            return self._maxwidth
        else:
            raise ValueError("maximum width was not yet defined")

    @maxwidth.setter
    def maxwidth(self, value):
        if value == None:
            if self._got_maxheight and self._maxheight != None:
                raise ValueError("both dimensions must be None, not just one")
        self._maxwidth = value
        self._got_maxwidth = True

    @property
    def maxheight(self):
        if self._got_maxheight:
            return self._maxheight
        else:
            raise ValueError("maximum height was not yet defined")

    @maxheight.setter
    def maxheight(self, value):
        if value == None:
            if self._got_maxwidth and self._maxwidth != None:
                raise ValueError("both dimensions must be None, not just one")
        self._maxheight = value
        self._got_maxheight = True

    def width(self):
        raise NotImplementedError("subclasses must override width")

    def height(self):
        raise NotImplementedError("subclasses must override height")

    def html(self):
        raise NotImplementedError("subclasses must override html")

    def respond(self):
        if self._got_maxwidth and self._got_maxheight:
            obj = {
                    "version": "1.0",
                    "type": "rich",
                    "html": self.html(),
                    "width": self.width(),
                    "height": self.height()
            }
            json_str = json.dumps(obj)
            return json_str
        else:
            raise RuntimeError("both maxwidth and maxheight must be defined")
