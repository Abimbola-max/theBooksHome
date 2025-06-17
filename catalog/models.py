import uuid
from django.conf import settings
from django.db import models
from user.models import Author

class Genre(models.Model):
    GENRE_CHOICES = (
        ("R", "ROMANCE"),
        ("C", "COMEDY"),
        ("P", "POLITICS"),
        ("F", "FINANCE"),
    )
    name = models.CharField(max_length=1, choices = GENRE_CHOICES, default = "R", unique=True)

    def __str__(self):
        return self.name

class Language(models.Model):
    LANGUAGE_CHOICES = (
    ("Y", "YORUBA"),
    ("I", "IGBO"),
    ("R" ,"RUSSIAN"),
    ("H", "HAUSA"),
    ("F", "FRENCH")
    )
    name = models.CharField(max_length=1, choices = LANGUAGE_CHOICES, default = "H")

    def __str__(self):
        return self.name

# class Author(settings.AUTH_USER_MODEL):
#     dob = models.DateField(blank=False, null=False)
#     dod = models.DateField(blank=True, null=True)

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.ManyToManyField(Author, related_name="books")
    summary = models.TextField()
    isbn = models.CharField(max_length=13, unique=True)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class BookInstance(models.Model):
    LOAN_STATUS = (
    ("A", "AVAILABLE"),
    ("B", "BORROWED"),
    ("M", "MAINTENANCE"),
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    status = models.CharField(max_length=1, choices = LOAN_STATUS, default="A", unique=True)
    return_date =models.DateTimeField(blank= False, null=False)
    comments = models.TextField(blank= True, null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.id




