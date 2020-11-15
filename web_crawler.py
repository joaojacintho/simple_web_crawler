from urllib.request import urlopen
from bs4 import BeautifulSoup

# Passing the URL for web crawler
url = 'https://dolarhoje.com/'
# Open the URL
html = urlopen(url)
# Using BeautifulSoup for best view HTML code
# And using html.parse for parse text in html
bs = BeautifulSoup(html, 'html.parser')

# Search in html for input with have id equals 'nacional'
find = bs.find('input', id='nacional')

# Taking the value in array
print(find['value'])