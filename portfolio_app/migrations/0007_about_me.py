# Generated by Django 3.2 on 2021-05-27 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio_app', '0006_contact_info'),
    ]

    operations = [
        migrations.CreateModel(
            name='About_Me',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('about_info', models.CharField(max_length=5000)),
            ],
        ),
    ]
