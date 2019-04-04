# Generated by Django 2.1.3 on 2019-03-31 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='summary',
        ),
        migrations.AddField(
            model_name='blog',
            name='body',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='blog',
            name='pub_date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='blog',
            name='title',
            field=models.CharField(max_length=200, null=True),
        ),
    ]