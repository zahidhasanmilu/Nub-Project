# Generated by Django 4.0.3 on 2022-03-15 04:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0006_remove_order_pid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='price',
        ),
        migrations.RemoveField(
            model_name='order',
            name='qty',
        ),
        migrations.RemoveField(
            model_name='order',
            name='uid',
        ),
    ]
