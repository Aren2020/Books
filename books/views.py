from typing import Any
from django.views.generic import ListView, TemplateView
from .models import Book, Review

class BookListView(ListView):
    model = Book
    context_object_name = 'book_list'
    template_name = 'books/book_list.html'


class BookDetailView(TemplateView):
    template_name = 'books/book_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        book = Book.objects.get(**kwargs)
        context['book'] = book
        context['reviews'] = book.reviews.select_related('author')
        return context
    