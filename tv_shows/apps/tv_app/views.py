from django.shortcuts import render,redirect
from .models import Shows
from django.contrib import messages

# Create your views here.


def index(request):

    # if request.method == "POST":
    #     Book.objects.create(title=request.POST['title'], desc=request.POST['description'])

    #     return redirect('/')
    context = {
    	    "all_shows": Shows.objects.all()
            }
    return render(request, "tv_app/index.html", context)


def view(request,show_id):
    this_show = Shows.objects.get(id=show_id)
    context = {
        "all_shows": Shows.objects.all(),
        "show_id" : show_id,
        "this_show" : this_show,
        }
    return render(request, "tv_app/view.html", context)

def edit(request, show_id):
    if request.method == "GET":
        this_show = Shows.objects.get(id=show_id)
        context = {
            "all_shows": Shows.objects.all(),
            "show_id" : show_id,
            "this_show" : this_show,
            }
        return render(request, "tv_app/edit.html", context)

    if request.method == "POST":
        errors = Shows.objects.basic_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request,value)
            return redirect("/shows/"+str(show_id)+"/edit")
        else:
            Shows_to_update = Shows.objects.get(id=show_id)
            Shows_to_update.title=request.POST['title']
            Shows_to_update.network=request.POST['network']
            Shows_to_update.release_date=request.POST['release_date']
            Shows_to_update.description=request.POST['description']
            Shows_to_update.save()
                
            return redirect("/shows/"+str(show_id))

def new(request):

    if request.method == "GET":

        context = {
    	    "all_shows": Shows.objects.all()
            }
        return render(request, "tv_app/add.html", context)

    if request.method == "POST":
        errors = Shows.objects.basic_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request,value)
            return redirect("/shows/new")
        else:
            Shows.objects.create(title=request.POST['title'], network=request.POST['network'],release_date=request.POST['release_date'],description=request.POST['description'])
        
            return redirect("/shows/")

def delete(request, show_id):
    Shows_to_delete = Shows.objects.get(id=show_id)
    Shows_to_delete.delete()

    return redirect("/shows/")
    




# this_book = Book.objects.get(id = book_id)
#         context = {
#         "all_books": Book.objects.all(),
#         "all_authors": Authors.objects.all(),
#         "book_id" : book_id,
#         "selected_id" : Book.objects.get(id = book_id),
#         "this_book" : this_book,
#         "selected_authors" : this_book.authors.all(),
#         "not_selected_authors": Authors.objects.exclude(books=this_book),
#         }