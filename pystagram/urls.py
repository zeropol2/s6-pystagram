from django.conf.urls import url
from django.conf.urls import include
from django.contrib import admin
from django.contrib.auth.views import login

urlpatterns = [
    url(r'^login/$', login,
        name='login_url',
        kwargs={'template_name': 'login.html'}),
    url(r'^photos/', include('photos.urls')),
    url(r'^admin/', admin.site.urls),
]
