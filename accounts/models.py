from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse

# Create your models here.
class CustomUser(AbstractUser):
    mobile_number = models.CharField(max_length=10, unique = True)
    age = models.PositiveIntegerField( blank=True, null=True)
    # def get_absolute_url(self):
    #     return reverse('', args=[str(self.name)])
    

# Model for category, it will add all the categories( we'll display them on the home page only, and use them in url)
class Category(models.Model):
    # cat_pk = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='static/img', default='')
    def get_absolute_url(self):
        return reverse('home')

    def __str__(self):
        return self.name
    

# Model for posts
class Blog(models.Model):
    # blog_pk = models.AutoField(primary_key=True)   <- we don't need it
    title = models.CharField(max_length=200)
    content = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    category_id = models.CharField(max_length=255)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, )
   

    # category = models.ForeignKey(Category, on_delete=models.CASCADE,)
    # It'll be used to filter posts according to categories
    
    def get_absolute_url(self):
        return reverse('', args=[str(self.category_id), str(self.id)])
        # return reverse('home')

    def __str__(self):
        return self.title 
    
