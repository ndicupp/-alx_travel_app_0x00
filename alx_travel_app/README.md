1. Duplicate the Project

From your terminal:
cp -r alx_travel_app alx_travel_app_0x00

Or on Windows:
xcopy alx_travel_app alx_travel_app_0x00 /E /I

2. Create Models — listings/models.py

Below is a clean and realistic implementation for Listing, Booking, Review.

one to one fields
from django.db import models

class User(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return str(self.name)

class Profile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.PROTECT,
        primary_key=True,
    )
    language = models.CharField(max_length=50)
    email = models.EmailField(max_length=70,blank=True,unique=True)

    def __str__(self):
        return str(self.email)


many to one fields
from django.db import models

class Author(models.Model): 
    name = models.CharField(max_length=50, blank=False, unique=True)

    def __str__(self):
        return str(self.name)

class Book(models.Model):
    author = models.ForeignKey(
        Author,
        on_delete=models.PROTECT,
        blank=False
    )

    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

many to many fields
from django.db import models

class Collection(models.Model):
  name = models.CharField(max_length=50)

  def __str__(self):
        return str(self.name)

class Book(models.Model):
  collection = models.ManyToManyField(Collection)

  title = models.CharField(max_length=100)

  def __str__(self):
        return str(self.title)

reate Serializers — listings/serializers.py

You only need ListingSerializer and BookingSerializer (as per instructions).

[
  {
    "model": "myapp.person",
    "pk": 1,
    "fields": {
      "first_name": "John",
      "last_name": "Lennon"
    }
  },
  {
    "model": "myapp.person",
    "pk": 2,
    "fields": {
      "first_name": "Paul",
      "last_name": "McCartney"
    }
  }
]

- model: myapp.person
  pk: 1
  fields:
    first_name: John
    last_name: Lennon
- model: myapp.person
  pk: 2
  fields:
    first_name: Paul
    last_name: McCartney

Create Seeder (Management Command)
File structure needed:
Using with command
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

rint inserted_pks
{
    <class 'faker.django.tests.Player'>: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    <class 'faker.django.tests.Game'>: [1, 2, 3, 4, 5]
}

seeder = Seed.seeder(locale='sv_SE')
seeder.faker.city()  # 'Västerås'

seeder = Seed.seeder('it_IT')

$ python runtests.py
$ python manage.py test django_seed




