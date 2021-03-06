# Generated by Django 3.0.4 on 2020-03-27 16:21

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mylibrary', '0017_auto_20200321_1055'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='borrow',
            options={'ordering': ['id'], 'verbose_name': '借阅关系', 'verbose_name_plural': '借阅关系'},
        ),
        migrations.AlterField(
            model_name='borrow',
            name='borrow_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 27, 16, 21, 1, 116135), verbose_name='借出时间'),
        ),
        migrations.AlterField(
            model_name='borrow',
            name='return_ddl',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 27, 16, 21, 1, 116169), verbose_name='归还期限'),
        ),
        migrations.AlterField(
            model_name='log',
            name='book',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='mylibrary.Book', verbose_name='相关书籍'),
        ),
    ]
