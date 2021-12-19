from django.core.mail import send_mail
from django.shortcuts import render
from django.conf import settings
# Create your views here.
from django.http import HttpResponse
from cuestionario.models import encuesta
from users.models import User


def index(request):
    return render(request, 'formulario.html')


def myindex(request):
    return render(request, 'index.html')


def email(request):
    if request.method == "POST":
        p1 = request.POST["p1"]
        p2 = request.POST["p2"]
        p3 = request.POST["p3"]
        p4 = request.POST["p4"]
        p5 = request.POST["p5"]
        p6 = request.POST["p6"]
        p7 = request.POST["p7"]
        p8 = request.POST["p8"]
        p9 = request.POST["p9"]
        p10 = request.POST["p10"]
        ob1 = request.POST["ob1"]
        ob2 = request.POST["ob2"]
        encuesta.save(encuesta(None, p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, ob1, ob2))
        User = request.user
        User.is_answered=True
        User.save()

        return render(request, "contactoExitoso.html")

    return render(request, 'index.html')
