# Generated by Django 4.0.3 on 2022-03-13 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='phone',
            field=models.IntegerField(max_length=11),
        ),
    ]
