from django.urls import path
from . import views
from . import test_method

app_name = 'web_scraping'

urlpatterns = [
    path('home', views.home),
    path('phishtank', views.phishtank_json),
    path('phishstats_country_url/<slug:country_code>', views.phishstats_country_url),
    path('phishstats_last_update', views.phishstats_last_update),
    path('god_url_add', views.calc_len),
    path('whois', views.whois),
    path('training', views.urls_training),
    path('test', test_method.tester),
    path('engine_execution', views.engine_execution),
]
