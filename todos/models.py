from django.db import models

from accounts.models import RegisterUserModel


# Create your models here.
class LabelTodosModel(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = 'Etiquetas'
        verbose_name = 'Etiqueta'

    def __str__(self):
        return self.name


class TodosUserModel(models.Model):
    STATUS_CHOICES = (
        ('pendiente', 'Pendiente'),
        ('en progreso', 'En progreso'),
        ('completada', 'Completada'),
    )

    user = models.ForeignKey(RegisterUserModel, on_delete=models.CASCADE, verbose_name='Nombre Usuario')
    title = models.CharField(max_length=100, verbose_name='Titulo', blank=True)
    description = models.TextField(verbose_name='Descripcion', blank=True)
    observations = models.TextField(verbose_name='Observaciones', blank=True)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='pendiente', verbose_name='Estado',
                              blank=True)
    due_date = models.DateField(verbose_name='Fecha de Vencimiento', blank=True)
    labels = models.ManyToManyField(LabelTodosModel, blank=True, verbose_name='Etiquetas')
    priority = models.ForeignKey('PriorityUserModel', on_delete=models.SET_NULL, null=True, verbose_name='Prioridad',
                                 blank=True)

    class Meta:
        verbose_name_plural = 'Tareas'
        verbose_name = 'Tarea'

    def __str__(self):
        return self.title


class PriorityUserModel(models.Model):
    PRIORITY_CHOICES = (
        ('alta', 'Alta'),
        ('media', 'Media'),
        ('baja', 'Baja')
    )
    priority = models.CharField(max_length=50, choices=PRIORITY_CHOICES, default='media', verbose_name='Prioridad')

    def __str__(self):
        return self.priority

    class Meta:
        verbose_name_plural = 'Prioridades'
        verbose_name = 'Prioridad'
