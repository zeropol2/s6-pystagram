from django.conf.urls import url

from . import views


app_name = 'photos'

urlpatterns = [
    url(r'^create/$',
        views.PhotoCreate.as_view(), name='create'),
]

