from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=20)

class Post(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    # related_name of posts, we can access category.posts to give us a list of posts with that category
    categories = models.ManyToManyField('Category', related_name='posts')

# allow users to make comments 
class Comment(models.Model):
    author = models.CharField(max_length=60)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    # many to one relationship defined with foreign key
    post = models.ForeignKey('Post', on_delete=models.CASCADE)