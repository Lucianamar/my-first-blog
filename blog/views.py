from django.shortcuts import render

# Create your views here.
def post_list(request):
    return render(request, 'blog/post_list.html', {})
from django.shortcuts import render

def post_list(request):
    return render(request, 'blog/post_list.html', {})