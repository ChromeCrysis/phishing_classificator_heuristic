# Generated by Django 4.0.3 on 2022-04-04 23:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_scraping', '0006_badurl_is_contains_com_badurl_len_url_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='badurl',
            name='verified_whois',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='godurl',
            name='verified_whois',
            field=models.BooleanField(default=False),
        ),
    ]
