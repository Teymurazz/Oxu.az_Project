from django.shortcuts import render, HttpResponse, get_object_or_404
from .models import News

def home_page(request):
    news = News.objects.all()
    data = {
        "xeberler": news
    }
    return render(request, "news/home.html", data)

def news_detail(request, news_id):
    news = get_object_or_404(News, pk=news_id)
    
    news.views_count += 1
    news.save()

   
    if request.method == 'POST' and 'like' in request.POST:
        news.likes_count += 1
        news.save()
    
    elif request.method == 'POST' and 'dislike' in request.POST:
        news.dislikes_count += 1
        news.save()
    

    
    data = {
        "news": news
    }

    return render(request, "news/news_detail.html", data)
