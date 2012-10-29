__author__ = 'saimanoj'

import os
import webapp2
from google.appengine.api import users
import jinja2
import config

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape = True)

class Handler(webapp2.RequestHandler):
    is_admin = False
    is_logged_in = False

    formA_attributes = ['rating2_1', 'rating2_2', 'rating2_3', 'rating3_1', 'rating3_2', 'rating3_3', 'rating3_4',
                        'rating3_5', 'rating3_6', 'rating4_1', 'rating4_2', 'rating4_3', 'rating4_4', 'rating4_5',
                        'rating4_6', 'rating4_7', 'rating4_8', 'rating4_9', 'rating4_10', 'rating5_1', 'rating5_2',
                        'rating5_3', 'rating5_4', 'rating5_5']

    formB_attributes = ['rating2_1', 'rating2_2', 'rating2_3', 'rating2_4', 'rating2_5', 'rating3_1', 'rating3_2',
                        'rating3_3', 'rating3_4', 'rating3_5', 'rating3_6', 'rating3_7', 'rating3_8', 'rating3_9',
                        'rating3_10']

    formC_attributes = ['rating2_1', 'rating2_2', 'rating2_3', 'rating3_1', 'rating3_2', 'rating3_3', 'rating3_4',
                        'rating3_5', 'rating4_1', 'rating4_2', 'rating4_3', 'rating4_4', 'rating4_5',
                        'rating4_6', 'rating4_7', 'rating4_8', 'rating4_9', 'rating4_10']


    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)


    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)


    def render(self, template, **kw):
        self.write(self.render_str(template, **kw))


    def initialize(self, *a, **kw):
        webapp2.RequestHandler.initialize(self, *a, **kw)
        self.user = users.get_current_user()
        if self.user:
            self.is_logged_in = True
            if self.user.nickname() in config.admins:
                self.is_admin = True
