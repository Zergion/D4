from django import template


register = template.Library()



@register.filter()
def currency(value):
   """
   value: значение, к которому нужно применить фильтр
   """

   return f'{value} Р'


@register.simple_tag(takes_context=True)
def url_replace(context, **kwargs):
   d = context['request'].GET.copy()
   for k, v in kwargs.items():
       d[k] = v
   return d.urlencode()