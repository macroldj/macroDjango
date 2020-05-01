# Generated by Django 2.2 on 2019-04-24 14:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('diarys', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Diary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='我的游记', max_length=20, verbose_name='题目')),
                ('content', models.TextField(verbose_name='内容')),
                ('image', models.ImageField(default='diary/default.jpg', upload_to='diary/%Y/%m', verbose_name='封面图')),
                ('checknum', models.IntegerField(default=0, verbose_name='查看数')),
                ('praisenum', models.IntegerField(default=0, verbose_name='点赞数')),
                ('commentsnum', models.IntegerField(default=0, verbose_name='评论数')),
                ('collectnum', models.IntegerField(default=0, verbose_name='收藏数')),
                ('is_published', models.BooleanField(default=False, verbose_name='是否发表')),
                ('add_times', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
            ],
            options={
                'verbose_name': '游记信息',
                'verbose_name_plural': '游记信息',
            },
        ),
    ]
