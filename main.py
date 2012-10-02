__author__ = 'saimanoj'

import webapp2
import handler

class MainPage(handler.Handler):
    def get(self):
        self.render()

app = webapp2.WSGIApplication([('/', MainPage)], debug=True)

