
from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, re_path, path


from .views import (
    articles_view,
    article_detail_view,
    articles_create_view,
    articles_update_view,
    articles_delete_view
)

urlpatterns = [
    path('list/', articles_view, name='list'),
    path('detail/', article_detail_view, name='detail'),
    path('add/new-article/', article_create_view, name='add'),
    path('edit/', article_update_view, name='edit'),
    path('delete/', article_delete_view, name='delete'),
]
