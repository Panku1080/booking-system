from rest_framework import routers
from .views import AvailabilityViewSet, BookingViewSet

router = routers.DefaultRouter()
router.register(r'availabilities', AvailabilityViewSet)
router.register(r'bookings', BookingViewSet)

urlpatterns = router.urls
