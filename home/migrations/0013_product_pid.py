# Generated by Django 4.0.3 on 2022-03-08 23:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_remove_product_pid'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='pid',
            field=models.ImageField(default=0, upload_to=''),
        ),
    ]
