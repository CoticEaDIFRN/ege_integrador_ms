from django.db import models

class Campus(models.Model):
    codigo_moodle = models.IntegerField(unique=True, null=False)
    codigo_suap = models.IntegerField(unique=True, null=False)
    nome_campus = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nome_campus