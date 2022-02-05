import time
import numpy as np
import pandas as pd
import selenium.webdriver as sw

from bs4 import BeautifulSoup

HOST_WEB = 'https://carwiz.co.il'

driver = sw.Chrome(executable_path="./chromedriver.exe")
driver.get(HOST_WEB + '/used-cars')

car_urls = []
while len(car_urls) < 1000:
	driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
	
	time.sleep(1)

	try:
		soup = BeautifulSoup(driver.page_source, 'html.parser')
	
		elms = soup.select('#root div main div.MuiContainer-root.MuiContainer-maxWidthLg > div:nth-child(2) > div > div > div a[href]')
		
		#elms is a list of all  the links in the page , each link represents page for one car:
		
		for elm in elms:
			car_url = HOST_WEB + elm['href']
			if car_url not in car_urls:
				car_urls.append(car_url)
				print(car_url)
		print(len(car_urls))
	except:
		print('error')

columns = ['version' , 'year' , 'engine' , 'current_mileage' , 'hand' , 'gearBox' , 'color' , 'original_onership' , 'next_test_in' , 'annual_licensing_fee' , 'price']
df_car_urls=pd.Dataframe(np.car_urls, columns




def readCSV( str, index) -> pd.DataFrame:
    return pd.read_csv('../data/' + str + '.csv', index_col=index)

def saveCSV(df: pd.DataFrame, name: str, index_label='index'):
    df.to_csv('../data/' + name + '.csv', index_label=index_label)