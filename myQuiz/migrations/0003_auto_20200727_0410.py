# Generated by Django 2.2.7 on 2020-07-26 22:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myQuiz', '0002_result'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactusinfo',
            name='email',
            field=models.EmailField(error_messages={'required': 'Please enter valid email'}, max_length=254),
        ),
        migrations.AlterField(
            model_name='contactusinfo',
            name='name',
            field=models.CharField(error_messages={'required': 'Please enter your name'}, max_length=50),
        ),
    ]