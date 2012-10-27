__author__ = 'saimanoj'

import webapp2
import admin_handler

class MainPage(admin_handler.AdminHandler):
    def get(self):
        if self.is_admin:
            self.render("download.jinja2")

#app = webapp2.WSGIApplication([('/download/data', MainPage)], debug=True)
