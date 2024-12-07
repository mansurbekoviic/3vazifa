# Generated by Django 5.0.6 on 2024-12-07 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Kurs nomi')),
                ('description', models.TextField(verbose_name='Kurs tavsiyasi')),
                ('created_on', models.DateTimeField(auto_now_add=True, verbose_name='Yaratilgan vaqti')),
                ('updated_on', models.DateTimeField(auto_now=True, verbose_name='Yangilangan vaqti')),
            ],
        ),
    ]
