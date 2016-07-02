from django import template


register = template.Library()


@register.filter(name='did_like')
def did_like(photo, user):
    return photo.like_set.filter(user=user, status=True).exists()
    # return Like.objectes.filter(photo=photo, user=user, status=True).exists()


