from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
]

# This pattern matches the empty string, i.e., it is like we are setting a start-up page..!

