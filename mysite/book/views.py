from django.shortcuts import render
from .models import Book
from django.http import HttpResponse

# Create your views here.


def search_form(request):
    return render(request, 'search_form.html')

def search(request):
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        books = Book.objects.filter(name='q')
        return render(request, 'search_results.html', {'books': books, 'query': q})
    else:
        return HttpResponse('Please submit a search term.')
