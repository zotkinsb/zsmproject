# Generated by Django 4.1.2 on 2022-12-17 16:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=3, verbose_name='Класс')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='URL')),
            ],
            options={
                'verbose_name': 'Класс',
                'verbose_name_plural': 'Классы',
            },
        ),
        migrations.CreateModel(
            name='Timetable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_lesson', models.CharField(blank=True, default='—', max_length=15, null=True, verbose_name='Первый урок')),
                ('first_cabinet', models.CharField(blank=True, default='—', max_length=10, null=True, verbose_name='Первый кабинет')),
                ('second_lesson', models.CharField(blank=True, default='—', max_length=15, null=True, verbose_name='Второй урок')),
                ('second_cabinet', models.CharField(blank=True, default='—', max_length=10, null=True, verbose_name='Второй кабинет')),
                ('third_lesson', models.CharField(blank=True, default='—', max_length=15, null=True, verbose_name='Третий урок')),
                ('third_cabinet', models.CharField(blank=True, default='—', max_length=10, null=True, verbose_name='Третий кабинет')),
                ('fourth_lesson', models.CharField(blank=True, default='—', max_length=15, null=True, verbose_name='Четвёртый урок')),
                ('fourth_cabinet', models.CharField(blank=True, default='—', max_length=10, null=True, verbose_name='Четвёртый кабинет')),
                ('fifth_lesson', models.CharField(blank=True, default='—', max_length=15, null=True, verbose_name='Пятый урок')),
                ('fifth_cabinet', models.CharField(blank=True, default='—', max_length=10, null=True, verbose_name='Пятый кабинет')),
                ('sixth_lesson', models.CharField(blank=True, default='—', max_length=15, null=True, verbose_name='Шестой урок')),
                ('sixth_cabinet', models.CharField(blank=True, default='—', max_length=10, null=True, verbose_name='Шестой кабинет')),
                ('seventh_lesson', models.CharField(blank=True, default='—', max_length=15, null=True, verbose_name='Седьмой урок')),
                ('seventh_cabinet', models.CharField(blank=True, default='—', max_length=10, null=True, verbose_name='Седьмой кабинет')),
                ('timetable_date', models.DateField(verbose_name='Дата расписания')),
                ('short_lesson', models.BooleanField(verbose_name='Короткие уроки')),
                ('short_break', models.BooleanField(verbose_name='Короткие перемены')),
                ('class_init', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='timetables.category', verbose_name='Класс')),
            ],
            options={
                'verbose_name': 'Расписание',
                'verbose_name_plural': 'Расписания',
            },
        ),
    ]