# Generated by Django 3.2.8 on 2021-12-08 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0027_auto_20211208_1316'),
    ]

    operations = [
        migrations.AddField(
            model_name='lot',
            name='status',
            field=models.BooleanField(default=1),
        ),
    ]
