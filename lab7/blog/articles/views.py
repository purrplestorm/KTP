from articles import models
from django.shortcuts import render
from django.shortcuts import redirect
from articles.models import Article
from django.http import HttpResponse
from django.http import Http404
from articles import views
import articles

def archive(request):
    return render(request, 'archive.html', {"posts": Article.objects.all()})

def get_article(request, article_id):
    try:
        post = Article.objects.get(id=article_id)
        return render(request, 'article.html', {"post": post})
    except Article.DoesNotExist:
        raise Http404

def create_post(request):
    if not request.user.is_anonymous:
        if request.method == "POST":
            form = {
                'text': request.POST["text"],
                'title': request.POST["title"]
            }
            if form["text"] and form["title"]:
                posts = Article.objects.all()
                checkTitle = True
                for post in posts:
                    if post.title == form["title"]:
                        checkTitle = False
                        break
                if checkTitle:
                    article = Article.objects.create(text=form["text"],
                                                     title=form["title"],
                                                     author=request.user)
                    return redirect('get_article', article_id=article.id)
                else:
                    form['errors'] = u"Статья с таким именем уже существует!"
                    return render(request, 'create_post.html', {'form': form})
            else:
                form['errors'] = u"Заполните все поля"
                return render(request, 'create_post.html', {'form': form})
        else:
            return render(request, 'create_post.html', {})
    else:
        raise Http404
