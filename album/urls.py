from django.urls import path, re_path
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('search/', views.search, name = 'search'),
    # path('single_image/<int:image_id>', views.single_image, name = 'single_image')
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)