from articles import models
from django.shortcuts import render
from articles.models import Article
from django.http import HttpResponse

def archive(request):
    return render(request, 'archive.html', {"posts": Article.objects.all()})


