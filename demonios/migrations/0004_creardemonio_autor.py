# Generated by Django 4.0.5 on 2022-07-25 03:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demonios', '0003_alter_creardemonio_reseña'),
    ]

    operations = [
        migrations.AddField(
            model_name='creardemonio',
            name='autor',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
