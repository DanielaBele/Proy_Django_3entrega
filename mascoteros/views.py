from django.shortcuts import render

def index(request):
    context = {"mensaje": "Somos un santuario para tu mascota"}
    return render(request, "mascoteros/index.html", context)