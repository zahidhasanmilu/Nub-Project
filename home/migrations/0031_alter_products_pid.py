# Generated by Django 4.0.6 on 2022-07-22 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0030_alter_products_pid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='pid',
            field=models.CharField(auto_created=True, max_length=50, primary_key=True, serialize=False),
        ),
    ]
