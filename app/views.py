from django.core.paginator import Paginator
from django.shortcuts import render

# Create your views here.


#str = "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Asperiores corporis dolore ducimus illum itaque, iusto molestias nemo nihil possimus quidem recusandae similique ut. Debitis doloribus et impedit magnam voluptas voluptate."


questions = [
    {
        "title": f"Title {i}",
        "text": f"This is text for {i} question.",
        "number": f"{i}"
    } for i in range(100)
]

def hot(request):
    paginator = Paginator(questions, 5)
    page = request.GET.get('page')
    content = paginator.get_page(page)
    return render(request, "hot.html", {'questions': content})

def new(request):
    paginator = Paginator(questions, 5)
    page = request.GET.get('page')
    content = paginator.get_page(page)
    return render(request, "new.html", {'questions': content})

def question(request):
    paginator = Paginator(questions, 5)
    page = request.GET.get('page')
    content = paginator.get_page(page)
    return render(request, "one question.html", {'questions': content})

def tag(request):
    paginator = Paginator(questions, 5)
    page = request.GET.get('page')
    content = paginator.get_page(page)
    return render(request, "listing.html", {'questions': content})

def login(request):
    return render(request, "login.html", {})

def signup(request):
    return render(request, "reg.html", {})

def ask(request):
    return render(request, "add question.html", {})

def settings(request):
    return render(request, "settings.html", {})
