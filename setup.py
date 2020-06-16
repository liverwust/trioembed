import setuptools

with open("README.rst", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="trioembed-liverwust",
    version="0.0.1",
    author="Louis Wust",
    author_email="louiswust@fastmail.fm",
    description="Triangle oEmbed wrapper",
    long_description=long_description,
    long_description_content_type="text/x-rst",
    url="https://github.com/liverwust/trioembed",
    packages=setuptools.find_packages(),
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.8",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content :: CGI Tools/Libraries",
    ],
    python_requires='>=3.8',
    install_requires=[
        "requests",
        "beautifulsoup4",
    ],
)
