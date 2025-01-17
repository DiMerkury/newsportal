from django_filters import FilterSet, ModelMultipleChoiceFilter, DateFilter
from django import forms
from .models import Post, Category

class DateInput(forms.DateInput):
    input_type = 'date'

class PostFilter(FilterSet):
   category = ModelMultipleChoiceFilter(
       field_name = 'category',
       queryset = Category.objects.all(),
       label = 'Категория',
       conjoined = True,
   )
   datetime_in = DateFilter(widget = DateInput(attrs={'class': 'datepicker'}), lookup_expr='gt', label='С даты создания')

   class Meta:
       model = Post
       fields = {
           'title': ['icontains'],
       }
