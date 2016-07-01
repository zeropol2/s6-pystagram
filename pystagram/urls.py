from django.conf import settings
from django.conf.urls import url
from django.conf.urls import include
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.views import login, logout

urlpatterns = [
    url(r'^login/$', login,
        name='login_url',
        kwargs={'template_name': 'login.html'}),
    url(r'^logout/$', logout,
        name='logout_url',
        kwargs={'next_page': '/login/'}),
    url(r'^photos/', include('photos.urls')),
    url(r'^admin/', admin.site.urls),
]

urlpatterns += static(
    settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
)
