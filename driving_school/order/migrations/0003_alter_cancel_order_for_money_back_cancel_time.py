# Generated by Django 3.2 on 2021-04-18 08:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_cancel_order_for_money_back'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cancel_order_for_money_back',
            name='Cancel_Time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 4, 18, 8, 38, 14, 129277)),
        ),
    ]
