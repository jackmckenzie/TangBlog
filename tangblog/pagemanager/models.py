from django.db import models

# Create your models here.

class Page(models.Model):
    created = models.DateTimeField(auto_add_new=True)
    modified = models.DateTimeField(auto_add=True)
    title = models.CharField(max_length=100)
    url = models.SlugField()
    body = model.TextField()
    parent = models.PositiveIntegerField(default=0)
    sort = models.PositiveIntegerField(
    def __str__(self):
        return self.body
    def get_parent(self):
        return self.parent
