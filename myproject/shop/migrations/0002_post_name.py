# Generated by Django 2.1.1 on 2021-07-01 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='name',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]