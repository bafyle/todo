# Generated by Django 3.2.5 on 2021-08-23 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task', models.TextField(verbose_name='Task')),
                ('added_date', models.DateTimeField(verbose_name='Creation date')),
                ('due_date', models.DateField(blank=True, null=True, verbose_name='Due date')),
                ('completed', models.BooleanField()),
            ],
        ),
    ]