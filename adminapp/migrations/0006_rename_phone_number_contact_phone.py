# Generated by Django 5.0.7 on 2024-10-30 09:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0005_alter_contact_address_alter_contact_email_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='phone_number',
            new_name='phone',
        ),
    ]
