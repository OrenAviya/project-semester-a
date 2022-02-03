from turtle import pd
import requests
from bs4 import BeautifulSoup
#import pandas as pd


one_car = requests.get('https://carwiz.co.il/used-cars/1b703714-c6c6-4c40-a62a-a445532dab9f/2018-%D7%A7%D7%99%D7%94-%D7%A1%D7%A4%D7%95%D7%A8%D7%98%D7%96')
soup = BeautifulSoup(one_car.content , 'html.parser')
# Details = soup.find('div' , class_='MuiBox-root jss1013 jss1007')
# print (Details)

muiBox = soup.select('h1')
muiBox = soup.select('h1.MuiTypography-root')
#print (soup.prettify)


# car_type = soup.select()

# with open ('cars' ) as html_file:
#     soup = BeautifulSoup(html_file , 'lxml')

# car = soup.find('div')
# print (car)









#res = requests.get('https://en.wikipedia.org/wiki/Windows_11')
#soup = BeautifulSoup(res.content, 'html.parser')

#labels = soup.select('.infobox.vevent tr .infobox-label')
#datas = soup.select('.infobox.vevent tr .infobox-data')
#for i in range(len(labels)):
 #   print(labels[i].getText() + ": " + datas[i].getText())

#exit()

#children_num = requests.get('https://www.cbs.gov.il/he/mediarelease/pages/2021/%D7%9E%D7%A9%D7%A4%D7%97%D7%95%D7%AA-%D7%91%D7%99%D7%A9%D7%A8%D7%90%D7%9C-%D7%A0%D7%AA%D7%95%D7%A0%D7%99%D7%9D-%D7%9C%D7%A8%D7%92%D7%9C-%D7%99%D7%95%D7%9D-%D7%94%D7%9E%D7%A9%D7%A4%D7%97%D7%94.aspx')
#print (children_num )
#Crime_data = requests.get('https://data.gov.il/dataset/netuny_peshia')
#print(Crime_data.text)
#crimes= BeautifulSoup(Crime_data.text)
#print(crimes, crimes.parser_class)
 
#print (hellow world)
 #from sklearn.pipeline import make_pipeline
