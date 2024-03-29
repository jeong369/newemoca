# Generated by Django 2.2.7 on 2019-12-02 14:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20191125_0929'),
        ('bigfive', '0002_auto_20191128_0929'),
    ]

    operations = [
        migrations.CreateModel(
            name='Adjective',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=1)),
                ('word', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Score',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grade', models.IntegerField(choices=[(1, '전혀 그렇지 않다.'), (2, '그렇지 않다.'), (3, '보통이다.'), (4, '약간 그렇다.'), (5, '매우 그렇다.')])),
            ],
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField()),
                ('question_ko', models.TextField(blank=True, null=True)),
                ('label', models.CharField(max_length=1)),
                ('facet', models.CharField(blank=True, max_length=20)),
                ('key', models.IntegerField()),
                ('score_users', models.ManyToManyField(related_name='score_tests', through='bigfive.Score', to='accounts.User')),
            ],
        ),
        migrations.RemoveField(
            model_name='ctest',
            name='user',
        ),
        migrations.RemoveField(
            model_name='etest',
            name='user',
        ),
        migrations.RemoveField(
            model_name='ntest',
            name='user',
        ),
        migrations.RemoveField(
            model_name='otest',
            name='user',
        ),
        migrations.DeleteModel(
            name='ATest',
        ),
        migrations.DeleteModel(
            name='CTest',
        ),
        migrations.DeleteModel(
            name='ETest',
        ),
        migrations.DeleteModel(
            name='NTest',
        ),
        migrations.DeleteModel(
            name='OTest',
        ),
        migrations.AddField(
            model_name='score',
            name='test',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bigfive.Test'),
        ),
        migrations.AddField(
            model_name='score',
            name='users',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.User'),
        ),
    ]
