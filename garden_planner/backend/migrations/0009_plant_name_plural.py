# Generated by Django 2.2.5 on 2019-09-26 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0008_auto_20190925_1430'),
    ]

    operations = [
        migrations.AddField(
            model_name='plant',
            name='name_plural',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]
