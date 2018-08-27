from django.db import models
from django.utils.translation import gettext_lazy as _

class Campus(models.Model):
    
    codigo_moodle = models.IntegerField(_('Código Moodle'), unique=True, null=False)
    codigo_suap = models.IntegerField(_('Código SUAP'), unique=True, null=False)
    nome = models.CharField(_('Nome'), max_length=100)
    
    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = _('Campus')
        verbose_name_plural = _('Campus')


class Curso(models.Model):

    codigo_moodle = models.IntegerField(_('Código Moodle'), unique=True, null=False)
    codigo_suap = models.IntegerField(_('Código SUAP'), unique=True, null=False)
    nome = models.CharField(_('Nome'), max_length=100)
    
    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = _('Curso')
        verbose_name_plural = _('Cursos')


class Papel(models.Model):
    
    codigo_moodle = models.IntegerField(_('Código Moodle'), unique=True, null=False)
    codigo_suap = models.IntegerField(_('Código SUAP'), unique=True, null=False)
    nome = models.CharField(_('Nome'), max_length=100)

    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = _('Papel')
        verbose_name_plural = _('Papeis')


