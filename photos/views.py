from django.shortcuts import render
from django.views.generic.edit import CreateView

from .models import Photo


class PhotoCreate(CreateView):
    model = Photo
    fields = ('image', 'description', )
    template_name = 'create_photo.html'

    def form_valid(self, form):
        new_photo = form.save(commit=False)
        new_photo.user = self.request.user
        new_photo.save()
        return super(PhotoCreate, self).form_valid(form)

