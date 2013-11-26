__author__ = 'saimanoj'

import handler
import random


class MainPage(handler.Handler):
    def get(self):
        urls = ['https://www.facebook.com/ysaimanojkumar', 'https://www.google.com/+SaiManojKumarYadlapati',
                'https://github.com/ysaimanojkumar']
        self.render('credits.jinja2', url=random.choice(urls))

