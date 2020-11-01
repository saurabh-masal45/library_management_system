from django.shortcuts import render
from django.http import HttpResponse
from .models import member, book_info, book_author, borrower, author, books
from django.utils import timezone
from datetime import date

# Create your views here.
book_id = 100


def index(request):
    return render(request, 'books/index.html')


def login(request):
    if request.method == "GET":
        return render(request, 'books/login.html')

    if request.method == "POST":
        mid = request.POST.get('mid')
        password = request.POST.get('password')
        m = member.objects.get(mid=mid, password=password)
        print(m.mname)

        try:
            b = borrower.objects.filter(mid = mid, return_date = None).order_by('bid')
            lst = []
            for i in range(b.count()):
                lst.append(b[i].bid)
            param = {'name': m.mname, 'mid': m.mid, 'num': m.no_of_issued_books, 'book': lst}
        except Exception as e:
            param = {'name': m.mname, 'mid': m.mid, 'num': m.no_of_issued_books}
        return render(request, 'books/member_home.html', param)


def admin(request):
    return render(request, 'books/admin_login.html')


def logout(request):
    return render(request, 'books/logout.html')


def register(request):
    return render(request, 'books/register.html')


def home(request):
    if request.method == "POST":
        password = request.POST.get('admin_password', '')
        if password == "admin":
            return render(request, 'books/home.html')
        else:
            return HttpResponse("Wrong Password")
    return render(request, 'books/home.html')


def member_home(request):
    if request.method == "POST":
        mname = request.POST.get('username', '')
        dept = request.POST.get('dept', '')
        member_type = request.POST.get('role', '')
        password = request.POST.get('password', '')
        reg = member(mname=mname, dept=dept, member_type=member_type, joining_date=timezone.now(), password=password)
        reg.save()
        mid = reg.mid
        param = {'name': reg.mname, 'mid': mid, 'num': reg.no_of_issued_books}
    return render(request, 'books/member_home.html', param)


def add_book(request):
    if request.method == "POST":
        title = request.POST.get('title')
        publisher = request.POST.get('publisher', '')
        price = request.POST.get('price', 0)
        no_of_copies = request.POST.get('no_of_copies', 0)
        auth = request.POST.get('author')
        add = book_info(title=title, publisher=publisher, price=price, no_of_copies=no_of_copies,
                        available_copies=no_of_copies)
        add.save()
        a = author.objects.get(aname=auth)

        bk_author = book_author(title=add, aid=a)
        bk_author.save()
        b_title = book_info.objects.get(title=title)
        cnt = book_info.objects.all().count()
        print(cnt)
        for i in range(int(no_of_copies)):
            #global book_id
            #book_id = 1
            add_b = books(title=b_title)
            add_b.save()
    return render(request, 'books/add_book.html')


def delete_book(request):
    if request.method == "POST":
        title = request.POST.get('title')
        publisher = request.POST.get('publisher')
        try:
            a = book_info.objects.get(title=title, publisher=publisher)
            a.delete()
        except Exception as e:
            return HttpResponse("<h3 style='text-align: center; color: red;'>Book not found</h3>")
    return render(request, 'books/delete_book.html')


def issue_book(request):
    if request.method == "POST":
        mid = request.POST.get('mid')
        title = request.POST.get('title')
        try:
            a = member.objects.get(mid=mid)
            num = a.no_of_issued_books
            print(num)
            if num <= 3:
                try:
                    b = book_info.objects.get(title=title)
                    avail = b.available_copies
                    if avail > 0:
                        a.no_of_issued_books = num + 1
                        b.available_copies = avail - 1
                        i = books.objects.filter(title=title, status='available').order_by('bid')[0]
                        i.status = 'issued'
                        a.save()
                        b.save()
                        i.save()
                        mem = member.objects.get(mid=mid)
                        book = books.objects.get(bid=i.bid)
                        borrow = borrower(bid=book, mid=mem)
                        borrow.save()

                except Exception as e:
                    return HttpResponse(
                        "<h3 style='color: red;width: 22%;margin-top: 200px;margin-left: 550px;'>Wrong Title!!</h3>")
        except Exception as e:
            return HttpResponse(
                "<h3 style='color: red;width: 22%;margin-top: 200px;margin-left: 550px;'>Member does not exist!!</h3>")

    return render(request, 'books/issue_book.html')


def return_book(request):
    if request.method == "GET":
        return render(request, 'books/return_book.html')
    if request.method == "POST":
        mid = request.POST.get('mid')
        bid = request.POST.get('bid')
        try:
            borrow = borrower.objects.get(mid=mid,bid=bid)
            a = member.objects.get(mid=mid)
            book = books.objects.get(bid=bid)
            borrow.return_date = date.today()
            print(borrow.return_date)
            diff = borrow.return_date - borrow.issue_date
            print(diff.days)
            if diff.days > 7:
                borrow.due = diff
            a.no_of_issued_books -= 1
            b = book_info.objects.get(title=book.title)
            b.available_copies += 1
            b.status = 'available'
            a.save()
            b.save()
            borrow.save()
        except Exception as e:
            return HttpResponse("<h3>This book is not issued by you!!</h3>")
        return render(request, 'books/return_book.html')


def view_book(request):
    book = book_info.objects.all()

    return render(request, 'books/view_book.html', {'books': book})


def add_author(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        a = author(aname=name, amail=email)
        a.save()
    return render(request, 'books/author.html')
