"""ChoreManager URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),
    # URL patterns for User views
    path('users/', views.user_list, name='user_list'),
    path('users/<int:user_id>/', views.user_detail, name='user_detail'),
    
    # URL patterns for ChoreList views
    path('chore-lists/', views.chore_lists, name='chore_list'),
    path('chore-lists/<int:list_id>/', views.chore_list_detail, name='chore_list_detail'),
    
    # URL patterns for Chore views
    path('chores/', views.chore, name='chore'),
    path('chores/<int:chore_id>/', views.chore_detail, name='chore_detail')
]
