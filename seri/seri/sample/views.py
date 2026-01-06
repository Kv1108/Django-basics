from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Book
from .serializers import BookSerializer

class BookListCreateAPIView(APIView):

    def get(self, request):
        book = Book.objects.all()
        serializer = BookSerializer(book, many = True)
        return Response(serializer.data, status = status.HTTP_200_OK)
    
    def post(self, request):
        serializer = BookSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.error, status = status.HTTP_400_BAD_REQUEST)
    
class BookDetailAPIView(APIView):

    def get_object(self, id):
        try:
            return Book.objects.get(id=id)
        except:
            return None
        
    def get(self, request, id):
        book = self.get_object(id)
        if not book:
            return Response({"error":"Book not found"}, status=404)
        
        serializer = BookSerializer(book)
        return Response(serializer.data)
    
    def put(self, request,id):
        book = self.get_object(id)
        if not book:
            return Response({"error": "Book not found"}, status=404)
        
        serializer = BookSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors, status=400)

    def delete(self, request, id):
        book = self.get_object(id)
        if not book:
            return Response({"error": "Book not found"}, status=404)

        book.delete()
        return Response(status=204)    