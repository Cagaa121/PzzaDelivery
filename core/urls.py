from django.urls import path, include, re_path
from django.views.static import serve
from django.conf import settings
from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pizza.urls'))


    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
]
