from pymongo import *
import time
client = MongoClient('139.59.29.224',27017)
<<<<<<< HEAD

db = client['login']
col = db['login']
data = {
	'_id' : '201401139',
	'Name' : 'Hardik Sardhara',
	'password' : '00000000'
}
col.insert_one(data)
=======
user = '201401140'
db = client['msg']
col = db['msg']
col.insert_one({'u1' : '201401140', 'u2' : '201401139', 'time' : time.time(), 'msg': 'Sample messege'})
col.insert_one({'u2' : '201401140', 'u1' : '201401139', 'time' : time.time(), 'msg': 'Reply to Sample messege'})

>>>>>>> 1c38b27d3d0b9b48408495552cb6488198336909
print 'done'