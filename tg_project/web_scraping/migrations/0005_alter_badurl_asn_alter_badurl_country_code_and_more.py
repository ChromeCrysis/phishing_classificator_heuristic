# Generated by Django 4.0.3 on 2022-03-14 21:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_scraping', '0004_remove_badurl_id_remove_godurl_id_alter_badurl_url_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='badurl',
            name='asn',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='badurl',
            name='country_code',
            field=models.CharField(max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='badurl',
            name='ip',
            field=models.CharField(max_length=11, null=True),
        ),
        migrations.AlterField(
            model_name='badurl',
            name='isp',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='badurl',
            name='phishstats_id',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='badurl',
            name='phishtank_id',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='badurl',
            name='target',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='godurl',
            name='asn',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='godurl',
            name='country_code',
            field=models.CharField(max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='godurl',
            name='ip',
            field=models.CharField(max_length=11, null=True),
        ),
        migrations.AlterField(
            model_name='godurl',
            name='isp',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='godurl',
            name='phishstats_id',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='godurl',
            name='phishtank_id',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='godurl',
            name='target',
            field=models.CharField(max_length=100, null=True),
        ),
    ]