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
        else:
            self.redirect(users.create_login_url(self.request.uri))

                
