# Generated by Django 2.1.5 on 2019-03-05 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academiya', '0005_master'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidate',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='master',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='planet',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]