from django.contrib.auth.models import User
from django.shortcuts import render
from app.models import *
from app.forms import *

def index(request):
    user = request.user.username
    folders = HyperlinkFolder.objects.all()
    issues = IssueItem.objects.all()
    context = {'user': user, 'folders': folders, 'issues': issues}
    return render(request, 'new_index.html', context)

def folder_new(request):
    title = 'New Hyperlink Folder'
    if request.method == 'POST':        
        form = HyperlinkFolderForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
    else:        
        form = HyperlinkFolderForm()
    context = {'title': title, 'form': form}
    return render(request, 'form.html', context)

def link_new(request):
    title = 'New Hyperlink Folder'
    if request.method == 'POST':        
        form = HyperlinkForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
    else:        
        form = HyperlinkForm()
    context = {'title': title, 'form': form}
    return render(request, 'form.html', context)

def issue_new(request):
    title = 'New Hyperlink Folder'
    if request.method == 'POST':        
        form = IssueItemForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
    else:        
        form = IssueItemForm()
    context = {'title': title, 'form': form}
    return render(request, 'form.html', context)