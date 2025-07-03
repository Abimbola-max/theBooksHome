from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.generics import RetrieveUpdateDestroyAPIView, CreateAPIView, ListCreateAPIView

from .models import Book, Author
from .serializers import BookSerializer, AuthorSerializer
from rest_framework.response import Response
from rest_framework import status
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


class AddAuthorView(ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class GetUpdateDeleteAuthorView(RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

# def delete_author(request, pk):
#     author = Author.objects.get(pk=pk)
#     author.delete()
#     return Response(status=status.HTTP_200_OK)
# def greet(request, name):
#     return render(request, "index.html", {'name': name})
