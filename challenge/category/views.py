from rest_framework.viewsets import ModelViewSet

from challenge.category.models import Category
from challenge.category.serializers import CategorySerializer


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.order_by('name').all()
    serializer_class = CategorySerializer
