from django.db import models
from django.contrib.auth.models import User


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_comment")
    story = models.ForeignKey("Story", on_delete=models.CASCADE, related_name="comment")
    content = models.CharField(max_length=1000)

    @property
    def user_name(self):
        return f'{self.user.first_name} {self.user.last_name}'