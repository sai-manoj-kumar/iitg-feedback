__author__ = 'saimanoj'

import webapp2
from google.appengine.api import users
import handler
import formA
import download

class MainPage(handler.Handler):
    def get(self):
        if self.user:
            if self.user.nickname() == "ysaimanojkumar":
                self.redirect('/download/1a2b3cd456gh')
            else:
                self.render('index.jinja2')
        else:
            self.redirect(users.create_login_url(self.request.uri))


app = webapp2.WSGIApplication([('/', MainPage),
    ('/formA', formA.MainPage),
    ('/download/.*', download.MainPage)],
    debug=True)

