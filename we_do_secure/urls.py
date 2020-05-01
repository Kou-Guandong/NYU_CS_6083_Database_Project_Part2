from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers
from insurance import views

from django.conf.urls import include, url
from django_registration.backends.one_step.views import RegistrationView
from django.urls import include, path

from django.contrib.auth import views as auth_views

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'drivers', views.DriverViewSet)
router.register(r'customers', views.CustomerViewSet)

urlpatterns = \
    [
        path('', views.index, name='index'),
        path('overview/', views.overview),
        path('overviewAPI/', views.overview_api),
        path('homes/', views.HomeList.as_view()),
        path('homes/<int:pk>/', views.HomeDetail.as_view()),
        path('customers/<int:pk>/', views.CustomerDetail.as_view()),
        path('admin/', admin.site.urls),
        path('accounts/register/',
             RegistrationView.as_view(success_url='/accounts/profile/'),
             name='django_registration_register'),
        path('accounts/', include('django_registration.backends.one_step.urls')),
        path('accounts/', include('django.contrib.auth.urls')),
        path('accounts/profile/', views.user_profile),
        path('api-auth/', include('rest_framework.urls')),
        url(r'^', include(router.urls)),
    ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# urlpatterns = format_suffix_patterns(urlpatterns)
