from django import template
from main_page.models import Category, Post

register = template.Library()


@register.inclusion_tag('main_page/menu_tpl.html')
def show_menu(menu_class='menu'):
    categories = Category.objects.all()
    return {'categories': categories, 'menu_class': menu_class}
