
from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, re_path, path


from .views import (
    articles_view,
    article_detail_view,
    article_create_view,
    article_update_view,
    article_delete_view,
    search_article_view,
)

app_name = "article"

urlpatterns = [
    path('list/', articles_view, name='list'),
    path('search/', search_article_view, name='search'),
    path('detail/<int:article_id>/', article_detail_view, name='detail'),
    path('create/', article_create_view, name='add'),
    path('edit/', article_update_view, name='edit'),
    path('delete/', article_delete_view, name='delete'),
]
