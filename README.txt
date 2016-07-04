Vice Analyzer -- tracking people's payments for "shady" activities on Venmo

Kenny Kyunghoon Lee
KL1214@nyu.edu

Introduction
    1. This program is a webscraper and data visualizer that extracts the public data on supposed transactions for
       narcotics, alcohols, and prostitution on Venmo. It extracts the data from vicemo.com and creates bar graphs to
       show what are the most commonly mentioned substance related words and emojis mentioned in Venmo transactions.
    2. Currently, there are four classes in the packagae
        1. LetMeScrapeThat()    [vicemo_scraper.py] [line 7]
        2. LetMeParseThat()     [vicemo_scraper.py] [line 40]
        3. LetMeAnalyzeThat()   [vicemo_scraper.py] [line 71]
        4. VicemoScraper()      [vicemo_scraper.py] [line 119]
        5. LetMeVisualizeThat() [visualizedata.py]  [line 3]
    3. [vicemo_scraper.py] is for the extraction of the data and analyzedata.py is for data analysis.
    4. DEMO (gif file): http://g.recordit.co/kzrtUat1eH.gif

Required External Dependencies
    1. Selenium webdriver (external module)
    2. PhantomJS
        -- Can be downloaded from http://phantomjs.org/download.html
        -- The executable file MUST BE located in PATH (where Python Interpreter is located (virtualenv))
        -- Necessary to obtain HTML codes of the website rendered by Javascript
    3. BeautifulSoup (BS4)
    4. matplotlib

How to Run?
    1. Make sure the dependencies are installed properly
    2. Place vicemo_scraper.py, visualizedata.py, and main.py in the same directory
    3. Run main.py
