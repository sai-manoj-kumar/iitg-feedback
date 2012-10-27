__author__ = 'saimanoj'

import webapp2
import handler
import formA

class MainPage(handler.Handler):
    def get(self):
        if self.is_admin:
            self.redirect('/admin')
        else:
            self.render('index.jinja2')


app = webapp2.WSGIApplication(
    [('/', MainPage),
     ('/formA/*', formA.MainPage)],
    debug = True)
