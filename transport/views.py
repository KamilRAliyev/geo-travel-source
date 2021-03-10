from django.shortcuts import render, redirect
from .models import *
from django.core.paginator import Paginator
from tours.models import *
from guides.models import *
from decimal import Decimal
from django.core.mail import send_mail
from django.conf import settings
from .forms import CarRentalForm
import datetime


# Create your views here.
def transfer(request):
    transports = TransformCars.objects.all()
    content = {
        'transports': transports,
        'category': TourCategory.objects.all(),
        'guide_pages': Guide.objects.all(),
        'transfer_static_pages': TransferStaticPage.objects.all(),
    }

    if request.method == 'POST':
            fr = request.POST.get('from')
            to = request.POST.get('to')
            direction = request.POST.get('direction')
            car_id = request.POST.get('radio')
            car = TransformCars.objects.get(pk=car_id)
            pass_num1 = request.POST.get('passenger_number1')
            fly1 = request.POST.get('fly1')
            fly2 = request.POST.get('fly2') or None
            date1 = request.POST.get('date1')
            time1 = request.POST.get('time1')
            dest_addr1 = request.POST.get('dest_addr1')
            full_name = request.POST.get('full_name')
            mobile = request.POST.get('mobile')
            email = request.POST.get('email')
            plate = request.POST.get('plate') or None
            passenger_number2 = request.POST.get('passenger_number2') or None
            date2 = request.POST.get('date2')or None
            time2 = request.POST.get('time2')or None
            date3 = request.POST.get('date3') or None
            time3 = request.POST.get('time3') or None
            dest_addr2 = request.POST.get('dest_addr2') or None
            #Transform order model registration for order:
            # order = TransferOrder()
            # order.fr = fr
            # order.to = to
            # order.transform_car = car
            # order.full_name = full_name
            # order.email = email
            # order.price = car.price
            # order.passenger_number_one_way = pass_num1
            # order.flight_one_way = fly1
            # order.phone_number = mobile
            # order.date_arrival = datetime.datetime.strptime(date1, "%m/%d/%Y")
            # try:
            #     order.date_arrival_time = datetime.datetime.strptime(time1, "%H:%M")
            # except:
            #     pass
            if direction == '1':
                mail = f"""
                    New Transfer Order:
                From: {fr}
                To: {to}
                Direction: one way
                Car: {car.name} . Price: {car.price}
                Passenger number: {pass_num1}
                Flight info: {fly1}
                Date/Time: {date1} {time1}
                Destination Address: {dest_addr1}
                    Passenger Info:
                Full Name: {full_name}
                Mobile: {mobile}
                Email: {email}
                Plate: {plate}
                """
                # try:
                #     order.save()
                # except:
                #     send_mail("Transfer model error", f"{mail}", settings.EMAIL_HOST_USER, ['kamilraliyev@gmail.com'],
                #               fail_silently=False)
                send_mail(f"New Transfer Order: {full_name} ({email})", mail, settings.EMAIL_HOST_USER, ['transport@geo-travel.az'],fail_silently=False)
            else:
                if direction == '2':
                    mail = f"""
                        New Transfer Order:
                    From: {fr}
                    To: {to}
                    Direction: return transfer
                    Car: {car.name} . Price: {car.price} x 2
                    Passenger number: {pass_num1}
                    Flight info: {fly1}
                    Date/Time: {date1} {time1}
                    Destination Address: {dest_addr1}
                    
                        Return Transfer:
                    Passenger number: {passenger_number2}
                    DATE AND DEPARTURE TIME: {date2} {time2}
                    DATE AND TIME OF VEHICLE DELIVERY: {date3} {time3}
                    ADDRESS OF VEHICLE DELIVERY: {dest_addr2}
                    
                        Passenger Info:
                    Full Name: {full_name}
                    Mobile: {mobile}
                    Email: {email}
                    Plate: {plate}
                    """
                    # order.passenger_number_two_way = passenger_number2
                    # try:
                    #     order.price = float(car.price) * 2
                    # except:
                    #     pass
                    # order.flight_two_way = fly2
                    # try:
                    #     order.date_arrival_time_two_way = datetime.datetime.strptime(time1, "%H:%M")
                    # except:
                    #     pass
                    # order.date_arrival_two_way = datetime.datetime.strptime(date2, "%m/%d/%Y")
                    # try:
                    #     order.save()
                    # except:
                    #     send_mail("Transfer model error", f"{mail}",settings.EMAIL_HOST_USER, ['kamilraliyev@gmail.com'], fail_silently=False)
                    send_mail(f"New Transfer Order: {full_name} ({email})", mail, settings.EMAIL_HOST_USER,
                              ['transport@geo-travel.az'], fail_silently=False)
    return render(request,'transport_form.html', content)


def car_rental_list(request):
    if request.method == 'GET':
        queryset = Vehicles.objects.all().order_by('created_at').reverse()

    if request.method == 'POST':
        queryset = Vehicles.objects.all().order_by('created_at').reverse()
        if request.POST.get('amount'):
            queryset = Vehicles.objects.filter(price__range=(Decimal(request.POST.get('amount')[1:]), Decimal(request.POST.get('amount2')[1:])))

        if request.POST.get('category') and request.POST.get('passcap') and request.POST.get('tr'):
            queryset = Vehicles.objects.filter(category__name__contains=request.POST.get('category'), passenger=int(request.POST.get('passcap')), transmission__contains=request.POST.get('tr'))

        elif request.POST.get('category') and request.POST.get('passcap'):
            queryset = Vehicles.objects.filter(category__name__contains=request.POST.get('category'), passenger=int(request.POST.get('passcap')))

        elif request.POST.get('passcap') and request.POST.get('tr'):
            queryset = Vehicles.objects.filter(passenger=int(request.POST.get('passcap')), transmission__contains=request.POST.get('tr'))

        elif request.POST.get('category') and request.POST.get('tr'):
            queryset = Vehicles.objects.filter(category__name__contains=request.POST.get('category'), transmission__contains=request.POST.get('tr'))

        else:
            if request.POST.get('category'):
                queryset = Vehicles.objects.filter(
                    category__name__contains=request.POST.get('category')
                )
            if request.POST.get('passcap'):
                queryset = Vehicles.objects.filter(
                    passenger=int(request.POST.get('passcap'))

                )
            if request.POST.get('tr'):
                queryset = Vehicles.objects.filter(
                    transmission__contains=request.POST.get('tr')
                )

    paginator = Paginator(queryset, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    content = {
        'page_obj': page_obj,
        'vehicles': queryset,
        'category': TourCategory.objects.all(),
        'transfer_static_pages': TransferStaticPage.objects.all(),
        'guide_pages': Guide.objects.all(),
    }
    return render(request, 'car_rental_list.html', context=content)


def vehicle_details(request, slug):
    vehicle = Vehicles.objects.get(slug=slug)
    category = TourCategory.objects.all()
    order_form = CarRentalForm(request.POST or None)
    content = {
        'vehicle': vehicle,
        'category': category,
        'form': order_form,
        'transfer_static_pages': TransferStaticPage.objects.all(),
        'guide_pages': Guide.objects.all(),
        'message': ''
    }
    if 'message' in request.session:
        content['message'] = request.session['message']
        request.session['message'] = ''

    return render(request, 'car_details.html', context=content)


def vehicle_order(request, slug):
    vehicle = Vehicles.objects.get(slug=slug)
    order_form = CarRentalForm(request.POST or None)
    if request.method == "POST":
        if order_form.is_valid():
            name = order_form.cleaned_data.get('full_name')
            email = order_form.cleaned_data.get('email')
            start_date_str = order_form.cleaned_data.get('start_date')
            end_date_str = order_form.cleaned_data.get('end_date')
            start_date = datetime.datetime.strptime(start_date_str, "%m/%d/%Y")
            end_date = datetime.datetime.strptime(end_date_str, "%m/%d/%Y")
            order = CarRentOrders()
            order.full_name = name
            order.email = email
            order.start_date = start_date
            order.end_date = end_date
            order.vehicle_name = vehicle.name
            order.vehicle_url = vehicle.get_absolute_url()
            if (end_date-start_date).days < 0:
                request.session['message'] = "ERROR: End Date should be later than Start Date"
                return redirect(f'{vehicle.get_absolute_url()}')
            else:
                price = vehicle.price*(end_date-start_date).days
            order.price = Decimal(price)
            order.save()
            send_mail(f"{name} | {vehicle.name}", f"""
                     New Order Information:

                     Orderer: {name} ({email})
                     Tour that order came: {vehicle.name} ({vehicle.get_absolute_url()})
                     Price: {str(price)}
                 """, settings.EMAIL_HOST_USER, ['e4mz3fbgnp@smart-email.me'], fail_silently=False)
            request.session['message'] = f"We got your message. We will contact you by {email}, in the shortest period."
    return redirect(f'{vehicle.get_absolute_url()}')


def transfer_static_page(request,slug):
    content = TransferStaticPage.objects.get(slug=slug)
    category = TourCategory.objects.all().order_by('order')
    price_table = TransferPriceTable.objects.filter(page=content).order_by('price')
    return render(request, 'static_page.html', context={
        'content': content,
        'category': category,
        'guide_pages': Guide.objects.all(),
        'transfer_static_pages': TransferStaticPage.objects.all(),
        'table': price_table
    })
