# Generated by Django 4.0.1 on 2022-02-01 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_alter_applications_consent'),
    ]

    operations = [
        migrations.AddField(
            model_name='reviews',
            name='publication',
            field=models.BooleanField(default=False, verbose_name='Публикация'),
        ),
    ]
