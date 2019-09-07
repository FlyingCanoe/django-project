# Generated by Django 2.2.4 on 2019-08-15 19:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('impaque_caculator', '0005_auto_20190814_0004'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='co2emisonprofile',
            name='co2_emission_metric',
        ),
        migrations.RemoveField(
            model_name='co2emisonprofile',
            name='distance_travele',
        ),
        migrations.CreateModel(
            name='Engement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('duration_of_the_engement', models.IntegerField()),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='impaque_caculator.Co2EmisonProfile')),
            ],
        ),
    ]
