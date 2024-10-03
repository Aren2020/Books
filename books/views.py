
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import ListView, TemplateView
from django.shortcuts import get_object_or_404
from django.db.models import Q 
from .models import Book

class BookListView(LoginRequiredMixin, ListView):
    model = Book
    context_object_name = 'book_list'
    template_name = 'books/book_list.html'


class BookDetailView(LoginRequiredMixin,
                     PermissionRequiredMixin,
                     TemplateView):
    template_name = 'books/book_detail.html'
    permission_required = 'books.special_status'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        book = get_object_or_404(Book, **kwargs)
        context['book'] = book
        context['reviews'] = book.reviews.select_related('author')
        return context
    
class SearchResultsListView(ListView):
    model = Book
    context_object_name = 'book_list'
    template_name = 'books/search_results.html'
    
    def get_queryset(self):
        query = self.request.GET.get('q')
        return Book.objects.filter(
            Q(title__icontains=query) | Q(author__icontains=query)
        )   
