import requests
from bs4 import BeautifulSoup as bs

# Load the webpage content
r = requests.get("https://keithgalli.github.io/web-scraping/example.html")

# Convert to a beautiful soup object
soup = bs(r.content)

print(soup.prettify())

first_header = soup.find("h2")
# Pass in a list of elements to look for
first_header = soup.find(["h2","h1"]) # Same result because it only find the first element of the list
headers = soup.find_all(["h1","h2"]) # Find all headers
print(headers)

paragraph = soup.find_all("p")
paragraph
# You can pass in attributes to the find/find_all function
paragraph = soup.find_all("p",attrs = {"id":"paragraph-id"})
paragraph

# You can nest find/fnd_all calls
body = soup.find("body")
body
div = body.find("div")
div
header = div.find("h1")
header

# We can search specific strings in our find/find_all calls
import re
# Without regular expression we need to look for an exact string which is not useful
paragraphs = soup.find_all("p",string = re.compile("Some"))
paragraphs

headers = soup.find_all("h2",string = re.compile("(H|h)eader"))
headers

# CSS selector
# style references https://www.w3schools.com/cssref/css_selectors.asp
print(soup.body.prettify())
content = soup.select("div p")
content

paragraphs = soup.select("h2 ~ p")
paragraphs

bold_text = soup.select("p#paragraph-id b")
bold_text

paragraphs = soup.select("body > p")
print(paragraphs)

for paragraph in paragraphs:
    print(paragraph.select("i"))

# Different properties of the HTML

# Use .string
header = soup.find("h2")
header.string

# If multiple child elements use get_text
div = soup.find("div")
print(div.prettify())
print(div.get_text())

# Get a specidic property from an element
link  = soup.find("a")
link['href']

paragraphs = soup.select("p#paragraph-id")
paragraphs[0]["id"]

# Code navigation

# Path syntax
print(soup.body.prettify())

# Know the terms: Parent,Sibling,Child












