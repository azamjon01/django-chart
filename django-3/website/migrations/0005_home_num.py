# Generated by Django 4.0.4 on 2022-05-30 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0004_home_brend'),
    ]

    operations = [
        migrations.AddField(
            model_name='home',
            name='num',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
