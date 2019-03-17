# Generated by Django 2.1.5 on 2019-03-16 13:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mypage', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('save_date', models.DateTimeField()),
                ('log_message', models.CharField(max_length=20)),
                ('log_text', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='mypage',
            name='user_name',
            field=models.CharField(default='0', max_length=30),
        ),
        migrations.AddField(
            model_name='question',
            name='question_text_num',
            field=models.PositiveIntegerField(default=2000),
        ),
        migrations.AlterField(
            model_name='mypage',
            name='age',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='mypage',
            name='high_grad_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='mypage',
            name='high_school_name',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AlterField(
            model_name='mypage',
            name='major_name',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AlterField(
            model_name='mypage',
            name='sub_major_name',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AlterField(
            model_name='mypage',
            name='univ_grad_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='mypage',
            name='univ_name',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AddField(
            model_name='log',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mypage.Question'),
        ),
    ]