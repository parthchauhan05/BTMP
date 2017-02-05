from flask import *
from pymongo import *

client = MongoClient('139.59.29.224',27017)
app = Flask(__name__)

@app.route('/login')
def login():
	user = str(request.args.get('user'))
	login_db = client.login
	login_collection = login_db.login
	x = login_collection.find_one({'_id':user})
	# print x
	return jsonify(**x) if x is not None else "Bad"

@app.route('/')
def main():
	return "<h3>Hello</h3>"

if __name__ == '__main__':
	app.secret_key = 'super secret key'
	app.run(host='0.0.0.0', port=5612, debug=False)