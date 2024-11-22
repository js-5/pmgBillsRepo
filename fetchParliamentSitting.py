from bs4 import BeautifulSoup
import requests
from datetime import datetime

# URL of the webpage
url = 'https://www.parliament.gov.za/parliament-programme'

# Send a GET request to the URL
response = requests.get(url)

# Parse the HTML content of the page
soup = BeautifulSoup(response.content, 'html.parser')

# Find the table body containing rows
table = soup.find('tbody')
date_list = []
if table:
    rows = table.find_all('tr')

    # Get the current year
    current_year = datetime.now().year

    for row in rows:
        # Find all <td> elements in the row
        cells = row.find_all('td')
        
        # Check if there are exactly 6 <td>s
        if len(cells) == 6:
            # Get the first and last <td>
            first_cell = cells[0].text.strip()  # The date
            last_cell = cells[-1].text.strip()  # The last column
            
            # Extract the year from the first cell (assuming it's a date)
            year = first_cell[:4]  # The first 4 characters of the date
            
            # Print the date if the last <td> has content and the year matches the current year
            if last_cell and year == str(current_year):
                date_list.append(first_cell)
file_name = "sitting_dates.txt"
date = []
for days in date_list:
    date.append(days[:10])
unique_dates = list(set(date))
unique_dates.sort()
with open(file_name,"w") as file:
    for item in unique_dates:
        file.write(item+"\n")