# Generated by Django 4.0.5 on 2022-07-06 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CrearDios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30, null=True)),
                ('simbolo', models.CharField(max_length=30, null=True)),
                ('origen', models.CharField(max_length=30, null=True)),
                ('reseña', models.CharField(max_length=30, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='DiosGriego',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('simbolo', models.CharField(max_length=30)),
                ('origen', models.CharField(max_length=30)),
                ('reseña', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='DiosRomano',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('simbolo', models.CharField(max_length=30)),
                ('origen', models.CharField(max_length=30)),
                ('reseña', models.CharField(max_length=1000)),
            ],
        ),
    ]
