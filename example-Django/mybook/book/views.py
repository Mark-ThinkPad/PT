from django.shortcuts import render


def index(request):
    return render(request, 'index.html', {'title': '图书列表', 'list': range(10)})
