# Generated by Django 5.1.4 on 2024-12-09 12:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0007_delete_ingredient'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='stock_in_time',
        ),
        migrations.RemoveField(
            model_name='product',
            name='stock_out_time',
        ),
    ]
