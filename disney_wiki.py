import requests
from bs4 import BeautifulSoup as bs

# Task 1 
r = requests.get("https://en.wikipedia.org/wiki/Toy_Story_3")
# Convert to beautiful soup object
soup = bs(r.content)

# Print out HTML
content = soup.prettify()
print(content)

# Grab table
info_box = soup.find(class_='infobox vevent')
info_rows = info_box.find_all('tr')
for row in info_rows:
    print(row.prettify())
    
movies_info = {}
# In case of multiple names in 1 content
def get_content_value(row):
    if row.find('li'):
        return [li.get_text(" ",strip=True) for li in row.find_all('li')]
    else:
        return row.find(class_='infobox-data').get_text()

for index,row in enumerate(info_rows):
    if index == 0:
        movies_info['title'] = row.find('th').get_text(" ",strip=True)
    elif index == 1: # We don't need a picture
        continue
    else:
        content_key = row.find(class_='infobox-label').get_text(" ",strip=True)
        content_value = get_content_value(row)
        movies_info[content_key] = content_value

# Task 2
def get_info_box(movie_url):
    r = requests.get(movie_url)
    # Convert to beautiful soup object
    soup = bs(r.content)

    # Grab table
    info_box = soup.find(class_='infobox vevent')
    info_rows = info_box.find_all('tr')
        
    movies_info = {}
    # In case of multiple names in 1 content

    for index,row in enumerate(info_rows):
        if index == 0:
            movies_info['title'] = row.find('th').get_text(" ",strip=True)
        elif index == 1: # We don't need a picture
            continue
        else:
            content_key = row.find(class_='infobox-label').get_text(" ",strip=True)
            content_value = get_content_value(row)
            movies_info[content_key] = content_value
    return movies_info
r = requests.get("https://en.wikipedia.org/wiki/List_of_Walt_Disney_Pictures_films")
# Convert to beautiful soup object
soup = bs(r.content)

base_path = "https://en.wikipedia.org"

movies = soup.select('.wikitable.sortable i a')
movies_info_list = []

for index,movie in enumerate(movies):
    try:
        relative_path = movie['href']
        full_path = base_path + relative_path
        movies_info_list.append(get_info_box(full_path))
    except Exception as e:
        print(movie.get_text())
        print(e)



