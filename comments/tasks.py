from celery import shared_task
from django.utils import timezone
from comments.models import Comment
from posts.models import Post


@shared_task
def auto_reply_to_comment(comment_id):
    try:
        comment = Comment.objects.get(id=comment_id)
        post = comment.post
        user = post.author

        reply_content = f"Thank you for your comment! Your response about '{post.title}' is important for us."

        Comment.objects.create(
            post=post,
            author=user,
            content=reply_content,
            created_at=timezone.now()
        )
    except Comment.DoesNotExist:
        pass