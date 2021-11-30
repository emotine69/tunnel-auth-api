# Generated by Django 3.2.9 on 2021-11-30 08:26

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_uid', models.CharField(help_text='char(1 -> 28).', max_length=32, primary_key=True, serialize=False, unique=True, verbose_name='user_uid')),
                ('user_name', models.CharField(help_text='char(1 -> 40).', max_length=40, unique=True, verbose_name='user_name')),
                ('user_email', models.EmailField(help_text='char(1 -> 100).', max_length=100, unique=True, verbose_name='user_email')),
                ('user_full_name', models.CharField(help_text='char(1 -> 50).', max_length=50, verbose_name='user_full_name')),
                ('province', models.CharField(help_text='char(1 -> 50).', max_length=50, verbose_name='province.')),
                ('district', models.CharField(help_text='char(1 -> 50).', max_length=50, verbose_name='district.')),
                ('ward', models.CharField(help_text='char(1 -> 50).', max_length=50, verbose_name='ward.')),
                ('detail_adr', models.TextField(help_text='char(1 -> 50).', max_length=50, verbose_name='detail_adr.')),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
            ],
            options={
                'verbose_name': 'user_uid.',
                'verbose_name_plural': 'user_uids.',
            },
        ),
    ]