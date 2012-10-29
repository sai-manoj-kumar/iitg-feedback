__author__ = 'saimanoj'

import admin_handler
import model

class MainPage(admin_handler.AdminHandler):
    def get(self):
        if self.is_admin:
            form_type = self.request.get("formView")
            if form_type == 'A':
                attributes = ['rating2_1', 'rating2_2', 'rating2_3', 'rating3_1', 'rating3_2', 'rating3_3', 'rating3_4',
                          'rating3_5', 'rating3_6', 'rating4_1', 'rating4_2', 'rating4_3', 'rating4_4', 'rating4_5',
                          'rating4_6', 'rating4_7', 'rating4_8', 'rating4_9', 'rating4_10', 'rating5_1', 'rating5_2',
                          'rating5_3', 'rating5_4', 'rating5_5']
                form_data = model.FormAData.all()
                count = form_data.count()
                keys_count = model.FormAKeys.all().count()
            elif form_type == 'B':
                attributes = ['rating2_1', 'rating2_2', 'rating2_3', 'rating2_4', 'rating2_5', 'rating3_1',
                              'rating3_2', 'rating3_3', 'rating3_4', 'rating3_5', 'rating3_6', 'rating3_7',
                              'rating3_8', 'rating3_9', 'rating3_10']
                form_data = model.FormBData.all()
                count = form_data.count()
                keys_count = model.FormBKeys.all().count()
            elif form_type == 'C':
                attributes =[]
#                form_data = model.FormCData.all()
#                count = form_data.count()
#                keys_count = model.FormCKeys.all().count()
            else:
                self.write('Wrong Form Type')
                return

            if form_data and 0 < count < keys_count:
                self.render("view_data.jinja2", count = count, records = form_data, attributes = attributes)
            elif count == keys_count:
                self.render("view_data.jinja2", count = count, records = form_data, attributes = attributes,
                    alert = 'Everyone has filled the feedback form.', alert_type = "success")
            else:
                self.render("view_data.jinja2", alert = 'No one has filled the feedback form yet.',
                    alert_type = "warning")
