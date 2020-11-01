from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path("login/", views.login, name='login'),
    path("admin_login/", views.admin, name='admin'),
    path("logout/", views.logout, name='logout'),
    path("registration/", views.register, name="register"),
    path("home/", views.home, name='home'),
    path("member_home/", views.member_home, name='member_home'),
    path("add_book/", views.add_book, name='add_book'),
    path("view_book/", views.view_book, name='view_book'),
    path("delete_book/", views.delete_book, name='delete_book'),
    path("issue_book/", views.issue_book, name='issue_book'),
    path("return_book/", views.return_book, name='return_book'),
    path("author/", views.add_author, name='add_author'),

]
