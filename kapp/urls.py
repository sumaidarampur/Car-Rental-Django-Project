import statistics
from django.urls import path
from kapp import views
from django.contrib import admin  # Django admin module
from django.urls import path       # URL routing
from kapp.views import *  # Import views from the authentication app
from django.conf import settings   # Application settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns=[
    path('', views.index),
    path('signup', views.signUp, name='signup'),
    path('login/', views.login, name='login'),
    path('contact_us/', views.contactUs, name='contact_us'),
    path('help', views.help, name='help'),
]
# # Serve media files if DEBUG is True (development mode)
# if settings.DEBUG:
#     urlpatterns += statistics(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
 
# # Serve static files using staticfiles_urlpatterns
# urlpatterns += staticfiles_urlpatterns()