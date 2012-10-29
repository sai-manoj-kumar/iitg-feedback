__author__ = 'saimanoj'

import admin_handler
import model

class MainPage(admin_handler.AdminHandler):
    def get(self):
        if self.is_admin:
            form_type = self.request.get('viewKeys')
            if form_type == 'A':
                keys = model.FormAKeys.all()
            elif form_type == 'B':
                keys = model.FormBKeys.all()
            elif form_type == 'C':
                keys = model.FormCKeys.all()
            else:
                self.write('Wrong Form Type')
                return
            if keys:
                self.render("view_keys.jinja2", count = keys.count(), keys = keys)
            else:
                self.render("view_keys.jinja2", error = 'No keys in the datastore.')
