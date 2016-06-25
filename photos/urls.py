from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from . import views


app_name = 'photos'

urlpatterns = [
    url(r'^create/$',
        login_required(views.PhotoCreate.as_view()),
        name='create'),
]

