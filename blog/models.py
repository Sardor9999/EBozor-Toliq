from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class Customer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    contact = models.OneToOneField(to="Contact", on_delete=models.CASCADE)
    address = models.ForeignKey(to="Address",  on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Order(models.Model):
    customer = models.ForeignKey(to=Customer, on_delete=models.CASCADE, related_name="orders")
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    product = models.ManyToManyField(to="Product", related_name="orders")
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.customer.first_name}-{self.total_price}"

class Contact(models.Model):
    email = models.EmailField(max_length=100)
    phone = PhoneNumberField(unique=True)

    def __str__(self):
        return f"{self.email} {self.phone}"
class Address(models.Model):
    UZB = 'uzb'
    RUS = 'rus'
    TJK = 'tjk'
    TKM = 'tkm'
    QZK = 'qzk'
    COUNTRIES = (
        (UZB, "UZBEKISTAN"),
        (RUS, "RUSSIYA"),
        (TJK, "TAJIKISTAN"),
        (TKM, "TURKMANISTAN"),
        (QZK, "QAZAKISTAN"),

    )
    street = models.CharField(max_length=150)
    city = models.CharField(max_length=150)
    zipcode = models.CharField(max_length=15)
    country = models.CharField(max_length=20, choices=COUNTRIES, default=UZB)

    def __str__(self):
        return f"{self.street} {self.city} {self.country}"

class Category(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)

    def __str__(self):
        return self.title

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    category = models.ForeignKey(to="Category", on_delete=models.CASCADE, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to="product/", null=True)
    in_stock = models.BooleanField(default=True)

class TGUser(models.Model):
    tg_id = models.PositiveBigIntegerField(unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    user_name = models.CharField(max_length=100, null=True, blank=True)
    about = models.TextField(null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name}-{self.last_name}"