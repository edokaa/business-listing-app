from django.db import models

# Create your models here.


class Avatar(models.Model):
    photo = models.CharField(max_length=50)


# class UserManager(BaseUserManager):
#     def create_user(self, email, username, phone, first_name, last_name, photo_url, password=None):
#         if not email:
#             raise ValueError("Email is required")
#         if not username:
#             raise ValueError("Username is required")
#         if not phone:
#             raise ValueError("provide a phone number")
#         if not first_name and last_name:
#             raise ValueError("provide a valid name")
#
#         user = self.model(
#             email=self.normalize_email(email),
#             phone=phone,
#             first_name=first_name,
#             last_name=last_name,
#             photo_url=photo_url,
#         )
#         user.set_password(password)
#         user.save(using=self._db)
#         return user
#
#     def create_customer(self, email, username, phone, first_name, last_name, photo_url, password=None):
#         customer = self.create_user(
#             email=email,
#             username=username,
#             phone=phone,
#             first_name=first_name,
#             last_name=last_name,
#             photo_url=photo_url,
#         )
#         customer.is_customer = True
#         customer.save(using=self._db)
#
#         return customer
#
#     def create_vendor(self, email, username, phone, first_name, last_name, photo_url, password=None):
#         vendor = self.create_user(
#             email=email,
#             username=username,
#             phone=phone,
#             first_name=first_name,
#             last_name=last_name,
#             photo_url=photo_url,
#         )
#         vendor.is_vendor = True
#         vendor.save(using=self._db)
#
#         return vendor
#
#     def create_superuser(self, email, username, phone, first_name, last_name, photo_url, password=None):
#         admin = self.create_user(
#             email=email,
#             username=username,
#             phone=phone,
#             first_name=first_name,
#             last_name=last_name,
#             photo_url=photo_url,
#         )
#         admin.is_admin = True
#         admin.is_superuser = True
#         admin.save(using=self._db)
#
#         return admin


# class User(AbstractUser):
#     phone = models.CharField(max_length=50, unique=True),
#     is_admin = models.BooleanField(default=False)
#     is_vendor = models.BooleanField(default=False)
#     is_customer = models.BooleanField(default=False)
#     photo_url = models.FileField(upload_to='static/uploads/profile_photos/',
#                                  default='static/uploads/profile_photos/nophoto-male.jpg')
#
#     def __str__(self):
#         return self.username
#
#     def has_perm(self, perm, obj=None):
#         return True
#
#     def has_module_perms(self, app_label):
#         return True
#

class Admin(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    lastLogin = models.DateTimeField()
    avatarId = models.ForeignKey(Avatar, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.username


class Vendor(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    # email = models.CharField(max_length=50)
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    avatarId = models.ForeignKey(Avatar, on_delete=models.SET_NULL, null=True)
    address = models.CharField(max_length=255)

    def __str__(self):
        return self.username


class Customer(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    # email = models.CharField(max_length=50)
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    avatarId = models.ForeignKey(Avatar, on_delete=models.SET_NULL, null=True)
    address = models.CharField(max_length=255)

    def __str__(self):
        return self.username


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
    logo = models.FileField(upload_to='static/uploads/logos/')
    landmark = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    website = models.CharField(max_length=50, blank=True)
    description = models.TextField(max_length=100, blank=True)
    location = models.ForeignKey(Campus, on_delete=models.RESTRICT)
    address = models.CharField(max_length=50)
    owner = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    longitute = models.CharField(max_length=50)
    latitude = models.CharField(max_length=50)
    addedon = models.DateTimeField(auto_now=True)
    phone = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Review(models.Model):
    star_choices = [(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')]
    star = models.IntegerField(choices=star_choices)
    business = models.ForeignKey(Business, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    msg = models.TextField(max_length=50, blank=True)
    createdAt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.star}Star >>> {self.business.name}"


class Uploads(models.Model):
    image_url = models.FileField(upload_to='static/uploads/images/')
    business = models.ForeignKey(Business, on_delete=models.CASCADE)

    def __str__(self):
        return self.business.name


# class Notification(models.Model):
#     sender
#     reciever
#     title
#     msg
#     sentAt
#
