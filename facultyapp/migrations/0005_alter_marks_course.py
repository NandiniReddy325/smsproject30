# Generated by Django 5.0.7 on 2024-10-28 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facultyapp', '0004_alter_marks_course'),
    ]

    operations = [
        migrations.AlterField(
            model_name='marks',
            name='course',
            field=models.CharField(choices=[('AOOP', 'Advanced Object Oriented Programming'), ('PFSD', 'Python FUll Stack Development')], max_length=50),
        ),
    ]
