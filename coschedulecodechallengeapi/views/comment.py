from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from coschedulecodechallengeapi.models import Comment, Story
from django.contrib.auth.models import User

class CommentView(ViewSet):
    def list(self, request):
        comments = Comment.objects.all()
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


        """Handle GET requests for single comment

        Returns:
            Response -- JSON serialized comment
        """
        comment = Comment.objects.get(pk=pk)
        serializer = CommentSerializer(comment)
        return Response(serializer.data)
    
    def create(self, request):
        """Handle POST operations

        Returns:
        Response -- JSON serialized comment instance"""
        user = User.objects.get(id=request.auth.user.id)
        story = Story.objects.get(pk=request.data["story"])
        comment = Comment.objects.create(
            user = user,
            story = story,
            content = request.data["content"]
        )
        serializer = CommentSerializer(comment)
        return Response(serializer.data)

    def update(self, request, pk):
        """Handle PUT requests for a comment

        Returns:
            Response -- Empty body with 204 status code
        """
    
       
        comment = Comment.objects.get(pk=pk)
        story = Story.objects.get(pk=request.data["story"])
        comment.content = request.data["content"]
        comment.story = story

        comment.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk):
        comment = Comment.objects.get(pk=pk)
        comment.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'story', 'content', 'user_name')