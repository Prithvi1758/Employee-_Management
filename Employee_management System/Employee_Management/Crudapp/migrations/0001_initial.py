# Generated by Django 5.1.5 on 2025-04-02 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('Roll_no', models.IntegerField(primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=50)),
                ('Email', models.EmailField(max_length=30)),
            ],
            options={
                'db_table': 'Student_details',
            },
        ),
    ]
