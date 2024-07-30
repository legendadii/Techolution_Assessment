from django.shortcuts import render,HttpResponse

# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from .models import LibraryUser, CheckoutLog
from .forms import LibraryUserForm
from django.contrib import messages
from books.models import Book

def user_list(request):
    users = LibraryUser.objects.all()
    return render(request, 'users/user_list.html', {'users': users})
    # return HttpResponse("sumbitted succesfully")


def user_detail(request, pk):
    try:
       user = get_object_or_404(LibraryUser, pk=pk)
       print(user)
       return render(request, 'users/user_detail.html', {'user': user})
    except :
        return HttpResponse("user not found")
    # return HttpResponse("sumbitted succesfully 2")

def user_create(request):
    if request.method == 'POST':
        form = LibraryUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'User added successfully.')
            return redirect('user_list')
    else:
        form = LibraryUserForm()
    return render(request, 'users/user_form.html', {'form': form})

def user_update(request, pk):
  try:
    user = get_object_or_404(LibraryUser, pk=pk)
    if request.method == 'POST':
        form = LibraryUserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, 'User updated successfully.')
            return redirect('user_list')
    else:
        form = LibraryUserForm(instance=user)
    return render(request, 'users/user_form.html', {'form': form})

  except:
    return HttpResponse("user not found")

def user_delete(request, pk):
  try:
    user = get_object_or_404(LibraryUser, pk=pk)
    if request.method == 'POST':
        user.delete()
        messages.success(request, 'User deleted successfully.')
        return redirect('user_list')
    return render(request, 'users/user_confirm_delete.html', {'user': user})
  except :
    return HttpResponse("user not found")

def checkout_book(request, user_id, book_id):
    user = get_object_or_404(LibraryUser, pk=user_id)
    book = get_object_or_404(Book, pk=book_id)

    if book.available:
        CheckoutLog.objects.create(user=user, book=book)
        book.available = False
        book.save()
        messages.success(request, 'Book checked out successfully.')
        
    else:
        messages.error(request, 'Book is not available for checkout.')
        # return HttpResponse('Book is not available for checkout.')
    
    return redirect('book_detail', pk=book_id)

def checkin_book(request, log_id):
    log = get_object_or_404(CheckoutLog, pk=log_id)
    log.checkin_date = timezone.now()
    log.book.available = True
    log.book.save()
    log.save()
    messages.success(request, 'Book checked in successfully.')
    
    return redirect('book_detail', pk=log.book.pk)


# from django.shortcuts import render, get_object_or_404, redirect
# from django.contrib import messages
# from .models import LibraryUser, CheckoutLog
# from .forms import LibraryUserForm
# from .storage import UserStorage  # Import UserStorage
# from books.models import Book
# from django.utils import timezone

# def user_list(request):
#     user_storage = UserStorage('users.json')
#     users = user_storage.get_entries()
#     return render(request, 'users/user_list.html', {'users': users})

# def user_detail(request, pk):
#     user_storage = UserStorage('users.json')
#     users = user_storage.get_entries()
#     user = next((u for u in users if u['id'] == pk), None)
#     return render(request, 'users/user_detail.html', {'user': user})

# def user_create(request):
#     if request.method == 'POST':
#         form = LibraryUserForm(request.POST)
#         if form.is_valid():
#             user = form.cleaned_data
#             user_storage = UserStorage('users.json')
#             user_storage.add_entry(user)
#             messages.success(request, 'User added successfully.')
#             return redirect('user_list')
#     else:
#         form = LibraryUserForm()
#     return render(request, 'users/user_form.html', {'form': form})

# def user_update(request, pk):
#     user_storage = UserStorage('users.json')
#     users = user_storage.get_entries()
#     user = next((u for u in users if u['id'] == pk), None)
#     if request.method == 'POST':
#         form = LibraryUserForm(request.POST, instance=user)
#         if form.is_valid():
#             updated_user = form.cleaned_data
#             for u in users:
#                 if u['id'] == pk:
#                     u.update(updated_user)
#             user_storage.save_data(users)
#             messages.success(request, 'User updated successfully.')
#             return redirect('user_list')
#     else:
#         form = LibraryUserForm(initial=user)
#     return render(request, 'users/user_form.html', {'form': form})

# def user_delete(request, pk):
#     user_storage = UserStorage('users.json')
#     users = user_storage.get_entries()
#     user = next((u for u in users if u['id'] == pk), None)
#     if request.method == 'POST':
#         users = [u for u in users if u['id'] != pk]
#         user_storage.save_data(users)
#         messages.success(request, 'User deleted successfully.')
#         return redirect('user_list')
#     return render(request, 'users/user_confirm_delete.html', {'user': user})

# def checkout_book(request, user_id, book_id):
#     user = get_object_or_404(LibraryUser, pk=user_id)
#     book = get_object_or_404(Book, pk=book_id)

#     if book.available:
#         CheckoutLog.objects.create(user=user, book=book)
#         book.available = False
#         book.save()
#         messages.success(request, 'Book checked out successfully.')
#     else:
#         messages.error(request, 'Book is not available for checkout.')
    
#     return redirect('book_detail', pk=book_id)

# def checkin_book(request, log_id):
#     log = get_object_or_404(CheckoutLog, pk=log_id)
#     log.checkin_date = timezone.now()
#     log.book.available = True
#     log.book.save()
#     log.save()
#     messages.success(request, 'Book checked in successfully.')
    
#     return redirect('book_detail', pk=log.book.pk)
