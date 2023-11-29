# Generated by Django 4.2.7 on 2023-11-29 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organization',
            name='director',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='sanction',
            name='date',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='sanction',
            name='period_of_execution',
            field=models.CharField(default='0', max_length=100),
        ),
    ]