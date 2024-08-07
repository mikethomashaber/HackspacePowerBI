import requests
import re
from bs4 import BeautifulSoup
import pandas as pd


#This script in run from PowerBI. When using Python as a datasource Power BI expects to recieve a printed dataframe.



#List of the Financial pages on wiki.nottinghack.org.uk to scrape with Beautiful Soup.
#This can be improved using a generated date - and stopping when we get to an empty page for the next month.
#Note this list of pages uses the latest page formating standard. Older pages use a fifferent page formatting standard, so would need both different scraping methods and most likely different PowerBi code to display the data.

datelist = ["Financials_2024_July","Financials_2024_January", "Financials_2024_February", "Financials_2024_March","Financials_2024_April","Financials_2024_May","Financials_2024_June","Financials_2023_January", "Financials_2023_February", "Financials_2023_March","Financials_2023_April","Financials_2023_May","Financials_2023_June", "Financials_2023_July", "Financials_2023_August", "Financials_2023_September","Financials_2023_October","Financials_2023_November","Financials_2023_December","Financials_2022_January", "Financials_2022_February", "Financials_2022_March","Financials_2022_April","Financials_2022_May","Financials_2022_June", "Financials_2022_July", "Financials_2022_August", "Financials_2022_September","Financials_2022_October","Financials_2022_November","Financials_2022_December","Financials_2021_January", "Financials_2021_February", "Financials_2021_March","Financials_2021_April","Financials_2021_May","Financials_2021_June", "Financials_2021_July", "Financials_2021_August", "Financials_2021_September","Financials_2021_October","Financials_2021_November","Financials_2021_December","Financials_2020_January", "Financials_2020_February", "Financials_2020_March","Financials_2020_April","Financials_2020_May","Financials_2020_June", "Financials_2020_July", "Financials_2020_August", "Financials_2020_September","Financials_2020_October","Financials_2020_November","Financials_2020_December"]

#We use a list of lists for pandas df. I call the list of lists 'lol', lol.
lol = []
 
for date in datelist:
   
    webpage = "https://wiki.nottinghack.org.uk/wiki/" + date
    print(date)

    yearMonth = date.split("_")
    shortDate =(yearMonth[2], yearMonth[1])
   

    page = requests.get(webpage)
    soup = BeautifulSoup(page.content, 'html.parser')

    

    
    #Get Overall Assets from lines on page with text in assetList
    #Basically use re.complie to make a regular expression to grep for
    #If the format of the wiki pages changes this code may need to change
    assetsList = ["Overall Assets","Current Assets","Petty Cash","Closing Stock","Stripe","TSB Account","Fixed Assets","Rental Deposit" ]
    for asset in assetsList:
        line = soup(text=re.compile(asset))
        for words in line:
            item = str(words)
            item2 =item.replace("\n","")
            
            lol.append(["Asset:", yearMonth[2] + yearMonth[1],item2])


    
    #Income
    incomeList = ["Donation","Events","Embroidery Induction","Laser Induction","Tool Usage","Workshops"]
    for income in incomeList:
        line = soup(text=re.compile(income))

        for words in line:
            item = str(words)
            item2 =item.replace("\n","")

            lol.append(["Income:", yearMonth[2] + yearMonth[1],item2])


    # We have two membership payments - I take the first one to be the £5 minimum payment
    incomeList = ["Membership Payment"]
    j = 0
    for income in incomeList:
        line = soup(text=re.compile(income))
       
        for words in line:
            if j == 0: data = "Membership Payments 1"
            if j == 1: data = "Membership Payments 2"
            item = str(words)
            item2 =item.replace("\n","")
            item3 =item2.replace("Membership Payments", data)
            
            lol.append(["Income:", yearMonth[2] + yearMonth[1],item2])

            
            j = 1

            
    #Expenses
    ExpensesList = ["Bank Service Charge","F6","G4,5,6","BOC Gas","Cleaning","Network and Servers","Resources","Trustees Misc","Tools and Equipment","Business Rates,","Electric","Internet " ]
    for expense in ExpensesList:
        line = soup(text=re.compile(expense))

        for words in line:
            item = str(words)
            item2 =item.replace("\n","")
            #print (yearMonth[2] + "," + yearMonth[1] + ":Expense:", item2 )
            
            lol.append(["Expense:", yearMonth[2] + yearMonth[1],item2])


    #Snackspace appears twice, I assume the first is income, the second expense, need to ask Matt.
    ExpensesList = ["Snackspace"]
    for expense in ExpensesList:
        line = soup(text=re.compile(expense))
        i = 0 
        for words in line:
            if i ==0: data = "Income"
            if i ==1: data = "Expense"
            item = str(words)
            item2 =item.replace("\n","")
            #print (yearMonth[2] + "," + yearMonth[1] + ":"+ data +":", item2 )
        
            lol.append([data, yearMonth[2] + yearMonth[1],item2])


            i = 1

df = pd.DataFrame(lol,columns=['Type','Date','Value'])
print(df)