"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path

from facebook.views import play
from facebook.views import play2
from facebook.views import profile
from facebook.views import event
from facebook.views import fail
from facebook.views import warn
from facebook.views import help
from facebook.views import newsfeed
from facebook.views import detail_feed
from facebook.views import new_feed
from facebook.views import edit_feed
from facebook.views import remove_feed


urlpatterns = [
    path('admin/', admin.site.urls),

    path('play/', play),
    path('play2/', play2),
    path('profile/', profile),
    path('event/', event),
    path('fail/', fail),
    path('warn/', warn),
    path('help/', help),

    # path에 아무것도 입력안하면, 도메인 홈의 역할이 되는 것.
    path('', newsfeed),
    path('feed/<pk>/',detail_feed), # <pk> : 글 번호. 장고에서 정한 기호.
    path('new/', new_feed),
    path('feed/<pk>/edit/', edit_feed),
    path('feed/<pk>/remove/',remove_feed)
]
