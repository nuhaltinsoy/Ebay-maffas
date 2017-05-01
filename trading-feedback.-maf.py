"""
# 
# EBAY trading API SCRIPT
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

#parties wrapped up
token_id = 'AgAAAA**AQAAAA**aAAAAA**RtIBWQ**nY+sHZ2PrBmdj6wVnY+sEZ2PrA2dj6wFl4ugDJeCpQydj6x9nY+seQ**oKYDAA**AAMAAA**XdZg+UJqLcBLoKTeQxK70ezK39ko8u1bGBzb2OeO82CpBQZi+Ymaj7cQgAmTGLgOuB5MZUfRSdSNZ44bGwq3Dmr3/vkEJs9dXEUsJtB2IoYGcVpl/qlXnMMX4uqXJ4C904wzbDJgAaRncNndsXJWW96n+aU1Gb6sQbSmE0zfu+6CLLOp1ryxPYvBQtOWu1XN+z+NeBmiGKJSR4AffF8L1u7nAAjeEgu4kEr7jbEohQLfInPRL43cC5bfHjZr2b0KBLYXq6I3G9eCAfzEJC8hTxSJaOBCHs182MeIygn6x4VV1R9g+iiMGuEzlHdAgAlohcfdb0xaVM9pLbtg+M1dqSK3ewuyo9y8hd8BM07bZupTv91vO6pL57+xHHq++oUnm2xHHCs9St0ZcF/7a6OGxZ7EyxE9NdSEljpzmJxPADgcS3EZKrCzF/g7HOUR80qGTLh+IvnvMGZNBE/hRyRpNntA3L2i9kLKHOEPX2WSskHaIXqiFaRrDBc6UnyoHbUy0dnzmzOmUqlD8BJ6r65EW37TfDsD5i7bpB43mVJ0V/Z6cC3k1vhPi89i0rJU5NqhAepjY0VRDKhkDpDQqvbe8xMVpd8uaWHWRKgHYsDrBbiLo39o7VaTN0WYge9Za2Ok+EnnZnRfyvVP14pQAE5lR7TzWrt9oCxk8OCwmcatAX3sAWpmIhmZG1IxSCLlIxeAgrXpg/NiBnPIb8JuU+yomgpMc/BTQmaZi3lQWIxB3zK78gtvyugkq5JXJTxXab5A'


sys.path.insert(0, '%s/../' % os.path.dirname(__file__))


def init_options():
    usage = "usage: %prog [options]"
    parser = argparse.ArgumentParser(usage=usage)

    parser.add_argument("-d", "--debug",
                        action="store_true", dest="debug", default=False,
                        help="Enabled debugging [default: %default]")
    args = parser.parse_args()
    return args

# FEEDBACK 

def feedback(args):
    try:
        api = Trading(debug=args.debug, appid=app_id, token=token_id, config_file=None, certid=cert_id, devid=dev_id)

        api.execute('GetFeedback', {'UserID': 'parties_wrapped_up'})
        dump(api)

        if int(api.response.reply.FeedbackScore) > 1:
            print(api.response.reply)
        else:
            print("Onwards and Forwards!")

    except ConnectionError as e:
        print(e)
        print(e.response.dict())



# Execute and Print

if __name__ == "__main__":
    args = init_options()

    
def n():
    print("\n\n")

n()
print("********** FEEDBACK**********")
feedback(args)  
feed = feedback(args)
print(feed)