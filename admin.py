__author__ = 'saimanoj'

from google.appengine.api import users
import webapp2
import handler
import download
import viewkeys
import genkeys

class MainPage(handler.Handler):
    def get(self):
        if self.is_admin:
            self.render("admin.jinja2")
        else:
            self.write("You are not logged in as admin. "
                       "If you are admin, logout your google account and login to your admin account")

app = webapp2.WSGIApplication([
    ('/admin/*', MainPage),
    ('/admin/viewkeys/*', viewkeys.MainPage),
    ('/admin/genkeys/*', genkeys.MainPage),
    ('/admin/download/*', download.MainPage)],
    debug = True)

