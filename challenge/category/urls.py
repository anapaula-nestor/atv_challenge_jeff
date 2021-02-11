from rest_framework.routers import SimpleRouter

from challenge.category.views import CategoryViewSet

router = SimpleRouter()
router.register(r'categories', CategoryViewSet, basename='categories')

urlpatterns = router.urls
