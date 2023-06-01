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
from rest_framework import status
from coschedulecodechallengeapi.models import Story


class ExternalStories(ViewSet):

    def list(self, request):

        top_stories_url = "https://hacker-news.firebaseio.com/v0/topstories.json?print=pretty"

        top_stories_response = requests.get(top_stories_url)

        if top_stories_response.status_code == 200:  
            data = top_stories_response.json()
            story_id_array = [data]

        else:
            print("Error: Request failed with status code", top_stories_response.status_code)


#        top_stories_object_array = []

        # for id in story_id_array:
        #     single_object_url = f"https://hacker-news.firebaseio.com/v0/item/{id}.json?print=pretty"
        #     response = requests.get(single_object_url)

        full_story_objects = []

        for id in story_id_array:
            full_object_url = f"https://hacker-news.firebaseio.com/v0/item/{id}.json?print=pretty"  
            response = requests.get(full_object_url)

            if response.status_code == 200:  # Successful request
                full_story_object = response.json()
                full_story_objects.append(full_story_object)
            else:
                print(f"Error: Request failed for object ID {id} with status code", response.status_code)

        for story_object in full_story_objects:
            array_of_story_objects = []

            new_object = {
                Story.by: story_object.by,
                Story.title: story_object.title,
                Story.url: story_object.url
            }
            array_of_story_objects.append(new_object)
            # response = Response(array_of_story_objects, status=status.HTTP_200_OK)
            # return response
            response = HttpResponse("Hello, World!")
            return response
#    print(new_object)
