"""example URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
import autofixture
from django.conf.urls import url, include
from django.contrib import admin
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
#sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'test_app'))
from . import views
#from search import views

#from search import views as search_views

urlpatterns = [
    url(r'^search/', views.search, name='search'),  # < here
    url(r'^results/', views.results, name='results'),  # < here
]


autofixture.autodiscover()
