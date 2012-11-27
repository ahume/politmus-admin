import logging
import math

from google.appengine.ext import webapp
from google.appengine.ext.webapp import template
from google.appengine.api import memcache
from google.appengine.ext import db

import utils

class MPProfileHandler(webapp.RequestHandler, utils.PolitmusAPIHandler):
	def get(self, slug):
		self.api_calls = []
		context = self.get_from_api('/mps/%s' % slug)
		context['api_calls'] = self.api_calls

		t = template.render('templates/mps_mp.html', context)

		self.response.out.write(t)

class MPListHandler(webapp.RequestHandler, utils.PolitmusAPIHandler):
	def get(self):
		self.api_calls = []

		page = int(self.request.get('page', 1))
		start_index = 1
		if page > 1:
			start_index = (page - 1) * 10
		count = 10

		context = self.get_from_api('/mps?start_index=%s&count=%s' % (start_index, count))
		context['api_calls'] = self.api_calls
		context['page'] = page
		context['total_pages'] = int(math.ceil(context['total'] / 10))
		if context['total_pages'] == 0:
			context['total_pages'] = 1

		logging.debug(dir(template))
		t = template.render('templates/mps_list.html', context)

		self.response.out.write(t)