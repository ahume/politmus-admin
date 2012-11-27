#!/usr/bin/env python

import logging

from google.appengine.ext import webapp
from google.appengine.ext.webapp import util

from views.users import UserProfileHandler, UserListHandler
from views.mps import MPProfileHandler, MPListHandler
from views.votes import CrudVoteHandler, UserVoteListHandler
from views.questions import QuestionHandler, QuestionListHandler

def main():

    logging.getLogger().setLevel(logging.DEBUG)
    application = webapp.WSGIApplication([

        ('/users/(.*)/votes/(.*)', UserVoteListHandler),
        ('/users/(.*)/votes', CrudVoteHandler),
        ('/users/(.*)', UserProfileHandler),
        ('/users', UserListHandler),

        ('/mps', MPListHandler),

        ('/questions/(.*)', QuestionHandler),
        ('/questions', QuestionListHandler),

    ], debug=True)
    util.run_wsgi_app(application)


if __name__ == '__main__':
    main()