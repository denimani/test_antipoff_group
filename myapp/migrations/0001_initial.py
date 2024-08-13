# Generated by Django 5.1 on 2024-08-13 21:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CadastralQuery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cadastral_number', models.CharField(max_length=100, verbose_name='Кадастровый номер')),
                ('latitude', models.FloatField(verbose_name='Широта')),
                ('longitude', models.FloatField(verbose_name='Долгота')),
                ('response', models.BooleanField(blank=True, null=True)),
            ],
        ),
    ]