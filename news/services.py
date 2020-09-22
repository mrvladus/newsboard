from .models import Post, Comment


def get_posts(counter, posts_on_page):  # Получение постов на странице и их кол-во
    return Post.objects.order_by('-post_date')[counter:counter + posts_on_page], Post.objects.all().count()


def get_post(post_id):
    return Post.objects.get(id=post_id)


def delete_post(post_id):
    Post.objects.get(id=post_id).delete()


def get_comments(post_id):
    return Comment.objects.filter(comment_post_id=post_id).order_by('-comment_date').values()


def publish_comment(post_id, comment_text):
    Comment.objects.create(comment_post_id=post_id, comment_text=comment_text)


def delete_comment(comment_id):
    Comment.objects.get(id=comment_id).delete()
