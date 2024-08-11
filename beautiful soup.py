#!/usr/bin/env python
# coding: utf-8

# ! pip install bs4
# ! pip install requests

#   # importing the required libraries
# from bs4 import BeautifulSoup
#  import requests

# # importing the required liabraries
# from bs4 import BeautifulSoup
# import requests

# In[4]:


import requests
from bs4 import BeautifulSoup

def fetch_wikipedia_headers(url):
    # Send a GET request to the Wikipedia page
    response = requests.get(url)
    response.raise_for_status()  # Check for request errors

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all header tags
    headers = {}
    for level in range(1, 7):
        tag_name = f'h{level}'
        headers[tag_name] = [header.get_text(strip=True) for header in soup.find_all(tag_name)]

    return headers

def display_headers(headers):
    # Display the headers
    for level, headers_list in headers.items():
        print(f"{level.upper()} Headers:")
        for header in headers_list:
            print(f"  - {header}")
        print()  # Print a newline for better readability

def main():
    url = 'https://en.wikipedia.org/wiki/Main_Page'  # Wikipedia's main page URL
    headers = fetch_wikipedia_headers(url)
    display_headers(headers)

if __name__ == '__main__':
    main()


# In[13]:


import requests
from bs4 import BeautifulSoup
import pandas as pd

def fetch_imdb_top_100(url):
    # Send a GET request to the IMDb Top 100 movies page
    response = requests.get(url)
    response.raise_for_status()  # Check for request errors

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all movie entries
    movies = soup.find_all('div', class_='titleColumn')

    # Initialize lists to hold the data
    names = []
    ratings = []
    years = []

    for movie in movies:
        # Extract the movie name
        name = movie.a.get_text()
        names.append(name)
        
        # Extract the release year
        year = movie.span.get_text().strip('()')
        years.append(year)
        
        # Extract the rating
        rating_div = movie.find_next_sibling('td', class_='imdbRating')
        rating = rating_div.strong.get_text()
        ratings.append(rating)
        
    return names, ratings, years

def create_dataframe(names, ratings, years):
    # Create a DataFrame from the lists
    df = pd.DataFrame({
        'Name': names,
        'Rating': ratings,
        'Year': years
    })
    return df

def main():
    url = 'https://m.imdb.com/chart/top/'
    names, ratings, years = fetch_imdb_top_100(url)
    df = create_dataframe(names, ratings, years)
    
    # Display the DataFrame
    print(df.head(100))  # Display top 100 rows

if __name__ == '__main__':
    main()


# In[14]:


import requests
from bs4 import BeautifulSoup
import pandas as pd

def fetch_restaurant_details(url):
    # Send a GET request to the Dineout page
    response = requests.get(url)
    response.raise_for_status()  # Check for request errors

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Initialize lists to hold the data
    names = []
    cuisines = []
    locations = []
    ratings = []
    image_urls = []

    # Find all restaurant entries
    restaurant_cards = soup.find_all('div', class_='restnt-card')

    for card in restaurant_cards:
        # Extract the restaurant name
        name_tag = card.find('a', class_='restnt-name')
        if name_tag:
            names.append(name_tag.get_text(strip=True))
        
        # Extract the cuisine
        cuisine_tag = card.find('div', class_='cuisine')
        if cuisine_tag:
            cuisines.append(cuisine_tag.get_text(strip=True))
        
        # Extract the location
        location_tag = card.find('div', class_='restnt-loc')
        if location_tag:
            locations.append(location_tag.get_text(strip=True))
        
        # Extract the rating
        rating_tag = card.find('div', class_='restnt-rating')
        if rating_tag:
            ratings.append(rating_tag.get_text(strip=True))
        
        # Extract the image URL
        image_tag = card.find('img', class_='no-img')
        if image_tag:
            image_urls.append(image_tag.get('data-src'))  # 'data-src' for lazy-loaded images

    return names, cuisines, locations, ratings, image_urls

def create_dataframe(names, cuisines, locations, ratings, image_urls):
    # Create a DataFrame from the lists
    df = pd.DataFrame({
        'Restaurant Name': names,
        'Cuisine': cuisines,
        'Location': locations,
        'Rating': ratings,
        'Image URL': image_urls
    })
    return df

def main():
    url = 'https://www.dineout.co.in/your-city'  # Replace with actual URL
    names, cuisines, locations, ratings, image_urls = fetch_restaurant_details(url)
    df = create_dataframe(names, cuisines, locations, ratings, image_urls)
    
    # Display the DataFrame
    print(df.head(10))  # Display top 10 rows for brevity

if __name__ == '__main__':
    main()


# In[15]:


import requests
from bs4 import BeautifulSoup
import pandas as pd

def fetch_presidents_data(url):
    # Send a GET request to the webpage
    response = requests.get(url)
    response.raise_for_status()  # Ensure the request was successful

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Initialize lists to hold the data
    names = []
    terms = []

    # Find the relevant table containing former Presidents
    table = soup.find('table', class_='tablepress')
    
    if not table:
        raise ValueError("Table with former Presidents data not found.")
    
    rows = table.find_all('tr')

    for row in rows[1:]:  # Skip the header row
        cells = row.find_all('td')
        if len(cells) >= 2:
            name = cells[0].get_text(strip=True)
            term = cells[1].get_text(strip=True)
            names.append(name)
            terms.append(term)

    return names, terms

def create_dataframe(names, terms):
    # Create a DataFrame from the lists
    df = pd.DataFrame({
        'Name': names,
        'Term of Office': terms
    })
    return df

def main():
    url = 'https://presidentofindia.nic.in/former-presidents'
    names, terms = fetch_presidents_data(url)
    df = create_dataframe(names, terms)
    
    # Display the DataFrame
    print(df)

if __name__ == '__main__':
    main()


# In[ ]:




