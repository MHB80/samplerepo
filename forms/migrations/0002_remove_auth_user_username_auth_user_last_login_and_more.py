# Generated by Django 5.0.6 on 2024-05-31 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='auth_user',
            name='username',
        ),
        migrations.AddField(
            model_name='auth_user',
            name='last_login',
            field=models.DateTimeField(blank=True, null=True, verbose_name='last login'),
        ),
        migrations.AlterField(
            model_name='auth_user',
            name='password',
            field=models.CharField(max_length=128, verbose_name='password'),
        ),
    ]
