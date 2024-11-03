# Generated by Django 5.0.6 on 2024-09-15 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mailing', '0002_remove_client_mailings_mailing_client_list'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mailing',
            name='client_list',
            field=models.ManyToManyField(help_text='Выберите клиентов для рассылки', related_name='Client', to='mailing.client', verbose_name='Клиенты'),
        ),
        migrations.AlterField(
            model_name='mailing',
            name='datetime_to_start',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Когда нужно разослать?'),
        ),
    ]
