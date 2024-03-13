from django.contrib import admin
from django.urls import path, include

from api.views import HomeView
from users.views import GetAuthMeViewSet

urlpatterns = [
    path('', include('drfpasswordless.urls')),
    path('', HomeView.as_view()),
    path('auth/me/', GetAuthMeViewSet.as_view()),
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
]
