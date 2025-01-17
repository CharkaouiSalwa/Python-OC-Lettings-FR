from django.contrib import admin
from django.urls import path, include

from . import views


def trigger_error(request):
    division_by_zero = 1 / 0
    return division_by_zero


urlpatterns = [
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),
    path('lettings/', include('lettings.urls')),
    path('profiles/', include('profiles.urls')),
    path('sentry-debug/', trigger_error),
]

# Associez les gestionnaires d'erreur 404 et 500 à nos vues personnalisées
handler404 = 'oc_lettings_site.views.custom_page_not_found'
handler500 = 'oc_lettings_site.views.custom_server_error'
