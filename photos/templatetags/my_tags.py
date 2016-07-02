from django import template
from django.template.base import VariableNode
from django.contrib.auth import get_user_model


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


@register.tag(name='addnim')
def add_nim(parser, token):
    nodelist = parser.parse(('endaddnim', 'end_add_nim', ))
    parser.delete_first_token()
    return NimNode(nodelist)


class NimNode(template.Node):
    def __init__(self, nodelist):
        self.nodelist = nodelist
        self.user_class = get_user_model()

    def render(self, context):
        output = []

        for node in self.nodelist:
            if not isinstance(node, VariableNode):
                output.append(node.render(context))
                continue

            obj = node.filter_expression.resolve(context)
            if not isinstance(obj, self.user_class):
                output.append(node.render(context))
                continue

            output.append('{}님'.format(node.render(context)))
        return ''.join(output)