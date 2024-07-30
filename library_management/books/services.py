from .models import Book
from .forms import BookForm

class BookService:
    @staticmethod
    def get_all_books():
        return Book.objects.all()

    @staticmethod
    def get_book_by_id(book_id):
        return Book.objects.get(pk=book_id)

    @staticmethod
    def get_book_by_isbn(isbn):
        return Book.objects.get(isbn=isbn)

    @staticmethod
    def create_book(data):
        form = BookForm(data)
        if form.is_valid():
            return form.save(), None
        return None, form.errors

    @staticmethod
    def update_book(book_id, data):
        book = Book.objects.get(pk=book_id)
        form = BookForm(data, instance=book)
        if form.is_valid():
            return form.save(), None
        return None, form.errors

    @staticmethod
    def delete_book(book_id):
        book = Book.objects.get(pk=book_id)
        book.delete()
