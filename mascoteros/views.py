from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.views.generic import TemplateView
from mascoteros.forms import DueñoForm, MascotaForm, EstadiaForm
from .models import Dueño, Mascota, Estadia

def index(request):
    context = {"mensaje": "Somos un santuario para tu mascota"}
    return render(request, "mascoteros/index.html", context)

class AboutView(TemplateView):
    template_name = "mascoteros/about.html"

def registro(request):
    if request.method == 'POST':
        form = DueñoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Usuario creado correctamente")
            return redirect('registro')
        else:
            messages.error(request, "Hubo un error al crear el usuario")
    else:
        form = DueñoForm()

    dueños = Dueño.objects.all()
    return render(request, "mascoteros/registro.html", {
        "dueño_form": form,
        "dueños": dueños
    })

def editar_dueño(request, pk):
    dueño = get_object_or_404(Dueño, pk=pk)
    if request.method == 'POST':
        form = DueñoForm(request.POST, instance=dueño)
        if form.is_valid():
            form.save()
            messages.success(request, "Dueño actualizado correctamente")
            return redirect('registro')
    else:
        form = DueñoForm(instance=dueño)

    dueños = Dueño.objects.all()
    return render(request, "mascoteros/registro.html", {
        "dueño_form": form,
        "dueños": dueños,
        "modo_edicion": True,
        "dueño_id": pk
    })

def eliminar_dueño(request, pk):
    dueño = get_object_or_404(Dueño, pk=pk)
    if request.method == 'POST':
        try:
            dueño.delete()
            messages.success(request, "Dueño eliminado correctamente")
        except Exception as e:
            messages.error(request, f"Error al eliminar: {e}")
    return redirect('registro')

def mascota(request, mascota_id=None):
    if mascota_id:
        mascota_instance = get_object_or_404(Mascota, id=mascota_id)
        form = MascotaForm(request.POST or None, instance=mascota_instance)
        modo = 'modificar'
    else:
        mascota_instance = None
        form = MascotaForm(request.POST or None)
        modo = 'crear'

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, f"Mascota {'modificada' if mascota_id else 'creada'} correctamente")
            return redirect('mascota')

    mascotas = Mascota.objects.select_related('dueño')
    return render(request, 'mascoteros/mascota.html', {
        'mascota_form': form,
        'mascotas': mascotas,
        'modo': modo,
        'mascota_id': mascota_id
    })

def eliminar_mascota(request, mascota_id):
    mascota = get_object_or_404(Mascota, id=mascota_id)
    if request.method == 'POST':
        mascota.delete()
        messages.success(request, "Mascota eliminada correctamente")
    return redirect('mascota')   

def estadia(request, id_estadia=None):
    if id_estadia:
        estadia_instance = get_object_or_404(Estadia, pk=id_estadia)
    else:
        estadia_instance = None

    if request.method == 'POST':
        form = EstadiaForm(request.POST, instance=estadia_instance)
        if form.is_valid():
            form.save()
            if estadia_instance:
                messages.success(request, "Estadía modificada correctamente")
            else:
                messages.success(request, "Estadía creada correctamente")
            return redirect('estadia')
        else:
            messages.error(request, "Corrige los errores antes de continuar.")
    else:
        form = EstadiaForm(instance=estadia_instance)

    estadias = Estadia.objects.select_related('mascota', 'dueño')

    return render(request, "mascoteros/estadia.html", {
        "estadia_form": form,
        "mascota_form": MascotaForm(),
        "dueño_form": DueñoForm(),
        "estadias": estadias,
        "dueños": Dueño.objects.all(),
        "modo_edicion": bool(estadia_instance),
        "id_estadia": id_estadia
    })

def eliminar_estadia(request, id_estadia):
    if request.method == 'POST':
        estadia = get_object_or_404(Estadia, pk=id_estadia)
        estadia.delete()
        messages.success(request, "Estadía eliminada correctamente")
    else:
        messages.error(request, "Acción no permitida.")
    return redirect('estadia')


