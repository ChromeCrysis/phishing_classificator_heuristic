# Generated by Django 4.0.3 on 2022-04-04 23:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_scraping', '0007_badurl_verified_whois_godurl_verified_whois'),
    ]

    operations = [
        migrations.AlterField(
            model_name='badurl',
            name='asn',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='badurl',
            name='country_code',
            field=models.CharField(blank=True, max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='badurl',
            name='date_create_domain',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='badurl',
            name='ip',
            field=models.CharField(blank=True, max_length=11, null=True),
        ),
        migrations.AlterField(
            model_name='badurl',
            name='is_contains_com',
            field=models.BooleanField(blank=True),
        ),
        migrations.AlterField(
            model_name='badurl',
            name='isp',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='badurl',
            name='len_url',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='badurl',
            name='phishstats_id',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='badurl',
            name='phishtank_id',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='badurl',
            name='target',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='badurl',
            name='verified_whois',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AlterField(
            model_name='godurl',
            name='asn',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='godurl',
            name='country_code',
            field=models.CharField(blank=True, max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='godurl',
            name='date_create_domain',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='godurl',
            name='ip',
            field=models.CharField(blank=True, max_length=11, null=True),
        ),
        migrations.AlterField(
            model_name='godurl',
            name='is_contains_com',
            field=models.BooleanField(blank=True),
        ),
        migrations.AlterField(
            model_name='godurl',
            name='isp',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='godurl',
            name='len_url',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='godurl',
            name='phishstats_id',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='godurl',
            name='phishtank_id',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='godurl',
            name='target',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='godurl',
            name='verified_whois',
            field=models.BooleanField(blank=True, default=False),
        ),
    ]
