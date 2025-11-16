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
    
xcopy alx_travel_app alx_travel_app_0x00 /E /I

from django.db import models
from django.contrib.auth.models import User


class Listing(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2)
    location = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    # Example: photo URLs, later you may use ImageField instead
    image_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title


class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="bookings")
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="bookings")

    check_in = models.DateField()
    check_out = models.DateField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Booking {self.id} - {self.user.username}"


class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reviews")
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="reviews")

    rating = models.PositiveIntegerField()  # 1–5
    comment = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review {self.rating}/5 for {self.listing.title}"

