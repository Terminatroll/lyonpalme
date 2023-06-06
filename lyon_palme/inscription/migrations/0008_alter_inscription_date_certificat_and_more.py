# Generated by Django 4.1.4 on 2023-06-06 10:43

from django.db import migrations, models
import django_cryptography.fields


class Migration(migrations.Migration):

    dependencies = [
        ('inscription', '0007_alter_inscription_code_postal'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inscription',
            name='date_certificat',
            field=django_cryptography.fields.encrypt(models.DateField(max_length=50, null=True)),
        ),
        migrations.AlterField(
            model_name='inscription',
            name='date_inscription',
            field=django_cryptography.fields.encrypt(models.DateField(max_length=50)),
        ),
        migrations.AlterField(
            model_name='inscription',
            name='date_naissance',
            field=django_cryptography.fields.encrypt(models.DateField(max_length=50)),
        ),
    ]