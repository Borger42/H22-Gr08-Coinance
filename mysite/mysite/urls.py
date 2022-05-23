"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from myapp import views

urlpatterns = [ #les path pour pouvoir naviguer dans différentes pages de notre site
    path('test', views.index, name='index'),
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    path('home/', views.home, name="home"),
    path('aboutus/', views.aboutus, name="aboutus"),
    path('actions/<str:action>', views.ActionsMonthly, name="actions"),
    path('daily/<str:action>', views.ActionsDaily, name="daily"),
    path('weekly/<str:action>', views.ActionsWeekly, name="weekly"),
    path('monthly/<str:action>', views.ActionsMonthly, name="monthly"),
    path('contact/', views.contact, name="contact"),
    path('Team/',views.team, name ='team'),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('register/', views.registerPage, name="register"),
    path('user/', views.userPage, name="user"),
    path('search_bar', views.search_bar, name="search_bar"),
    path('search/<str:mot_cle>', views.search_page, name="search_page"),
    path('calculateur/', views.calculateur, name="search_page"),

]


