'''Imported modules'''
from flask import *
from pymongo import *
import time

''' Some GLOBAL variables '''
client = MongoClient('139.59.29.224',27017)
app = Flask(__name__)

''' Routine for feed '''
@app.route('/feed')
def feed():
	# client = MongoClient('139.59.29.224',27017)
	db = client['feed']
	all_col = db.collection_names()
	del all_col[all_col.index('system.indexes')]
	feed = list()
	for i in all_col:
		col = db[i]
		for i in col.find():
			feed.append(i)

	return jsonify(feed)


''' Routine for deleting messege '''
@app.route('/msgd')
def msgd():
	u1 = str(request.args.get('u1'))
	u2 = str(request.args.get('u2'))
	msg = str(request.args.get('msg'))
	msg_db = client['msg']
	msg_collection = msg_db['msg']
	msg_collection.delete_one({'u1' : u1, 'u2' : u2,'msg' : msg})
	return 'msg deleted'

''' Routine for sending messeges '''
@app.route('/msg')
def msg():
	u1 = str(request.args.get('u1'))
	u2 = str(request.args.get('u2'))
	msg = str(request.args.get('msg'))
	msg_db = client['msg']
	msg_collection = msg_db['msg']
	data = {
		'u1' : u1,
		'u2' : u2,
		'msg' : msg,
		'time' : time.time()
	}
	msg_collection.insert_one(data)
	return 'SENT'

''' Routine for getting messeges '''
@app.route('/get')
def get():
	t = 0
	ans = dict()
	u1 = str(request.args.get('u1'))
	u2 = str(request.args.get('u2'))
	login_db = client['msg']
	login_collection = login_db['msg']
	x = login_collection.find({'$or' : [{'$and' : [{'u1':u1 }, {'u2' : u2}]}, {'$and' :  [{'u1' : u2 }, {'u2' : u1 }]}]}).sort('time')
	if x.count() == 0:
		return 'NO CHAT FOUND'
	for i in x:
		del i['_id']
		ans[t] = i
		t += 1
	return jsonify(ans)

''' Routine for login '''
@app.route('/login')
def login():
	user = str(request.args.get('user'))
	login_db = client.login
	login_collection = login_db.login
	x = login_collection.find_one({'_id':user})
	# print x
	return jsonify(**x) if x is not None else "Bad"

''' Home Page '''
@app.route('/')
def main():
	return "<h3>Hello</h3>"

''' Run main App '''
if __name__ == '__main__':
	app.secret_key = 'super secret key'
	app.run(host='0.0.0.0', port=5612, debug=True)

