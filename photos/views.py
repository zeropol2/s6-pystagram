from django.contrib.auth.decorators import login_required
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

create_photo = login_required(PhotoCreate.as_view())


def delete_photo(request, pk):
    pass


def view_photo(request, pk):
    pass


def list_photos(request):
    pass


def create_comment(request, pk):
    pass


def delete_comment(request, pk):
    pass





