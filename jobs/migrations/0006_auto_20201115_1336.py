# Generated by Django 3.1.2 on 2020-11-15 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0005_auto_20201113_2314'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='publication_date',
            field=models.DateTimeField(),
        ),
    ]
