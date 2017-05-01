# -*- coding: utf-8 -*-
"""
# 
# EBAY trading API SCRIPT
#
# VERSION 1.0.0
#
# MAFFAS 2017
#

"""
import os
import sys
import datetime
import argparse
import ebaysdk
#import csv 
import lxml
from common import dump
from ebaysdk.utils import getNodeText
from ebaysdk.exception import ConnectionError
from ebaysdk.trading import Connection as Trading

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

site_id = input("PLEASE CHOOSE A GLOBAL ID:\n") # enter the country 

item_id = input("Please Enter Item Number Here: ")

file_name = input("Please Enter a Filename: ")

app_id = 'YOUR APP ID'
cert_id = 'YOUR CERT ID'
dev_id = 'DEV ID'
token_id = 'YOUR TOKEN'


sys.path.insert(0, '%s/../' % os.path.dirname(__file__))


def init_options():
    usage = "usage: %prog [options]"
    parser = argparse.ArgumentParser(usage=usage)

    parser.add_argument("-d", "--debug",
                        action="store_true", dest="debug", default=False,
                        help="Enabled debugging [default: %default]")
    args = parser.parse_args()
    return args

# Get Store Catergories
    
def get_item(args):
    try:
        api = Trading(debug=args.debug, appid=app_id, token=token_id,
certid=cert_id, devid=dev_id, warnings=True, timeout=20, siteid=site_id, config_file=None)

        storeData = {
            'MessageID': 'IT CIRCLE CONSULT PYTHON - MAFFAS',
            'ItemID': item_id,
        }

        api.execute('GetItem', storeData)
        dump(api)
        f = open('E:\\pathto\\maf-ebay\\maf-ebay-dev\\get-item\\'+ file_name + '.xml','a')

        f.write(str(api.response.content)[2:-1]) # write result, removes the b' from the start, from position [2] until the ' at the end [-1]

        f.close() #close html
      
        
    except ConnectionError as e:
        print(e)
        print(e.response.dict())



# Execute and Print

if __name__ == "__main__":
    args = init_options()

    print("HERE WE GO.........")


print("********** GETTING ITEM **********")

get_item(args)

print("\n\nAll Good with no Errors, Tot Ziens!\n\n")
