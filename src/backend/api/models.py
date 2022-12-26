from api import db
from werkzeug.security import generate_password_hash, check_password_hash


class Product(db.Document):
	name = db.StringField(max_length=120, required=True)
	price = db.DecimalField(precision=2, required=True)
	description = db.StringField(min_length=120, required=True)
	owner = db.ReferenceField('User', required=True)
	# specs =
	# tags =

	def __repr__(self):
		return '<Product {}>'.format(self.name)

class User(db.Document):
	email = db.EmailField(unique=True, required=True)
	username = db.StringField(max_length=20, unique=True, required=True)
	password_hash = db.StringField(max_length=128, required=True)
	products = db.ListField(db.ReferenceField('Product'))

	def __repr__(self):
		return '<User {}>'.format(self.username)

	def set_password(self, password):
		self.password_hash = generate_password_hash(password)

	def check_password(self, password):
		return check_password_hash(self.password_hash, password)