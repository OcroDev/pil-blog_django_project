from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.home_view, name='home'),
]

#indica a django donde se guardaron las imagenes de las bases de datos
urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)