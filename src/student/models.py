from django.db import models
from datetime import date


# Create your models here.
class StudentModel(models.Model):
    GENDER_CHOICES = [
        ('M', 'Masculin'),
        ('F', 'Feminin'),

    ]
    id = models.AutoField(primary_key=True, verbose_name="ID")
    first_name = models.CharField(null=True, blank=True, max_length=50, verbose_name="Prénom")
    last_name = models.CharField(max_length=50, null=True, blank=True, verbose_name="Nom de famille")
    city = models.CharField(max_length=50, null=True, blank=True, verbose_name="Ville")
    phone = models.CharField(max_length=20, verbose_name="Téléphone")
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, verbose_name="Genre")
    address = models.TextField(blank=True, verbose_name="Adresse")
    date_of_birth = models.DateField(null=True, blank=True, verbose_name="Date de naissance")
    level = models.CharField(max_length=50, verbose_name="Niveau")
    reg_number = models.CharField(max_length=50, null=True, blank=True, verbose_name="Numéro d'inscription")

    def __str__(self):
        return self.first_name + ' ' + self.last_name

    def get_age(self):
        return date.today().year - self.date_of_birth.year
