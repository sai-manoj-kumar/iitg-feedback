__author__ = 'saimanoj'

from google.appengine.api import users
import handler

class MainPage(handler.Handler):
    def get(self):
        if self.is_logged_in:
            if self.is_admin:
                self.render("download.jinja2")
            else:
                self.write("You are not an admin and can not download data")
        else:
            self.redirect(users.create_login_url(self.request.uri))

