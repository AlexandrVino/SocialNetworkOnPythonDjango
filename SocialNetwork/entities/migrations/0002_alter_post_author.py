# Generated by Django 3.2 on 2021-04-11 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entities', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.IntegerField(null=True),
        ),
    ]