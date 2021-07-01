from django.http import response
from django.http.response import Http404, JsonResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from .models import Post
import os
from django.conf import settings

# Create your views here.
# blog App 에서 구현할 서비스를 작성합니다.

def index(request):
    post_list = Post.objects.all()
    output = ','.join([p.title for p in post_list])
    return HttpResponse(output)

def index2(request):
    post_list = Post.objects.all()
    return render(request, 'blog/index.html', {'post_list':post_list})

# def detail(request, id): #urls.py 에서 인자로 받기로 한 url정보
#     try:
#         post = Post.objects.get(id=id)
#     except Post.DoesNotExist:
#         raise Http404("page not found")
#     return render(request, 'blog/detail.html', {'post':post})

def detail(request, id): #urls.py 에서 인자로 받기로 한 url정보
    post = get_object_or_404(Post, id=id)
    return render(request, 'blog/detail.html', {'post':post})

def json_test(request):
    music = {'singer':'BTS', 'songs': ['Fake Love', 'DNA', '피땀눈물', '봄날']}
    return JsonResponse(music, json_dumps_params={'ensure_ascii': False})

def excel_download(request):
    filepath = os.path.join(settings.BASE_DIR, 'demo.xlsx')
    filename = os.path.basename(filepath)
    with open(filepath, 'rb') as f:
        response = HttpResponse(f, content_type = 'application/vnd.ms-excel')
        response["Content-Disposition"] = "attachment; filename={}".format(filename)
        return response

def get_redirect1(request):
    return redirect('/blog/', permanent=True) 

def get_redirect2(request):
    return redirect('http://google.com')

def test2(request, id):
    print(type(id))
    return HttpResponse(id)
