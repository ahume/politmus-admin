import logging
from google.appengine.ext import db

class UserMessage(db.Expando):
	body = db.TextProperty()
	dt = db.DateTimeProperty()