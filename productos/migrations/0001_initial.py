# Generated by Django 5.1.2 on 2024-11-03 23:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Paleta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', models.CharField(max_length=20)),
                ('escote', models.CharField(max_length=20)),
                ('fecha', models.DateField()),
            ],
        ),
    ]
