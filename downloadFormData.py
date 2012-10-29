__author__ = 'saimanoj'

import model
import admin_handler

class MainPage(admin_handler.AdminHandler):
    def get(self):
        if self.is_admin:
            form_type = self.request.get('formDownload')
            self.response.headers['Content-Type'] = 'text/csv'
            if form_type == 'A':
                attributes = self.formA_attributes
                form_data = model.FormAData.all()
                self.response.headers['Content-Disposition'] = "attachment; filename=formA_data.csv"
            elif form_type == 'B':
                attributes = self.formB_attributes
                form_data = model.FormBData.all()
                self.response.headers['Content-Disposition'] = "attachment; filename=formB_data.csv"
            elif form_type == 'C':
                attributes = self.formC_attributes
                form_data = model.FormCData.all()
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
