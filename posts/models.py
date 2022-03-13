from distutils.command.upload import upload
from django.db import models

class Post(models.Model):
  title = models.CharField(max_length=250)
  description = models.TextField(blank=True, null=True)
  image = models.ImageField(upload_to="post/images")
  created_at = models.DateTimeField(auto_now_add=True, blank=True)

  def __str__(self) -> str:
      return self.title