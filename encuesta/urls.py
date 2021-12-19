"""encuesta URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import include, path
from django.contrib.auth.decorators import login_required


from users.views import Login,logoutUser
from cuestionario.views import index,email
from charts.views import chart

urlpatterns = [

    path('admin/', admin.site.urls),
    path('accounts/login/', Login.as_view(), name='login'),
    path('logout', login_required(logoutUser),name='logout'),
    path('response/', login_required(email), name='email'),
    path('chart', login_required(chart),name='chart'),
    path('',login_required(index),name='form')


]
