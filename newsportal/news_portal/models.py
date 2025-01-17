from django.db import models
from django.db.models import Sum
from django.contrib.auth.models import User

news = 'NW'
article = 'AR'

TYPE_POST = [
    (news, 'Новость'),
    (article, 'статья')
]

class Author(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    rating = models.IntegerField(default = 0)

    def update_rating(self):
        per = 0
        per = (self.posts.aggregate(Sum('rating'))['rating__sum'] * 3) or 0
        per += Comment.objects.filter(user = self.id).aggregate(Sum('rating'))['rating__sum'] or 0
        per += Comment.objects.filter(post__in = self.posts.values('id')).aggregate(Sum('rating'))['rating__sum'] or 0
        self.rating = per
        self.save()

    def __str__(self):
        return self.user.username

class Category(models.Model):
    name_category = models.CharField(max_length=100, unique = True)

    def __str__(self):
        return self.name_category

class Post(models.Model):
    type = models.CharField(max_length=2, choices=TYPE_POST, default=news)
    title = models.CharField(max_length=100)
    text = models.TextField()
    rating = models.IntegerField(default = 0)
    datetime_in = models.DateTimeField(auto_now_add = True)
    author = models.ForeignKey(Author, related_name='posts', on_delete = models.CASCADE)
    category = models.ManyToManyField(Category, through = 'PostCategory')

    def preview(self) -> str:
        return self.text[:125] + '...' if len(self.text) > 124 else self.text[:125]

    def like(self):
        self.rating += 1
        self.save()
    
    def dislike(self):
        self.rating -= 1
        self.save()

    def __str__(self):
        return f'{self.title} Date: {self.datetime_in} {self.text[:20]} '
    
class PostCategory(models.Model):
    post =  models.ForeignKey(Post, on_delete = models.CASCADE)
    category = models.ForeignKey(Category, on_delete = models.CASCADE)

class Comment(models.Model):
    text = models.TextField()
    datatime_in = models.DateTimeField(auto_now_add = True)
    rating = models.IntegerField(default = 0)
    post = models.ForeignKey(Post, on_delete = models.CASCADE)
    user = models.ForeignKey(User, on_delete = models.CASCADE)

    def like(self):
        self.rating += 1
        self.save()
    
    def dislike(self):
        self.rating -= 1
        self.save()
