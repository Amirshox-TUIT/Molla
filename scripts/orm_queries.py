from apps.pages.models import *


def task1_get_all_books():
    """Return all Book objects"""
    books = Book.objects.all()
    print(books)


def task2_get_available_books():
    """Return all available books (is_available=True)"""
    books = Book.objects.filter(is_available=True)
    print(books)

def task3_get_books_published_after(year):
    """Return books published after the given year"""
    books = Book.objects.filter(publish_date__gt=year)
    print(books)


def task4_get_books_by_author(author_name):
    """Return books by the specified author"""
    books = Book.objects.filter(books=author_name)
    print(books)


def task5_get_books_in_price_range(min_price, max_price):
    """Return books within the specified price range"""
    books = Book.objects.filter(price__gte=min_price, price__lte=max_price)
    print(books)
