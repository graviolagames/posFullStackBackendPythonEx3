# Generated by Django 4.2.1 on 2023-05-27 23:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0002_rename_avatar_inventory_idavatar_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='inventory',
            old_name='idAvatar',
            new_name='avatar',
        ),
        migrations.RenameField(
            model_name='inventory',
            old_name='idItem',
            new_name='item',
        ),
    ]