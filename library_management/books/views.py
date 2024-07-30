# from django.shortcuts import render,HttpResponse

# # Create your views here.
# from django.shortcuts import render, get_object_or_404, redirect
# from .models import Book
# from .forms import BookForm
# from django.contrib import messages

# def book_list(request):
#     books = Book.objects.all()
#     return render(request, 'books/book_list.html', {'books': books})
#     # return HttpResponse("sumbitted succesfully ")

# def book_detail(request, pk):
#   try:
#     book = get_object_or_404(Book, pk=pk)
#     return render(request, 'books/book_detail.html', {'book': book})
#     # return HttpResponse("sumbitted succesfully ")
#   except:
#     return HttpResponse("user not found")

# def book_detail_by_isbn(request, isbn):
#   try:
#     book = get_object_or_404(Book, isbn=isbn)
#     return render(request, 'books/book_detail.html', {'book': book})
#     # return HttpResponse("sumbitted succesfully ")
#   except:
#     return HttpResponse("user not found")

# def book_create(request):
#     if request.method == 'POST':
#         form = BookForm(request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Book added successfully.')
#             return redirect('book_list')
#     else:
#         form = BookForm()
#     return render(request, 'books/book_form.html', {'form': form})

# def book_update(request, pk):
#   try:
#     book = get_object_or_404(Book, pk=pk)
#     if request.method == 'POST':
#         form = BookForm(request.POST, instance=book)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Book updated successfully.')
#             return redirect('book_list')
#     else:
#         form = BookForm(instance=book)
#     return render(request, 'books/book_form.html', {'form': form})
#   except:
#     return HttpResponse("user not found")

# def book_delete(request, pk):
#   try:
#     book = get_object_or_404(Book, pk=pk)
#     if request.method == 'POST':
#         book.delete()
#         messages.success(request, 'Book deleted successfully.')
#         return redirect('book_list')
#     return render(request, 'books/book_confirm_delete.html', {'book': book})
#   except:
#     return HttpResponse("user not found")






# ***********************************by class *********************************************
from django.shortcuts import render, get_object_or_404, redirect,HttpResponse
from django.contrib import messages
from .models import Book
from .forms import BookForm
from .services import BookService

def book_list(request):
 try:
    books = BookService.get_all_books()
    return render(request, 'books/book_list.html', {'books': books})
 except :
    return HttpResponse("no book found")

def book_detail(request, pk):
 try:
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'books/book_detail.html', {'book': book})
 except :
    return HttpResponse("no bbok found")
 

def book_create(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            BookService.create_book(form.cleaned_data)
            messages.success(request, 'Book added successfully.')
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'books/book_form.html', {'form': form})

def book_update(request, pk):
 try:
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            BookService.update_book(book.pk, form.cleaned_data)
            messages.success(request, 'Book updated successfully.')
            return redirect('book_list')
    else:
        form = BookForm(instance=book)
    return render(request, 'books/book_form.html', {'form': form})
 except:
    return HttpResponse("no book found")

def book_delete(request, pk):
 try:
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        BookService.delete_book(book.pk)
        messages.success(request, 'Book deleted successfully.')
        return redirect('book_list')
    return render(request, 'books/book_confirm_delete.html', {'book': book})
 except:
    return HttpResponse("no book found")

def book_detail_by_isbn(request):
 try:
    isbn = request.GET.get('isbn')
    if isbn:
        try:
            book = BookService.get_book_by_isbn(isbn)
            return render(request, 'books/book_detail.html', {'book': book})
        except Book.DoesNotExist:
            messages.error(request, 'Book with the given ISBN not found.')
            return redirect('book_list')
    else:
        messages.error(request, 'No ISBN provided.')
        return redirect('book_list')
 except:
    return HttpResponse("no not found")




#      storage.py 
# from django.shortcuts import render, get_object_or_404, redirect
# from django.contrib import messages
# from .models import Book
# from .forms import BookForm
# from .storage import BookStorage  # Ensure this is imported correctly
# from django.utils import timezone
# from django.http import JsonResponse
# from django.http import HttpResponseBadRequest, JsonResponse
# import json

# def book_list(request):
#     if request.is_ajax():  # Ensure the request is AJAX
#         books = Book.objects.all()
#         books_list = list(books.values())
#         return JsonResponse(books_list, safe=False)
#     else:
#         books = Book.objects.all()
#         return render(request, 'books/book_list.html', {'books': books})

# # def book_list(request):
# #     book_storage = BookStorage('books.json')
# #     books = book_storage.get_entries()
# #     return render(request, 'books/book_list.html', {'books': books})

# def book_detail(request, pk):
#     book_storage = BookStorage('books.json')
#     books = book_storage.get_entries()
#     book = next((b for b in books if b['id'] == pk), None)
#     print(book.isbn)
#     return render(request, 'books/book_detail.html', {'book': book})

# def book_detail_by_isbn(request, isbn):
#     book_storage = BookStorage('books.json')
#     books = book_storage.get_entries()
#     book = next((b for b in books if b['isbn'] == isbn), None)
#     return render(request, 'books/book_detail.html', {'book': book})


# def book_create(request):
#     if request.method == 'POST':
#         try:
#             data = json.loads(request.body)
#             form = BookForm(data)
#             if form.is_valid():
#                 form.save()
#                 messages.success(request, 'Book added successfully.')
#                 return JsonResponse({'success': True})
#             else:
#                 return JsonResponse({'success': False, 'errors': form.errors})
#         except json.JSONDecodeError:
#             return HttpResponseBadRequest('Invalid JSON')
#     else:
#         form = BookForm()
#     return render(request, 'books/book_form.html', {'form': form})

# # def book_create(request):
# #     if request.method == 'POST':
# #         form = BookForm(request.POST)
# #         if form.is_valid():
# #             book = form.cleaned_data
# #             book_storage = BookStorage('books.json')
# #             book_storage.add_entry(book)
# #             messages.success(request, 'Book added successfully.')
# #             return redirect('book_list')
# #     else:
# #         form = BookForm()
# #     return render(request, 'books/book_form.html', {'form': form})

# def book_update(request, pk):
#     book_storage = BookStorage('books.json')
#     books = book_storage.get_entries()
#     book = next((b for b in books if b['id'] == pk), None)
#     if request.method == 'POST':
#         form = BookForm(request.POST, instance=book)
#         if form.is_valid():
#             updated_book = form.cleaned_data
#             for b in books:
#                 if b['id'] == pk:
#                     b.update(updated_book)
#             book_storage.save_data(books)
#             messages.success(request, 'Book updated successfully.')
#             return redirect('book_list')
#     else:
#         form = BookForm(initial=book)
#     return render(request, 'books/book_form.html', {'form': form})

# def book_delete(request, pk):
#     book_storage = BookStorage('books.json')
#     books = book_storage.get_entries()
#     book = next((b for b in books if b['id'] == pk), None)
#     if request.method == 'POST':
#         books = [b for b in books if b['id'] != pk]
#         book_storage.save_data(books)
#         messages.success(request, 'Book deleted successfully.')
#         return redirect('book_list')
#     return render(request, 'books/book_confirm_delete.html', {'book': book})
