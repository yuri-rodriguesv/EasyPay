from django.shortcuts import render
from .models import Topic
from .forms import TopicForm
from django.http import HttpResponseRedirect
from django.urls import reverse
def index(request):
    """Display the homepage"""
    return render(request, 'easypays/index.html')


def topics(request):
    """Display all topics"""
    topics = Topic.objects.order_by('date_added') 
    context = {'topics': topics}
    return render(request, 'easypays/topics.html',context)

def topic(request, topic_id):
    """Display a single topic and its entries"""
    topic = Topic.objects.get(id=topic_id) 
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'easypays/topic.html',context)

def new_topic(request):
    """Create a new topic"""
    if request.method != 'POST':
        # Nenhum dado submetido; cria um formulario em branco
        form = TopicForm()
    else:
        # Dados de POST submetidos; processa os dados
        form = TopicForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('topics'))
    context = {'form': form}
    return render(request, 'easypays/new_topic.html', context)

