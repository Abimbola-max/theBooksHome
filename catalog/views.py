from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.generics import RetrieveUpdateDestroyAPIView, CreateAPIView, ListCreateAPIView, get_object_or_404
from rest_framework.permissions import IsAuthenticated

from .models import Book, Author, BookImage, BookInstance
from .serializers import BookSerializer, AuthorSerializer, AddBookSerializer, BookImageSerializer, \
    BookInstanceSerializer
from rest_framework.response import Response
from rest_framework import status, viewsets


# Create your views here.
# @api_view()
# def get_books(request):
#     books = Book.objects.all()
#     serializer = BookSerializer(books, many=True)
#     return Response(serializer.data, status=status.HTTP_200_OK)
#
# @api_view(["POST"])
# def add_author(request):
#     author = AuthorSerializer(data=request.data)
#     author.is_valid(raise_exception=True)
#     author.save()
#     return Response(author.data, status=status.HTTP_201_CREATED)
#
# @api_view()
# def get_authors(request):
#     authors = Author.objects.all()
#     serializer = AuthorSerializer(authors, many=True)
#     return Response(serializer.data, status=status.HTTP_200_OK)
#
# @api_view(['PUT', 'PATCH'])
# def update_author(request, pk):
#     author = Author.objects.get(pk=pk)
#     serializer = AuthorSerializer(author, data=request.data)
#     serializer.is_valid(raise_exception=True)
#     serializer.save()
#     return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def image_detail(request, pk):
    book_image =  get_object_or_404(BookImage, pk=pk)
    serializer = BookSerializer(book_image)
    return Response(serializer.data, status=status.HTTP_200_OK)

class AddAuthorView(ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class GetUpdateDeleteAuthorView(RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return AddBookSerializer
        elif self.request.method== "PUT":
            return AddBookSerializer
        return BookSerializer

class BookImageViewSet(viewsets.ModelViewSet):
    queryset = BookImage.objects.all()
    serializer_class = BookImageSerializer
    # permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        book_id = self.kwargs.get("book_pk")
        if not book_id:
            raise ValueError("book_id missing in kwargs")
        serializer.save(book_id=book_id)

# def delete_author(request, pk):
@permission_classes([IsAuthenticated])
@api_view(['POST'])
def borrow_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    user = request.user
    data = BookInstanceSerializer(data=request.data)
    data.is_valid(raise_exception=True)
    book_instance = BookInstance()
    book_instance.user = user
    book_instance.book = book
    book_instance.return_date = data.validated_data['return_date']
    book_instance.comments = data.validated_data['comments']
    book_instance.save()
    return Response({"message": f"{book} borrowed successfully"}, status=status.HTTP_200_OK)


    # return {"book_id": self.kwargs["book_pk"]}
#     author = Author.objects.get(pk=pk)
#     author.delete()
#     return Response(status=status.HTTP_200_OK)
# def greet(request, name):
#     return render(request, "index.html", {'name': name})
