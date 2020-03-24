import pandas as pd
from datetime import date

#TODO:  Error handling
#TODO:  Add in arguments for file export type
#TODO:  Add a date column of the pull date to the dataframe

#where our data is located
URL = 'https://www.worldometers.info/coronavirus/#countries'

#pulled up the URL and inspected the page to find the right info for the table
#this will grab the table we are after as a list
df_in_list = pd.read_html(URL, attrs = {'id': 'main_table_countries_today'})

#convert list to dataframe
df = df_in_list[0]

#replace NaN with zeros
df = df.fillna(0)

#get today's date
today = date.today()

#format the date so it can be used as part of the file name
filedate = today.strftime("%m%d%Y")

#build out the path - make changes here for customization
path = 'C:\export\CV'+ filedate + '.xlsx'

df.to_excel(path)