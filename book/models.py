from django.db import models


# Create your models here.
class BookStoreModel(models.Model):
    CATEGORY_CHOICES = (
        ("Mystery", "Mystery"),
        ("Thriller", "Thriller"),
        ("Sci-Fi", "Sci-Fi"),
        ("Humor", "Humor"),
        ("Fantasy", "Fantasy"),
        ("Horror", "Horror"),
        ("Romance", "Romance"),
        ("Westerns", "Westerns"),
        ("Biographies", "Biographies"),
        ("History", "History"),
        ("Cookbooks", "Cookbooks"),
        ("Poetry", "Poetry"),
        ("True Crime", "True Crime"),
        ("Drama", "Drama"),
        ("Action", "Action"),
        ("Adventure", "Adventure"),
        ("Satire", "Satire"),
        ("Anthology", "Anthology"),
    )
    id = models.IntegerField(primary_key=True)
    book_name = models.CharField(max_length=100, default="Unknown book")
    author = models.CharField(max_length=25, default="Unknown")
    category = models.CharField(max_length=25, choices=CATEGORY_CHOICES)
    first_published = models.DateTimeField(auto_now_add=True, null=True)
    last_published = models.DateTimeField(auto_now=True, null=True)

    def __str__(self) -> str:
        return f"{self.book_name} by {self.author}"
