# Generated by Django 4.0.6 on 2022-07-22 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0031_alter_products_pid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='pid',
            field=models.IntegerField(auto_created=True, primary_key=True, serialize=False),
        ),
    ]