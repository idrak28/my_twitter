from django.shortcuts import render
from .models import Tweet
from django.shortcuts import get_object_or_404
from .forms import TweetForm
# Create your views here.
def index(request):
    return render(request,'index.html')



def tweet_list(request):
    tweets=Tweet.objects.all().order_by('-created_at')
    return render(request, 'tweet_list.html', {'tweet':tweets})


def tweet_create(request):
    pass