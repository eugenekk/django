from django import forms
from .models import Book

class BookForm(forms.Form):
    title = forms.CharField(label="제목")
    author = forms.CharField(label="저자")
    publisher = forms.CharField(label="출판사", required=False)
