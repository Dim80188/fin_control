# Generated by Django 3.2.7 on 2022-01-10 09:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('h_finance', '0004_alter_inkome_data'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='inkome',
            options={'ordering': ['-data_i']},
        ),
        migrations.RenameField(
            model_name='inkome',
            old_name='data',
            new_name='data_i',
        ),
    ]
