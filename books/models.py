from django.db import models
from datetime import date


# Create your models here.
class member(models.Model):
    mid = models.AutoField(primary_key=True)
    mname = models.CharField(max_length=20)
    dept = models.CharField(max_length=10)
    member_type = models.CharField(max_length=10)
    joining_date = models.DateField(default=date.today)
    no_of_issued_books = models.IntegerField(default=0)
    password = models.CharField(max_length=20, default="")

    def __str__(self):
        return str(self.mid)


class book_info(models.Model):
    title = models.CharField(max_length=50, primary_key=True)
    publisher = models.CharField(max_length=50)
    price = models.IntegerField()
    no_of_copies = models.IntegerField()
    available_copies = models.IntegerField()

    def __str__(self):
        return self.title


class author(models.Model):
    aid = models.AutoField(primary_key=True)
    aname = models.CharField(max_length=50)
    amail = models.EmailField()

    def __str__(self):
        return str(self.aid)


class books(models.Model):
    bid = models.AutoField(primary_key=True)
    title = models.ForeignKey(book_info, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, default='available')

    def __str__(self):
        return str(self.bid)


class book_author(models.Model):
    title = models.OneToOneField(book_info, on_delete=models.CASCADE, primary_key=True)
    aid = models.ForeignKey(author, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.title)


class borrower(models.Model):
    bid = models.OneToOneField(books, on_delete=models.CASCADE, primary_key=True)
    mid = models.ForeignKey(member, on_delete=models.CASCADE)
    issue_date = models.DateField(default=date.today)
    return_date = models.DateField(null=True, default=None)
    book_due = models.IntegerField(default=0)

    def __str__(self):
        return str(self.mid)
