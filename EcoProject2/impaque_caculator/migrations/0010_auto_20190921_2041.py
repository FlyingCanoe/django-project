# Generated by Django 2.2.4 on 2019-09-21 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('impaque_caculator', '0009_auto_20190816_2022'),
    ]

    operations = [
        migrations.AddField(
            model_name='engagement',
            name='emison_metric',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='co2emisonprofile',
            name='consumption_metric',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='engagement',
            name='distance',
            field=models.IntegerField(help_text="nombre de km parcourue durent l'engament"),
        ),
        migrations.AlterField(
            model_name='engagement',
            name='duration',
            field=models.IntegerField(help_text="durée de l'engament en jour"),
        ),
    ]
