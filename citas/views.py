from django.shortcuts import render
from django.utils import timezone 
from django.utils.timezone import make_aware 
from django.shortcuts import render, get_object_or_404, redirect
from .models import Cita

#  Listar citas activas y eliminadas
def listar_citas(request):
    citas_activas = Cita.objects.filter(eliminada=False)
    citas_eliminadas = Cita.objects.filter(eliminada=True)
    return render(request, "citas/listar.html", {
        "citas_activas": citas_activas,
        "citas_eliminadas": citas_eliminadas
    })

#  Crear una nueva cita
def crear_cita(request):
    if request.method == "POST":
        fecha_hora = request.POST["fecha_hora"]
        paciente = request.POST["paciente"]
        tipo_cita = request.POST["tipo_cita"]
        tipo_cita_personalizado = request.POST.get("tipo_cita_personalizado", "")
        medico = request.POST["medico"]

        # Convertir la fecha y hora recibida a un objeto datetime naive
        fecha_hora_obj = timezone.datetime.strptime(fecha_hora, '%Y-%m-%dT%H:%M')

        # Convertir el datetime naive a un datetime con zona horaria
        fecha_hora_obj = make_aware(fecha_hora_obj)

        # Validar que la fecha y hora no sean en el pasado
        if fecha_hora_obj < timezone.now():
            # Si la fecha es en el pasado, mostrar un error y no guardar la cita
            return render(request, "citas/crear.html", {
                "error_message": "La fecha y hora de la cita no pueden ser en el pasado, por favor editalas para poder agendar tu cita correctamente."
            })
        
        # Si es una fecha válida, guardar la cita
        if tipo_cita == "Otra":
            tipo_cita_guardar = "Otra"
        else:
            tipo_cita_guardar = tipo_cita
            tipo_cita_personalizado = ""

        Cita.objects.create(
            fecha_hora=fecha_hora_obj,
            paciente=paciente,
            tipo_cita=tipo_cita_guardar,
            tipo_cita_personalizado=tipo_cita_personalizado,
            medico=medico
        )
        return redirect("listar_citas")

    return render(request, "citas/crear.html")

#  Editar una cita existente (sin modificar paciente ni número de cita)
def editar_cita(request, id):
    cita = get_object_or_404(Cita, numero_cita=id)
    if request.method == "POST":
        cita.fecha_hora = request.POST["fecha_hora"]
        cita.tipo_cita = request.POST["tipo_cita"]
        cita.tipo_cita_personalizado = request.POST.get("tipo_cita_personalizado", "")

        if cita.tipo_cita != "Otra":
            cita.tipo_cita_personalizado = ""

        cita.medico = request.POST["medico"]
        cita.save()
        return redirect("listar_citas")

    return render(request, "citas/editar.html", {"cita": cita})

# Eliminar una cita (sin borrar, solo  un borrado lógico)
def eliminar_cita(request, id):
    cita = get_object_or_404(Cita, numero_cita=id)
    cita.eliminada = True
    cita.save()
    return redirect("listar_citas")

