from django import template

register = template.Library()

BAD_WORDS = {'текст', 'слово1', 'слово2', 'слово3', 'слово4', 'слово5', 'слово6', 'слово7', 'слово8'}

@register.filter()
def censor(value):
   value_words = value.split()
   censor_words =[]
   for word in value_words:
      if word.lower() in BAD_WORDS:
         censor_words.append(word[0]+'*' * (len(word)-1))
      else:
         censor_words.append(word)
   return ' '.join(censor_words)

@register.filter()
def get_list_categoty(post):
   return ", ".join([category.name_category for category in post.category.all()])