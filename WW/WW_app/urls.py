"""WW URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
    path('admin/', admin.site.urls),
    path('home/', views.home, name='home'),
    path('index/', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('my_profile/', views.my_profile, name='my_profile'),
    path('logout/',views.logout,name="logout"),
    path('post_project/', views.post_project, name='post_project'),
    path('post_job/', views.post_job, name='post_job'),
    path('fpwd/', views.fpwd, name='fpwd'),
    path('otp/', views.sendotp, name='otp'),
    path('reset-password/', views.reset_password, name='reset-password'),
    path('companies/',views.companies,name="companies"),
    path(r'^company-profile/(?P<pk>\d+)/$',views.company_profile,name="company-profile"),
    path('follow/',views.follow,name="follow"),
    path('forum/',views.forum,name="forum"),
    path('add_question/',views.add_question,name="add_question"),
    path('update-dp/',views.update_dp,name="update-dp"),
    path('profiles/',views.profiles,name="profiles"),
    path(r'^company_details/(?P<pk>\d+)/$',views.company_details,name="company_details"),
    path(r'^freelancer_details/(?P<pk>\d+)/$',views.freelancer_details,name="freelancer_details"),
    path(r'^messages/(?P<pk>\d+)/$',views.messages,name="messages"),
    
]
