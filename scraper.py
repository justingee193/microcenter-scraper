# Use Beautifulsoup and requests to extract data from htlm and url

import requests
from bs4 import BeautifulSoup
import time
from random import randint
from url import urls, stores

filename = "output.csv"
f = open(filename, "a" , encoding='utf-8')

headers = "product_id,product_name,price,category_name,brand_name,stock,store_id,state_abv,city,rating,reviews,offer\n"
f.write(headers)

urls = urls
stores = stores

for store, id in stores.items():
	print("------------ " + store + " ------------")
	for category, href in urls.items():
		print(category, end='')
		for pg in range(1, 2): # page change
			try:
				url = href.format(pg, id) # change for each category and alter for each page and store
				headers = {'User-Agent' : 'Mozilla/5.0'}

				req = requests.get(url, headers=headers).text.encode('utf-8')
				source = BeautifulSoup(req, "lxml")

				containers = source.find_all('div', { 'class' : "detail_wrapper"})
			except HTTPError as e:
				print(e)
				break

			for container in containers:

				try:
					product_id = container.a['data-id'].strip()
				except IndexError:
					product_id = 'null'

				try:
					product_name = container.a['data-name'].strip()
				except IndexError:
					product_name = 'null'

				try:
					price = container.a['data-price'].strip()
				except IndexError:
					price = 'null'

				try:
					category_name = container.a['data-category'].strip()
				except IndexError:
					category_name = 'null'

				try:	
					brand_name = container.a['data-brand'].strip()
				except IndexError:
					brand_name = 'null'

				try:
					stock = container.find('div', {"class" : "stock"}).strong.text.strip()
				except IndexError:
					stock = 'null'

				try:
					store_id = id
				except IndexError:
					store_id = 'null'

				try:
					state_abv = store[:2]
				except:
					state_abv = 'null'

				try:
					city = store[5:]
				except:
					city = 'null'

				try:
					rating = container.find('div', {"class" : "ratingstars"}).img['alt'].strip()
				except:
					rating = 'null'

				try:
					reviews = container.find('div', {"class" : "ratingstars"}).span.text.strip()
				except:
					reviews = 'null'

				try:
					offer = container.find('div', {"class" : "highlight clear"}).text.strip()
				except IndexError:
					offer = 'null'

				f.write(product_id.replace(",","") + "," + product_name.replace(",","") + "," + price.replace(",","") + "," + 
					category_name.replace(",","") + "," + brand_name.replace(",","") + "," + stock.replace(",","") + "," +
					store_id.replace(",","") + "," + state_abv.replace(",","") + "," + city.replace(",","") + "," + 
					rating.replace(",","") + "," + reviews.replace(",","") + "," + offer.replace(",","") + "\n")
			print(" ----- ", end='')
			time.sleep(randint(2,10))
		print("Success")
f.close()
print("--- Webscrape Finished ---")