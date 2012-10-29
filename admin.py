__author__ = 'saimanoj'

import webapp2
import admin_handler
import downloadFormData
import viewkeys
import downloadkeys
import genkeys
import viewdata

class MainPage(admin_handler.AdminHandler):
    def get(self):
        if self.is_admin:
            self.render("admin.jinja2")

app = webapp2.WSGIApplication([
    ('/admin/*', MainPage),
    ('/admin/viewkeys/*', viewkeys.MainPage),
    ('/admin/downloadkeys/*', downloadkeys.MainPage),
    ('/admin/viewdata/*', viewdata.MainPage),
    ('/admin/genkeys/*', genkeys.MainPage),
    ('/admin/download/*', downloadFormData.MainPage)],
    debug = True)
