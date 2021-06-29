from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# blog App 에서 구현할 서비스를 작성합니다.

def index(request):
    return HttpResponse("Hello World")


def test2(request, id):
    print(type(id))
    return HttpResponse(id)
