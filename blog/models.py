from django.db import models
from django.urls import reverse

# Create your models here.
STATUS_CHOICES = (
    ("complete", "complete"),
    ("pending", "pending"),
)

class Post(models.Model):
    title = models.CharField(max_length=300)
    description = models.TextField()
    status = models.CharField(max_length=100, choices=STATUS_CHOICES)
    created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ["-created",]
        verbose_name = "Post"
        verbose_name_plural = "Posts"

    def __str__(self):
        return str(self.title)
    
    def get_absolute_url(self):
        return reverse("post_detail", args=[self.pk])

