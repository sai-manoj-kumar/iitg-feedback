__author__ = 'saimanoj'

import handler

class MainPage(handler.Handler):
    def get(self):
        self.render('credits.jinja2')

