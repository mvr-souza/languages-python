from django.contrib import admin
from .models import Course


# ModelAdmin para customização do site de administração
class CourseAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'start_date', 'created_at']
    search_fields = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

# Registro do modelo.
admin.site.register(Course, CourseAdmin)
