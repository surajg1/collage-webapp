# Generated by Django 3.0 on 2020-03-09 05:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0008_delete_notice'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('link', models.CharField(max_length=200)),
                ('discription', models.CharField(max_length=200)),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='common.Teacher')),
            ],
        ),
    ]