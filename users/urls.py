from rest_framework import routers

from .views import AuthViewSet, UserViewSet

router = routers.DefaultRouter(trailing_slash=False)
# router.register('auth', AuthViewSet, basename='auth')
router.register(r'user', UserViewSet, basename='user')


urlpatterns = router.urls
