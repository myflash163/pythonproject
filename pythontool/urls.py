from django.urls import path
from pythontool import views

urlpatterns = [
    path('hello/',views.hello,{'a':'123'}, name='hello')
]