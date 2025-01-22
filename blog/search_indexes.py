import datetime
from haystack import indexes
from .models import Blog

class BlogIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True,use_template=True) #template_name="search/indexes/blog/blog_search.txt")
    owner = indexes.CharField(model_attr="owner")
    title = indexes.CharField(model_attr="title")
    description = indexes.CharField(model_attr="description")

    title_auto = indexes.EdgeNgramField(model_attr="title")
    description_auto = indexes.EdgeNgramField(model_attr="description")
    suggestions = indexes.FacetCharField()


    def get_model(self):
        return Blog
    
    def perpare(self,obj):
        prepare_data = super(BlogIndex,self).prepare(obj)
        prepare_data["suggestions"] = prepare_data["text"]
        return prepare_data
    
    def index_queryset(self,using=None):
        return self.get_model().objects.filter(updated_at__lte=datetime.datetime.now())
    