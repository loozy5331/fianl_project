# Generated by Django 2.1.5 on 2019-03-14 11:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyPage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('age', models.IntegerField()),
                ('high_school_name', models.CharField(max_length=30)),
                ('high_adm_date', models.DateField()),
                ('high_grad_date', models.DateField(auto_now=True)),
                ('univ_name', models.CharField(max_length=30)),
                ('major_name', models.CharField(max_length=30)),
                ('sub_major_name', models.CharField(max_length=30)),
                ('univ_adm_date', models.DateField()),
                ('univ_grad_date', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_title', models.CharField(max_length=200)),
                ('question_text', models.TextField()),
                ('myPage', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mypage.MyPage')),
            ],
        ),
    ]
