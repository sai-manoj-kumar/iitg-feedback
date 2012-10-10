__author__ = 'saimanoj'

from google.appengine.api import users
import random
import string
import model
import handler
import config

class GenerateKeys(handler.Handler):
    def get(self):
        if self.user :
            if self.user.nickname() in config.admins:
                key = ''.join(random.choice('abcdefghkmnqrstuvwxyzABCDEFGHJKMNQRSTUVWXYZ'*7 + string.digits*13) for x in range(10))
                key_entry = model.Keys(keyPhrase=key, formFilled=False)
                if key_entry.put():
                    self.write("Keys generated and stored successfully")
                else:
                    self.write("Keys Can't be stored")
            else:
                self.write("You are not an admin and can not perform Key generation")
        else:
            self.redirect(users.create_login_url(self.request.uri))
