from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import Cancha, Deporte, Reserva
from .forms import CanchaForm, ReservaForm, LoginForm


def log_in(request):
    form = LoginForm(request.POST or None)
    context = {'message': None, 'form': form}
    if request.POST and form.is_valid():
        user = authenticate(**form.cleaned_data)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('canchas:home')
            else:
                context['message'] = 'El usuario ha sido desactivado'
        else:
            context['message'] = 'Usuario o contraseña incorrecta'
    return render(request, 'canchas/login.html', context)


@login_required
def log_out(request):
    logout(request)
    return redirect('canchas:log-in')


@login_required
def cancha_list(request):
    canchas = Cancha.objects.filter(activa=True)
    return render(request, 'canchas/index.html', {'canchas': canchas})


@login_required
def cancha_detail(request, pk):
    try:
        cancha = Cancha.objects.get(pk=pk)
    except Cancha.DoesNotExist:
        raise Http404("Esta cancha no existe")
    return render(request, 'canchas/detail.html', {'cancha': cancha})


@login_required
def cancha_create(request, **kwargs):
    form = CanchaForm(request.POST or None, request.FILES or None)
    if request.POST and form.is_valid():
        form.save()
        return redirect('canchas:home')
    return render(request, 'canchas/form.html', {'form': form})


@login_required
def cancha_update(request, **kwargs):
    cancha = Cancha.objects.get(pk=kwargs.get('pk'))
    form = CanchaForm(request.POST or None, request.FILES or None, instance=cancha)
    if request.POST and form.is_valid():
        form.save()
        return redirect('canchas:home')
    return render(request, 'canchas/form.html', {'form': form})


@login_required
def cancha_delete(request, **kwargs):
    cancha = Cancha.objects.get(pk=kwargs.get('pk'))
    cancha.activa = False
    cancha.save()
    return redirect('canchas:home')


@login_required
def deporte_list(request):
    deportes = Deporte.objects.all()
    return render(request, 'canchas/deporte/deporte_list.html', {'deportes': deportes})


@login_required
def reserva_list(request):
    reservas = Reserva.objects.all()
    return render(request, 'canchas/reserva/reserva_list.html', {'reservas': reservas})


@login_required
def reserva_create(request, **kwargs):
    form = ReservaForm(request.POST or None)
    if request.POST and form.is_valid():
        reserva = form.save(commit=False)
        reserva.usuario = request.user
        reserva.save()
        return redirect('canchas:reserva-list')
    return render(request, 'canchas/reserva/reserva_form.html', {'form': form})
