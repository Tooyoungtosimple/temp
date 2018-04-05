from django.forms import ModelForm
from Book.models import Book,Indent

class BookForm(ModelForm):
    class Meta:
        model=Book
        fields="__all__"
