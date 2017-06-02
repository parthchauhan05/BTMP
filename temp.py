from pymongo import *
import time
client = MongoClient('139.59.29.224',27017)

db = client['feed']
col = db['Models Of Computations']
# data = {
# 	'question' : 'Sample Question 1',
# 	'asked by' : '201401140',
# 	'answers' : {
# 		'_id' : '201401139',
# 		'answer' : 'Answer to sample question 1'
# 	}
# }
# col.insert_one(data)
# print 'done'
for i in col.find():
	print i