# date: Monday 19th, February 2024
# author: reyesjl
# description: gets a list of all major cities in the United States
# usage: python maul

import requests
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/List_of_United_States_cities_by_population"

# Fetch the page content
response = requests.get(url)
html_content = response.text

# Parse the HTML
soup = BeautifulSoup(html_content, 'html.parser')

# Find the table headers 
#table_headers = soup.find_all('th')

# Find tables
tables = soup.find_all('table')

# Designated table
target_table = tables[4]
table_rows = target_table.find_all('tr')

cities = []

# Loop through each row and print the content
for row in table_rows:
    cells = row.find_all(['td'])
    city_state_cells = cells[:2]

    for cell in city_state_cells:
        print(cell.get_text(strip=True))

