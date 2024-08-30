from datetime import date

from django.db import models

class TeacherModel(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="ID")
    first_name = models.CharField(max_length=50, verbose_name="Prénom")
    last_name = models.CharField(max_length=50, verbose_name="Nom")
    city = models.CharField(max_length=50, verbose_name="Ville")
    phone = models.CharField(max_length=50, verbose_name="Téléphone")
    address = models.TextField(verbose_name="Adresse")
    date_of_birth = models.DateField(verbose_name="Date de naissance")
    subject = models.CharField(max_length=50, verbose_name="Matière")
    vacant = models.CharField(max_length=50, verbose_name="Vacant")
    next_meeting_subject = models.CharField(max_length=50, verbose_name="Sujet de la prochaine réunion")

    def __str__(self):
        return self.first_name + ' ' + self.last_name

    def get_age(self):
        return date.today().year - self.date_of_birth.year