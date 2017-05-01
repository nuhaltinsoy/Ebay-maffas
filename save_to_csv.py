import xml.etree.ElementTree as ET
import csv

tree = ET.parse("test15.xml")
root = tree.getroot()

# Open File for writing using "a" which will create a new one 

ebay_item_data = open('ebay.csv', 'a', encoding="utf-8")

#create a csv writing object

csvwrite = csv.writer(ebay_item_data)
ebay_item_data_header = []

count = 0

for tags in root.findall('item'):
    item = []
    quantity = []
    if count == 0:
        itemid = tags.find('ItemID').tag
        ebay_item_data_header.append(itemid)
        csvwrite.writerow(ebay_item_data_header)
        count =+ 1
        itemid = tags.find('ItemID').tag
        ebay_item_data_header.append(itemid)
        csvwrite.writerow(ebay_item_data_header)
        
ebay_item_data.close()
