import requests
import pandas as pd
import lxml
import html5lib 
from bs4 import BeautifulSoup

url = 'https://hms.nottinghack.org.uk/statistics/membership'
html = requests.get(url).content
df_list = pd.read_html(html)
#filename = "membership.csv"
#file1 = open(filename, "w", encoding="utf-8")  # write mode


df0 = df_list[0]
df1 = df_list[1]
df3 = df_list[0] + df_list[1]



print(df1)

#file1.write(data1 + data2)
