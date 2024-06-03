from django.contrib import admin

from .models import LabelTodosModel, TodosUserModel, PriorityUserModel


# Register your models here.
@admin.register(LabelTodosModel)
class LabelTodosModelAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(TodosUserModel)
class TodosUserModelAdmin(admin.ModelAdmin):
    list_display = ('user', 'title', 'description', 'status', 'due_date', 'display_labels', 'priority')

    def display_labels(self, obj):
        labels = obj.labels.all()
        return ', '.join(label.name for label in labels)

    display_labels.short_description = 'Etiquetas'


@admin.register(PriorityUserModel)
class PriorityUserModelAdmin(admin.ModelAdmin):
    list_display = ('priority',)
