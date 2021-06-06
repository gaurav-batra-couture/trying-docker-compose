import flask_sqlalchemy

db = flask_sqlalchemy.SQLAlchemy()


class Coin(db.Model):
	__tablename__ = 'Coin'
	id = db.Column(db.Integer,primary_key = True)
	name = db.Column(db.String(100))
	price = db.Column(db.Integer)
