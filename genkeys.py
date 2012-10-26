__author__ = 'saimanoj'

from google.appengine.api import users
from google.appengine.ext import db
import random
import model
import handler

class GenerateKeys(handler.Handler):
    def post(self):
        if self.is_logged_in:
            if self.is_admin:
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
                        if model.Keys.by_name(key) is None:
                            keys.append(key)
                            key_entries.append(model.Keys(keyPhrase=key, formFilled=False))
                            i += 1
                result = db.put(key_entries)
                if result:
                    self.redirect('/admin/genkeys')
                else:
                    self.write("Keys Can't be stored")
            else:
                self.write("You are not an admin and can not perform Key generation")
        else:
            self.redirect(users.create_login_url(self.request.uri))

    def get(self):
        count = model.Keys.all().count()
        error = self.request.get("error")

        if error:
            self.render("generated_keys.jinja2", count=count, error=error)
        else:
            self.render("generated_keys.jinja2", count=count)

