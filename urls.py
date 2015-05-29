"""addressbook URL Configuration"""

from django.conf.urls import include, url
from book import views


urlpatterns = [
    
            url(r'^$', views.index, name = 'index'),
            url(r'^book/login/$', views.userlogin, name = 'login'), # login page
            url(r'^book/userprofile/$', views.profile_user, name = 'userprofile'), # user profile
            url(r'^book/edit/$', views.edit_profile, name = 'edit'), # edit profile
            url(r'^book/register/$', views.signup, name = 'register'), # registeration
            url(r'^book/pin/$', views.gen_random, name = 'generate_pin'), #pin generation
            url(r'^book/(?P<user_id>\d+)/$', views.pub_profile, name = 'public_profile'), #public profile
            url(r'^book/contacts/$', views.user_contacts, name = 'mycontacts'), # user contacts
            url(r'^book/logout/$', views.signout, name = 'logout'), # logout
           ]
