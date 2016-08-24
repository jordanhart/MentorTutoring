from flask import Flask,jsonify
from flask_pymongo import PyMongo

app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'mentortutoringdb'
app.config['MONGO_URI'] = 'mongodb://localhost:27017/mentortutoringdb'

mongo = PyMongo(app)

@app.route('/newuser/<a>/<b>',methods= ['GET'])

def newacc(a,b):
	#result = str(a) + str(b) + str(c)
	#return jsonify({'name':str(a), 'email':str(b), 'googleauth':str(c)})

	user = mongo.db.mentortutoringdb
	user.insert({'name' : str(a), 'email' : str(b)})
	return 'Added user'

app.run(debug=True)