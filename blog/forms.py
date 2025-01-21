from django import forms
from .models import *

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = [
            "title","description",
        ]

    def create(self,owner):
        title = self.cleaned_data.get("title")
        description = self.cleaned_data.get("description")
        blog = Blog.objects.create(
            title=title,description=description,owner=owner
        )
        return blog