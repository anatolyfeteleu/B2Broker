from django.urls import include, path

urlpatterns = [
    path("core/", include("core.urls")),
]
