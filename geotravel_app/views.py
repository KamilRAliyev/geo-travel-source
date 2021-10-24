from django.core.paginator import Paginator
from django.shortcuts import render, HttpResponse, reverse, get_object_or_404, redirect
from tours.models import *
from guides.models import *
from tours.views import *
from transport.models import *
from .models import VisaServices, AboutUs, ContactFormInfo, SiteSettings, EvisaOrders, CookiePolicy
from .forms import ContactForm, EvisaForm
from django.core.mail import send_mail
from django.conf import settings
import datetime
from django.utils import translation
from django.shortcuts import redirect

# Create your views here.

def contact(request):
    form = ContactForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            name = form.cleaned_data.get('name')
            email = form.cleaned_data.get('email')
            message = form.cleaned_data.get('message')
            subject = form.cleaned_data.get('subject')

            Contact = ContactFormInfo()
            Contact.fullname = name
            Contact.email = email
            Contact.subject = subject
            Contact.message = message

            Contact.save()
            send_mail(f"{name} | {message[:100]}", f"""
New Contact Information:
Person: {name} ({email})
Subject: {subject}
Message:{message}""", settings.EMAIL_HOST_USER, ['office@geo-travel.az'], fail_silently=False)
            return redirect('home')
    else:
        return redirect('home')

def home_page(request):
    category = TourCategory.objects.all().order_by('order')
    form = ContactForm(request.POST or None)
    if request.method == "GET":
        tours = Tour.objects.all().order_by('created_at').reverse()[:15]
        return render(request, "geo/index.html", context=
        {
            'category': category,
            'guide_pages': Guide.objects.all(),
            'transfer_static_pages': TransferStaticPage.objects.all(),
            'tour': tours,
            'form': form,
            'popular_tours': Tour.objects.filter(rating=5).order_by('created_at')[:8],
            'rent_a_car': Vehicles.objects.all().order_by('created_at').reverse()[:8],
            'site_settings': SiteSettings.objects.first()
        })
    if request.method == "POST":
        if request.POST.get("num_days") != "0" and request.POST.get('city') !="0":
            tours = Tour.objects.filter(duration = request.POST.get("num_days"), city__contains = request.POST.get('city')).order_by('created_at').reverse()
        elif request.POST.get("num_days") == "0" and request.POST.get('city') !="0":
            tours = Tour.objects.filter(city__contains = request.POST.get('city')).order_by('created_at').reverse()
        elif request.POST.get("num_days") != "0" and request.POST.get('city') == "0":
            tours = Tour.objects.filter(duration = request.POST.get('num_days')).order_by('created_at').reverse()
        elif request.POST.get("num_days") == "0" and request.POST.get('city') == "0":
            tours = Tour.objects.all().order_by('created_at').reverse()
        paginator = Paginator(tours, 5)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context = {
            'page_obj': page_obj,
            'tours': tours,
            'guide_pages': Guide.objects.all(),
            'category': category,
            'form': form,
            'transfer_static_pages': TransferStaticPage.objects.all(),
            'popular_tours': Tour.objects.filter(rating=5).order_by('created_at')[:8],
            'rent_a_car': Vehicles.objects.all().order_by('created_at').reverse()[:8],
            'site_settings': SiteSettings.objects.first()
        }
        return render(request, 'tours-list.html', context=context)


def e_visa(request):
    content = VisaServices.objects.get(name_en='E-visa to Azerbaijan')
    category = TourCategory.objects.all().order_by('order')
    form = EvisaForm()
    content = {
        'content': content,
        'category': category,
        'guide_pages': Guide.objects.all(),
        'transfer_static_pages': TransferStaticPage.objects.all(),
        'form': form,
    }
    if 'message' in request.session:
        content['message'] = request.session['message']
        request.session['message'] = ''
    return render(request, 'forms/evisaform.html', context=content)


def e_visa_order(request):
    if request.method == 'POST':
        form = EvisaForm(request.POST, request.FILES)
        if form.is_valid():
            name = form.cleaned_data.get('fullname')
            email = form.cleaned_data.get('email')
            number = form.cleaned_data.get('number')
            passport = request.FILES['passport']
            document = request.FILES['document']
            order = EvisaOrders()
            order.fullname = name
            order.email = email
            order.phone_number = number
            order.passport_scans = passport
            order.document_scans = document
            order.save()
            request.session['message'] = f"Dear {name}, we got your order. We\'ll contact to you in short time."
            send_mail(f"{name} | {email}", f"""New E-Visa Order Information:
Person: {name} ({email})
Number: {number}
Time: {datetime.datetime.now()}
Passport attach: media/{order.passport_scans.name}
Document attach: media/{order.document_scans.name}
""", settings.EMAIL_HOST_USER, ['visas@geo-travel.az'],
                      fail_silently=False)
            return redirect('e_visa')
    return redirect('e_visa')


def who_we_are(request):
    content = AboutUs.objects.get(name_en='Who We Are?')
    category = TourCategory.objects.all().order_by('order')
    return render(request, 'geo/static_page.html', context={
        'content': content,
        'category': category,
        'guide_pages': Guide.objects.all(),
        'transfer_static_pages': TransferStaticPage.objects.all(),
    })


def where_you_can_meet_us(request):
    content = AboutUs.objects.get(name_en='Where you can meet us?')
    category = TourCategory.objects.all().order_by('order')
    return render(request, 'geo/static_page.html', context={
        'content': content,
        'category': category,
        'guide_pages': Guide.objects.all(),
        'transfer_static_pages': TransferStaticPage.objects.all(),
    })


def our_mission(request):
    content = AboutUs.objects.get(name_en='Our Mission')
    category = TourCategory.objects.all().order_by('order')
    return render(request, 'geo/static_page.html', context={
        'content': content,
        'category': category,
        'guide_pages': Guide.objects.all(),
        'transfer_static_pages': TransferStaticPage.objects.all(),
    })


def sahman(request):
    content = AboutUs.objects.get(name_en='SAHMAN')
    category = TourCategory.objects.all().order_by('order')
    return render(request, 'geo/static_page.html', context={
        'content': content,
        'category': category,
        'guide_pages': Guide.objects.all(),
        'transfer_static_pages': TransferStaticPage.objects.all(),
    })


def error_404(request, exception):
    content = False #AboutUs.objects.get(name_en='Our Mission')
    category = TourCategory.objects.all().order_by('order')
    return render(request, 'errors/404.html', context={
        'content': content,
        'category': category,
        'guide_pages': Guide.objects.all(),
        'transfer_static_pages': TransferStaticPage.objects.all(),
    })


def cookie_policy(request):
    content = CookiePolicy.objects.all()[0]
    category = TourCategory.objects.all().order_by('order')
    return render(request, 'geo/static_page.html', context={
        'content': content,
        'category': category,
        'guide_pages': Guide.objects.all(),
        'transfer_static_pages': TransferStaticPage.objects.all(),
    })
