"""
# 
# EBAY trading API SCRIPT
#
# CHECK USER TOKEN
#
# VERSION 1.0.0
#
# MAFFAS 2017
"""
import os
import sys
import datetime
import argparse
import ebaysdk
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
app_id = 'ITCircle-Test-PRD-a6c385072-a322116b'
cert_id = 'PRD-6c3850728fda-97a2-4f6b-8dc0-e8ae'
dev_id = 'd8db78bb-6384-49df-944f-211222854ad5'
token_id = 'AgAAAA**AQAAAA**aAAAAA**Bt8BWQ**nY+sHZ2PrBmdj6wVnY+sEZ2PrA2dj6wNkoGgDZaApAmdj6x9nY+seQ**oKYDAA**AAMAAA**/+r8suX9+9Nzi88hYwcJxeD4cfzezFLYm0kodgQTeAWKt1M/RdlUVnfyk6LFnIyEK97So8yHlr63j+LtwzwXAWYj4Ar+CCy63aZRasRDP/6VpUZS4BaslitBgnsgl7hWZ5C3NtQ5fo83nS/oEhDhG+tjegkaryV7HT6ncXqPwjdiQwJmfZfhTq1EJvwN17cTwvqgvLlsyZvL+G/ZaWnNk/3TPgjyVdYGiaRlIFJLmTxcpTDe4x3KeHRYNK2FB0RRFXhdAneInUc8aFuN6+UARsiy96DwuJIgdp4Pi41TcBn3ScDIUj9puD84rmc1e6ylHmqeLbt7NSvd/KH2egmXTotoXDVqYZ1WT/3bPGeki3WigExoPGfLW3YgDEDZoz+smFA/de0wn/qlhUqExuXQrMK1nSMc6YKzB44pZRzse/aaDJS5xggUUKnOfeaXlnyMtqxYIzEP4zZRD3flfTwTlAqZdnBoZyw4NxGKMVsyuZUcl/3NMU2j4AUD30hGUcHuuOL82v+LK4LN3BnFc+BUtigI1740wdLfoaatRWrfBUY1YBMJNTZiwa+x3ptMD/HLcY9cxzcL/JDMr5PvXsNemh87G4/G8CXJfQRzg0UYnS+WSJ7wdH+ZIgzCXN9SB/rbVBdls+kkZaP3NR2afVm9HWoxoeG/wHJgVO52GwFpOJ8cZqDF5FHkQGf8XdZgAiJ2WSBGUZkC/pnFkrWXlA+C1tsoE9CVYYbySSO5u8yAi4e14AXk2xp9RqFpaHJ6b0yB'


# Error Control

def init_options():
    usage = "usage: %prog [options]"
    parser = argparse.ArgumentParser(usage=usage)

    parser.add_argument("-d", "--debug",
                        action="store_true", dest="debug", default=False,
                        help="Enabled debugging [default: %default]")
    args = parser.parse_args()
    return args

# insert item here ready to list..

def verifyAddItem(args):
    """http://www.utilities-online.info/xmltojson/#.UXli2it4avc
    """
    try:
        api = Trading(debug=args.debug, siteid=site_id, appid=app_id, token=token_id, config_file=None, certid=cert_id, devid=dev_id)

        myitem =  {
  "Item": {
    "Title": "PYTHON TEST",
    "Description": "This is the first book in the Harry Potter series. In excellent condition!",
    "PrimaryCategory": { "CategoryID": "377" },
    "StartPrice": "1.0",
    "CategoryMappingAllowed": "true",
    "ConditionID": "4000",
    "Country": "US",
    "Currency": "USD",
    "DispatchTimeMax": "3",
    "ListingDuration": "Days_7",
    "ListingType": "Chinese",
    "PaymentMethods": "PayPal",
    "PayPalEmailAddress": "johnashu1@hotmail.com",
    "PictureDetails": { "PictureURL": "http://www.itcircleconsult.com/eb2017/hottub/pics/left2.png" },
    "PostalCode": "95125",
    "Quantity": "1",
    "ReturnPolicy": {
      "ReturnsAcceptedOption": "ReturnsAccepted",
      "RefundOption": "MoneyBack",
      "ReturnsWithinOption": "Days_30",
      "Description": "If you are not satisfied, return the book for refund.",
      "ShippingCostPaidByOption": "Buyer"
    },
    "ShippingDetails": {
      "ShippingType": "Flat",
      "ShippingServiceOptions": {
        "ShippingServicePriority": "1",
        "ShippingService": "USPSMedia",
        "ShippingServiceCost": "2.50"
      }
    },
    "Site": "US"
  }
}

        api.execute('VerifyAddItem', myitem)
        dump(api)

    except ConnectionError as e:
        print(e)
        print(e.response.dict())

# ERROR CODES IF PROBLEMS


# Execute and Print

if __name__ == "__main__":
    args = init_options()

    print("Trading API Samples for version %s" % ebaysdk.get_version())

def n():
    print("\n\n")
n()
print("**********ADD ITEMS**********")
verifyAddItem(args)
addz = verifyAddItem(args)
print(addz)
n()
