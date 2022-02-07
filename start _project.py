from turtle import pd
import pandas as pd
import time
import numpy as np
import pandas as pd
import requests 
from bs4 import BeautifulSoup
v_indexes = [ 0 ]
eleven_columns = ['version' , 'year' , 'engine' , 'current_mileage' , 'hand' , 'gearBox' , 'color' , 'original_onership' , 'next_test_in' , 'annual_licensing_fee' , 'price']
nine_columns = ['version' , 'year' , 'engine' , 'current_mileage' , 'hand' , 'gearBox' , 'color' , 'original_onership' , 'annual_licensing_fee' ]
Details = pd.DataFrame(index= v_indexes , columns= v_columns )
cars = pd.read_csv(r"C:\Users\avoav\Introduction to Data Science\Project סמסטר א\project-semester-a\DataFrame_cars_urls\cars_urls_data.csv" ,index_col=0 )

cars = cars.rename( columns = {'0' : 'url'} )

# for i in cars.index:
one_car = requests.get(cars['url'][0]) 
soup = BeautifulSoup(one_car.content , 'html.parser')
    
    # how to choose only the second td each time?
    
Det = soup.select('td' , class_='MuiTableCell-root MuiTableCell-body MuiTableCell-alignLeft MuiTableCell-paddingNone')
df_Det = pd.DataFrame( columns= v_columns)
det_array = []
for i in range(len(Det)):
    if (i%2 != 0):
        det_array.append(Det[i].get_text())
        if (Det[i].get_text() == None):
            det_array.append(None)
if len(det_array) ==9:
    df_det_array = pd.DataFrame(np.array([det_array]) , columns = nine_columns  ) 
df_det_array 
#how to append data with different number of columns 
df_Det.append(df_det_array , ignore_index = True , sort = True)
df_Det
#Details.append(df_Det , ignore_index = True , )

#cars_details = details[0]

#driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

#print (soup.prettify)
# muiBox = soup.select('h1')
# muiBox = soup.select('h1.MuiTypography-root')
# details = soup.select('h2.MuiTypography-root[tabindex="0"]')


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
