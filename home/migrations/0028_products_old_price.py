# Generated by Django 4.0.6 on 2022-07-22 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0027_alter_products_pid'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='old_price',
            field=models.FloatField(default=0),
        ),
    ]
