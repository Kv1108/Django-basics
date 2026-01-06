from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookListCreateAPIView, BookDetailAPIView

#router = DefaultRouter()
#router.register('books', BookViewSet, basename='book')

urlpatterns = [
    #path('', include(router.urls)),
    path('manual/books/', BookListCreateAPIView.as_view()),
    path('manual/books/<int:id>/', BookDetailAPIView.as_view()),
]
