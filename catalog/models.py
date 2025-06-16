import uuid
from django.conf import settings
from django.db import models

class Genre(models.Model):
    GENRE_CHOICES = (
        ("R", "ROMANCE"),
        ("C", "COMEDY"),
        ("P", "POLITICS"),
        ("F", "FINANCE"),
    )
    name = models.CharField(max_length=1, choices = GENRE_CHOICES, default = "R")

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

class Book(models.Model):
    title = models.CharField(max_length=255)
    # author = ""
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
    status = models.CharField(max_length=1, choices = LOAN_STATUS, default="A")
    return_date =models.DateTimeField(blank= False, null=False)
    comments = models.TextField(blank= True, null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)




