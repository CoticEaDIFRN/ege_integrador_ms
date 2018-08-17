from django.db import models

class Papel(models.Model):
    codigo_moodle = models.IntegerField(unique=True, null=False)
    codigo_suap = models.IntegerField(unique=True, null=False)
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome