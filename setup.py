from setuptools import setup, find_packages

setup(
    name="catifier",
    version="0.1",
    packages=find_packages(),

    # Project uses reStructuredText, so ensure that the docutils get
    # installed or upgraded on the target machine
    install_requires=["instagram-scraper", "opencv-python", "pillow"],

    package_data={
        # If any package contains *.txt or *.rst files, include them:
        # "": ["*.txt", "*.rst"],
        # And include any *.msg files found in the "hello" package, too:
        "catifier": ["resources/*.png", "resources/*.xml"],
    },

    # metadata to display on PyPI
    # author="Me",
    # author_email="me@example.com",
    # description="This is an Example Package",
    # keywords="hello world example examples",
    # url="http://example.com/HelloWorld/",   # project home page, if any
    # project_urls={
    #     "Bug Tracker": "https://bugs.example.com/HelloWorld/",
    #     "Documentation": "https://docs.example.com/HelloWorld/",
    #     "Source Code": "https://code.example.com/HelloWorld/",
    # }

    # could also include long_description, download_url, etc.
)