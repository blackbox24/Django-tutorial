## haySTACK TUTORIALS

## INSTALLATION 
### usin SOLR
- [X] install django-haystack package `pip install haystack[elasticsearch]`
- [x] install py pack `pysolr` 
- [x] create a model for a poll or note-takin application 
- [x] install a search engine on ubuntu distro

## Configuration
- [X] add `"haystack"` to `INSTALLED_APPS` array
- [x] add signal processor for the haystack. This signal will update objects in an index `HAYSTACK_SIGNAL_PROCESSOR = 'haystack.signals.RealtimeSignalProcessor'`
- [x] conf HAYSTACK_CONNECTIONS
    ```py
    HAYSTACK_CONNECTIONS = {
        'default': {
            'ENGINE': 'haystack.backends.solr_backend.SolrEngine',
            'URL': 'http://127.0.0.1:8983/solr'
            # ...or for multicore...
            # 'URL': 'http://127.0.0.1:8983/solr/mysite',
        },
    }

    # OR
    HAYSTACK_CONNECTIONS = {
        'default': {
            'ENGINE': 'haystack.backends.solr_backend.SolrEngine',
            'URL': 'http://127.0.0.1:8983/solr/tester',                 # Assuming you created a core named 'tester' as described in installing search engines.
            'ADMIN_URL': 'http://127.0.0.1:8983/solr/admin/cores'
            # ...or for multicore...
            # 'URL': 'http://127.0.0.1:8983/solr/mysite',
        },
    }
    ```
## Handling Data
- [x] create a new file called `search_indexes.py` and copy and paste the ff
    ```py
    import datetime
    from haystack import indexes
    from .models import Blog

    class BlogIndex(indexes.SearchField, indexes.Indexable): # model_name + Index
        text = indexes.CharField(document=True,use_template=True,template_name="search/blog_search.txt")
        owner = indexes.CharField(model_attr="owner")
        title = indexes.CharField(model_attr="title")
        pub_data = indexes.DateTimeField(model_attr="updated_at")

        def get_model(self):
            return Blog
        
        def index_queryset(self,using=None):
            return self.get_model().objects.all()
        

    ```
- [x] create `search.html` in templates/search directory  

## Add The SearchView to your root Url conf
- [x] include `haystack.urls` with url name of search 

## Build index
- [x] run `Python manage.py rebuild_index` in your terminal 


### using whoosh
- [x] install `whoosh` package
- [x] define conf or whoosh
- [x] create a `search_indexes`
- [x] define urls in root urlconf
- [x] run `py manage.py rebuild_index`