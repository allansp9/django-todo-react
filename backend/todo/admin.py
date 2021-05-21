from django.contrib import admin
from .models import Todo


class TodoAdmin(admin.ModelAdmin):
    '''Admin View for Todo'''

    list_display = ('title', 'description', 'completed')

# Register your models here.


admin.site.register(Todo, TodoAdmin)
