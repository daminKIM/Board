from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Board 

# Create your views here.
def create(request) :
    post = Board()
    post.title = request.GET['title']
    post.body = request.GET['body']
    post.pub_date = timezone.datetime.now()
    post.save()
    return redirect ('home')

def home(request) :
    postings = Board.objects
    return render(request, 'home.html',{'post':postings})

def detail(request, post_id) :
    post_detail = get_object_or_404(Board, pk = post_id)
    return render(request, 'detail.html', {'detail':post_detail})

def upload(request) :
    return render(request, 'upload.html')

