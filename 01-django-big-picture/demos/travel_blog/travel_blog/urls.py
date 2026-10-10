
from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path

from travel_blog import settings
from trips.views import landing_page, detail_page, comment

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", landing_page, name="landing"),
    path("trips/<int:pk>", detail_page, name="trip_detail"),
    path("trips/comment/<int:pk>", comment, name="trip_comment"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
