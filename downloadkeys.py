__author__ = 'saimanoj'

__author__ = 'saimanoj'

import admin_handler
import model

class MainPage(admin_handler.AdminHandler):
    def get(self):
        if self.is_admin:
            form_type = self.request.get('downloadKeys')
            if form_type == 'A':
                keys = model.FormAKeys.all()
                self.response.headers['Content-Disposition'] = "attachment; filename=formA-keys.csv"
            elif form_type == 'B':
                keys = model.FormBKeys.all()
                self.response.headers['Content-Disposition'] = "attachment; filename=formB-keys.csv"
            elif form_type == 'C':
                keys = model.FormCKeys.all()
                self.response.headers['Content-Disposition'] = "attachment; filename=formC-keys.csv"
            else:
                self.write('Wrong Form Type')
                return
            self.response.headers['Content-Type'] = 'text/csv'

            if keys:
                self.write('Keys\n')
                for key in keys:
                    self.write(key.keyPhrase+'\n')
            else:
                self.render("view_keys.jinja2", error = 'No keys in the datastore.')
