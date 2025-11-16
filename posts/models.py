from django.db import models

# Create your models here.




class Category(models.Model):
    name = models.CharField(max_length=100)


    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    categories = models.ForeignKey(Category,on_delete=models.CASCADE, related_name='posts',null=True,blank=True)

    def __str__(self):
        return self.title
