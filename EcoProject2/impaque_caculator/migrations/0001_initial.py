# Generated by Django 2.2.4 on 2019-08-13 23:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CoEmisonProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('consumption_metric', models.FloatField()),
                ('dumy', models.FloatField()),
                ('dummy', models.IntegerField()),
                ('distance_travele', models.FloatField()),
                ('is_diesel', models.BooleanField()),
                ('co_emission_metric', models.FloatField(blank=True)),
            ],
        ),
    ]
