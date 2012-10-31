__author__ = 'saimanoj'

from google.appengine.api import users
import handler

class MainPage(handler.Handler):
    def get(self):
        self.redirect(users.create_logout_url('/'))
