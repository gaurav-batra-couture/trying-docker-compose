# Generated by Django 3.2.4 on 2021-06-06 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Coin',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.TextField()),
                ('price', models.TextField()),
            ],
        ),
    ]
