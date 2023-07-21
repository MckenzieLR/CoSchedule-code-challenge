from django.db import models
from django.contrib.auth.models import User


class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_rating")
    story = models.ForeignKey("Story", on_delete=models.CASCADE, related_name="story_rating")
    rating = models.IntegerField(null=True)

    @property
    def user_name(self):
        return f'{self.user.first_name} {self.user.last_name}'