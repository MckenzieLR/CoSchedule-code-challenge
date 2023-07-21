# Get list of stories 
# https://hacker-news.firebaseio.com/v0/topstories.json?print=pretty
# loop through stories id array and populate individual story models (array of story objects)
# pass through each story id into endpoint(url) as a parameter 
# https://hacker-news.firebaseio.com/v0/item/36104547.json?print=pretty 
# get single story (for ratings or comments) (retrieve)
# create StorySerializer

import requests
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from django.http import HttpResponse
from rest_framework import status, serializers
from coschedulecodechallengeapi.models import Story
import json
from django.contrib.auth.models import User


class ExternalStories(ViewSet):

    #gets external api topstories 
    # limits top 10 stories
    def list(self, request):

        top_stories_url = "https://hacker-news.firebaseio.com/v0/topstories.json?print=pretty"


        top_stories_response = requests.get(top_stories_url)

        if top_stories_response.status_code == 200:  
            data = top_stories_response.json()
            limit = 10  # Specify the desired limit here
            story_id_array = data[:limit]

        else:
            print("Error: Request failed with status code", top_stories_response.status_code)



        full_story_objects = []

    # looping through story_id_array to get each story id and pass as parameter to get the full story object 
        for id in story_id_array:
            full_object_url = f'https://hacker-news.firebaseio.com/v0/item/{id}.json?print=pretty' 
            response = requests.get(full_object_url)

            if response.status_code == 200:  # Successful request
                full_story_object = response.json()
                full_story_objects.append(full_story_object)
            else:
                print(f"Error: Request failed for object ID {id} with status code", response.status_code)
    #builds new_story using story model, adds stories to array and saves them to the database
        stories = []
        for story_object in full_story_objects:
            new_story = Story()
            # new_story.by = ("hello", "hi", "hey")
            print( 'new_story', new_story)
            print('story_object', story_object)
            new_story.id=story_object['id']
            new_story.by=story_object['by']
            new_story.title=story_object['title']

            if 'url' in story_object:
                new_story.url = story_object['url']
            elif 'text' in story_object:
                new_story.text = story_object['text']


            stories.append(new_story)
            new_story.save()
        serializer = StorySerializer(stories, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk):
        story=Story.objects.get(pk=pk)
        serializer=StorySerializer(story)
        return Response(serializer.data)
    
        
class StorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Story
        fields = ('id', 'by', 'title', 'url', 'story_comment', 'story_rating')
        depth=1
