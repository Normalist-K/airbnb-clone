# Generated by Django 2.2.5 on 2020-01-02 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0006_auto_20191114_0047'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='guests',
            field=models.IntegerField(help_text='How many people will be staying?'),
        ),
    ]