from django.db import models


class Post(models.Model):
    post_text = models.CharField(max_length=2000)
    post_header = models.CharField(max_length=255)
    post_author = models.CharField(max_length=50)
    post_date = models.DateTimeField(auto_now_add=True)


class Comment(models.Model):
    comment_post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment_text = models.CharField(max_length=255)
    comment_date = models.DateTimeField(auto_now_add=True)
