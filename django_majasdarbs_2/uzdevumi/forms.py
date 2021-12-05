from django.forms import (Form, CharField, FileField)


class UploadCsvForm(Form):
    izvēlies_csv_failu = FileField()



class UserEmailForm(Form):
    username = CharField()
    email = CharField()


