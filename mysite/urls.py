
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from rest_framework_jwt.views import obtain_jwt_token

from blog import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
    path('', include('blog.urls')),
    path('api/posts/', include('blog.api.urls'), name='posts-api'),
    path('api/comments/', include('blog.api_comments.urls'), name='comments-api'),
    path('api-token-auth/', obtain_jwt_token),
]


#  path('', views.like_post, name="like_post"),  url(r'^like/$', views.like_post, name="like_post"),
