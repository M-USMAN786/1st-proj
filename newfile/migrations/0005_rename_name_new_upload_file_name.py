# Generated by Django 5.0.7 on 2024-08-01 23:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newfile', '0004_rename_file_name_new_upload_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='new_upload',
            old_name='name',
            new_name='file_name',
        ),
    ]
