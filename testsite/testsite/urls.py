
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from books.views import *

from django.urls import path, include

from login.views import *
from testsite import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('books.urls')),
    path('registration/', include('login.urls')),




] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT )