# Generated by Django 3.2 on 2021-04-16 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='instructor_information',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=200)),
            ],
        ),
    ]