from django.db import models
from django.utils.translation import gettext_lazy as _

class Campus(models.Model):
    
    label = 'Código Moodle'
    codigo_moodle = models.IntegerField(_(label), unique=True, null=False)

    label = 'Código SUAP'
    codigo_suap = models.IntegerField(_('Código SUAP'), unique=True, null=False)
    
    label = 'Nome'
    nome = models.CharField(_(label), max_length=100)
    
    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = _('Campus')
        verbose_name_plural = _('Campus')


class Curso(models.Model):
    
    label = 'Código Moodle'
    t_help = 'Deve ser o mesmo código do Moodle'
    codigo_moodle = models.IntegerField(_(label), help_text=_(t_help), unique=True, null=False)
    
    label = 'Código SUAP'
    codigo_suap = models.IntegerField(_('Código SUAP'), unique=True, null=False)
    
    label = 'Nome'
    nome = models.CharField(_(label), max_length=100)
    
    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = _('Curso')
        verbose_name_plural = _('Cursos')


class Papel(models.Model):
    
    label = 'Código Moodle'
    codigo_moodle = models.IntegerField(_(label), unique=True, null=False)

    label = 'Código SUAP'
    codigo_suap = models.IntegerField(_('Código SUAP'), unique=True, null=False)
    
    label = 'Nome'
    nome = models.CharField(_(label), max_length=100)

    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = _('Papel')
        verbose_name_plural = _('Papeis')


