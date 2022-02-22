from html import unescape
from datetime import datetime
from django.shortcuts import render
from YouTubeSearch.settings import YOUTUBE_API_KEY
from googleapiclient.discovery import build
from youtube_search_api.models import QueryResult


youtube = build('youtube', 'v3',
                developerKey=YOUTUBE_API_KEY)

# Create your views here.


def index(request):
    if not QueryResult.objects.all().exists():
        query = 'Apple'
        youtube_request = youtube.search().list(
            part='snippet',
            q=query,
            type='video',
            maxResults=50
        )
        response = youtube_request.execute()
        items = response['items']
        for item in items:
            video_url = "https://www.youtube.com/watch?v=" + \
                item['id']['videoId']
            channel_name = unescape(item['snippet']['channelTitle'])
            title = unescape(item['snippet']['title'])
            description = unescape(item['snippet']['description'])
            thumbnail_url = item['snippet']['thumbnails']['high']['url']
            publish_time = datetime.strptime(
                item['snippet']['publishedAt'],  "%Y-%m-%dT%H:%M:%SZ")

            result = QueryResult(video_url=video_url, channel_name=channel_name, title=title,
                                 description=description, thumbnail_url=thumbnail_url,
                                 publish_time=publish_time)
            result.save()

    return render(request, 'youtube_search_api/index.html')


def search(request):
    query = request.GET['query']
    search_type = request.GET['search_type']
    results = QueryResult.objects.filter(title__icontains=query)
    im_feeling_lucky = False
    if search_type == 'im_feeling_lucky':
        im_feeling_lucky = True
    context = {'videos': results, 'query': query,
               'im_feeling_lucky': im_feeling_lucky}
    return render(request, 'youtube_search_api/search.html', context)
