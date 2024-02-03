# from django.http import HttpResponse
from django.shortcuts import render
from customers.models import Customer
from books.models import Book, BookTitle

def home_view(request):
    """ Create a function view to return http response """
    qs = Customer.objects.all()
    # obj = Book.objects.get(id=5)
    obj = BookTitle.objects.get(id=2)
    books = obj.books
    title = obj.title
    print(books, title)


    context = {
        'qs': qs,
        'obj': obj,
    }

    return render(request, 'main.html', context)