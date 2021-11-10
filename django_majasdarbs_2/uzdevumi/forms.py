from django.forms import (Form, CharField)

class UserEmailForm(Form):
    username = CharField()
    email = CharField()