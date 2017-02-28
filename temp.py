from pymongo import *
import time
client = MongoClient('139.59.29.224',27017)
user = '201401140'
db = client['msg']
col = db['msg']
col.insert_one({'u1' : '201401140', 'u2' : '201401139', 'time' : time.time(), 'msg': 'Sample messege'})
col.insert_one({'u2' : '201401140', 'u1' : '201401139', 'time' : time.time(), 'msg': 'Reply to Sample messege'})

print 'done'