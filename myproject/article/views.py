# from myproject import article
from django.shortcuts import render
from .models import Article

# Create your views here.
def article_list(request):
    qs = Article.objects.all()
    q = request.GET.get('q') # client 가 보낸 검색창 입력값
    if q:
        qs = qs.filter(title__icontains=q)
    return render(request, 'article/article_list.html', {'article_list' : qs, 'q':q})