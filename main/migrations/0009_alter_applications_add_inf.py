# Generated by Django 4.0.1 on 2022-01-26 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_alter_applications_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applications',
            name='add_inf',
            field=models.TextField(blank='True', verbose_name='Дополнительная информация'),
        ),
    ]
