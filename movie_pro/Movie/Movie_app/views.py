from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.db import IntegrityError
from .models import FilmAdd


def sign(request):
    if request.method == 'POST':
        firstname = request.POST['First Name']
        lastname = request.POST['Last Name']
        username = request.POST['UserName']
        email = request.POST['Email']
        password = request.POST['password']

        # Check if the username already exists
        if User.objects.filter(username=username).exists():
            return HttpResponse("Username already exists. Please choose a different username.")

        try:
            myuser = User.objects.create_user(username=username, email=email, password=password, first_name=firstname,
                                              last_name=lastname)
            myuser.save()
            return redirect('loginn')
        except IntegrityError:
            return HttpResponse("An error occurred during user creation. Please try again.")

    # Always return a response, even if not POST
    return render(request, 'sign.html')


def loginn(request):
    if request.method == 'POST':
        username = request.POST['UserName']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('create_item')
        else:
            return redirect('sign')

    return render(request, 'login.html')



def create_item(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        image = request.FILES.get('image')
        obj = FilmAdd(name=name, description=description, image=image)
        obj.save()
        return redirect('movie_output_view')

    return render(request, 'create_film.html')
def movie_output_view(request):
    movies = FilmAdd.objects.all()
    return render(request, 'list.html', {'movies': movies})
