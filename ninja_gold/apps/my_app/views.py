from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string
from time import gmtime, strftime
import random

# def name(request):
#     context = {
#         "name" : "ELI",
#         "favorite_color" : "blue",
#         "pets" : ["dog","cat","dragon"]
#     }
#     return render(request, "my_app/index.html", context)

# def one_more(request,id,color):
#     return HttpResponse(f"id is {id} and color is {color}")

def index(request):
    if 'total' in request.session:
        total = request.session['total']
    else:
        request.session['total'] =0

    if 'activity' in request.session:
        activity = request.session['activity']
    else:
        request.session['activity'] =[]


    return render(request, "my_app/index.html")

def process(request):
    # if request.method == "POST":
    if request.POST['action'] == 'casino':
        casinoearn=random.randrange(5,10)
        luck=random.randrange(0,2)
        if luck==0:
            request.session['total'] += casinoearn
            request.session['activity'].append('You have earned ' + str(casinoearn) + ' golds from the ' + 'casino')
                
            
        else:
            request.session['total'] -= casinoearn
            request.session['activity'].append('You have lost ' + str(casinoearn) + ' golds from the ' + 'casino')
    elif request.POST['action'] == "farm":
        farmearn=random.randrange(10,20)
        request.session['total'] += farmearn
        request.session['activity'].append('You have earned ' + str(farmearn) + ' golds from the ' + 'farm')
    elif request.POST['action'] == "cave":
        caveearn=random.randrange(5,10)
        request.session['total'] += caveearn
        request.session['activity'].append('You have earned ' + str(caveearn) + ' golds from the ' + 'cave')
            
            
    elif request.POST['action'] == 'house':
        houseearn=random.randrange(2,5)
        request.session['total'] += houseearn
        request.session['activity'].append('You have earned ' + str(houseearn) + ' golds from the ' + 'house')
            
            
            
                
            
   
    return redirect('/')
        
        





# def random(request):
#     context = {
#         "number" : get_random_string(length=14)
#     }
#     if 'counter' in request.session:
#         request.session['counter'] += 1
#     else:
#         request.session['counter'] = 1

#     return render(request, "my_app/random.html", context)


def reset(request):
    request.session.clear()

    return redirect('/')



# Create your views here.
