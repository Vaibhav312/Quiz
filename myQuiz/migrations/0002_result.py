# Generated by Django 2.2.7 on 2020-07-26 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myQuiz', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_score', models.CharField(max_length=20)),
            ],
        ),
    ]