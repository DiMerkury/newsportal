from django.urls import path
# Импортируем созданное нами представление
from .views import PostList, PostDetail, NewsList, SearchPost, PostCreate, PostUpdate, PostDelete


urlpatterns = [
   # path — означает путь.
   # В данном случае путь ко всем товарам у нас останется пустым,
   # чуть позже станет ясно почему.
   # Т.к. наше объявленное представление является классом,
   # а Django ожидает функцию, нам надо представить этот класс в виде view.
   # Для этого вызываем метод as_view.

   #path('', NewsList.as_view()),
   #path('posts/', PostList.as_view()),
   #path('posts/<int:pk>', PostDetail.as_view()),

   path('news/', PostList.as_view(), name='post_list'),
   path('news/<int:pk>', PostDetail.as_view(), name='post_detail'),
   path('news/search/', SearchPost.as_view(), name='post_search'),
   path('news/create/', PostCreate.as_view(), name='news_create'),
   path('news/<int:pk>/edit/', PostUpdate.as_view(), name = 'news_update'),
   path('news/<int:pk>/delete/', PostDelete.as_view(), name = 'news_delete'),
   path('articles/create/', PostCreate.as_view(), name='articles_create'),
   path('articles/<int:pk>/edit/', PostUpdate.as_view(), name = 'articles_update'),
   path('articles/<int:pk>/delete/', PostDelete.as_view(), name = 'articles_delete'),
]