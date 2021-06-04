import json
from flask import Flask,request
import flask_sqlalchemy

from table import db,Coin
import config


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = config.DATABASE_CONNECTION_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.app_context().push()
db.init_app(app)
db.create_all()

@app.route('/')
def helloWorld():
	return json.dumps({"hello": "world"})

@app.route('/get',methods=['GET'])
def getAll():
	coins = Coin.query.all()
	all_coins = []
	for coin in coins:
		new_coin = {
			"id": coin.id,
			"name": coin.name,
			"price": coin.price
		}

		all_coins.append(new_coin)

	return json.dumps(all_coins), 200

@app.route('/add',methods=['POST'])
def addCoin():
	data = request.get_json()
	name = data['name']
	price = data['price']

	coin = Coin(name = name,price = price)
	db.session.add(coin)
	db.session.commit()

	return json.dumps("Added"), 200




# if __name__ == '__main__':
	# app.run(host='0.0.0.0',port = 8080, debug = True)