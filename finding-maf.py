"""
# 
# EBAY FINDING API SCRIPT, SAVES TO CSV FILE..
#
# VERSION 1.0.0
#
# MAFFAS 2017
"""
import ebaysdk 
from ebaysdk.finding import Connection as finding 
import os
import sys 
import datetime 
import csv 
import lxml

# country list
print("""
Site ID  Site Name 	       Global ID

0 	     United States 	    EBAY-US
2 	     Canada (English) 	EBAY-ENCA
3 	     UK 	            EBAY-GB
15 	     Australia 	        EBAY-AU
16 	     Austria 	        EBAY-AT
23 	     Belgium (French) 	EBAY-FRBE
71 	     France 	        EBAY-FR
77 	     Germany 	        EBAY-DE
100      Motors 	        EBAY-MOTOR
101      Italy 	            EBAY-IT
123      Belgium (Dutch) 	EBAY-NLBE
146      Netherlands 	    EBAY-NL
186      Spain 	            EBAY-ES
193      Switzerland 	    EBAY-CH
201      Hong Kong 	        EBAY-HK
203      India 	            EBAY-IN
205      Ireland 	        EBAY-IE
207      Malaysia 	        EBAY-MY
210      Canada (French) 	EBAY-FRCA
211      Philippines 	    EBAY-PH
212      Poland 	        EBAY-PL
216      Singapore 	        EBAY-SG

""")

site_id = input("PLEASE CHOOSE A GLOBAL ID:\n") # enter the country site to search
keyword = input("Keywords: ") # user enters keywords
cat_id = input("CAtergory Id Number (1 FOR ALL CATERGORIES): ") # user enters keywords
condition = input("Condition Used or New (Capital first letter): ") # user enters keywords
min_price = input("MIN Price: ") # user enters keywords
max_price = input("MAX Price: ") # user enters keywords
entries = input("Number of Entries (max 400): ") # user enters keywords

api = finding(siteid=site_id, appid='ITCircle-Test-PRD-a6c385072-a322116b', config_file=None) #easay to change script but will link this to a yaml file soooon

api.execute('findItemsAdvanced', { #executes calls to the api
    'keywords': keyword,
    'categoryId' : [cat_id], #catergory ids seperated by commas
    'itemFilter': [
        {'name': 'Condition', 'value': [condition]},
        {'name': 'MinPrice', 'value': [min_price], 'paramName': 'Currency', 'paramValue': 'GBP'},
        {'name': 'MaxPrice', 'value': [max_price], 'paramName': 'Currency', 'paramValue': 'GBP'}
    ],
    'paginationInput': {
        'entriesPerPage': entries,
        'pageNumber': '1'
    },
    'sortOrder': 'CurrentPriceHighest'
})

dictstr = api.response.dict() # dictstr now contains the returned data from the API

for item in dictstr['searchResult']['item']:
    with open('E:\\ITCIRCLECONSULT\\GITHUB\\maf-ebay\\finding_data.csv', 'a', newline='', encoding='utf-8') as csvfile:
        ebay_write = csv.writer(csvfile, delimiter=' ',
                                quotechar=' ', quoting=csv.QUOTE_MINIMAL)
        ebay_write.writerow("ItemID: %s" % item['itemId'])
        ebay_write.writerow("Title: %s" % item['title'])
        ebay_write.writerow("CategoryID: %s" % item['primaryCategory']['categoryId'])
        ebay_write.writerow("Condition: %s" % item['condition'])
        print("Title: %s" % item['title'])
        print("CategoryID: %s" % item['primaryCategory']['categoryId'])
        print("Condition: %s" % item['condition'])

print("\n\nAll Good with no Errors, Tot Ziens!\n\n")


