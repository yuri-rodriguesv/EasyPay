from django.shortcuts import render
from .models import Topic
def index(request):
    return render(request, 'easypays/index.html')


def topics(request):
    topics = Topic.objects.order_by('date_added') 
    context = {'topic': topics}
    return render(request, 'easypays/topics.html',context)