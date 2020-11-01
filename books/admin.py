from django.contrib import admin

# Register your models here.
from .models import member, book_info, author, book_author, borrower, books

admin.site.register(member)
admin.site.register(book_info)
admin.site.register(author)
admin.site.register(book_author)
admin.site.register(borrower)
admin.site.register(books)
