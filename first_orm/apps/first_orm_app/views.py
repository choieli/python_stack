# from django.shortcuts import render

# # Create your views here.


# def index(request):
#     # if 'total' in request.session:
#     #     total = request.session['total']
#     # else:
#     #     request.session['total'] =0

#     # if 'activity' in request.session:
#     #     activity = request.session['activity']
#     # else:
#     #     request.session['activity'] =[]


#     return render(request, "my_app/index.html")


# other imports
from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string
from time import gmtime, strftime
import random
from .models import Users
# show all of the data from a table
def index(request):
    context = {
    	"all_users": Users.objects.all()
    }
    return render(request, "first_orm_app/index.html", context)