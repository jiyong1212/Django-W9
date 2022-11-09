"""jgDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path, include
# [코드 작성] page 앱 폴더의 views.py 가져오기
from page import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('page/', include('page.urls')),
    path('game/', include('game.urls')),
    # [코드 작성] account 앱의 urls.py 연결
    path('account/', include('account.urls')),
    # [코드 작성] http://127.0.0.1:8000/ 경로로 접근할 때 index 페이지로 바로 접근할 수 있도록 경로 설정
    path('',views.index),
]
