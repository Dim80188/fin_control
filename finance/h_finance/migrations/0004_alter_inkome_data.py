# Generated by Django 3.2.7 on 2022-01-10 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('h_finance', '0003_inkome'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inkome',
            name='data',
            field=models.DateField(null=True),
        ),
    ]
