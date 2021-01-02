import json
import matplotlib.pyplot as plt 
import pymongo
import pandas as pd
import sys
import re

client=pymongo.MongoClient('mongodb+srv://Ishika_joshi:rnSrKfN6DJiDsjD@cluster0.fk7fo.mongodb.net/test')
db=client.StackOverflow
collection=db.Posts
freq={}
cnt=0

for i in collection.find():
	
		
	if('Tags' in i and 'ViewCount' in i):
		#print(i['ViewCount'])
		l=re.findall("\<(.*?)\>", i['Tags'])
		#print("check1")
		for j in l:
			r={}

			if (j not in freq):
				r['ViewCount']=int(i['ViewCount'])
				if 'Body' in i:
					r['Body']=i['Body']
				else:
					r['Body']=' '

				if 'Body' in i:
					r['allBody']=i['Body']
				else:
					r['allBody']=' '

				if 'Score' in i:
					r['Score']=int(i['Score'])
				else:
					r['Score']=0


				if 'FavoriteCount' in i:
					r['Fav']=int(i['FavoriteCount'])
				else:
					r['Fav']=0


				if 'AnswerCount' in i:
					r['AnsCount']=int(i['AnswerCount'])
				else:
					r['AnsCount']=0

				if 'CommentCount' in i:
					r['ComCount']=int(i['CommentCount'])
				else:
					r['ComCount']=0

				if 'CreationDate' in i:
					r['CreationDate']=[i['CreationDate']]
				else:
					r['CreationDate']=[]

				if 'OwnerUserId' in i:
					r['name']=int(i['OwnerUserId'])
				else:
					r['name']=' '


				freq[j]=r
				#print("check2")
			else:
				# freq[j]['ViewCount']+=int(i['ViewCount'])
				# freq[j]['Fav']+=int(i['FavoriteCount'])
				# freq[j]['AnsCount']+=int(i['AnswerCount'])
				# freq[j]['ComCount']+=int(i['CommentCount'])
				# freq[j]['allBody']+=(i['Body'])
				# freq[j]['Score']+=int(i['Score'])
				# freq[j]['CreationDate'].append(i['CreationDate'])
				if 'Body' in i:
					freq[j]['allBody']+=i['Body']


				if 'Score' in i:
					freq[j]['Score']+=int(i['Score'])
				else:
					freq[j]['Score']+=0


				if 'FavoriteCount' in i:
					freq[j]['Fav']+=int(i['FavoriteCount'])
				else:
					freq[j]['Fav']+=0


				if 'AnswerCount' in i:
					freq[j]['AnsCount']+=int(i['AnswerCount'])
				else:
					freq[j]['AnsCount']+=0

				if 'CommentCount' in i:
					freq[j]['ComCount']+=int(i['CommentCount'])
				else:
					freq[j]['ComCount']+=0

				if 'CreationDate' in i:
					freq[j]['CreationDate'].append([i['CreationDate']])

				if 'CommentCount' in i:
					freq[j]['ComCount']+=int(i['CommentCount'])
				else:
					freq[j]['ComCount']+=0




			
		
		print(cnt)
		cnt+=1



with open('user.json', 'w') as info_json:
    json.dump(freq, info_json)

