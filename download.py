__author__ = 'saimanoj'

from google.appengine.api import users
import webapp2
import handler
import config


class MainPage(handler.Handler):
    def get(self):
        if self.user:
            if self.user.nickname() in config.admins:
                self.write("Hello, Download World")
            else:
                self.write("You are not an admin and can not download data")
        else:
            self.redirect(users.create_login_url(self.request.uri))

app = webapp2.WSGIApplication([('/download/data', MainPage)], debug=True)
