# Generated by Django 5.0.6 on 2024-07-19 21:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_alter_adminuser_groups_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='AdminUser',
        ),
    ]
