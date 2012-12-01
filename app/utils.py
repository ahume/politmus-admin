import json
import urllib2
import logging
import datetime
from urllib import urlencode

from google.appengine.ext import db

import models

hostname = 'http://localhost:8080'
#hostname = 'http://politmus-api.appspot.com'

class PolitmusAPIHandler(object):

	def get_from_api(self, url):
		url = '%s%s' % (hostname, url)
		self.api_calls.append(url)
		return json.load(urllib2.urlopen(url))

	def post_to_api(self, url, data):
		url = '%s%s' % (hostname, url)
		return json.load(urllib2.urlopen(url, urlencode(data)))


def add_message(message):
    m = models.UserMessage(body=message, dt=datetime.datetime.now())
    m.put()

def get_messages():
    messages = models.UserMessage.all()
    if messages.count() > 0:
        m = [message.body for message in messages]
        db.delete(messages)
        return m
    return None
