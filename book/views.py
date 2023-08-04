from django.shortcuts import render, redirect
from book.forms import BookStoreForm
from book.models import BookStoreModel


# Create your views here.
def home(req):
    return render(req, "home.html")


def store_book(req):
    if req.method == "POST":
        form = BookStoreForm(req.POST)
        if form.is_valid():
            form.save()
            return redirect("show_books")
    else:
        form = BookStoreForm()

    return render(req, "store_book.html", {"form": form})


def show_books(req):
    query_set = BookStoreModel.objects.all()
    return render(req, "show_books.html", {"result": query_set})


def edit_book(req, id):
    book_model = BookStoreModel.objects.get(pk=id)
    form = BookStoreForm(instance=book_model)
    if req.method == "POST":
        form = BookStoreForm(req.POST, instance=book_model)
        if form.is_valid():
            form.save()
            return redirect("show_books")
    else:
        form = BookStoreForm(instance=book_model)

    return render(req, "store_book.html", {"form": form, "sec_title": "Edit Book"})


def delete_book(req, id):
    BookStoreModel.objects.get(pk=id).delete()
    return redirect("show_books")
