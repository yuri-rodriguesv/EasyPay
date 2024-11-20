from django.shortcuts import render
from .models import Topic, Entry
from .forms import TopicForm, EntryForm
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from django.contrib.auth.decorators import login_required


def index(request):
    """Display the homepage"""
    return render(request, 'easypays/index.html')

@login_required
def topics(request):
    """Display all topics"""
    topics = Topic.objects.filter(owner=request.user).order_by('date_added') 
    context = {'topics': topics}
    return render(request, 'easypays/topics.html',context)

@login_required
def topic(request, topic_id):
    """Display a single topic and its entries"""
    topic = Topic.objects.get(id=topic_id) 

    if topic.owner!=request.user:
        raise Http404("You do not have permission to view this topic.")
    
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'easypays/topic.html',context)

@login_required
def new_topic(request):
    """Create a new topic"""
    if request.method != 'POST':
        # Nenhum dado submetido; cria um formulario em branco
        form = TopicForm()
    else:
        # Dados de POST submetidos; processa os dados
        form = TopicForm(request.POST)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()
            print("Topic created")
            return HttpResponseRedirect(reverse('topics'))
    context = {'form': form}
    return render(request, 'easypays/new_topic.html', context)

@login_required
def new_entry(request,topic_id):
    """Create a new entry for a topic"""
    topic = Topic.objects.get(id=topic_id)

    if topic.owner!=request.user:
        raise Http404("You do not have permission to view this topic.")
    
    form = EntryForm(request.POST)

    if request.method != 'POST':
        form = EntryForm()
    else:
        # Dados de POST submetidos; processa os dados
        form = EntryForm(request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return HttpResponseRedirect(reverse('topic', args=[topic_id]))
    context = {'topic': topic, 'form': form}
    return render(request, 'easypays/new_entry.html', context)

@login_required
def edit_entry(request, entry_id):
    """Edit an existing entry"""
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic

    if topic.owner!=request.user:
        raise Http404("You do not have permission to view this topic.")

    if request.method != 'POST':
        form = EntryForm(instance=entry)
    else:
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('topic', args=[topic.id]))
    context = {'entry': entry, 'topic': topic, 'form': form}
    return render(request, 'easypays/edit_entry.html', context)