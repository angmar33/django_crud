# Generated by Django 2.0.7 on 2018-07-30 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Coin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coin_name', models.CharField(max_length=30)),
                ('coin_price', models.IntegerField()),
                ('created_at', models.DateField()),
            ],
        ),
    ]
