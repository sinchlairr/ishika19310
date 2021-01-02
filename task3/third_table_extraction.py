from pymongo import MongoClient
import base64
import gridfs
import json
from tabula import convert_into

client=MongoClient('mongodb+srv://Ishika_joshi:rnSrKfN6DJiDsjD@cluster0.5zuik.mongodb.net/test')
db=client.camelDb
connection=db.test1
#tmp={"hello":"world"}

convert_into("PDF2.pdf","test.json",output_format="json")


# Loading or Opening the json file 
with open('test2.json') as file: 
    file_data = json.load(file) 
      

if isinstance(file_data, list): 
    connection.insert_many(file_data)   
else: 
    connection.insert_one(file_data) 
