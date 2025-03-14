from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .models import Blog
from .forms import BlogForm

from haystack.views import SearchView
from haystack.query import SearchQuerySet
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

class BlogSearchView(SearchView):
    template = "blog/search.html"

    def extra_content(self):
        content = super(BlogSearchView,self).extra_context()
        content["query"] = self.request.GET.get("q","")
        return content

def search(request):
    query = request.GET.get("q")
    results = SearchQuerySet().filter(content=query)
    return render(request,"blog/search.html",{"pages":results})
