# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Answer', models.TextField()),
                ('CreatedTime', models.DateTimeField()),
                ('ModifiedTime', models.DateTimeField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='AnswerAttachment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('FilePath', models.CharField(max_length=100)),
                ('AnswerID', models.ForeignKey(to='webapp.Answer')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='AnswerVote',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Value', models.IntegerField()),
                ('AnswerId', models.ForeignKey(to='webapp.Answer')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Comment', models.TextField()),
                ('CreatedTime', models.DateTimeField()),
                ('ModifiedTime', models.DateTimeField()),
                ('AnswerID', models.ForeignKey(to='webapp.Answer')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Title', models.CharField(max_length=200)),
                ('QuestionText', models.TextField()),
                ('CreatedTime', models.DateTimeField()),
                ('ModifiedTime', models.DateTimeField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='QuestionAttachment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('FilePath', models.CharField(max_length=100)),
                ('QuestionID', models.ForeignKey(to='webapp.Question')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='QuestionComment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Comment', models.TextField()),
                ('CreatedTime', models.DateTimeField()),
                ('ModifiedTime', models.DateTimeField()),
                ('QuestionID', models.ForeignKey(to='webapp.Question')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='QuestionTag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('QuestionID', models.ForeignKey(to='webapp.Question')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='QuestionVote',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Value', models.IntegerField()),
                ('QuestionID', models.ForeignKey(to='webapp.Question')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SiteSettings',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('isPublic', models.BooleanField(default=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Tag', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('UserName', models.CharField(max_length=50)),
                ('FirstName', models.CharField(max_length=50)),
                ('LastName', models.CharField(max_length=50)),
                ('Email', models.CharField(max_length=50)),
                ('Password', models.CharField(max_length=1000)),
                ('Created', models.DateTimeField()),
                ('Modified', models.DateTimeField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserBadge',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('BadgeID', models.IntegerField()),
                ('UserID', models.ForeignKey(to='webapp.User')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserSettings',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('isAdmin', models.BooleanField(default=False)),
                ('UserID', models.ForeignKey(to='webapp.User')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='questionvote',
            name='UserID',
            field=models.ForeignKey(to='webapp.User'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='questiontag',
            name='TagID',
            field=models.ForeignKey(to='webapp.Tag'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='questioncomment',
            name='UserID',
            field=models.ForeignKey(to='webapp.User'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='question',
            name='UserID',
            field=models.ForeignKey(to='webapp.User'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='comment',
            name='UserID',
            field=models.ForeignKey(to='webapp.User'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='answervote',
            name='UserID',
            field=models.ForeignKey(to='webapp.User'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='answer',
            name='QuestionID',
            field=models.ForeignKey(to='webapp.Question'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='answer',
            name='UserID',
            field=models.ForeignKey(to='webapp.User'),
            preserve_default=True,
        ),
    ]
