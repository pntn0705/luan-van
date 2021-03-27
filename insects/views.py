from django.shortcuts import render
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Insect, Insect_Image, Rect
import cv2
import json
from django.core import serializers
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from . import forms
# Create your views here.


def insect_slug(request, slug):
    #insect = Insect.objects.get(slug=slug)
    return HttpResponse(slug)


def home(request):
    args = {}
    img = {}
    img2 = {}
    img3 = {}
    f1 = open(
        "images/validation/Ant/Label/6dc059ecb7153297.txt", "r").read().split()
    img["url"] = "6dc059ecb7153297.jpg"
    img["x"] = f1[1]
    img["y"] = f1[2]
    img["w"] = f1[3]
    img["h"] = f1[4]
    shape = cv2.imread(
        "images/validation/Ant/6dc059ecb7153297.jpg").shape[:2]
    img["shape_h"] = shape[0]
    img["shape_w"] = shape[1]

    f2 = open(
        "images/validation/Ant/Label/f443370194c5f693.txt", "r").read().split()
    img2["url"] = "f443370194c5f693.jpg"
    img2["x"] = f2[1]
    img2["y"] = f2[2]
    img2["w"] = f2[3]
    img2["h"] = f2[4]
    shape = cv2.imread(
        "images/validation/Ant/f443370194c5f693.jpg").shape[:2]
    img2["shape_h"] = shape[0]
    img2["shape_w"] = shape[1]

    f3 = open(
        "images/validation/Ant/Label/714c75d57baedbd8.txt", "r").read().split()
    img3["url"] = "714c75d57baedbd8.jpg"
    img3["x"] = f3[1]
    img3["y"] = f3[2]
    img3["w"] = f3[3]
    img3["h"] = f3[4]
    shape = cv2.imread(
        "images/validation/Ant/714c75d57baedbd8.jpg").shape[:2]
    img3["shape_h"] = shape[0]
    img3["shape_w"] = shape[1]

    args["images"] = [img, img2, img3]
    print(args["images"])
    args["labels"] = [[],
                      [open(
                          "images/validation/Ant/Label/f443370194c5f693.txt", "r").read().splitlines()],
                      [open("images/validation/Ant/Label/714c75d57baedbd8.txt", "r").read().splitlines()]]
    print("=================================================")
    print(args["images"])

    rect = Rect.objects.all()

    args['rects'] = rect[:30]
    print(rect[0].image.image.url)
    return render(request, 'insect/home.html', args)


def image(request, image):
    image_data = open(
        "images/validation/Ant/" + image, "rb").read()
    response = HttpResponse(image_data, content_type='image')
    return response


def getAllInsect(request):
    insect = Insect.objects.all()
    data = serializers.serialize('json', insect)
    print(data)
    return HttpResponse(data)


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('/admin')
    else:
        form = AuthenticationForm()
    return render(request, 'insect/login.html', {'form': form})


def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        form2 = forms.CreateEmployee(request.POST)
        if form.is_valid():
            user = form.save()
            employee = form2.save()
            employee.user = user
            employee.save()
            login(request, employee)
            return redirect('insects:home')
    else:
        form = UserCreationForm()
        form2 = forms.CreateEmployee()
    return render(request, 'insect/register.html', {'UserCreationForm': form, 'form': form2})
