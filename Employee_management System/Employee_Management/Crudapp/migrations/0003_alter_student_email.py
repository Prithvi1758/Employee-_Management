# Generated by Django 5.1.4 on 2025-04-08 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Crudapp', '0002_student_department'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='Email',
            field=models.EmailField(max_length=30, unique=True),
        ),
    ]
