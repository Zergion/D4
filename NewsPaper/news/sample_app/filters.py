from django_filters import FilterSet
from django.forms import DateTimeInput
from .models import Post


class Post(FilterSet):

    added_after = DateTimeFilter(
        field_name='added_at',
        lookup_expr='gt',
        widget=DateTimeInput(
            format='%Y-%m-%dT%H:%M',
            attrs={'type': 'datetime-local'},
        ),
    )


class Meta:

       model = Post

       fields = {

           'name': ['icontains'],

           'quantity': ['gt'],
           'price': [
               'lt',
               'gt',
           ],
       }