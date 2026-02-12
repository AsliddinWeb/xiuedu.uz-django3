from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns

# Admin custom
admin.site.site_title = "XIU Admin"
admin.site.site_header = "Xalqaro Innovatsion Universitet"
admin.site.index_title = "Boshqaruv Paneli"

# Til almashtirishsiz URL'lar
urlpatterns = [
    path('admin/', admin.site.urls),
    path('i18n/', include('django.conf.urls.i18n')),
]

# Til bilan URL'lar
urlpatterns += i18n_patterns(
    path('', include('apps.home.urls')),
)

# Media va Static
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)