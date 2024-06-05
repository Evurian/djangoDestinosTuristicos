# destinos/views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import DestinosTuristicos
from .forms import DestinosTuristicosForm

def lista_destinos(request):
    destinos = DestinosTuristicos.objects.all()
    return render(request, 'destinos/lista_destinos.html', {'destinos': destinos})

def añadir_destino(request):
    if request.method == 'POST':
        form = DestinosTuristicosForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('lista_destinos')
    else:
        form = DestinosTuristicosForm()
    return render(request, 'destinos/añadir_destino.html', {'form': form})

def modificar_destino(request, pk):
    destino = get_object_or_404(DestinosTuristicos, pk=pk)
    if request.method == 'POST':
        form = DestinosTuristicosForm(request.POST, request.FILES, instance=destino)
        if form.is_valid():
            form.save()
            return redirect('lista_destinos')
    else:
        form = DestinosTuristicosForm(instance=destino)
    return render(request, 'destinos/modificar_destino.html', {'form': form})

def eliminar_destino(request, pk):
    destino = get_object_or_404(DestinosTuristicos, pk=pk)
    if request.method == 'POST':
        destino.delete()
        return redirect('lista_destinos')
    return render(request, 'destinos/eliminar_destino.html', {'destino': destino})
