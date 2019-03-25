from django.db import models

class Post(models.Model):
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    view_count = models.IntegerField(default=0)
    image = models.ImageField(upload_to="images/")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
       return self.title
    
    def comments(self):
        return Comment.objects.filter(post=self)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    body = models.CharField(max_length=300)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.body
