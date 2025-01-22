from django.urls import path
from .views import *

app_name = "blog"

urlpatterns = [
    path("",index,name="index"),
    path("add",createBlog,name="add-blog"),
    # path("search/", BlogSearchView.as_view() ,name="blog-search"),
]