__author__ = 'saimanoj'

from google.appengine.api import users
from google.appengine.ext import db
import random
import string
import time
import model
import handler

class GenerateKeys(handler.Handler):
    def post(self):
        if self.is_logged_in:
            if self.is_admin:
                num_keys = int(self.request.get("num_keys"))
#                timestamp = time.time()
                key_entries = []
                for i in range(num_keys):
                    key = ''.join(random.choice(
                        'abcdefghkmnqrstuvwxyzABCDEFGHJKMNQRSTUVWXYZ' * 7 + string.digits * 13) for x in range(10))
                    key_entries.append(model.Keys(keyPhrase=key, formFilled=False))
                if db.put(key_entries):
                    self.write("Keys generated and stored successfully")
                else:
                    self.write("Keys Can't be stored")
            else:
                self.write("You are not an admin and can not perform Key generation")
        else:
            self.redirect(users.create_login_url(self.request.uri))
