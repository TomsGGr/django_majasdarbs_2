from django.db import models

class Juzeru_klase(models.Model):

    user = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
