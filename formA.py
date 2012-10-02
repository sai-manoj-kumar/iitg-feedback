__author__ = 'saimanoj'

import handler
import model

class MainPage(handler.Handler):
    def get(self):
        self.render('formA.jinja2')

    def post(self):
        key = self.request.get('key')
        values = {}
        for i in range(1, 4):
            values['rating2_' + str(i)] = int(self.request.get('rating2.' + str(i)))

        for i in range(1, 7):
            values['rating3_' + str(i)] = int(self.request.get('rating3.' + str(i)))

        for i in range(1, 11):
            values['rating4_' + str(i)] = int(self.request.get('rating4.' + str(i)))

        for i in range(1, 6):
            values['rating5_' + str(i)] = int(self.request.get('rating5.' + str(i)))

        values['comment'] = self.request.get('comment')
        entry = model.FormA(keyPhrase=key, **values)
        if entry.put():
            self.write("Successfully Written in database")

