# Generated by Django 3.2.5 on 2021-08-24 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0003_alter_task_task'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='task',
            field=models.CharField(max_length=100, verbose_name='Task'),
        ),
    ]