from django.contrib import admin
from .models import Campus
from .models import Curso
from .models import Papel


class CampusAdmin(admin.ModelAdmin):

    list_display = ['nome', 'created_at']
    search_fields = ['id','nome', 'codigo_moodle', 'codigo_suap', 'created_at']


class CursoAdmin(admin.ModelAdmin):

    list_display = ['nome', 'created_at']
    search_fields = ['id','nome', 'codigo_moodle', 'codigo_suap', 'created_at']

class PapelAdmin(admin.ModelAdmin):

    list_display = ['nome', 'created_at']
    search_fields = ['id','nome', 'codigo_moodle', 'codigo_suap', 'created_at']



admin.site.register(Campus, CampusAdmin)
admin.site.register(Curso, CursoAdmin)
admin.site.register(Papel, PapelAdmin)
