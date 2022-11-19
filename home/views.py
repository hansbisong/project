
from django.shortcuts import render
from users.models import Post
from django.views.generic import ListView

def home(request):
  context = {'post': Post.objects.all()}
  return render(request, 'home_page.html', context)

def post(request):
  if request.method == 'POST':
    post = Post.objects.all(request.POST)
    context = {'post':post}
  return render(request,'home_page.html', context)


#class PostListView(ListView):
  #model = Post
  #template_name = 'home_page.html'
  #context_object_name = 'post'
 # ordering = ['date_published']
# Create your views here.
