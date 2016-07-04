# Vicemo Scraper

Kenny Kyunghoon Lee
kenny.k.lee@nyu.edu




## Introduction
1. Vicemo Scraper is a Python webscraper that collects data from [vicemo.com](http://www.vicemo.com/), which tracks real
, publicly available Venmo transactions involving drugs, booze, and sex, created by Mike Lacher and Chris Baker. 
This module automatically cleanses and analyzes the data to create a simple visualization on the what the most 
frequently mentioned words and emojis related to sex, alcohol and drugs are on Venmo on a real-time basis.
2. There are three .py files.
    * main.py
    * vicemo_scraper.py
    * visualization.py
2. There are five relevant classes.
    1. LetMeScrapeThat()    [vicemo_scraper.py]
    2. LetMeParseThat()     [vicemo_scraper.py]
    3. LetMeAnalyzeThat()   [vicemo_scraper.py]
    4. VicemoScraper()      [vicemo_scraper.py]
    5. LetMeVisualizeThat() [visualizedata.py]
3. [vicemo_scraper.py] is for the extraction of the data and analyzedata.py is for data analysis.
4. DEMO (gif file): http://g.recordit.co/kzrtUat1eH.gif

## Required External Dependencies
1. [Selenium webdriver](http://www.seleniumhq.org/projects/webdriver/) (An headless web browser)
2. [PhantomJS](http://phantomjs.org/)
    * Can be downloaded from http://phantomjs.org/download.html
    * The executable file MUST BE located in PATH (where Python Interpreter is located (virtualenv))
    * Necessary to obtain HTML codes of the website rendered by Javascript
3. BeautifulSoup (BS4)
4. matplotlib

## How to Run?
1. Make sure the dependencies are installed properly.
2. Place vicemo_scraper.py, visualizedata.py, and main.py in the same directory.
3. Run main.py
    * __NOTE:__ depending on your connection, it can take 15 - 30 seconds for the module to finish running. 
