from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Room, Message
# Create your views here.


def home(request):
    return render(request, 'index.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('profile')
        else:
            messages.info(request, "Invalid login information")
            return render(request, 'login.html')
    else:
        return render(request, 'login.html')


def register(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name', False)
        last_name = request.POST.get('last_name', False)
        username = request.POST.get('username', False)
        email = request.POST.get('email', False)
        password1 = request.POST.get('pass1')
        password2 = request.POST.get('pass2')
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username already taken")
                return redirect('register')
            else:
                user = User.objects.create_user(
                    username=username, password=password1, email=email, first_name=first_name, last_name=last_name)
                user.save()
                return redirect('login')
        else:
            messages.info(request, "Password didnot matched with previous one")
            return redirect('register')

    else:
        return render(request, "register.html")


@login_required
def profile(request):
    if request.user.is_authenticated:
        return render(request, 'profile.html')

    else:
        return redirect('login')


@login_required
def createroom(request):
    if request.method == 'POST':
        newroomname = request.POST.get('new_room', False)
        print(newroomname)
        if Room.objects.filter(roomname=newroomname).exists():
            messages.info(request, "Choose different room name")
            return redirect('createroom')
        else:
            room = Room.objects.create(roomname=newroomname)
            room.save()
            messages.info(request, "room created sucessfully :)")
            return redirect('createroom')
    else:
        return render(request, 'createroom.html')


@login_required
def viewroom(request):
    rooms = Room.objects.all()
    return render(request, 'viewroom.html', {"rooms": rooms})


@login_required
def room(request, room_name):
    if Room.objects.filter(roomname=room_name).exists():
        images = Message.objects.filter(room=room_name).order_by('-created_at')[:5]
        deserialized_images = []
        for image in images:
            img = image.content
            deserialized_images.append({
                    'img': img,
                    'username': image.user,
                    'message_length':image.length
                })            
        return render(request, 'room.html', {'roomname': room_name, 'images': deserialized_images})
    else:
        return redirect('login')
