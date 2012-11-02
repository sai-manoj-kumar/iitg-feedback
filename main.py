__author__ = 'saimanoj'

import webapp2
import handler
import formA, formB, formC
import failOne
import failTwo
import failThree
import success

class MainPage(handler.Handler):
    def get(self):
        if self.is_admin:
            self.redirect('/admin')
        else:
            self.render('index.jinja2')


app = webapp2.WSGIApplication(
    [('/', MainPage),
     ('/success/*', success.MainPage),
     ('/fail1/*', failOne.MainPage),
     ('/fail2/*', failTwo.MainPage),
     ('/fail3/*', failThree.MainPage),
     ('/formA/*', formA.MainPage),
     ('/formB/*', formB.MainPage),
     ('/formC/*', formC.MainPage)],
    debug = True)
