import vicemo_scraper
import visualizedata

# target website
link = "http://www.vicemo.com/"

print("WARNING: this process may take about 15 - 25 seconds depending on your connection speed!")
print()
print("=====================================================")
print("Track transactions for drugs, booze, and sex on Venmo")
print("=====================================================")
print("Please, wait")

# first we set up an instance of VicemoScraper and extract data
scraper = vicemo_scraper.VicemoScraper(link)
emoji, str = scraper.get_data()

# then we set up two instances of LetMeVisualizeThat for str data and emoji data
visualize_str = visualizedata.LetMeVisualizeThat(str)
visualize_emoji = visualizedata.LetMeVisualizeThat(emoji)
visualize_str.plot_bar_chart_words()
visualize_emoji.plot_bar_chart_emojis()

