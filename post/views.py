from django.shortcuts import render
from django.http import HttpResponse

from .models import Posts

# Create your views here.
def index(request):
    #return HttpResponse('Hello from POSTS')

    pst = Posts.objects.all()[:10]

    context = {
        'title':'Latest Posts',
        'posts': pst
    }

    return render(request, 'post/index.html', context)

def details(request, id):
    post = Posts.get(id=id)

    context = {
        'post': post
    }

    return render(request, 'posts/details.html', context)