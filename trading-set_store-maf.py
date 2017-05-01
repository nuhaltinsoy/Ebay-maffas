# -*- coding: utf-8 -*-
"""
# 
# EBAY trading API SCRIPT
#SET STORE
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

file_name = input("Please Enter a Filename: ")

custom_header = """ <div id="essHeaderContainer"><meta name="viewport" content="width=device-width, initial-scale=1.0 , maximum-scale=1.0, user-scalable=no"><link href="http://www.2011partieswrappedup.esellersolutions.com/shop/css/main.css" rel="stylesheet" type="text/css"><link href="http://www.2011partieswrappedup.esellersolutions.com/shop/css/essdrop.css" rel="stylesheet" type="text/css"><link href="http://www.2011partieswrappedup.esellersolutions.com/shop/css/carousel.css" rel="stylesheet" type="text/css"><link href="http://www.2011partieswrappedup.esellersolutions.com/shop/css/responsive.css" rel="stylesheet" type="text/css"> <script type="text/javascript">var a=" src='http://www.2011partieswrappedup.esellersolutions.com/shop/js/plugins.js'";document.write("<script type='text/javascript'"+a+">");document.write('</scr'+'ipt>');var b=" src='http://www.2011partieswrappedup.esellersolutions.com/shop/js/slick-nav.js'";document.write("<script type='text/javascript'"+b+">");document.write('</scr'+'ipt>');var footercats=" src='http://www.2011partieswrappedup.esellersolutions.com/shop/footercats.js'";document.write("<script type='text/javascript'"+footercats+">");document.write('</scr'+'ipt>');var footer=" src='http://www.2011partieswrappedup.esellersolutions.com/shop/footer.js'";document.write("<script type='text/javascript'"+footer+">");document.write('</scr'+'ipt>');var c=" src='http://www.2011partieswrappedup.esellersolutions.com/shop/js/general.js'";document.write("<script type='text/javascript'"+c+">");document.write('</scr'+'ipt>');</script> <div class="userNote"><div class="essWrap"><img src="http://www.2011partieswrappedup.esellersolutions.com/shop/images/usernote.gif"></div></div><div id="essHeader" class="essWide"><div class="header-top"><div class="essWrap"><div class="welcome-msg">Welcome to our ebay store..</div><div class="top-nav"><ul><li><a target="_top" href="http://stores.ebay.co.uk/Parties-Wrapped-Up/About-Us.html">About us</a>|</li><li><a target="_top" href="http://stores.ebay.co.uk/Parties-Wrapped-Up/Payment.html">Payment</a>|</li><li><a target="_top" href="http://stores.ebay.co.uk/Parties-Wrapped-Up/Shipping.html">Shipping</a>|</li><li><a target="_top" href="http://stores.ebay.co.uk/Parties-Wrapped-Up/Terms-and-conditions.html">Terms &amp; Conditions</a>|</li><li><a target="_top" href="http://stores.ebay.co.uk/Parties-Wrapped-Up/Contact-Us.html">Contact us</a></li></ul></div></div></div><div class="main-head"><div class="essWrap"><div class="shoplogo"> <a href="http://stores.ebay.co.uk/Parties-Wrapped-Up" target="_top"><img src="http://www.2011partieswrappedup.esellersolutions.com/shop/images/logo-partieswrappedup.png" alt="logo partieswrappedup"/></a></div><div class="header-right"><div class="joinLinks"> <a href="http://my.ebay.co.uk/ws/eBayISAPI.dll?AcceptSavedSeller&linkname=includenewsletter&sellerid=2011partieswrappedup" target="_top" class="cls1"><img src="http://www.2011partieswrappedup.esellersolutions.com/shop/images/icon-email.png"><div class="popup"><span>Join Mailing List</span></div> </a> <a href="http://my.ebay.co.uk/ws/eBayISAPI.dll?AcceptSavedSeller&linkname=includefavoritestore&sellerid=2011partieswrappedup" class="cls2"><img src="http://www.2011partieswrappedup.esellersolutions.com/shop/images/icon-fav.png"><div class="popup"><span>Add to favourites</span></div> </a> <a href="http://feedback.ebay.co.uk/ws/eBayISAPI.dll?ViewFeedback2&userid=2011partieswrappedup&ftab=FeedbackAsSeller" target="_top" class="cls3"><img src="http://www.2011partieswrappedup.esellersolutions.com/shop/images/icon-feedback.png"><div class="popup"><span>Feedback</span></div> </a></div><div class="cInfo"> <span>Contact Us:</span> <span class="num">01435 862759</span> | <a href="mailto:info@partieswrappedup.co.uk">info@partieswrappedup.co.uk</a></div><div class="eclear">clear</div><div id="topSearch"><form action="http://stores.ebay.co.uk/Parties-Wrapped-Up/_i.html" method="get" target="_top"> <input type="text" class="search-text" name="_nkw" id="nkw"> <input type="submit" value="Search" id="searchbtn" onClick="search()"/></form></div> <a class="fdb" href="http://feedback.ebay.co.uk/ws/eBayISAPI.dll?ViewFeedback2&userid=2011partieswrappedup&ftab=FeedbackAsSeller">Read our feedback</a><div class="eclear">clear</div></div><div class="eclear">clear</div></div></div><div id="topcatz" class="essWide"><div class="essWrap"> <script type="text/javascript">var a=" src='http://www.itcircleconsult.com/eb2017/party/shop/topcatz.js'";document.write("<script type='text/javascript'"+a+">");document.write('</scr'+'ipt>');</script> </div></div><div class="top-info"><div style="float: right;" class="box tle"> <a target="_top" href="http://stores.ebay.co.uk/Parties-Wrapped-Up/Can-We-Help-You.html">Can we help you<span>?</span> </a></div><div class="box cls1"><a target="_top" href="http://stores.ebay.co.uk/Parties-Wrapped-Up/Shipping.html"><img src="http://www.2011partieswrappedup.esellersolutions.com/shop/images/icon-delivery2.gif">Next Day Delivery <br> Available </a></div><div class="box cls2"><a target="_top" href="http://stores.ebay.co.uk/Parties-Wrapped-Up/Shipping.html"><img src="http://www.2011partieswrappedup.esellersolutions.com/shop/images/icon-delivery3.gif">international<br> delivery</a></div><div class="box cls3"><a target="_top" href="http://stores.ebay.co.uk/Parties-Wrapped-Up/Shipping.html"><img src="http://www.2011partieswrappedup.esellersolutions.com/shop/images/icon-delivery1.gif">FREE UK STANDARD<br>DELIVERY </a></div><div class="box cls4"><a target="_top" href="http://stores.ebay.co.uk/Parties-Wrapped-Up/Contact_Us.html"><img src="http://www.2011partieswrappedup.esellersolutions.com/shop/images/icon-delivery4.gif">contact us<br> 01435 862759</a></div><div class="eclear">clear</div></div><div class="colRight-wrap essWrap"><div class="ess-colRight"><div class="rBox rScroll"><h3 class="block-title"><span>New Arrivals</span></h3><div class="pad"><div class="inr-pad"> <script type="text/javascript">var featuredItemNew=" src='http://www.2011partieswrappedup.esellersolutions.com/shop/featuredItemNew.js'";document.write("<script type='text/javascript'"+featuredItemNew+">");document.write('</scr'+'ipt>');</script> </div></div></div><div class="promo-widget rBox"> <script type="text/javascript">var rightpromo1=" src='http://www.2011partieswrappedup.esellersolutions.com/shop/editable/js/right-promo1.js'";document.write("<script type='text/javascript'"+rightpromo1+">");document.write('</scr'+'ipt>');var rightpromo2=" src='http://www.2011partieswrappedup.esellersolutions.com/shop/editable/js/right-promo2.js'";document.write("<script type='text/javascript'"+rightpromo2+">");document.write('</scr'+'ipt>');</script> </div></div></div></div></div>"""

app_id = 'ITCircle-Test-PRD-a6c385072-a322116b'
cert_id = 'PRD-6c3850728fda-97a2-4f6b-8dc0-e8ae'
dev_id = 'd8db78bb-6384-49df-944f-211222854ad5'

#johnbarlow1981
token_id = 'AgAAAA**AQAAAA**aAAAAA**Bt8BWQ**nY+sHZ2PrBmdj6wVnY+sEZ2PrA2dj6wNkoGgDZaApAmdj6x9nY+seQ**oKYDAA**AAMAAA**/+r8suX9+9Nzi88hYwcJxeD4cfzezFLYm0kodgQTeAWKt1M/RdlUVnfyk6LFnIyEK97So8yHlr63j+LtwzwXAWYj4Ar+CCy63aZRasRDP/6VpUZS4BaslitBgnsgl7hWZ5C3NtQ5fo83nS/oEhDhG+tjegkaryV7HT6ncXqPwjdiQwJmfZfhTq1EJvwN17cTwvqgvLlsyZvL+G/ZaWnNk/3TPgjyVdYGiaRlIFJLmTxcpTDe4x3KeHRYNK2FB0RRFXhdAneInUc8aFuN6+UARsiy96DwuJIgdp4Pi41TcBn3ScDIUj9puD84rmc1e6ylHmqeLbt7NSvd/KH2egmXTotoXDVqYZ1WT/3bPGeki3WigExoPGfLW3YgDEDZoz+smFA/de0wn/qlhUqExuXQrMK1nSMc6YKzB44pZRzse/aaDJS5xggUUKnOfeaXlnyMtqxYIzEP4zZRD3flfTwTlAqZdnBoZyw4NxGKMVsyuZUcl/3NMU2j4AUD30hGUcHuuOL82v+LK4LN3BnFc+BUtigI1740wdLfoaatRWrfBUY1YBMJNTZiwa+x3ptMD/HLcY9cxzcL/JDMr5PvXsNemh87G4/G8CXJfQRzg0UYnS+WSJ7wdH+ZIgzCXN9SB/rbVBdls+kkZaP3NR2afVm9HWoxoeG/wHJgVO52GwFpOJ8cZqDF5FHkQGf8XdZgAiJ2WSBGUZkC/pnFkrWXlA+C1tsoE9CVYYbySSO5u8yAi4e14AXk2xp9RqFpaHJ6b0yB'

sys.path.insert(0, '%s/../' % os.path.dirname(__file__))


def init_options():
    usage = "usage: %prog [options]"
    parser = argparse.ArgumentParser(usage=usage)

    parser.add_argument("-d", "--debug",
                        action="store_true", dest="debug", default=False,
                        help="Enabled debugging [default: %default]")
    args = parser.parse_args()
    return args

# set store Catergories
    
def set_store(args):
    try:
        api = Trading(debug=args.debug, appid=app_id, token=token_id,
certid=cert_id, devid=dev_id, warnings=True, timeout=20, siteid=site_id, config_file=None)

        storeData = {
                    "Store":{
                        "CustomHeader": "HOW CAN I GET SOME HTML IN HERE?a?a?a?a",
                        "CustomHeaderLayout":"CustomHeaderShown",
                        "Theme": {
                        "ThemeID": "1",
                        "Name": "Fireworks",
                        "ColorScheme": {
                        "ColorSchemeID": "1",
                        "Name": "Fireworks - Orange",
                        "Color": {
                            "Primary": "A9A9A9",
                            "Secondary": "F4F4F4",
                            "Accent": "FD7714"
                        },
                        "Font": {
                            "NameFace": "Arial",
                            "NameSize": "M",
                            "NameColor": "FFFFFF",
                            "TitleFace": "Arial",
                            "TitleSize": "XS",
                            "TitleColor": "FFFFFF",
                            "DescFace": "Arial",
                            "DescSize": "XS",
                            "DescColor": "333333"
                       },
                    "MessageID":" IT CIRCLE CONSULT - MAFFAS - PYTHON ",
                    "Version":"837"
                    }
                        }
                    }
        }

        api.execute('SetStore', storeData )
        dump(api)
        f = open('E:\\ITCIRCLECONSULT\\GITHUB\\maf-ebay\\maf-ebay-dev\\get-item\\'+ file_name + '.xml','a')

        f.write(str(api.response.content)[2:-1]) # write result, removes the b' from the start, from position [2] until the ' at the end [-1]

        f.close() #close html
      
        
    except ConnectionError as e:
        print(e)
        print(e.response.dict())



# Execute and Print

if __name__ == "__main__":
    args = init_options()

    print("HERE WE GO.........")


print("********** SETTING STORE **********")

set_store(args)

print("\n\nAll Good with no Errors, Tot Ziens!\n\n")
