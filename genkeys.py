__author__ = 'saimanoj'

from google.appengine.api import users
from google.appengine.ext import db
import random
import string
import model
import handler

class GenerateKeys(handler.Handler):
    def post(self):
        if self.is_logged_in:
            if self.is_admin:
                num_keys = int(self.request.get("num_keys"))
                key_entries = []
                keys = []
                i = 0
                while i < num_keys:
                    key = ''.join(random.choice(
                        'abcdefghkmnqrstuvwxyzABCDEFGHJKMNQRSTUVWXYZ' * 7 + '23456789' * 13) for x in range(10))
                    if key not in keys:
                        keys.append(key)
                        key_entries.append(model.Keys(keyPhrase=key, formFilled=False))
                        i += 1
                result = db.put(key_entries)
                if result:
                    self.redirect('/admin/genkeys')
                #                    write("Keys generated and stored successfully")
                else:
                    self.write("Keys Can't be stored")
            else:
                self.write("You are not an admin and can not perform Key generation")
        else:
            self.redirect(users.create_login_url(self.request.uri))

    def get(self):
        self.render("notify_admin.jinja2")
