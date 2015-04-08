from django.db import models
from django.core.urlresolvers import reverse
from django.utils import timezone

class PostQuerySet(models.QuerySet):
    def published(self):
        return self.filter(publish_on__lte=timezone.now())

class Tag(models.Model):
    slug = models.SlugField(max_length=200, unique=True)

    def __str__(self):
        return self.slug

class Post(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    slug = models.SlugField(max_length=200, unique=True)
    publish_on = models.DateTimeField(
            default=timezone.now
    )
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    tags = models.ManyToManyField(Tag, blank=True)

    objects = PostQuerySet.as_manager()

    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"slug": self.slug})

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.publish_on:
            self.publish_on = timezone.now()
        super(Post, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "Blog Post"
        verbose_name_plural = "Blog Posts"
        ordering = ["-created"]



