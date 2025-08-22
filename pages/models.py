from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User


class Author(models.Model):
  name = models.CharField(max_length=50)
  email = models.EmailField()

  def __str__(self):
    return self.name

class Post(models.Model):
  title = models.CharField(max_length=100)
  content = models.TextField()
  published_date = models.DateTimeField(auto_now_add=True)
  author = models.ForeignKey(User, on_delete=models.CASCADE)
  slug = models.SlugField(unique=True, blank=True)

  def __str__(self):
    return self.title

  def save(self, *args, **kwargs):
    if not self.slug and self.title:
      self.slug = slugify(self.title) 
      
    super().save(*args, **kwargs)

  def short_content(self):
    return self.content[:100] + "..."

  def __str__(self):
    return self.title

class Meta:
  ordering = ['-published_date']

