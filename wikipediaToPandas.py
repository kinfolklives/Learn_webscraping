import requests
import pandas as pd
from bs4 import BeautifulSoup

wikipage = "https://en.wikipedia.org/wiki/List_of_sovereign_states_and_dependent_territories_by_continent_(data_file)"
result = requests.get(wikipage)
if result.status_code == 200:
    soup = BeautifulSoup(result.content, "lxml")
table = soup.find('table', {'class':'wikitable sortable'})
new_table = []
for row in table.find_all('tr')[1:]:
    columns = row.find_all('td')
    new_table.append([column.get_text() for column in columns])
df = pd.DataFrame(new_table, columns=['ContinentCode', 'Alpah2', 'Alpah3', 'PhoneCode', 'Name'])
df['Name'] = df['Name'].str.replace("\n","")



