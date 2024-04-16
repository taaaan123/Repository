from django.shortcuts import render, redirect, get_object_or_404
from django.db import transaction
from django.db.models import Max
from django.http import HttpResponse
from .models import Car
from .forms import CarForm

def car_list(request):
    cars = Car.objects.all().order_by('order')
    cars_colors = Car.objects.values('color').distinct()
    first_order = Car.objects.order_by('order')[0]
    last_order = Car.objects.order_by('-order')[0]
    return render(request, 'cars/car_list.html', {'cars': cars,'cars_colors': cars_colors, 'first_order': first_order.order, 'last_order': last_order.order})

def car_detail(request, pk):
    car = get_object_or_404(Car, pk=pk)
    return render(request, 'cars/car_detail.html', {'car': car})

def car_create(request):
    if request.method == 'POST':
        form = CarForm(request.POST)
        if form.is_valid():
            new_car = form.save(commit=False)
            last_order = Car.objects.aggregate(Max('order'))['order__max']
            # last_order = Car.objects.order_by('-order').first()
            if last_order is not None:
                new_car.order = last_order + 1
            else:
                new_car.order = 1
            new_car.save()
            return redirect('car_list')
    else:
        form = CarForm()
    return render(request, 'cars/car_form.html', {'form': form})

def car_update(request, pk):
    car = get_object_or_404(Car, pk=pk)
    if request.method == 'POST':
        form = CarForm(request.POST, instance=car)
        if form.is_valid():
            form.save()
            return redirect('car_list')
    else:
        form = CarForm(instance=car)
    return render(request, 'cars/car_form.html', {'form': form})

def car_delete(request, pk):
    car = get_object_or_404(Car, pk=pk)
    if request.method == 'POST':
        car.delete()
        return redirect('car_list')
def show_car(request, color):
    cars = Car.objects.filter(color=color).order_by('order')
    first_order = Car.objects.filter(color=color).order_by('order')[0]
    last_order = Car.objects.filter(color=color).order_by('-order')[0]
    return render(request, 'cars/show_car.html',{'cars': cars, 'first_order': first_order.order,'last_order': last_order.order})

def swap_cars(request, pk, type, color):
    current_record = Car.objects.get(pk=pk)
    current_order = current_record.order
    if color != 'all':
        next_record = Car.objects.filter(order__gt=current_record.order, color=color).order_by('order').first()
        previous_record = Car.objects.filter(order__lt=current_record.order, color=color).order_by('-order').first()
    else:
        next_record = Car.objects.filter(order__gt=current_record.order).order_by('order').first()
        previous_record = Car.objects.filter(order__lt=current_record.order).order_by('-order').first()
    if type == 'previous':
        current_record.order = previous_record.order
        previous_record.order = current_order
        current_record.save()
        previous_record.save()
        if color != 'all':
            cars = Car.objects.filter(color=color).order_by('order')
            first_order = Car.objects.filter(color=color).order_by('order')[0]
            last_order = Car.objects.filter(color=color).order_by('-order')[0]
            return render(request, 'cars/show_car.html',{'cars': cars, 'first_order': first_order.order,'last_order': last_order.order})
        else:
            return redirect('car_list')
    else:
        current_record.order = next_record.order
        next_record.order = current_order
        current_record.save()
        next_record.save()
        if color != 'all':
                cars = Car.objects.filter(color=color).order_by('order')
                first_order = Car.objects.filter(color=color).order_by('order')[0]
                last_order = Car.objects.filter(color=color).order_by('-order')[0]
                return render(request, 'cars/show_car.html',{'cars': cars, 'first_order': first_order.order,'last_order': last_order.order})
        else:
            return redirect('car_list')

