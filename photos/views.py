from django.shortcuts import render
from django.views.generic.edit import CreateView

from .models import Photo


class PhotoCreate(CreateView):
    model = Photo
    fields = ('image', 'description', )
    template_name = 'create_photo.html'

