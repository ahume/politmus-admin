import logging

from google.appengine.ext import webapp
from google.appengine.ext.webapp import template
from google.appengine.api import memcache
from google.appengine.ext import db

import utils

class QuestionHandler(webapp.RequestHandler, utils.PolitmusAPIHandler):
	def get(self, question_key):
		self.api_calls = []
		context = self.get_from_api('/questions/%s' % question_key)
		context['api_calls'] = self.api_calls

		context['username'] = self.request.get('username')

		logging.debug(dir(template))
		t = template.render('templates/questions_question.html', context)

		self.response.out.write(t)