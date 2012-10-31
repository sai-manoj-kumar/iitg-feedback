__author__ = 'saimanoj'

import handler
import model

class MainPage(handler.Handler):
    def get(self):
        self.render('formA.jinja2')

    def post(self):
        key = self.request.get('key')
        values = {}
        if not key or key == '':
            self.render('formA.jinja2', error = 'Key is not entered')
            return

        for attr in self.formA_attributes:
            val = self.request.get(attr)
            if (val == '1' or val == '2' or val == '3' or val == '4' or val == '5'):
                values[attr] = int(val)
            else:
                self.render('formA.jinja2', error = 'You should select all the options')
                return

        values['comment'] = self.request.get('comment')
        key_record = model.FormAKeys.by_name(key)

        if key_record:
            if not key_record.formFilled:
                feedback_entry = model.FormAData(keyPhrase = key, **values)
                key_record.formFilled = True
                if key_record.put() and feedback_entry.put():
                    self.redirect('/success')
                else:
                    self.redirect('/fail1')
            else:
                self.redirect('/fail2')
        else:
            self.redirect('/fail3')
