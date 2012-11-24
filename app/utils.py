import json
import urllib2
import logging
from urllib import urlencode

#hostname = 'http://localhost:8085'
hostname = 'http://politmus-api.appspot.com'

class PolitmusAPIHandler(object):

	def get_from_api(self, url):
		url = '%s%s' % (hostname, url)
		self.api_calls.append(url)
		return json.load(urllib2.urlopen(url))

	def post_to_api(self, url, data):
		url = '%s%s' % (hostname, url)
		return json.load(urllib2.urlopen(url, urlencode(data)))
