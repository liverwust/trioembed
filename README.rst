#######################
Triangle oEmbed wrapper
#######################

No matter how our new website is hosted (Squarespace or otherwise), we would
like it to embed a "digital composite" using names, pictures, and other
information from ChapterSpot. National requires that the undergraduates keep
ChapterSpot up-to-date, which means that the names & pictures on the website
will always be up-to-date as well.

The `ChapterSpot site`_ (actually just a demo for now) does not offer an
iframe-able version of the membership page, which necessitates web scraping
and manipulation of the rendered markup. This cannot be done in the web browser
due to the `same-origin policy`_ and must be done by a server-side app instead.

.. _ChapterSpot site: http://group9999.chapterspot.com/leaders
.. _same-origin policy: https://developer.mozilla.org/en-US/docs/Web/Security/Same-origin_policy
