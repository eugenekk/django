from django.shortcuts import render
from django.views.generic import CreateView
from .models import Book
from .forms import BookForm
from django.http import HttpResponse
# Create your views here.

# book_new = CreateView.as_view(model=Book, fielss='__all__')

def book_new(request):
    if request.method == 'POST':
        form = BookForm(request.POST) # 데이터 바인딩
        if form.is_valid():
            print(form.cleaned_data);
    else:
        form = BookForm()
    return render(request, 'book/book_form.html', {'form':form})

def book_list(request):
    return HttpResponse("hello")