from django import template
from django.conf import settings

register = template.Library()


@register.filter
def mediapath(value):
    """
    Фильтр, который добавляет префикс MEDIA_URL к пути изображения.
    """
    return f"{settings.MEDIA_URL}{value}"


@register.simple_tag
def mediapath_tag(value):
    """
    Шаблонный тег, который добавляет префикс MEDIA_URL к пути изображения.
    """
    return f"{settings.MEDIA_URL}{value}"
