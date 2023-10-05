from django.contrib import admin
from school_api.models import Student, Course, Registration

class Students(admin.ModelAdmin):
    list_display = ('id', 'nome', 'rg', 'cpf', 'data_nascimento')
    list_display_links = ('id', 'nome')
    search_fields = ('id', 'nome',)
    list_per_page = 20


admin.site.register(Student, Students)

class Courses(admin.ModelAdmin):
    list_display = ('id', 'codigo_curso', 'descricao', 'nivel')
    list_display_links = ('id', 'codigo_curso')
    search_fields = ('id', 'codigo_curso',)
    list_per_page = 20

admin.site.register(Course, Courses)


class Registrations(admin.ModelAdmin):
    list_display = ('id', 'student', 'course', 'periodo')
    list_display_links = ('id',)

admin.site.register(Registration, Registrations)



