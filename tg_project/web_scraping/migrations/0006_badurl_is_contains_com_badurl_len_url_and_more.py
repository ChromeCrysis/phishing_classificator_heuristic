# Generated by Django 4.0.3 on 2022-04-04 23:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_scraping', '0005_alter_badurl_asn_alter_badurl_country_code_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='badurl',
            name='is_contains_com',
            field=models.BooleanField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='badurl',
            name='len_url',
            field=models.IntegerField(default=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='godurl',
            name='is_contains_com',
            field=models.BooleanField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='godurl',
            name='len_url',
            field=models.IntegerField(default=False),
            preserve_default=False,
        ),
    ]
