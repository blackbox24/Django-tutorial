from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .models import Blog
from .forms import BlogForm

from allauth.account.views import login
# Using Django Templates

@login_required()
def index(request):
    blog = Blog.objects.filter(owner=request.user)
    blog_count = blog.count()
    return render(request,"blog/index.html",{"blogs":blog,"count":blog_count})

@login_required()
def createBlog(request):
    if request.method == "POST":
        form = BlogForm(request.POST)
        
        if form.is_valid():
            newblog = form.create(owner=request.user)
            return redirect("blog:index")
    else:
        form = BlogForm()
    template_name = "blog/create.html"
    return render(request,template_name,{"form":form})