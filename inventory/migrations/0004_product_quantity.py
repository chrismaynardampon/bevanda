# Generated by Django 5.1.4 on 2024-12-09 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0003_ingredient'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='quantity',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
