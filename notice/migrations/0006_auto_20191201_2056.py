# Generated by Django 2.2.7 on 2019-12-01 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notice', '0005_info_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='info',
            name='available',
            field=models.CharField(choices=[('1', '공개'), ('0', '비공개')], max_length=1),
        ),
    ]
