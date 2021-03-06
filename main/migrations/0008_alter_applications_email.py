# Generated by Django 4.0.1 on 2022-01-26 19:42

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_alter_applications_email_alter_applications_mobile_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applications',
            name='email',
            field=models.EmailField(help_text='Укажите ваш действующий Email', max_length=100, validators=[django.core.validators.EmailValidator(message='Введите корректный email!')], verbose_name='Почта'),
        ),
    ]
