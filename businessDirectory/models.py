from django.db import models
from django.contrib.auth.models import AbstractUser, User


# Create your models here.


class User(AbstractUser):
    is_admin = models.BooleanField(default=False)
    is_vendor = models.BooleanField(default=False)
    is_customer = models.BooleanField(default=False)
    phone = models.CharField(max_length=20, blank=True)
    photo_url = models.FileField(upload_to='static/uploads/profile_photos/',
                                 default='static/uploads/profile_photos/nophoto-male.jpg')

    def __str__(self):
        return self.first_name


class Category(models.Model):
    name = models.CharField(max_length=50)
    img = models.FileField(upload_to='static/uploads/thumbs/')

    def __str__(self):
        return self.name


class Campus(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Business(models.Model):
    name = models.CharField(max_length=50)
    logo = models.FileField(upload_to='static/uploads/logos/', default='static/uploads/logos/no-image.png')
    landmark = models.CharField(max_length=50, blank=True)
    email = models.CharField(max_length=50, blank=True)
    website = models.CharField(max_length=50, blank=True)
    description = models.TextField(max_length=255, blank=True)
    location = models.ForeignKey(Campus, on_delete=models.RESTRICT)
    address = models.CharField(max_length=100, blank=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    latitude = models.CharField(max_length=50, default=6.8644553)
    longitude = models.CharField(max_length=50, default=7.4060996)
    added_on = models.DateTimeField(auto_now=True)
    phone = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.name


class Review(models.Model):
    star_choices = [(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')]
    star = models.IntegerField(choices=star_choices)
    business = models.ForeignKey(Business, on_delete=models.CASCADE)
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    msg = models.TextField(max_length=50, blank=True)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.star}Star >>> {self.business.name}"


class Uploads(models.Model):
    image_url = models.FileField(upload_to='static/uploads/images/')
    business = models.ForeignKey(Business, on_delete=models.CASCADE)

    def __str__(self):
        return self.business.name


class Notification(models.Model):
    #  since it will only be sent by the admin... no need specifying the sender..
    # besides it will through an error since its just one user model we're using
    # and can't

    receiver = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    msg = models.TextField(max_length=255)
    is_read = models.BooleanField(default=False)
    sent_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class CustomerMessage(models.Model):
    #  sent by the customer to the vendor of a business...
    # This is in no way an alternative of a chatting system
    # just for simplicity sake

    receiver = models.ForeignKey(User, on_delete=models.CASCADE)
    # business =
    msg = models.TextField(max_length=255)
    is_read = models.BooleanField(default=False)
    sent_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.sent_at


class CustomerSavedListing(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    business = models.ForeignKey(Business, on_delete=models.CASCADE)
    saved_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.business.name


class VendorBusinessRequest(models.Model):
    vendor = models.ForeignKey(User, on_delete=models.CASCADE)
    business_name = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    campus = models.ForeignKey(Campus, on_delete=models.RESTRICT)
    is_added = models.BooleanField(default=False)
    sent_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.business_name
