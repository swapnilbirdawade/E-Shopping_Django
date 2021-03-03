from django.contrib import admin
from django.urls import path, include
from . import settings
from django.conf.urls.static import static


admin.site.site_header = "E-Shopping Website"
admin.site.site_title = "sqlite_Eshop"
admin.site.index_title = "E-Shopping"

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', include('store.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
