__author__ = 'saimanoj'

import random
import string
import model
import handler

class GenerateKeys(handler.Handler):
    def get(self):
        key = ''.join(random.choice('abcdefghkmnqrstuvwxyzABCDEFGHJKMNQRSTUVWXYZ'*7 + string.digits*13) for x in range(10))
        key_entry = model.Keys(keyPhrase=key, formFilled=False)
        if key_entry.put():
            self.write("Keys generated and stored successfully")

