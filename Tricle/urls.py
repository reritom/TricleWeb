"""Tricle URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from Tricle import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name='home'),
    url(r'^accounts/', include('accounts.urls', namespace='accounts')),
    url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^scrambler/', include('scrambler.urls', namespace='scrambler')),
    url(r'^scrambler/', include('django.contrib.auth.urls')),
    url(r'^test/$', views.TestPage.as_view(), name='test'),
    url(r'^privacy$', views.PrivacyPage.as_view(), name='privacy'),
    url(r'contact/$', views.ContactPage.as_view(), name='contact'),
    url(r'global/$', views.stats, name='global'),
    url(r'go/$', views.GettingStarted.as_view(), name='go'),
    url(r'about/$', views.AboutPage.as_view(), name='about'),
    url(r'^scrambler/$', views.ScramRedirect),
    url(r'^iaw/$', views.cleanup, name="cleanup"),
    url(r'^api/', include('API.urls', namespace='api')),
]
