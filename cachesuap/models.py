from django.db import models
from django.utils.translation import gettext_lazy as _

class Campus(models.Model):
    
    label = 'Código Moodle'
    codigo_moodle = models.IntegerField(_(label), unique=True, null=False, help_text="Informe o código do Moodle")

    label = 'Código SUAP'
    codigo_suap = models.IntegerField(_('Código SUAP'), unique=True, null=False, help_text="Informe o código do SUAP")
    
    label = 'Nome'
    nome = models.CharField(_(label), max_length=100, help_text="Informe o nome do Campus")

    created_at = models.DateTimeField('Criado em', auto_now=True)

    
    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = _('Campus')
        verbose_name_plural = _('Campi')
        ordering = ['nome'] 
        

class Curso(models.Model):
    
    label = 'Código Moodle'
    codigo_moodle = models.IntegerField(_(label), unique=True, null=False, help_text="Informe o código do Moodle")
    
    label = 'Código SUAP'
    codigo_suap = models.IntegerField(_(label), unique=True, null=False, help_text="Informe o código do SUAP")
    
    label = 'Nome'
    nome = models.CharField(_(label), max_length=100, help_text="Informe o nome do Curso")

    created_at = models.DateTimeField('Criado em', auto_now=True)
    
    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = _('Curso')
        verbose_name_plural = _('Cursos')
        ordering = ['nome']


class Papel(models.Model):
    
    label = 'Código Moodle'
    codigo_moodle = models.IntegerField(_(label), unique=True, null=False, help_text="Informe o código do Moodle")

    label = 'Código SUAP'
    codigo_suap = models.IntegerField(_('Código SUAP'), unique=True, null=False, help_text="Informe o código do SUAP")
    
    label = 'Nome'
    nome = models.CharField(_(label), max_length=100, help_text="Informe qual o seu Papel. Ex.: Professor(a), Aluno(a)")

    created_at = models.DateTimeField('Criado em', auto_now=True)


    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = _('Papel')
        verbose_name_plural = _('Papeis')
        ordering = ['nome'] #Ordena o Papel por ordem crescente 'Nome'


