# Generated by Django 2.1.1 on 2019-04-18 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0024_auto_20190418_0728'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='year',
            field=models.CharField(choices=[('senior', 'senior'), ('sophomore', 'sophomore'), ('junior', 'junior'), ('graduate', 'graduate'), ('freshman', 'freshman')], default='', max_length=20),
        ),
    ]
