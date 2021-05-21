from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from menu.views import *
from menu.models import *
from django.conf.urls import url, include
urlpatterns = [
    path('all/', create, name="create"),
    # path('users/', users, name="users"),
    ]
