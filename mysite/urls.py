"""mysite URL Configuration

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
from django.contrib import admin
from django.urls import path,include
from blog import views as blog_views

urlpatterns = [
    path('classification/', blog_views.blog_classification, name='classification'),
    path('detail/', blog_views.blog_detail, name='article_content'),
    path('admin/', admin.site.urls),
    path('comments/', include('django_comments.urls')),
    path('', blog_views.blog_list, name='blog_list'),
]
