from pymongo import *
import time
client = MongoClient('139.59.29.224',27017)

db = client['login']
col = db['login']
data = {
	'_id' : '201401139',
	'Name' : 'Hardik Sardhara',
	'password' : '00000000'
}
col.insert_one(data)
print 'done'