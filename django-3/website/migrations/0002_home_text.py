# Generated by Django 4.0.4 on 2022-05-27 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='home',
            name='text',
            field=models.CharField(default=1, max_length=70),
            preserve_default=False,
        ),
    ]