from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.urls import reverse
import os
import csv


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    page_number = int(request.GET.get('page', 1))
    csv_file = os.path.join('data-398-2018-08-30.csv')
    with open(csv_file, newline='', encoding="utf-8") as file:
        bus_stations = list(csv.DictReader(file))
        paginator = Paginator(bus_stations, 10)
        page = paginator.get_page(page_number)
        context = {
            'bus_stations': page.object_list,
            'page': page,
        }
    return render(request, 'stations/index.html', context)
