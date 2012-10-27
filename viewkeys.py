__author__ = 'saimanoj'

import admin_handler
import model

class MainPage(admin_handler.AdminHandler):
    def get(self):
        if self.is_admin:
            keys = model.Keys.all()
            if keys:
                self.render("view_keys.jinja2", count = keys.count(), keys = keys)
            else:
                self.render("view_keys.jinja2", error = 'No keys in the datastore.')
