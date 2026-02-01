from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

# Admin custom
admin.site.site_title = "XIU Admin"
admin.site.site_header = "Xalqaro Innovatsion Universitet"
admin.site.index_title = "Boshqaruv Paneli"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.home.urls')),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)