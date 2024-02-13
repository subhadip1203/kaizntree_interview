from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination
from .models import Category, Item
from .serializers import CategorySerializer, ItemSerializer


class ItemPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100
    
    
class CategoryListCreateView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    
    def get_queryset(self):
        # Filter the queryset based on the authenticated user
        return Category.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        # Associate the user with the category before saving
        serializer.save(user=self.request.user)

class ItemListCreateView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    pagination_class = ItemPagination 
    
    def get_queryset(self):
        # Filter the queryset based on the authenticated user
        queryset = Item.objects.filter(user=self.request.user)
    
        # Check if 'tag' parameter is present in the request
        tag_param = self.request.query_params.get('tag', None)
        if tag_param:
            # Filter items based on the provided tag
            queryset = queryset.filter(tags__icontains=tag_param)
            
        return queryset

    def perform_create(self, serializer):
        # Associate the user with the Item before saving
        serializer.save(user=self.request.user)