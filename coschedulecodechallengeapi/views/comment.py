from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from coschedulecodechallengeapi.models import Comment, Story
from django.contrib.auth.models import User

class CommentView(ViewSet):

    #GET method gets all comments from database
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
    #POST method to create a new comment, gets user logged in and story selected to add comment to 
    def create(self, request):
       
        user = User.objects.get(id=request.auth.user.id)
        story = Story.objects.get(pk=request.data["story"])
        comment = Comment.objects.create(
            user = user,
            story = story,
            content = request.data["content"]
        )
        serializer = CommentSerializer(comment)
        return Response(serializer.data)
    
    #gets individual comment from pk 
    def retrieve(self, request, pk):
        comment = Comment.objects.get(pk=pk)
        serializer = CommentSerializer(comment)
        return Response(serializer.data)

    #PUT method edit comment and save to existing comment 
    def update(self, request, pk):
    
       
        comment = Comment.objects.get(pk=pk)
        story = Story.objects.get(pk=request.data["story"])
        comment.content = request.data["content"]
        comment.story = story

        comment.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)

    #DELETE method gets comment by pk and deletes it from database
    def destroy(self, request, pk):
        comment = Comment.objects.get(pk=pk)
        comment.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

class StorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Story
        fields=('id', 'title')

class CommentSerializer(serializers.ModelSerializer):
    story = StorySerializer(many=False)
    class Meta:
        model = Comment
        fields = ('id', 'story', 'content', 'user_name')