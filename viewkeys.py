__author__ = 'saimanoj'

from google.appengine.api import users
import handler
import model

class MainPage(handler.Handler):
    def get(self):
        if self.is_admin:
            keys = model.Keys.all()
            if keys:
                self.render("view_keys.jinja2", count = keys.count(), keys = keys)
            else:
                self.render("view_keys.jinja2", error = 'No keys in the datastore.')
        else:
            self.write("You are not an admin and can not perform this operation.")
        if not self.is_logged_in:
            self.redirect(users.create_login_url(self.request.uri))

