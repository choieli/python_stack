from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string
from time import gmtime, strftime
import random
from .models import Book, Authors
# show all of the data from a table
def index(request):

    if request.method == "POST":
        Book.objects.create(title=request.POST['title'], desc=request.POST['description'])

        return redirect('/')
    

    if request.method == "GET":

        context = {
    	    "all_books": Book.objects.all()
            }
        return render(request, "ba_app/index.html", context)


def view(request, book_id):
    if request.method == "GET":
        this_book = Book.objects.get(id = book_id)
        context = {
        "all_books": Book.objects.all(),
        "all_authors": Authors.objects.all(),
        "book_id" : book_id,
        "selected_id" : Book.objects.get(id = book_id),
        "this_book" : this_book,
        "selected_authors" : this_book.authors.all(),
        "not_selected_authors": Authors.objects.exclude(books=this_book),
        }
        return render(request, "ba_app/view.html", context)

    if request.method == "POST":

        book = Book.objects.get(id = book_id)
        author =request.POST['author_id']
        book.authors.add(author)
    
        return redirect("/books/"+str(book_id))

    



