# Generated by Django 4.2.1 on 2023-05-27 13:19

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('avatar', '0002_inventory_alter_avatar_idinventory'),
    ]

    operations = [
        migrations.AddField(
            model_name='inventory',
            name='name',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
    ]