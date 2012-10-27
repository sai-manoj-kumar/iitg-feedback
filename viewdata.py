__author__ = 'saimanoj'

import handler
import model

class MainPage(handler.Handler):
    def get(self):
        if self.is_admin:
            attributes = ['rating2_1', 'rating2_2', 'rating2_3', 'rating3_1', 'rating3_2', 'rating3_3', 'rating3_4',
                          'rating3_5', 'rating3_6', 'rating4_1', 'rating4_2', 'rating4_3', 'rating4_4', 'rating4_5',
                          'rating4_6', 'rating4_7', 'rating4_8', 'rating4_9', 'rating4_10', 'rating5_1', 'rating5_2',
                          'rating5_3', 'rating5_4', 'rating5_5']

            formA_data = model.FormA.all()
            count = formA_data.count()
            keys_count = model.Keys.all().count()
            if formA_data and 0 < count < keys_count:
                self.render("view_data.jinja2", count = count, records = formA_data, attributes = attributes)
            elif count == keys_count:
                self.render("view_data.jinja2", count = count, records = formA_data, attributes = attributes,
                    alert = 'Everyone has filled the feedback form.', alert_type = "success")
            else:
                self.render("view_data.jinja2", alert = 'No one has filled the feedback form yet.',
                    alert_type = "warning")
        else:
            self.write("You are not an admin and can not perform this operation.")

