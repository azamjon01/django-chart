# Generated by Django 4.0.4 on 2022-05-27 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_home_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='home',
            name='brend',
            field=models.CharField(default=1, max_length=90),
            preserve_default=False,
        ),
    ]
