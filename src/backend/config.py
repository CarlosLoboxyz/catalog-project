import os


basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
	SECRET_KEY = os.environ.get('SECRET_KEY') or 'pk-starstorm'	
	MONGODB_SETTINGS = {
		'db': 'flask',
		'host': 'localhost',
		'port': 27017,	
	}