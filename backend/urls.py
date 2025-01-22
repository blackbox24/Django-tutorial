from django.contrib import admin
from django.urls import path,include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework.permissions import AllowAny

schema = get_schema_view(
    openapi.Info(
        title="Tutorial APIs",
        default_version="1.0.0",
        description="Django Tutorials for all packages"
    ),
    public=True,
    permission_classes=(AllowAny,),
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("",include("Auths.urls")),
    path("blog/",include("blog.urls")),
    path("accounts/",include("allauth.urls")),
    path("search/",include("haystack.urls")),
    path("docs/",schema.with_ui("swagger",cache_timeout=0),name="swagger-doc"),
    path("sonar/",include("django_sonar.urls")),
]
