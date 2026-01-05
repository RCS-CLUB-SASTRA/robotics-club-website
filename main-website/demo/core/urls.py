from django.urls import path
from .views import events_list, blogs_list

urlpatterns = [
    path('events/', events_list, name='events-list'),
    path('blogs/', blogs_list, name='blogs-list'),
]
