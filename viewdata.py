__author__ = 'saimanoj'

import admin_handler
import model

class MainPage(admin_handler.AdminHandler):
    def get(self):
        if self.is_admin:
            form_type = self.request.get("formView")
            if form_type == 'A':
                attributes = self.formA_attributes
                form_data = model.FormAData.all()
                count = form_data.count()
                keys_count = model.FormAKeys.all().count()
            elif form_type == 'B':
                attributes = self.formB_attributes
                form_data = model.FormBData.all()
                count = form_data.count()
                keys_count = model.FormBKeys.all().count()
            elif form_type == 'C':
                attributes = self.formC_attributes
                form_data = model.FormCData.all()
                count = form_data.count()
                keys_count = model.FormCKeys.all().count()
            else:
                self.write('Wrong Form Type')
                return

            if form_data and 0 < count < keys_count:
                self.render("view_data.jinja2", count = count, records = form_data, attributes = attributes)
            elif count == keys_count and count != 0:
                self.render("view_data.jinja2", count = count, records = form_data, attributes = attributes,
                    alert = 'Everyone has filled the feedback form.', alert_type = "success")
            else:
                self.render("view_data.jinja2", alert = 'No one has filled the feedback form yet.',
                    alert_type = "warning")
