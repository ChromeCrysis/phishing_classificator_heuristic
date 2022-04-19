from pyexpat import model
from shutil import _ntuple_diskusage
from statistics import mode
from django.db import models

# Create your models here.


class GodURL(models.Model):
    url = models.TextField(primary_key=True)
    ip = models.CharField(max_length=40, null=True, blank=True)
    create_domain = models.TimeField(null=True, blank=True)
    expiration_domain = models.TimeField(null=True, blank=True)
    country_code = models.CharField(max_length=3, null=True, blank=True)
    target = models.CharField(max_length=100, null=True, blank=True)
    asn = models.CharField(max_length=255, null=True, blank=True)
    isp = models.CharField(max_length=255, null=True, blank=True)
    len_url = models.IntegerField(blank=True)
    is_contains_com = models.BooleanField(blank=True)
    phishtank_id = models.IntegerField(null=True, blank=True)
    phishstats_id = models.IntegerField(null=True,blank=True)
    verified_whois = models.BooleanField(default=False, blank=True)
    is_phishing = models.BooleanField()

class BadURL(models.Model):
    url = models.TextField(primary_key=True)
    ip = models.CharField(max_length=40, null=True, blank=True)
    create_domain = models.TimeField(null=True, blank=True)
    expiration_domain = models.TimeField(null=True, blank=True)
    target = models.CharField(max_length=100, null=True, blank=True)
    asn = models.CharField(max_length=255, null=True, blank=True)
    isp = models.CharField(max_length=255, null=True, blank=True)
    len_url = models.IntegerField(blank=True)
    is_contains_com = models.BooleanField(blank=True)
    phishtank_id = models.IntegerField(null=True, blank=True)
    phishstats_id = models.IntegerField(null=True, blank=True)
    verified_whois = models.BooleanField(default=False, blank=True)
    is_phishing = models.BooleanField()

    