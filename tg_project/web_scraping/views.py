import csv
from email import header
from tokenize import String
from urllib import request


import requests
from django.http import HttpResponse
from django.shortcuts import render
from requests import get
import json
from django.db.models import Count
from .models import BadURL, GodURL, Urls
from django.contrib import messages
from datetime import datetime

#Math libs
import numpy as np
import pandas as pd

# Machine learning libs
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, mean_squared_error
from sklearn.preprocessing import OneHotEncoder
from sklearn import preprocessing
from sklearn.compose import ColumnTransformer



# Create your views here.

def home(request):
    badurl = BadURL.objects.values('target').annotate(total=Count('target'))
    godurls = GodURL.objects.all()

    context = {
        'godurls' : godurls,
        'badurls' : badurl
    }

    return render(request, 'home.html', context)

def phishtank_json(request):
    url = 'http://data.phishtank.com/data/online-valid.json'

    response = get(url=url)

    dados = json.loads(response.text)

    for dado in dados:
        print(dado)

    return render(request, 'home.html')

def phishstats_country_url(request, country_code):
    url = f'https://phishstats.info:2096/api/phishing?_where=(countrycode,eq,{country_code})'

    response = get(url=url)

    dados = json.loads(response.text)

    for dado in dados:
        bad_url = BadURL(
            url=dado['url'],
            ip=dado['ip'],
            country_code=dado['countrycode'],
            asn=dado['asn'],
            isp=dado['isp'],
            phishstats_id=dado['id']
            )
        bad_url.save()
    
    messages.success(request, f'{len(dados)} URLs de Phishing inseridas', extra_tags='success')
    
    return render(request, 'home.html')

def phishstats_last_update(request):
    url = f'https://phishstats.info:2096/api/phishing?_sort=-id'
    url = 'https://phishstats.info:2096/api/phishing?_where=(title,like,~samsung~)&_sort=-id'

    response = get(url=url)

    dados = json.loads(response.text)

    for dado in dados:
        bad_url = BadURL(
            url=dado['url'],
            ip=dado['ip'],
            country_code=dado['countrycode'],
            asn=dado['asn'],
            isp=dado['isp'],
            phishstats_id=dado['id'],
            target='Samsung'
            )
        bad_url.save()
    
    messages.success(request, f'{len(dados)} URLs de Phishing inseridas', extra_tags='success')
    
    return render(request, 'home.html')


def god_url_add(request):
    url = GodURL(
        url='https://store.playstation.com/pt-br/concept/10000669',
        ip='23.37.210.197',
        country_code='US',
        target='Playstation'
    )

    url.save()

    godlurls = GodURL.objects.count()

    context = {
        'godurls_count' : godlurls
    }
    print(context)
    return render(request, 'home.html', context)

def calc_len(request):
    for url in BadURL.objects.all():
        contains = True if '.com' in url.url else False
        url.len_url=len(url.url)
        url.is_contains_com=contains
        url.save()
    return render(request, 'home.html')

def whois(request):
    url_api = f'''https://api.apilayer.com/whois/'''
    headers = {'apikey' : 'x0j7kgaPH8DX03V4Hihd8qx26hz1UkTX'}

    ips_verificados = []
    for url in BadURL.objects.filter(verified_whois=True):
        ips_verificados.append(url.ip)

    lista = str(ips_verificados).replace('[', '(').replace(']',')')
    WHERE = f"verified_whois = false AND ip NOT IN {lista} "

    while True:
        try:
            url = BadURL.objects.extra(where=[WHERE])
            print(len(url))
            url = url[0]
        except:
            print('Todas dominios anaisados')
        if 'www' in url.url:
            pass
        else:
            domain = url.url.split('//')[1].split('/')[0]
        url_final = f'{url_api}query?domain={domain}'
        r = requests.get(url=url_final, headers=headers)

        if r.status_code == 404:
            url.verified_whois = True
            url.save()
        elif r.status_code == 400:
            pass
        elif r.status_code == 429:
            print('cabo a graça')
        else:
            creation_date = json.loads(r.content)['result']['creation_date']
            expiration_date = json.loads(r.content)['result']['expiration_date']

            creation_date = creation_date[-1] if isinstance(creation_date, list) else creation_date
            expiration_date = expiration_date[-1] if isinstance(expiration_date, list) else expiration_date

            url.create_domain = datetime.strptime(creation_date,'%Y-%m-%d %H:%M:%S')
            url.expiration_domain = datetime.strptime(expiration_date,'%Y-%m-%d %H:%M:%S')
            url.save()

        ips_verificados.append(url.ip)
        lista = str(ips_verificados).replace('[', '(').replace(']',')')
        WHERE = f'verified_whois = false AND ip NOT IN {lista} '

def urls_training():
    # Pre processamento
    urls = Urls.objects.all()
    vurls = urls.values_list()
    urls_np = np.core.records.fromrecords(vurls, names=[f.name for f in Urls._meta.fields])
    label_encoder = preprocessing.LabelEncoder()
    urls_encoded = label_encoder(urls_np)
    X_encoded = urls_encoded
    y = urls_np['is_phishing']
    Xtr, Xval, ytr, yval = train_test_split(X_encoded, y, test_size=0.5, random_state=0)
    arvores = RandomForestClassifier(random_state=0, n_estimators=40, criterion='entropy', n_jobs=-1)
    arvores.fit(Xtr, ytr)
    c = arvores.predict(Xval)
    accuracy = arvores.score(Xval, yval)

def engine_execution(request):
    if request.method == 'GET':

        context = {
            'score' : main(request.GET.get('url'))
        }

        return HttpResponse(json.dumps(context), content_type='application/json')
