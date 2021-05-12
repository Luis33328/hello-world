from django.contrib import admin

from .models import Disciplina, Curso, Matricula

admin.site.register(Disciplina)
admin.site.register(Curso)
admin.site.register(Matricula)
