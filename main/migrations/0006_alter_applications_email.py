# Generated by Django 4.0.1 on 2022-01-26 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_applications_consent_alter_reviews_consent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applications',
            name='email',
            field=models.EmailField(max_length=50, verbose_name='Почта'),
        ),
    ]
