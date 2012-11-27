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
		data = self.get_from_api('/users/%s/questions' % username)
		logging.debug(data)
		context['answered_questions'] = data['answered_questions']
		context['unanswered_questions'] = data['unanswered_questions']
		context['api_calls'] = self.api_calls

		context['messages'] = utils.get_messages()
		context['remaining'] = 100 - context['comparisons']['mp']['politmus_score']

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