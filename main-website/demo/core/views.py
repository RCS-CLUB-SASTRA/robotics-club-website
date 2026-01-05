from django.http import JsonResponse
from .models import Event, BlogPost


def events_list(request):
    """
    Return a list of all events as JSON
    """
    events = Event.objects.all().values()
    return JsonResponse(list(events), safe=False)


def blogs_list(request):
    """
    Return a list of all blog posts as JSON
    """
    blogs = BlogPost.objects.all().values()
    return JsonResponse(list(blogs), safe=False)
