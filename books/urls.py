from django.urls import path
from django.views.decorators.cache import cache_page
from .views import BookListView, BookDetailView, SearchResultsListView

urlpatterns = [
    path('', cache_page(60 * 15)(BookListView.as_view()), name = 'book_list'),
    path('<uuid:pk>/', cache_page(60 * 15)(BookDetailView.as_view()), name = 'book_detail'),
    path('search/', cache_page(60 * 15)(SearchResultsListView.as_view()), name = 'search_results'),
]