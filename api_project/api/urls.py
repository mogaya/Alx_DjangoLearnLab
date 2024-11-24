from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookList, BookViewSet
from rest_framework.authtoken.views import obtain_auth_token

# Step 2: Set Up a Router
# Routers in DRF automatically determine the URL conf based on your ViewSet.

# Configure the Router:
# In api/urls.py, import DefaultRouter from rest_framework.routers and register your BookViewSet.
# Register the BookViewSet with the router as follows:
# router.register(r'books_all', BookViewSet, basename='book_all')

# Initializing the router
router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')

urlpatterns = [
    # Route for the BookList view (ListAPIView)
    path('books/', BookList.as_view(), name='book-list'),

    # Include the router URLs for BookViewSet (all CRUD operations)
    path('', include(router.urls)),

    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
]