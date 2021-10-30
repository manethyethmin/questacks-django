# Generated by Django 3.2.8 on 2021-10-27 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0007_question_views'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='tags',
            field=models.CharField(default='', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='views',
            field=models.IntegerField(default=0),
        ),
    ]
