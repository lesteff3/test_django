
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView

from .forms import *
from .models import *


# class BookHome(ListView):
#     model = Books
#     template_name = 'books/index.html'
#     extra_context = {'title': 'shop_books'}
#
#     def get_queryset(self):
#         return Books.objects.filter(is_published=True)
#
#     def index(self, request):
#         book = Books.objects.all()
#         for i in book:
#             if i.count <= 0:
#                 i.is_published = False
#                 i.save()
#             else:
#                 i.is_published = True
#                 i.save()
#         return render(request, 'books/index.html', {'i':i})
#
#

def index(request):
    public = Books.objects.filter(is_published=True)
    for i in public:
        if i.count <= 0:
            i.is_published = False
            i.save()

    return render(request, 'books/index.html', { 'public' : public})


def stats(request):
    author = Books.objects.all()
    count_book = Books.objects.values_list('count', flat=True)
    count = 0
    for i in count_book:
        count += i
    stock_book = Books.objects.values_list('stock', flat=True)
    count_stock = 0

    for c in stock_book:
        count_stock += c

    sell_books = count_stock / count

    return render(request, 'books/stats.html', {
        'count': count,
        'count_stock': count_stock,
        'author': author,
        'sell_books': float('{:.3f}'.format(sell_books))
    })


def create(request):
    error = ''
    if request.method == "POST":
        form = BooksForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма была не верной'

    form = BooksForm()

    data = {
        'form': form,
        'error': error
    }
    return render(request, 'books/create.html', data)




class BookDetailView(View):
    def get(self,request, pk):
        book = Books.objects.get(id=pk)
        book.count = book.count - 1
        book.stock = book.stock + 1

        book.save()


        return render(request, 'books/details_view.html', {'book':book})