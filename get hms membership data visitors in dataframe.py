import requests
import pandas as pd
import lxml
import html5lib 
from bs4 import BeautifulSoup

#This script gets data from the membership page of HMS. This data has alreday been processed
#getting the data direct from cacti may be a better idea.
#powerbi can use the cacti api endpoints directly as a web import

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
