# Generated by Django 2.1.5 on 2019-02-24 10:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=150)),
                ('age', models.IntegerField()),
                ('email', models.EmailField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Planet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.SlugField(unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='candidate',
            name='planet',
            field=models.ForeignKey(max_length=50, on_delete=django.db.models.deletion.CASCADE, to='academiya.Planet'),
        ),
    ]
