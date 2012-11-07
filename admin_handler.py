__author__ = 'saimanoj'

from google.appengine.api import users
import handler

class AdminHandler(handler.Handler):
    def initialize(self, *a, **kw):
        handler.Handler.initialize(self, *a, **kw)
        if not self.is_logged_in:
            self.redirect(users.create_login_url(self.request.uri))
        elif not self.is_admin:
            self.write('You are not logged in as admin.\n'
                       'If you are admin, <a href="/admin/logout">logout</a> your current google account and login to your admin account.')
