__author__ = 'saimanoj'

import admin_handler
from google.appengine.ext import db
import random
import model

class MainPage(admin_handler.AdminHandler):
    def post(self):
        if self.is_admin:
            form_type = self.request.get("formType")
            num_keys = self.request.get("num_keys")
            if num_keys.isdigit() and int(num_keys) > 0:
                num_keys = int(num_keys)
            else:
                error = 'Enter a Number greater than Zero.'
                self.redirect('/admin/genkeys?error=' + error)
                return
            key_entries = []
            keys = []
            i = 0
            while i < num_keys:
                key = ''.join(random.choice(
                    'abcdefghkmnqrstuvwxyzABCDEFGHJKMNQRSTUVWXYZ' * 7 + '23456789' * 13) for x in range(10))
                if key not in keys:
                    if form_type == 'A':
                        if model.FormAKeys.by_name(key) is None:
                            keys.append(key)
                            key_entries.append(model.FormAKeys(keyPhrase = key, formFilled = False))
                            i += 1
                    elif form_type == 'B':
                        if model.FormBKeys.by_name(key) is None:
                            keys.append(key)
                            key_entries.append(model.FormBKeys(keyPhrase = key, formFilled = False))
                            i += 1
                    elif form_type == 'C':
                        if model.FormCKeys.by_name(key) is None:
                            keys.append(key)
                            key_entries.append(model.FormCKeys(keyPhrase = key, formFilled = False))
                            i += 1
                    else:
                        self.write('Wrong Form Type')
                        return
            result = db.put(key_entries)
            if result:
                self.redirect('/admin/viewkeys')
            else:
                self.write("Keys Can't be stored")

    def get(self):
        if self.is_admin:
            count = model.FormAKeys.all().count()
            error = self.request.get("error")

            if error:
                self.render("generated_keys.jinja2", count = count, error = error)
            else:
                keys = model.FormAKeys.all()
                self.render("generated_keys.jinja2", count = count, keys = keys)
