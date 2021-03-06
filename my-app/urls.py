"""{{ project_name }} URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf.urls import url
from django.contrib import admin
from django.views.generic.base import TemplateView
from new_app.views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^battles/', get_battles),
    url(r'^battleDetails/', get_battle_details),
    url(r'^battleTypeAggregate/', get_aggregate_battle_type),
    url(r'^attackerKingAggregate/', get_aggregate_active_attacker_king),
    url(r'^defenderKingAggregate/', get_aggregate_active_defender_king),
    url(r'^minMaxAvgDefenderSize/', get_min_max_average_defender_size),
    url(r'^.*', TemplateView.as_view(template_name="home.html"), name="home")
]
