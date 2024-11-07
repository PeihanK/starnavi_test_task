from django.conf import settings
from django.db import models
from posts.models import Post
from starnavi_test.moderation import toxic_content


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_blocked = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if toxic_content(self.content):
            self.is_blocked = True
        super().save(*args, **kwargs)


