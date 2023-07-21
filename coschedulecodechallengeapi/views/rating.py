from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from coschedulecodechallengeapi.models import Rating, Story
from django.contrib.auth.models import User

class RatingView(ViewSet):

    def list(self, request):
        ratings = Rating.objects.all()
        serializer = RatingSerializer(ratings, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk):
        rating = Rating.objects.get(pk=pk)
        serializer = RatingSerializer(rating)
        return Response(serializer.data)
    
    def create(self, request):
        user = User.objects.get(id=request.auth.user.id)
        story = Story.objects.get(pk=request.data["story"])
        rating = Rating.objects.create(
            user = user,
            story = story,
            rating = request.data["rating"]
        )
        serializer = RatingSerializer(rating)
        return Response(serializer.data)

    def update(self, request, pk):
       
        rating = Rating.objects.get(pk=pk)
        story = Story.objects.get(pk=request.data["story"])
        rating.rating = request.data["rating"]
        rating.story = story

        rating.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk):
        rating = Rating.objects.get(pk=pk)
        rating.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ('id', 'story', 'rating', 'user_name')