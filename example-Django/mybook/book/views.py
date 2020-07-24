from django.shortcuts import render
from book.models import Book


def index(request):
    book_list = Book.objects.all()
    return render(request, 'index.html', {'title': '图书列表', 'book_list': book_list})


def detail(request, bid):
    """
    书籍详情
    :param request: 请求对象
    :param bid: book id
    :return:
    """
    book = Book.objects.get(id=bid)
    return render(request, 'detail.html', {'book': book})
