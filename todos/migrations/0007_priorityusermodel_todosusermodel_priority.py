# Generated by Django 5.0.6 on 2024-06-03 20:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0006_alter_todosusermodel_description_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='PriorityUserModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('priority', models.CharField(choices=[('alta', 'Alta'), ('media', 'Media'), ('baja', 'Baja')], default='media', max_length=50, verbose_name='Prioridad')),
            ],
            options={
                'verbose_name': 'Prioridad',
                'verbose_name_plural': 'Prioridades',
            },
        ),
        migrations.AddField(
            model_name='todosusermodel',
            name='priority',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='todos.priorityusermodel', verbose_name='Prioridad'),
        ),
    ]
