__author__ = 'saimanoj'

import webapp2
from google.appengine.api import users
import handler
import formA
import generate_keys
import config

class MainPage(handler.Handler):
    def get(self):
        if self.user:
            if self.user.nickname() in config.admins:
                self.redirect('/download/data')
            #                TODO redirect to a nice webpage to click the "download form data" button.
            else:
                self.render('index.jinja2')
        else:
            self.redirect(users.create_login_url(self.request.uri))


app = webapp2.WSGIApplication([('/', MainPage),
    ('/formA/*', formA.MainPage)],
    debug=True)
