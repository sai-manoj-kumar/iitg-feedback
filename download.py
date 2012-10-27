__author__ = 'saimanoj'

from google.appengine.api import users
import webapp2
import handler


class MainPage(handler.Handler):
    def get(self):
        if self.is_admin:
            self.render("download.jinja2")
        else:
            self.write("You are not an admin and can not download data")

app = webapp2.WSGIApplication([('/download/data', MainPage)], debug=True)
