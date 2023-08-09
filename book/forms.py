from django import forms
from book.models import BookStoreModel


class BookStoreForm(forms.ModelForm):
    class Meta:
        model = BookStoreModel
        fields = ["book_name", "author", "category"]
        widgets = {
            "book_name": forms.TextInput(
                attrs={
                    "class": "bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:border-2 focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5"
                }
            ),
            "author": forms.TextInput(
                attrs={
                    "class": "bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:border-2 focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5"
                }
            ),
            "category": forms.Select(
                attrs={
                    "class": "bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:border-2 focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 hover:bg-sky-200"
                }
            ),
        }
