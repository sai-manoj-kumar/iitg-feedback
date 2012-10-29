__author__ = 'saimanoj'

import model
import admin_handler

class MainPage(admin_handler.AdminHandler):
    def get(self):
        if self.is_admin:
            form_type = self.request.get('formDownload')
            self.response.headers['Content-Type'] = 'text/csv'
            if form_type == 'A':
                attributes = ['rating2_1', 'rating2_2', 'rating2_3', 'rating3_1', 'rating3_2', 'rating3_3', 'rating3_4',
                              'rating3_5', 'rating3_6', 'rating4_1', 'rating4_2', 'rating4_3', 'rating4_4', 'rating4_5',
                              'rating4_6', 'rating4_7', 'rating4_8', 'rating4_9', 'rating4_10', 'rating5_1', 'rating5_2',
                              'rating5_3', 'rating5_4', 'rating5_5']
                form_data = model.FormAData.all()
                self.response.headers['Content-Disposition'] = "attachment; filename=formA_data.csv"
            elif form_type == 'B':
                attributes = ['rating2_1', 'rating2_2', 'rating2_3', 'rating2_4', 'rating2_5', 'rating3_1',
                              'rating3_2', 'rating3_3', 'rating3_4', 'rating3_5', 'rating3_6', 'rating3_7',
                              'rating3_8', 'rating3_9', 'rating3_10']
                form_data = model.FormBData.all()
                self.response.headers['Content-Disposition'] = "attachment; filename=formB_data.csv"
            elif form_type == 'C':
                attributes = []
#                form_data = model.FormCData.all()
                self.response.headers['Content-Disposition'] = "attachment; filename=formC_data.csv"
            else:
                self.write('Wrong Form Type')
                return
            
            form_data = list(form_data)
            for attr in attributes:
                self.write(attr + ',')
            self.write('comment\n')

            for record in form_data:
                for attr in attributes:
                    self.write(str(getattr(record, attr)) + ',')
                self.write(getattr(record, 'comment') + '\n')
