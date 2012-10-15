__author__ = 'saimanoj'

from google.appengine.api import users
import webapp2
import handler
import download
import config

class MainPage(handler.Handler):
    def get(self):
        if self.user:
            if self.user.nickname() in config.admins:
                self.render("admin.jinja2")
            else:
                self.write("You are not an admin. If you are admin logout your google account and login to your admin account")
        else:
            self.redirect(users.create_login_url(self.request.uri))

app = webapp2.WSGIApplication([
    ('/admin',MainPage),
    ('/admin/download', download.MainPage),
    ('/admin/download/.*', download.MainPage)],
    debug=True)

