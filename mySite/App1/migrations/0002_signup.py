# Generated by Django 4.0.4 on 2022-05-29 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Signup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('psw', models.CharField(max_length=50)),
            ],
        ),
    ]
