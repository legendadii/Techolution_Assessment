from django.db import models

# Create your models here.
from django.db import models

class LibraryUser(models.Model):
    name = models.CharField(max_length=200)
    user_id = models.CharField(max_length=50, unique=True)
    email = models.EmailField()

    def __str__(self):
        return self.name

class CheckoutLog(models.Model):
    book = models.ForeignKey('books.Book', on_delete=models.CASCADE)
    user = models.ForeignKey(LibraryUser, on_delete=models.CASCADE)
    checkout_date = models.DateTimeField(auto_now_add=True)
    checkin_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f'{self.book} checked out by {self.user}'
