from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('travel_frame.common.urls')),
    path('accounts/', include('travel_frame.accounts.urls')),
    path('destinations/', include('travel_frame.destinations.urls')),
    path('travel_photos/',include('travel_frame.travel_photos.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
