from django.urls import path
from .views import (PostListView,
                    PostDetailView,
                    PostCreateView,
                    PostUpdateView,
                    PostDeleteView
                    )

from . import views

urlpatterns = [
    path('',PostListView.as_view(), name = 'blog-home' ),
    path('post/<slug:slug>/',PostDetailView.as_view(), name = 'post-detail' ),
    path('post/new/',PostCreateView.as_view(), name = 'post-create' ),
    path('post/update/<slug:slug>/',PostUpdateView.as_view(), name = 'post-update' ),
    path('post/<slug:slug>/delete/',PostDeleteView.as_view(), name = 'post-delete' ),
    # path('post/new/',views.post_create, name = 'post-create' ),

 ]