import re
from selenium import webdriver
from bs4 import BeautifulSoup
from time import sleep


class LetMeScrapeThat(object):
    """
    Using Selenium Webdriver and PhantomJS, we simulate opening the actual website to let
    javascript render the target website and update all html codes containing data that we want to extract.
    """
    def __init__(self):
        print("Accessing data.")
        self.phantom_webpage = webdriver.PhantomJS()
        self.phantom_webpage.set_window_size(1120, 550)

    def scrape_vicemo(self, link, howmany = 100):
        self.phantom_webpage.get(link)
        print('Visiting the data source: {}'.format(link))
        print("Please, wait.")
        sleep(2)  # We make the scraper wait until the website loads completely
        for int in range((howmany // 100)-1):
            # each "scroll" yields 100 transactions on Venmo; the web driver has to sleep so that all data can load
            self.phantom_webpage.execute_script("window.scrollTo(0, 10000);")
            sleep(2)

        # from the phantom_webpage, find all web elements with the class "transaction" and returns the outcome
        # as a list variable "webele". "howmany" controls the number of observed transactions being extracted.
        webele = self.phantom_webpage.find_elements_by_class_name("transaction")[:howmany + 1]

        # enter list comprehension to extract the HTML codes from each web element
        self.transactions = [ele.get_attribute("innerHTML") for ele in webele]
        self.datalength = len(self.transactions)
        # shuts down the phantom webpage
        self.phantom_webpage.quit()

class LetMeParseThat(object):
    """
    Using BeautifulSoup, we parse the html extracted from web elements
    """
    def __init__(self,list_of_html):
        print("Parsing data.")
        self.soup_list = [BeautifulSoup(html, "html.parser") for html in list_of_html]
        self.desc_tags_compiler =[soup_ele.find_all('div',attrs={'class':'description'}) for soup_ele in self.soup_list]

    def extract_string_data(self):
        # extracts strings from the <div> tags with class="description"
        self.string_compiler = [soup_ele.find('div', attrs={'class':'description'}).string
                                for soup_ele in self.soup_list
                                if soup_ele.find('div', attrs={'class':'description'}).string]

    def extract_emoji_data(self):
        # extracts emojis from the <span> tags with class="emoji emoji-sizer"
        self.emoji_compiler = []
        for soup_ele in self.soup_list:
            for span in soup_ele.find_all('span', attrs={'class':['emoji','emoji-sizer']}):
                self.emoji_compiler.append(span['title'])

class LetMeAnalyzeThat(object):
    common_english_words = ['the',	'be', 'to', 'of', 'and', 'a', 'in', 'that', 'have', 'I', 'it', 'for', 'not', 'on',
                         'with', 'he', 'as', 'you',	'do', 'at', 'this', 'but', 'his', 'by', 'from', 'they', 'we', 'say',
                         'her', 'she', 'or', 'an', 'will', 'my', 'one', 'all', 'would', 'there', 'their', 'what', 'so',
                         'up', 'out', 'if',	'about', 'who',	'get', 'which', 'go', 'me', 'when', 'make', 'can', 'like',
                         'time', 'no', 'just', 'him', 'know', 'take', 'people', 'into', 'year', 'your', 'good', 'some',
                         'could','them', 'see', 'other', 'than', 'then', 'now', 'look', 'only', 'come', 'its', 'over',
                         'think', 'also', 'back', 'after', 'use', 'two', 'how',	'our', 'work', 'first',	'well',	'way',
                         'even', 'new',	'want', 'because', 'any', 'these', 'give', 'day', 'most', 'us', '']
    def __init__(self):
        print("Analyzing data.")
        pass

    def analyze_string_data(self, string_data):
        """
        takes a list made up of phrases of strings, cleanses them and adds to vice_compiler
        creates a dictionary of unique words and counts their occurances
        """
        vice_compiler = []
        for ele in string_data:
            for word in ele.split():
                # cleanse the word using Regular expression and string methods
                regex = re.compile('[^a-zA-Z]')
                cleansed_word = regex.sub('',word.lower().rstrip())
                vice_compiler.append(cleansed_word)
        # creates a dictionary of unique words with zero initial count
        # drop the word in the dictionary if it is just a useless common English word
        self.vice_str_dict = {key : 0 for key in set(vice_compiler) if key not in self.common_english_words}

        for ele in vice_compiler:
            if ele in self.vice_str_dict:
                self.vice_str_dict[ele] += 1
        return self.vice_str_dict

    def analyze_emoji_data(self, emoji_data):
        """
        takes a list of strings (names of the emojis), creates a dictionary of unique strings and counts occurences
        """
        # creates a dictionary of unique emojis with zero initial count
        self.vice_emoji_dict = {key : 0 for key in set(emoji_data)}
        for ele in emoji_data:
            if ele in self.vice_emoji_dict:
                self.vice_emoji_dict[ele] += 1
        return self.vice_emoji_dict

class VicemoScraper(object):
    def __init__(self, link):
        print("Starting the Scraper.")
        # commence scraping
        # set up a Scraper instance that uses LetMeScrapeThat class
        self.scraper = LetMeScrapeThat()
        self.scraper.scrape_vicemo(link, howmany=300)

    def get_data(self):
        # set up a Parser instance that uses LetMeParseThat class
        parser = LetMeParseThat(self.scraper.transactions)

        # extract string data and emoji data from Venmo transactions
        parser.extract_string_data()
        parser.extract_emoji_data()

        # set up an Analyzer instance that uses LetMeAnalyzeThat class
        analyzer = LetMeAnalyzeThat()
        self.str_data = analyzer.analyze_string_data(parser.string_compiler)
        self.emoji_data = analyzer.analyze_emoji_data(parser.emoji_compiler)
        return self.emoji_data, self.str_data

if __name__ == '__main__':
    scraper = LetMeScrapeThat()
    link = "http://www.vicemo.com/"
    scraper.scrape_vicemo(link,150)
    print(scraper.transactions)
    # print(scraper.datalength)
    parser = LetMeParseThat(scraper.transactions)
    parser.extract_string_data()
    # parser.make_soup()
