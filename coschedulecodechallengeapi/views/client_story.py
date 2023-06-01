from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from coschedulecodechallengeapi.models import Story
from django.contrib.auth.models import User

class ClientStoryView(ViewSet):
    def list(self, request):
        stories = Story.objects.all()
        serializer = StorySerializer(stories, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class StorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Story
        fields = ('id', 'by', 'title', 'url')