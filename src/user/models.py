from django.db import models

# Create your models here.
class UserModel(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="ID")
    user_name = models.CharField(max_length=50, verbose_name="Nom d'utilisateur")
    password = models.CharField(max_length=50, verbose_name="Mot de passe")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Créé à")

    def __str__(self):
        return self.user_name