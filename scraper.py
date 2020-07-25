# Use Beautifulsoup and requests to extract data from htlm and url

import requests
from bs4 import BeautifulSoup
import time
from random import randint

filename = "output.csv"
f = open(filename, "a" , encoding='utf-8')

headers = "product_id,product_name,price,category_name,brand_name,stock,store_id,state_abv,city,rating,reviews,offer\n"
f.write(headers)

urls = {"Video Cards" : "https://www.microcenter.com/search/search_results.aspx?N=4294966937&NTK=all&page={}&cat=Video-Cards-%3a-MicroCenter&storeid={}"}
"""
		"AMD Processors/CPUs" : "https://www.microcenter.com/search/search_results.aspx?N=4294966995+4294819840&NTK=all&page={}&cat=AMD-%3a-Processors-%3a-MicroCenter&storeid={}",
		"Intel Processors/CPUs" : "https://www.microcenter.com/search/search_results.aspx?N=4294966995+4294820689&NTK=all&page={}&cat=Intel-%3a-Processors-%3a-MicroCenter&storeid={}",
		"AMD Motherboards" : "https://www.microcenter.com/search/search_results.aspx?N=4294966996+4294818892&NTK=all&page={}&cat=AMD-%3a-Motherboards-%3a-MicroCenter&storeid={}",
		"Intel Motherboards" : "https://www.microcenter.com/search/search_results.aspx?N=4294966996+4294818573&NTK=all&page={}&cat=Intel-%3a-Motherboards-%3a-MicroCenter&storeid={}",
		"Desktop Memory/RAM" : "https://www.microcenter.com/search/search_results.aspx?N=4294966965&NTK=all&page={}&cat=Desktop-Memory/RAM-:-MicroCenter&storeid={}"
}
"""
stores = {
	"CA - Tustin" : "101",
	"CO - Denver" : "181"}
"""
	"GA - Duluth" : "065",
	"GA - Marietta" : "041",
	"IL - Chicago" : "151",
	"IL - Westmont" : "025",
	"KS - Overland Park" : "191",
	"MA - Cambridge" : "121",
	"MD - Rockville" : "085",
	"MD - Parkville" : "125",
	"MI - Madison Heights" : "055",
	"MN - St. Louis Park" : "045",
	"MO - Brentwood" : "095", 
	"NJ - North Jersey" : "075",
	"NY - Westbury" : "171", 
	"NY - Brooklyn" : "115",
	"NY - Flushing" : "145",
	"NY - Yonkers" : "105",
	"OH - Columbus" : "141",
	"OH - Mayfield Heights" : "051",
	"OH - Sharonville" : "071",
	"PA - St. Davids" : "061",
	"TX - Houston" : "155",
	"TX - Dallas" : "131",
	"VA - Fairfax" : "081"
}
"""
for store, id in stores.items():
	for category, href in urls.items():
		print(store + " " + category)
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
					category_name.replace(",","") + "," + stock.replace(",","") + "," + brand_name.replace(",","") + "," + 
					store_id.replace(",","") + "," + state_abv.replace(",","") + "," + city.replace(",","") + "," + 
					rating.replace(",","") + "," + reviews.replace(",","") + "," + offer.replace(",","") + "\n")
			time.sleep(randint(2,10))
f.close()
print("--- Webscrape Finished ---")