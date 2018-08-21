from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('campus/', include('campus.urls')),
    path('papeis/', include('papeis.urls')),
    path('admin/', admin.site.urls),
]
