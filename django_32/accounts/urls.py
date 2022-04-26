
from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, re_path, path


from .views import (
    user_login_view,
    user_logout_view,
    user_register_view,
)

app_name = "accounts"

urlpatterns = [
    path('login/', user_login_view, name='login'),
    path('logout/', user_logout_view, name='logout'),
    path('register/', user_register_view, name='register'),
]
