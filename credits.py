__author__ = 'saimanoj'

import handler
import random

class MainPage(handler.Handler):
    def get(self):
        urls = ['https://www.facebook.com/ysaimanojkumar','https://plus.google.com/116737306836663798171/posts',
                'https://github.com/saimanoj/','https://twitter.com/ysaimanoj',
                'http://in.linkedin.com/in/ysaimanojkumar']
        self.render('credits.jinja2', url = random.choice(urls))

