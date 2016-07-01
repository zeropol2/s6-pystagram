from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.views.generic.edit import CreateView

from .models import Photo


class PhotoCreate(CreateView):
    model = Photo
    fields = ('title', 'content', 'image', 'description', )
    template_name = 'create_photo.html'

    def form_valid(self, form):
        new_photo = form.save(commit=False)
        new_photo.user = self.request.user
        new_photo.save()
        return super(PhotoCreate, self).form_valid(form)

create_photo = login_required(PhotoCreate.as_view())


def delete_photo(request, pk):
    pass


def view_photo(request, pk):
    photo = get_object_or_404(Photo, pk=pk)

    ctx = {
        'photo': photo,
    }

    return render(request, 'view_photo.html', ctx)


def list_photos(request):
    pass


def create_comment(request, pk):
    pass


def delete_comment(request, pk):
    pass





