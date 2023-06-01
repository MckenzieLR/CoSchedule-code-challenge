from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from coschedulecodechallengeapi.views.comment import CommentView
from coschedulecodechallengeapi.views.rating import RatingView
from coschedulecodechallengeapi.views.story import ExternalStories
from coschedulecodechallengeapi.views.client_story import ClientStoryView
from coschedulecodechallengeapi.views.auth import login_user, register_user
from rest_framework import routers


router = routers.DefaultRouter(trailing_slash=False)
router.register(r'comments', CommentView, 'comment')
router.register(r'stories', ClientStoryView, 'story')
router.register(r'ratings', RatingView, 'rating')
router.register(r'externaldatasource', ExternalStories, 'externalstory')

urlpatterns = [
    path('register', register_user),
    path('login', login_user),   
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
