from typing import cast
from django.core.management.base import BaseCommand
from django.db.models.fields import DurationField
from faker import Faker
import faker
import faker.providers as provider
from tours.models import TourCategory, Tour, TourPriceTable
import random

Faker.seed(0)

TourCategory.objects.create(name="New Year tours", order=0),
TourCategory.objects.create(name="Hallowen tours", order=0),
TourCategory.objects.create(name="Novruz tours", order=0),
TourCategory.objects.create(name="Kurban holidays", order=0),
TourCategory.objects.create(name="Ramazan holiday", order=0),


CATEGORIES = TourCategory.objects.all()
print(CATEGORIES)

class Command(BaseCommand):
    help = "for generating fake data with Faker"

    def handle(self, *args,**kwargs):
        fake = Faker()
        
        for i in range(100):
            a = Tour(
                name=f"{fake.location_on_land()[2]} {fake.location_on_land()[-1]}", 
                description=fake.paragraph(nb_sentences=1),
                price = float(fake.bothify(text="###.##")),
                duration=5,
                city=fake.location_on_land()[2],
                rating=5,
                category= CATEGORIES[random.randrange(0,len(CATEGORIES)-1)]
            )
            
            a.save()

            TourPriceTable.objects.create(tour=a, price=40.00, desc="per person (for 10 pax)")
            TourPriceTable.objects.create(tour=a, price=45.00, desc="per person (for 9 pax)")
            TourPriceTable.objects.create(tour=a, price=50.00, desc="per person (for 8 pax)")
            TourPriceTable.objects.create(tour=a, price=55.00, desc="per person (for 7 pax)")
            TourPriceTable.objects.create(tour=a, price=60.00, desc="per person (for 6 pax)")
            TourPriceTable.objects.create(tour=a, price=65.00, desc="per person (for 5 pax)")
            TourPriceTable.objects.create(tour=a, price=70.00, desc="per person (for 4 pax)")
            TourPriceTable.objects.create(tour=a, price=85.00, desc="per person (for 3 pax)")
            TourPriceTable.objects.create(tour=a, price=115.00, desc="per person (for 2 pax)")
            TourPriceTable.objects.create(tour=a, price=140.00, desc="per person (for 1 pax)")
