# pip install feedparser
import feedparser
import pprint
import json
import os
# install the two functions from the html_table_generator.py file (should be in same folder)
from html_table_generator import create_header, create_row, create_table

# Download
d1 = feedparser.parse("http://www.fuelwatch.wa.gov.au/fuelwatch/fuelWatchRSS?Product=1&Region=23")
d2 = feedparser.parse("http://www.fuelwatch.wa.gov.au/fuelwatch/fuelWatchRSS?Product=1&Region=23&Day=tomorrow")

currency = '$'
l1 = []
l2 = []
l3 = []
l4 = []

# Filter the required items from the dictionary
for item in d1['entries']:
    l1.append({'name':item['trading-name'], 'location':item['location'], 'price':currency + item['price'], 'day':'today'})

for item in d2['entries']:
    l2.append({'name':item['trading-name'], 'location':item['location'], 'price':currency + item['price'], 'day':'tomorrow'})

l3 = l1 + l2

# Sort based on the price feild using an anonymous function
l4 = sorted(l3, reverse=True, key=lambda k: k['price']) #

html_string = ''
html_index = ''

#create header
html_string += create_header('Name', 'Location', 'Price', 'Day')
# pass the strings in l4 in to the create_row function to make the HTML and add to html_string. This will generate a large string of HTML
for i in range(len(l4)):
    html_string += create_row(l4[i]['name'],l4[i]['location'],l4[i]['price'],l4[i]['day'])

# pass HTML string of rows into main <table> tag
html_index = create_table(html_string)

# Path dependent on OS and PC
#path = '/home/ben/Dropbox/Programming/Python/pdpd/week03/'
#path = 'C:/Users/Ben.Scott/Dropbox/Programming/Python/pdpd/week03/'
path = os.path.dirname(os.path.abspath(__file__))
# create a index.html document and write our string of HTML to it
file = open(os.path.join(path, 'index.html'), 'w')
file.write(html_index)
file.close()
