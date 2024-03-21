from django.shortcuts import render, redirect, get_object_or_404
from .models import Car
from .forms import CarForm

def car_list(request):
    cars = Car.objects.all()
    cars_colors = Car.objects.values('color').distinct()
    return render(request, 'cars/car_list.html', {'cars': cars,'cars_colors': cars_colors})

def car_detail(request, pk):
    car = get_object_or_404(Car, pk=pk)
    return render(request, 'cars/car_detail.html', {'car': car})

def car_create(request):
    if request.method == 'POST':
        form = CarForm(request.POST)
        if form.is_valid():
            form.save()
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
    cars = Car.objects.filter(color=color)
    return render(request, 'cars/show_car.html', {'cars': cars})

def get_id(request, pk):
    pass
