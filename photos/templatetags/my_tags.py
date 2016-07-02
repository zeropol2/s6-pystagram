from django import template


register = template.Library()


@register.filter(name='did_like')
def did_like(photo, user):
    return photo.like_set.filter(user=user, status=True).exists()
    # return Like.objectes.filter(photo=photo, user=user, status=True).exists()


@register.simple_tag
def helloworld(*args, **kwargs):
    msg = []
    msg.append(', '.join([str(a) for a in args]))

    msg.append('<ul>')
    for k, v in kwargs.items():
        msg.append('<li>{} : {} </li>'.format(k, v))
    msg.append('</ul>')

    return ''.join(msg)
