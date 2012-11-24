import logging

from google.appengine.ext import webapp
from google.appengine.ext.webapp import template
from google.appengine.api import memcache
from google.appengine.ext import db

import utils

class UserProfileHandler(webapp.RequestHandler, utils.PolitmusAPIHandler):
	def get(self, username):
		self.api_calls = []
		context = self.get_from_api('/users/%s' % username)
		context['questions'] = self.get_from_api('/users/%s/questions/unanwsered' % username)['questions']
		context['api_calls'] = self.api_calls

		logging.debug(dir(template))
		t = template.render('templates/users_user.html', context)

		self.response.out.write(t)

class UserListHandler(webapp.RequestHandler, utils.PolitmusAPIHandler):
	def get(self):
		self.api_calls = []
		context = self.get_from_api('/users?count=20')
		context['api_calls'] = self.api_calls

		logging.debug(dir(template))
		t = template.render('templates/users_list.html', context)

		self.response.out.write(t)