# Generated by Django 4.0.7 on 2022-11-12 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='biology',
            name='theme',
            field=models.TextField(max_length=300),
        ),
        migrations.AlterField(
            model_name='english',
            name='theme',
            field=models.TextField(max_length=300),
        ),
        migrations.AlterField(
            model_name='ft',
            name='theme',
            field=models.TextField(max_length=300),
        ),
        migrations.AlterField(
            model_name='history',
            name='theme',
            field=models.TextField(max_length=300),
        ),
        migrations.AlterField(
            model_name='math',
            name='theme',
            field=models.TextField(max_length=300),
        ),
        migrations.AlterField(
            model_name='phisics',
            name='theme',
            field=models.TextField(max_length=300),
        ),
    ]
