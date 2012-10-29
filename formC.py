__author__ = 'saimanoj'

import handler
import model

class MainPage(handler.Handler):
    def get(self):
        self.render('formC.jinja2')

    def post(self):
        key = self.request.get('key')
        values = {}
        for i in range(1, 4):
            values['rating2_' + str(i)] = int(self.request.get('rating2.' + str(i)))

        for i in range(1, 6):
            values['rating3_' + str(i)] = int(self.request.get('rating3.' + str(i)))

        for i in range(1, 11):
            values['rating4_' + str(i)] = int(self.request.get('rating4.' + str(i)))

        values['comment'] = self.request.get('comment')
        key_record = model.FormCKeys.by_name(key)

        if key_record:
            if not key_record.formFilled:
                feedback_entry = model.FormCData(keyPhrase=key, **values)
                key_record.formFilled = True
                if key_record.put() and feedback_entry.put():
                    self.write("Form C Submission Successful.")
                else:
                    self.write("Error writing to database")
            else:
                self.write("You have already filled the form")
        else:
            self.write("Entered key is wrong")
