from django.shortcuts import render, redirect
from .models import Sucursal, Transporte, Repartidor, Paquete
from .forms import PaqueteForm, TransporteForm
from datetime import datetime
import random

def index(request):
    sucursales = Sucursal.objects.all()   # pylint: disable=no-member
    return render(request, 'gestion/index.html', {'sucursales': sucursales})

def options(request):
    if request.method == "POST":
        sucursalId = request.POST.get("sucursales")
        request.session["sucursal"] = sucursalId
        if sucursalId:
            request.session["id"] = sucursalId
            sucursalInstance = Sucursal.objects.get(id=sucursalId)  # pylint: disable=no-member
            return render(request, "gestion/options.html", {'sucursal': sucursalInstance})
        else:
            return render(request, "gestion/index.html", {
            "error": "Debe seleccionar una sucursal.",
            "sucursales": Sucursal.objects.all() # pylint: disable=no-member
        })
    else:
        return redirect('index')  # redirigimos si alguien entra por GET

def registerPackage(request):
    sucursalId = request.session.get("sucursal")
    if not sucursalId:
        return redirect('index')
    sucursalInstance = Sucursal.objects.get(id=sucursalId)  # pylint: disable=no-member
    if request.method == "POST":
        form = PaqueteForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            ultPaquete = Paquete.objects.order_by('-id').first()   # pylint: disable=no-member
            nuevo = Paquete(
                numeroenvio = ultPaquete.numeroenvio + 10 if ultPaquete else 10,
                peso=cd['peso'],
                nomdestinatario=cd['nomdestinatario'],
                dirdestinatario=cd['dirdestinatario'],
                observaciones=cd['observaciones'],
                sucursal=sucursalInstance,
                transporte=None,
                repartidor=None,
                entregado=False
            )
            nuevo.save()
            return render(request, "gestion/message.html", {"aviso": "Paquete registrado con éxito"})
    else:
        form = PaqueteForm()
        contexto = {
        "form": form,
        "sucursal": sucursalInstance
        }
        return render(request, "gestion/registerPackage.html", contexto)

def selectTransport(request):
    sucursalId = request.session.get("sucursal")
    if not sucursalId:
        return redirect('index')
    sucursalInstance = Sucursal.objects.get(id=sucursalId)  # pylint: disable=no-member
    if request.method == "POST":
        form = TransporteForm(request.POST, sucursal=sucursalInstance)
        if form.is_valid():
            cd = form.cleaned_data
            fechahorasalida = datetime.now()
            ultTransporte = Transporte.objects.order_by('-id').first()   # pylint: disable=no-member
            nuevo = Transporte(
                numerotransporte = ultTransporte.numerotransporte + 10 if ultTransporte else 10,
                fechahorasalida = fechahorasalida,  #¡¡¡ACA HAY QUE ARREGLAR, YA QUE ESTOY PIDIENDO QUE ELIJAN UN TRANSPORTE PERO HAY QUE GENERARLO!!!
                sucursal = sucursalInstance
            )
            nuevo.save()
            paquetesSelec = cd['paquetes']  # Paquetes seleccionados del formulario
            # Asignar los paquetes seleccionados al transporte y marcar como entregados
            for paquete in paquetesSelec:
                print("PAQUETE:",paquete)
                paquete.entregado = True
                paquete.transporte = nuevo  # Asociamos el paquete con el transporte
                paquete.save()
            return render(request, "gestion/message.html", {"aviso": "Transporte registrado con éxito"})
        else:
            return render(request, "gestion/message.html", {"aviso": "Error al registrar el transporte"})
    else:
        form = TransporteForm(sucursal=sucursalInstance)
        contexto = {
        "form": form,
        "sucursal": sucursalInstance
        }
        return render(request, "gestion/selectTransport.html", contexto)
        

def transportArrival(request):
    return render(request, 'gestion/transportArrival.html')

def message(request, aviso):
    return render(request, 'gestion/message.html',aviso)