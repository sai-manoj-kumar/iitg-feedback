__author__ = 'saimanoj'

import webapp2
import handler

class MainPage(handler.Handler):
    def get(self):
        self.write("Hello, Download World")

app = webapp2.WSGIApplication([('/download/1a2b3cd456gh', MainPage)], debug=True)

