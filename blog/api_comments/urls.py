from django.conf.urls import url
from django.contrib import admin
from django.urls import path

from .views import (
    # CommentCreateAPIView,
    CommentDetailAPIView,
    CommentListAPIView,

)

urlpatterns = [
    path('', CommentListAPIView.as_view(), name='list'),
    # path('create/', CommentCreateAPIView.as_view(), name='create'),
    path('<int:pk>/', CommentDetailAPIView.as_view(), name='detail'),
    # path('<int:pk>/edit/', CommentUpdateAPIView.as_view(), name='update'),
    # path('<int:pk>/delete/', CommentDeleteAPIView.as_view(), name='delete'),
]