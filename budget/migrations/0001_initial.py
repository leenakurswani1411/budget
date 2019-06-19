# Generated by Django 2.2.2 on 2019-06-14 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ExpenseAccount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='title')),
                ('balance', models.IntegerField(default=0, verbose_name='balance')),
                ('description', models.CharField(blank=True, max_length=200, null=True, verbose_name='Description')),
            ],
        ),
        migrations.CreateModel(
            name='ExpenseItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title1', models.CharField(max_length=100, verbose_name='Title1')),
                ('amount', models.IntegerField(default=0, verbose_name='Amount')),
                ('description', models.CharField(blank=True, max_length=200, null=True, verbose_name='Description')),
                ('date', models.DateField(max_length=200, verbose_name='Date')),
                ('account', models.CharField(max_length=200, verbose_name='Account')),
            ],
        ),
    ]