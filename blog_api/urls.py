from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from apps.accounts.views import login_view, register_view, logout_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('blog/', include('apps.posts.urls')),
    path('api/users/', include("apps.accounts.api.urls", namespace='users-api')),
    path('api/posts/', include("apps.posts.api.urls", namespace='posts-api')),
    path('ckeditor/', include('ckeditor_uploader.urls')),

]



if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)