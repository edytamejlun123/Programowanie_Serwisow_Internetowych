# Generated by Django 4.2.9 on 2024-01-06 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Auto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.FloatField()),
                ('gearbox', models.CharField(choices=[('manual', 'manual'), ('automat', 'automat'), ('hybryd', 'hybryd')], max_length=255)),
            ],
            options={
                'verbose_name': 'Auto',
                'verbose_name_plural': 'Auto',
            },
        ),
    ]
