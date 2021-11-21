from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from .models import *
from guides.models import *
from decimal import Decimal
from django.shortcuts import get_object_or_404
from .forms import TourCommentForm
from django.core.mail import send_mail
from django.conf import settings
from transport.models import *


# Create your views here.


def tour_list_view(request, **kwargs):
    category = TourCategory.objects.all()

    if request.method == 'GET':
        queryset = Tour.objects.all().order_by('created_at').reverse()

    if request.method == 'POST':
        queryset = Tour.objects.all().order_by('created_at').reverse()
        if request.POST.get('city'):
            queryset = Tour.objects.filter(city__contains=request.POST.get('city')).order_by('created_at').reverse()
        if request.POST.get('amount'):
            queryset = Tour.objects.filter(
                price__range=(Decimal(request.POST.get('amount')[1:]), Decimal(request.POST.get('amount2')[1:])))

    paginator = Paginator(queryset, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj,
        'tours': queryset,
        'guide_pages': Guide.objects.all(),
        'category': category,
        'transfer_static_pages': TransferStaticPage.objects.all(),

    }
    return render(request, 'tours-list.html', context=context)


def tour_category_view(request, pk):
    category = TourCategory.objects.all()
    if request.method == 'GET':
        queryset = Tour.objects.all().filter(category=pk).order_by('created_at').reverse()
    if request.method == 'POST':
        queryset = Tour.objects.all().filter(category=pk).order_by('created_at').reverse()
        if request.POST.get('city'):
            queryset = Tour.objects.filter(city__contains=request.POST.get('city'), category=pk).order_by(
                'created_at').reverse()
        if request.POST.get('amount'):
            queryset = Tour.objects.filter(
                price__range=(Decimal(request.POST.get('amount')[1:]), Decimal(request.POST.get('amount2')[1:])),
                category=pk)

    paginator = Paginator(queryset, 5)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj,
        'tours': queryset,
        'category': category,
        'transfer_static_pages': TransferStaticPage.objects.all(),
        'guide_pages': Guide.objects.all(),
        'this_category': get_object_or_404(TourCategory, pk=pk)
    }
    return render(request, 'tours-list.html', context=context)


def tour_details(request, slug):
    tour = Tour.objects.get(slug=slug)
    category = TourCategory.objects.all()
    comment_form = TourCommentForm(request.POST or None)
    comments = TourComments.objects.filter(tour=tour.pk)
    price_table = TourPriceTable.objects.filter(tour=tour).order_by('price')
    if request.method == "POST":
                name = request.POST.get('full_name')
                email = request.POST.get('email')
                select = request.POST.get('select')[0]
                order = TourOrders()
                order.full_name = name
                order.price = TourPriceTable.objects.get(pk=select).price
                order.email = email
                order.tour_name = tour.name
                order.save()
            #     send_mail(f"{name} | {tour.name}", f"""
            #     New Order Information:

            #     Orderer: {name} ({email})
            #     Tour that order came: {tour.name} ({tour.get_absolute_url()})
            #     Tour Option: {TourPriceTable.objects.get(pk=select).desc}
            #     Price: ${order.price}
            # """, settings.EMAIL_HOST_USER, ['mice@geo-travel.az'], fail_silently=False)

                return render(request, 'tour-details.html', context={
                    'tour': tour,
                    'tour_slider': TourSliderImages.objects.filter(tour=tour.pk),
                    'category': category,
                    'comment_form': comment_form,
                    'guide_pages': Guide.objects.all(),
                    'message': f"We got your message. We will contact you by {email}, in the shortest period.",
                    'comments': comments,
                    'table': price_table
                })

    context = {
        'tour': tour,
        'tour_slider': TourSliderImages.objects.filter(tour=tour.pk),
        'category': category,
        'comment_form': comment_form,
        'guide_pages': Guide.objects.all(),
        'transfer_static_pages': TransferStaticPage.objects.all(),
        'comments': comments,
        'table': price_table
    }
    return render(request, 'tour-details.html', context=context)


def tour_comment(request, slug):
    tour = Tour.objects.get(slug=slug)
    form = TourCommentForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            name = form.cleaned_data.get('full_name')
            email = form.cleaned_data.get('email')
            comment = form.cleaned_data.get('comment')
            tcomment = TourComments()
            tcomment.full_name = name
            tcomment.email = email
            tcomment.comment = comment
            tcomment.tour = tour
            tcomment.save()
    slug = tour.slug
    return redirect(f'/tours/tour/{slug}')
