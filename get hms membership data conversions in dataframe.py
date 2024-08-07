import requests
import pandas as pd
import lxml
import html5lib 
from bs4 import BeautifulSoup

#This script gets data from a page on HMS that is available without logging in. The page has membership metrics including statistics
#Another script gets membership data perday direct from cacti, and this may be a better source. Power BI can create the stats as required.

url = 'https://hms.nottinghack.org.uk/statistics/membership'
html = requests.get(url).content
df_list = pd.read_html(html)

df0 = df_list[0]
df1 = df_list[1]
df3 = df_list[0] + df_list[1]

print(df1)

