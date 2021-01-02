# -*- coding: utf-8 -*-
"""
Created on Sat Jan  2 20:53:43 2021


"""
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import pymongo
import pandas as pd
import sys
import re

client = pymongo.MongoClient("mongodb+srv://Ishika_joshi:rnSrKfN6DJiDsjD@cluster0.fk7fo.mongodb.net/test")
db=client.StackOverflow
collection=db.Tags
freq={}
cnt=0

for i in collection.find():
    
    if ('TagName' in i and 'Count' in i):
        freq[i['TagName']]=int(i['Count'])
        

print("ok")
wordcloud=WordCloud()
wordcloud.generate_from_frequencies(freq)
plt.figure()
plt.imshow(wordcloud,interpolation="bilinear")
plt.axis("off")
plt.show()