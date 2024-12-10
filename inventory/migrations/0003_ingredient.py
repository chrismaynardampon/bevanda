# Generated by Django 5.1.4 on 2024-12-09 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0002_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('quantity', models.PositiveIntegerField()),
                ('stock_in_date', models.DateField(blank=True, null=True)),
                ('stock_in_time', models.TimeField(blank=True, null=True)),
                ('stock_out_date', models.DateField(blank=True, null=True)),
                ('stock_out_time', models.TimeField(blank=True, null=True)),
            ],
        ),
    ]