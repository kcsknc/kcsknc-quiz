# Generated by Django 2.0.5 on 2018-09-27 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0002_auto_20180921_2058'),
    ]

    operations = [
        migrations.CreateModel(
            name='c_questions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=1000)),
                ('a', models.CharField(max_length=1000)),
                ('b', models.CharField(max_length=1000)),
                ('c', models.CharField(max_length=1000)),
                ('d', models.CharField(max_length=1000)),
                ('answer', models.CharField(max_length=1)),
            ],
            options={
                'verbose_name_plural': 'DBMS_questions',
            },
        ),
        migrations.CreateModel(
            name='c_score',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=264, null=True)),
                ('regno', models.CharField(max_length=264, unique=True)),
                ('year', models.CharField(choices=[('firstyear', 'I'), ('secondyear', 'II'), ('thirdyear', 'III')], default='third', max_length=26)),
                ('Score', models.CharField(max_length=10, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ca_questions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=1000)),
                ('a', models.CharField(max_length=1000)),
                ('b', models.CharField(max_length=1000)),
                ('c', models.CharField(max_length=1000)),
                ('d', models.CharField(max_length=1000)),
                ('answer', models.CharField(max_length=1)),
            ],
            options={
                'verbose_name_plural': 'ca_questions',
            },
        ),
        migrations.CreateModel(
            name='ca_score',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=264, null=True)),
                ('regno', models.CharField(max_length=264, unique=True)),
                ('year', models.CharField(choices=[('firstyear', 'I'), ('secondyear', 'II'), ('thirdyear', 'III')], default='third', max_length=26)),
                ('Score', models.CharField(max_length=10, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='cpp_questions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=1000)),
                ('a', models.CharField(max_length=1000)),
                ('b', models.CharField(max_length=1000)),
                ('c', models.CharField(max_length=1000)),
                ('d', models.CharField(max_length=1000)),
                ('answer', models.CharField(max_length=1)),
            ],
            options={
                'verbose_name_plural': 'cpp_questions',
            },
        ),
        migrations.CreateModel(
            name='cpp_score',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=264, null=True)),
                ('regno', models.CharField(max_length=264, unique=True)),
                ('year', models.CharField(choices=[('firstyear', 'I'), ('secondyear', 'II'), ('thirdyear', 'III')], default='third', max_length=26)),
                ('Score', models.CharField(max_length=10, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='dm_questions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=1000)),
                ('a', models.CharField(max_length=1000)),
                ('b', models.CharField(max_length=1000)),
                ('c', models.CharField(max_length=1000)),
                ('d', models.CharField(max_length=1000)),
                ('answer', models.CharField(max_length=1)),
            ],
            options={
                'verbose_name_plural': 'DM_questions',
            },
        ),
        migrations.CreateModel(
            name='dm_score',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=264, null=True)),
                ('regno', models.CharField(max_length=264, unique=True)),
                ('year', models.CharField(choices=[('firstyear', 'I'), ('secondyear', 'II'), ('thirdyear', 'III')], default='third', max_length=26)),
                ('Score', models.CharField(max_length=10, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='java_questions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=1000)),
                ('a', models.CharField(max_length=1000)),
                ('b', models.CharField(max_length=1000)),
                ('c', models.CharField(max_length=1000)),
                ('d', models.CharField(max_length=1000)),
                ('answer', models.CharField(max_length=1)),
            ],
            options={
                'verbose_name_plural': 'DBMS_questions',
            },
        ),
        migrations.CreateModel(
            name='java_score',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=264, null=True)),
                ('regno', models.CharField(max_length=264, unique=True)),
                ('year', models.CharField(choices=[('firstyear', 'I'), ('secondyear', 'II'), ('thirdyear', 'III')], default='third', max_length=26)),
                ('Score', models.CharField(max_length=10, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='os_questions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=1000)),
                ('a', models.CharField(max_length=1000)),
                ('b', models.CharField(max_length=1000)),
                ('c', models.CharField(max_length=1000)),
                ('d', models.CharField(max_length=1000)),
                ('answer', models.CharField(max_length=1)),
            ],
            options={
                'verbose_name_plural': 'os_questions',
            },
        ),
        migrations.CreateModel(
            name='os_score',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=264, null=True)),
                ('regno', models.CharField(max_length=264, unique=True)),
                ('year', models.CharField(choices=[('firstyear', 'I'), ('secondyear', 'II'), ('thirdyear', 'III')], default='third', max_length=26)),
                ('Score', models.CharField(max_length=10, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='vb_questions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=1000)),
                ('a', models.CharField(max_length=1000)),
                ('b', models.CharField(max_length=1000)),
                ('c', models.CharField(max_length=1000)),
                ('d', models.CharField(max_length=1000)),
                ('answer', models.CharField(max_length=1)),
            ],
            options={
                'verbose_name_plural': 'vb_questions',
            },
        ),
        migrations.CreateModel(
            name='vb_score',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=264, null=True)),
                ('regno', models.CharField(max_length=264, unique=True)),
                ('year', models.CharField(choices=[('firstyear', 'I'), ('secondyear', 'II'), ('thirdyear', 'III')], default='third', max_length=26)),
                ('Score', models.CharField(max_length=10, null=True)),
            ],
        ),
    ]
