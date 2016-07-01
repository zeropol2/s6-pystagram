from django.db import models
from django.conf import settings
from django.core.urlresolvers import reverse_lazy


class Photo(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to='%Y/%m/%d/', null=True, blank=True)
    description = models.TextField(max_length=500, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse_lazy('photos:view_photo', kwargs={'pk': self.pk})

