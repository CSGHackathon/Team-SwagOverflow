# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-27 13:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FavoriteShow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='FavoriteTeam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Show',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='ShowEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('channel_name', models.CharField(max_length=32)),
                ('channel_number', models.IntegerField()),
                ('show', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='events', to='swag.Show')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('league', models.CharField(choices=[('MLB', 'Major League Baseball'), ('NBA', 'National Basketball League'), ('NFL', 'National Football League'), ('NHL', 'National Hockey League')], max_length=8)),
                ('logo_url', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='TeamEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('channel_name', models.CharField(max_length=32)),
                ('channel_number', models.IntegerField()),
                ('away_team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='away_games', to='swag.Team')),
                ('home_team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='home_games', to='swag.Team')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('email', models.CharField(max_length=128)),
                ('phone', models.CharField(max_length=16)),
            ],
        ),
        migrations.AddField(
            model_name='favoriteteam',
            name='team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='swag.Team'),
        ),
        migrations.AddField(
            model_name='favoriteteam',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='swag.User'),
        ),
        migrations.AddField(
            model_name='favoriteshow',
            name='show',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='swag.Show'),
        ),
        migrations.AddField(
            model_name='favoriteshow',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='swag.User'),
        ),
    ]
