from django.conf import settings
from django.db import models
from starnavi_test.moderation import toxic_content


class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='posts')
    created_at = models.DateTimeField(auto_now_add=True)
    is_blocked = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if toxic_content(self.content):
            self.is_blocked = True
        super().save(*args, **kwargs)

