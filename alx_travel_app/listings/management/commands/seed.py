$ python manage.py seed api --number=15
$ python manage.py seed api --number=15 --seeder "MyModel.my_field" "1.1.1.1"
seeder.add_entity(MyModel, 10, {
    'my_field': '1.1.1.1',
})

from django_seed import Seed

seeder = Seed.seeder()

from myapp.models import Game, Player
seeder.add_entity(Game, 5)
seeder.add_entity(Player, 10)

inserted_pks = seeder.execute()

seeder.add_entity(Player, 10, {
    'score':    lambda x: random.randint(0, 1000),
    'nickname': lambda x: seeder.faker.email(),
})
seeder.execute()

print inserted_pks
{
    <class 'faker.django.tests.Player'>: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    <class 'faker.django.tests.Game'>: [1, 2, 3, 4, 5]
}

seeder = Seed.seeder(locale='sv_SE')
seeder.faker.city()  # 'Västerås'

seeder = Seed.seeder('it_IT')

$ python runtests.py

$ python manage.py test django_seed

listings/
    management/
        __init__.py
        commands/
            __init__.py
            seed.py
from django.core.management.base import BaseCommand
from listings.models import Listing


class Command(BaseCommand):
    help = "Seed the database with sample listings"

    def handle(self, *args, **kwargs):
        sample_listings = [
            {
                "title": "Lakefront Cabin",
                "description": "Beautiful cabin with a stunning view of the lake.",
                "price_per_night": 120.00,
                "location": "Kigali, Rwanda",
                "image_url": "https://example.com/cabin.jpg",
            },
            {
                "title": "Modern Apartment",
                "description": "Stylish apartment located in the city center.",
                "price_per_night": 75.50,
                "location": "Nairobi, Kenya",
                "image_url": "https://example.com/apartment.jpg",
            },
            {
                "title": "Beach House",
                "description": "Relaxing beach house only steps from the ocean.",
                "price_per_night": 200.00,
                "location": "Mombasa, Kenya",
                "image_url": "https://example.com/beach.jpg",
            },
        ]

        for data in sample_listings:
            Listing.objects.get_or_create(**data)

        self.stdout.write(self.style.SUCCESS("Database successfully seeded!"))

python manage.py makemigrations
python manage.py migrate

python manage.py seed

Database successfully seeded!

