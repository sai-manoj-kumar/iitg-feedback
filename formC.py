__author__ = 'saimanoj'

import handler
import model

class MainPage(handler.Handler):
    def get(self):
        self.render('formC.jinja2')

    def post(self):
        key = self.request.get('key')
        values = {}
        if not key or key == '':
            self.write('Key is not entered')
            return

        for attr in self.formC_attributes:
            val = self.request.get(attr)
            if val or val != '':
                values[attr] = int(val)
            else:
                self.write('You should enter all form fields.')
                return

        values['comment'] = self.request.get('comment')
        key_record = model.FormCKeys.by_name(key)

        if key_record:
            if not key_record.formFilled:
                feedback_entry = model.FormCData(keyPhrase=key, **values)
                key_record.formFilled = True
                if key_record.put() and feedback_entry.put():
                    self.redirect('/success')
                else:
                    self.redirect('/fail1')
            else:
                self.redirect('/fail2')
        else:
            self.redirect('/fail3')
