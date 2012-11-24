import logging
import os
import json

from google.appengine.ext import webapp
from google.appengine.ext.webapp import template
from google.appengine.api import memcache
from google.appengine.ext import db

import utils

class CrudVoteHandler(webapp.RequestHandler, utils.PolitmusAPIHandler):

	def get(self, username):
		self.api_calls = []
		context = self.get_from_api('/users/%s/votes' % username)
		context['api_calls'] = self.api_calls

		t = template.render('templates/votes_list.html', context)
		self.response.out.write(t)

	def post(self, username):

		question = self.request.get('question')

		context = self.post_to_api('/users/%s/votes' % username, {
			'question': question,
			'selection': self.request.get('selection')
		})

		self.redirect('/questions/%s?username=%s' % (question, username))

class UserVoteListHandler(webapp.RequestHandler, utils.PolitmusAPIHandler):

	def get(self, username, question_key):
		self.api_calls = []
		context = self.get_from_api('/users/%s/votes/%s' % (username, question_key))
		context['api_calls'] = self.api_calls

		t = template.render('templates/votes_vote.html', context)
		self.response.out.write(t)