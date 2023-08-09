from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from book.forms import BookStoreForm
from book.models import BookStoreModel
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import FormView, CreateView, DeleteView, UpdateView


class HomeView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        print(kwargs)
        # return {"name": "HomeView", "roll": kwargs.get("roll")}
        context = super().get_context_data(**kwargs)
        context = {"name": "HomeView", "age": 20}
        context.update(kwargs)
        return context


"""
def home(req):
    return render(req, "home.html")
"""


class BookFormView(CreateView):
    model = BookStoreModel
    template_name = "store_book.html"
    form_class = BookStoreForm
    success_url = reverse_lazy("show_books")


"""
def store_book(req):
    if req.method == "POST":
        form = BookStoreForm(req.POST)
        if form.is_valid():
            form.save()
            return redirect("show_books")
    else:
        form = BookStoreForm()

    return render(req, "store_book.html", {"form": form})
"""


class BookListView(ListView):
    model = BookStoreModel
    template_name = "show_books.html"
    context_object_name = "result"
    ordering = ["book_name"]

    # def get_queryset(self):
    #     return BookStoreModel.objects.filter(book_name__startswith="h")


"""
def show_books(req):
    query_set = BookStoreModel.objects.all()
    return render(req, "show_books.html", {"result": query_set})
"""


class BookDetailView(DetailView):
    model = BookStoreModel
    template_name = "book_detail.html"
    context_object_name = "item"
    pk_url_kwarg = "pk"


class BookUpdateView(UpdateView):
    model = BookStoreModel
    template_name = "store_book.html"
    form_class = BookStoreForm
    success_url = reverse_lazy("show_books")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["sec_title"] = "Edit Book"
        return context


"""
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

    return render(req, "store_book.html", {"sec_title": "Edit Book", "form": form})
"""


class BookDeleteView(DeleteView):
    model = BookStoreModel
    template_name = "book_confirm_delete.html"
    success_url = reverse_lazy("show_books")


"""
def delete_book(req, pk):
    BookStoreModel.objects.get(pk=pk).delete()
    return redirect("show_books")
"""
