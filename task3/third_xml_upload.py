import json 
import xml.etree.ElementTree as ET  
from pymongo import MongoClient

client=MongoClient('mongodb+srv://Ishika_joshi:rnSrKfN6DJiDsjD@cluster0.5zuik.mongodb.net/test')
db=client.StackOverflow2
connection=db.Users
tree=ET.iterparse('Users.xml', events=['start'])
d=[]
for event, elem in tree:
    if event == 'start':
        connection.insert_one(elem.attrib)
#         d.append(elem.tag)

        
