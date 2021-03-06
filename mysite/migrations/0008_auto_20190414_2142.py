# Generated by Django 2.1.1 on 2019-04-14 21:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0007_auto_20190414_2130'),
    ]

    operations = [
        migrations.AddField(
            model_name='film',
            name='name',
            field=models.TextField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='person',
            name='gender',
            field=models.CharField(choices=[('Female', 'Female'), ('Male', 'Male')], default='male', max_length=7),
        ),
        migrations.AlterField(
            model_name='person',
            name='year',
            field=models.CharField(choices=[('sophomore', 'sophomore'), ('senior', 'senior'), ('graduate', 'graduate'), ('freshman', 'freshman'), ('junior', 'junior')], default='freshman', max_length=20),
        ),
    ]
