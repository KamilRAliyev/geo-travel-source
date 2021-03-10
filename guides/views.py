from django.shortcuts import render
from .models import Guide, GuideOrder, GuidePriceTable
from .forms import GuideForm
from tours.models import *
from django.core.mail import send_mail
from django.conf import settings
from django.core.paginator import Paginator
from transport.models import *


# Create your views here.
def guide_list_view(request):
    queryset = Guide.objects.all()
    paginator = Paginator(queryset, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj,
        'guides': queryset,
        'guide_pages': Guide.objects.all(),
        'category': TourCategory.objects.all().order_by('order'),
        'transfer_static_pages': TransferStaticPage.objects.all(),
    }
    return render(request, 'guide_list.html', context=context)


def guide(request, slug):
    content = Guide.objects.get(slug=slug)
    category = TourCategory.objects.all().order_by('order')
    form = GuideForm(request.POST or None)
    price_table = GuidePriceTable.objects.filter(page=content).order_by('price')

    if request.method == "POST":
        if form.is_valid():
            name = form.cleaned_data.get('name')
            email = form.cleaned_data.get('email')
            message = form.cleaned_data.get('message')

            order = GuideOrder()
            order.name = name
            order.email = email
            order.message = message
            order.save()
            # email(, email, )
            send_mail(f"{name} | {message[:100]}", f"""
New Order Information:
Orderer: {name} ({email})
Guide page that order came: {content.name}
Message:{message}
            """, settings.EMAIL_HOST_USER, ['office@geo-travel.az'], fail_silently=False)

            return render(request,'guide.html', context={
                'content': content,
                'form': form,
                'guide_pages': Guide.objects.all(),
                'category': category,
                'table': price_table,
                'transfer_static_pages': TransferStaticPage.objects.all(),
                'message': f"We got your message. We will contact you by {email}, in the shortest period."
            })

    return render(request,'guide.html',context={
        'content': content,
        'category': category,
        'guide_pages': Guide.objects.all(),
        'transfer_static_pages': TransferStaticPage.objects.all(),
        'form': form,
        'table': price_table
    })
