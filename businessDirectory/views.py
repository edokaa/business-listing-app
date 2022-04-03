from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate, login, logout

from bizdir.settings import BASE_DIR
from .models import Category, Business, Campus, Review, Uploads, User, CustomerSavedListing, CustomerMessage, \
    Notification, VendorBusinessRequest
from .forms import AddListingForm, AddCategoryForm


import os

# =====================================================================
# =================== Anonymous User / General ========================
# =====================================================================


class IndexView(View):
    def get(self, request):
        title = 'Search and post category top ads'

        side = sideBarWidget()
        context = {
            'title': title,
            'categories': side['categories'],
            'campuses': side['campuses'],
            'recent_posts': side['recent_posts'],
        }
        return render(request, 'home.html', context)


class CategoryView(View):
    def get(self, request, pk):
        title = 'Category'
        category = Category.objects.get(id=pk)
        businesses = Business.objects.filter(category_id=category.id)

        side = sideBarWidget()

        context = {
            'title': title,
            'categories': side['categories'],
            'campuses': side['campuses'],
            'recent_posts': side['recent_posts'],
            'businesses': businesses,
            'category': category,
        }
        return render(request, 'category.html', context)


class LoginView(View):
    def get(self, request, type):
        title = f"{type} Login"
        context = {
            'title': title,
            'usertype': type
        }
        return render(request, 'login.html', context)

    def post(self, request, type):
        context = {}
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('businessDirectory:home')
        else:
            context['error'] = 'Invalid Credentials, try again!'
        return render(request, 'login.html', context)


class RegisterView(View):
    def get(self, request, type):
        title = f"{type} Register"

        context = {
            'title': title,
            'user_type': type,
        }
        return render(request, 'register.html', context)

    def post(self, request, type):
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        phone = request.POST['phone']
        email = request.POST['email']
        password = request.POST['password']
        is_customer = False
        is_vendor = False

        if type == 'customer':
            is_customer = True
            is_vendor = False
        if type == 'vendor':
            is_vendor = True
            is_customer = False

        User.objects.create_user(
            username=username,
            first_name=first_name,
            last_name=last_name,
            phone=phone,
            email=email,
            password=password,
            is_customer=is_customer,
            is_vendor=is_vendor,
        )
        return HttpResponseRedirect(reverse('businessDirectory:login', args=(type,)))


class CampusBusinessView(View):
    def get(self, request, pk):
        campus = Campus.objects.get(id=pk)
        anchor = f"List of Businesses in {campus.name} Campus"
        title = 'Businesses Listing'
        businesses = Business.objects.filter(location_id=pk).order_by('name')
        side = sideBarWidget()

        context = {
            'title': title,
            'categories': side['categories'],
            'campuses': side['campuses'],
            'recent_posts': side['recent_posts'],
            'businesses': businesses,
            'anchor': anchor,
            'campus': campus,
        }
        return render(request, 'business-listing.html', context)


class BusinessListView(View):
    def get(self, request):
        title = 'Businesses Listing'
        businesses = Business.objects.all().order_by('name')
        side = sideBarWidget()

        context = {
            'title': title,
            'categories': side['categories'],
            'campuses': side['campuses'],
            'recent_posts': side['recent_posts'],
            'businesses': businesses,
        }
        return render(request, 'business-listing.html', context)

    def post(self, request):
        campus = request.POST['campus']
        category = request.POST['category']
        title = 'Businesses Listing'
        camp = cate = ''
        if campus == 'any' and category != 'any':
            businesses = Business.objects.filter(category_id=category)
            camp = 'All Campuses'
            cate = Category.objects.get(id=category)
        elif category == 'any' and campus != 'any':
            businesses = Business.objects.filter(location_id=campus)
            cate = 'All Listings'
            camp = Campus.objects.get(id=campus)

        elif category == 'any' and campus == 'any':
            businesses = Business.objects.all()
            cate = 'All Listings'
            camp = 'all campuses'
        else:
            businesses = Business.objects.filter(location_id=campus, category_id=category)
            camp = Campus.objects.get(id=campus)
            cate = Category.objects.get(id=category)

        side = sideBarWidget()

        context = {
            'title': title,
            'categories': side['categories'],
            'campuses': side['campuses'],
            'recent_posts': side['recent_posts'],
            'businesses': businesses,
            'category': cate,
            'campus': camp,
        }
        return render(request, 'business-listing.html', context)


class BusinessDetailsView(View):
    def get(self, request, pk):
        title = 'Business Details'
        images = Uploads.objects.filter(business_id=pk)
        reviews = Review.objects.all().filter(business_id=pk).order_by('-created_at')

        business = Business.objects.get(id=pk)

        side = sideBarWidget()

        context = {
            'title': title,
            'categories': side['categories'],
            'campuses': side['campuses'],
            'recent_posts': side['recent_posts'],
            'business': business,
            'reviews': reviews,
            'images': images,
            'api_key': get_google_key(),
        }
        return render(request, 'business-detail.html', context)

    def post(self, request, pk):
        # add review
        if 'rating' in request.POST:
            Review.objects.create(
                star=request.POST['rating'],
                business_id=pk,
                customer_id=request.user.id,
                msg=request.POST['comment']
            )

        # send the business  message
        if 'message' in request.POST:
            CustomerMessage.objects.create(
                receiver_id=Business.objects.get(id=pk).owner_id,
                msg=request.POST['message']
            )

        # add biz to saved list
        if 'saved_listing' in request.POST:
            CustomerSavedListing.objects.create(
                customer_id=request.user.id,
                business_id=pk
            )

        return HttpResponseRedirect(reverse('businessDirectory:business-details', args=(pk,)))



# =====================================================================
# ================================ ADMIN ==============================
# =====================================================================


class AdminDashboardView(LoginRequiredMixin, View):
    login_url = '/admin/login-page/'
    redirect_field_name = 'admin/'

    def get(self, request):
        if request.user.is_customer or request.user.is_vendor:
            return redirect('businessDirectory:home')

        title = 'Admin Dashboard'
        side = sideBarWidget()
        customer_count = User.objects.all().filter(is_customer=1).count
        vendor_count = User.objects.all().filter(is_vendor=1).count
        businesses = Business.objects.all().order_by('name')
        context = {
            'title': title,
            'recent_posts': side['recent_posts'],
            'businesses': businesses,
            'categories': side['categories'],
            'campuses': side['campuses'],
            'category_count': side['cats'].count,
            'campus_count': side['cams'].count,
            'customer_count': customer_count,
            'business_count': businesses.count,
            'vendor_count': vendor_count,

        }
        return render(request, 'admin/admin-dashboard.html', context)


class DashboardListingsView(LoginRequiredMixin, View):
    login_url = '/admin/login-page/'
    redirect_field_name = 'admin/'

    def get(self, request):
        title = 'Admin Dashboard'
        businesses = Business.objects.all().order_by('name')
        form = AddListingForm()
        side = sideBarWidget()
        vendors = User.objects.all().filter(is_vendor=1)

        context = {
            'title': title,
            'categories': side['categories'],
            'campuses': side['campuses'],
            'recent_posts': side['recent_posts'],
            'businesses': businesses,
            'vendors': vendors,
            'form': form,
        }
        return render(request, 'admin/listing.html', context)

    def post(self, request):
        form = AddListingForm(request.POST)
        if form.is_valid():
            name = request.POST['name']
            category = request.POST['category']
            location_id = request.POST['location']
            owner_id = request.POST['vendor']

            Business.objects.create(
                name=name,
                location_id=location_id,
                owner_id=owner_id,
                category_id=category,
            )
        return HttpResponseRedirect(reverse('businessDirectory:admin-listing'))


class DashboardUsersView(LoginRequiredMixin, View):
    login_url = '/admin/login-page/'
    redirect_field_name = 'admin/'

    def get(self, request, type):
        if type == 'customers':
            users = User.objects.all().filter(is_customer=1)
            reviews = []
            for customer in users:
                # just so it won't be empty i.e. since we're using just a single template for both user type
                reviews.append(Review.objects.all().filter(customer_id=customer.id).count())
            users = dict(zip(users, reviews))
            user_type = 'Customer'
        else:
            users = User.objects.all().filter(is_vendor=1)
            vendor_listings = []
            for vendor in users:
                vendor_listings.append(Business.objects.all().filter(owner_id=vendor.id).count())
            users = dict(zip(users, vendor_listings))
            user_type = 'Vendor'
        count = len(users)
        side = sideBarWidget()
        context = {
            'users': users,
            'user_type': user_type,
            'campuses': side['campuses'],
            'categories': side['categories'],
            'category_count': side['cats'].count,
            'count': count,
        }
        return render(request, 'admin/users.html', context)

    def post(self, request, type):
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        phone = request.POST['phone']
        email = request.POST['email']
        password = request.POST['password']
        is_customer = False
        is_vendor = False

        if type == 'customers':
            is_customer = True
            is_vendor = False
        else:
            is_vendor = True
            is_customer = False

        User.objects.create_user(
            username=username,
            first_name=first_name,
            last_name=last_name,
            phone=phone,
            email=email,
            password=password,
            is_customer=is_customer,
            is_vendor=is_vendor,
        )
        return HttpResponseRedirect(reverse('businessDirectory:users', args=(type,)))
        # sets user as inactive


class BusinessRequestView(View):
    context = {}
    context['title'] = 'Business Requests'

    def get(self, request):
        side = sideBarWidget()
        vendor_requests = VendorBusinessRequest.objects.all()
        if request.user.is_vendor:
            vendor_requests = VendorBusinessRequest.objects.all().filter(vendor_id=request.user.id)

        self.context['vendor_requests'] = vendor_requests
        self.context['campuses'] = side['campuses']
        self.context['categories'] = side['categories']
        return render(request, 'admin/business_request.html', self.context)


def addBusinessRequest(request, pk):
    v_request = VendorBusinessRequest.objects.get(id=pk)

    # Add the business

    Business.objects.create(
        name=v_request.business_name,
        location_id=v_request.campus.id,
        owner_id=v_request.vendor.id,
        category_id=v_request.category.id,
    )

    # changed request status to approved

    v_request.is_added = True
    v_request.save()

    # send vendor a notification
    Notification.objects.create(
        receiver_id=v_request.vendor.id,
        title='Approval of Proposed Business',
        msg=f"Dear {v_request.vendor.first_name},\nthis is to notify you that your business title {v_request.business_name} has been approved.\n Kindly Add all the necessary details as soon as possible.\n Signed\nAdmin."
    )

    return HttpResponseRedirect(reverse('businessDirectory:vendor-requests'))


def deleteBusinessRequest(request, pk):
    v_request = VendorBusinessRequest.objects.get(id=pk)

    # send the vendor a notification if the request wasn't approved

    if not v_request.is_added:
        Notification.objects.create(
            receiver_id=v_request.vendor.id,
            title='Disapproval of Proposed Business',
            msg=f"Dear {v_request.vendor.first_name}This is to notify you that your business title {v_request.business_name} was declined, appologies for any inconvinience.\n Signed\nAdmin."
        )
    v_request.delete()
    return HttpResponseRedirect(reverse('businessDirectory:vendor-requests'))


class BusinessCategoryView(LoginRequiredMixin, View):
    login_url = '/admin/login-page/'
    redirect_field_name = 'admin/'

    context = {}

    context['title'] = 'Business Categories'

    def get(self, request):
        categories = Category.objects.all()
        side = sideBarWidget()
        self.context['categories'] = side['categories']
        self.context['campuses'] = side['campuses']
        self.context['count'] = categories.count()
        self.context['form'] = AddCategoryForm()

        return render(request, 'admin/categories.html', self.context)

    def post(self, request):
        # add
        form = AddCategoryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('businessDirectory:admin-categories'))


def deleteCategory(request, pk):
    category = Category.objects.get(id=pk)
    category.delete()
    return HttpResponseRedirect(reverse('businessDirectory:admin-categories'))


# =====================================================================
# ============================= VENDORS ===============================
# =====================================================================

class VendorNotificationView(LoginRequiredMixin,View):
    login_url = '/vendor/login/'
    redirect_field_name = '/vendor/listings/'
    context = {}

    def get(self, request):
        notifications = Notification.objects.all().filter(receiver_id=request.user.id).order_by('-sent_at')
        side = sideBarWidget()
        self.context['categories'] = side['categories']
        self.context['campuses'] = side['campuses']
        self.context['notifications'] = notifications
        return render(request, 'vendor/notifications.html', self.context)


class VendorMessageView(LoginRequiredMixin,View):
    login_url = '/vendor/login/'
    redirect_field_name = '/vendor/listings/'
    context = {}

    def get(self, request):
        messages = CustomerMessage.objects.all().filter(receiver_id=request.user.id).order_by('-sent_at')
        side = sideBarWidget()
        self.context['categories'] = side['categories']
        self.context['campuses'] = side['campuses']
        self.context['messages'] = messages
        return render(request, 'vendor/messages.html', self.context)


class VendorListingsView(LoginRequiredMixin,View):
    login_url = '/vendor/login/'
    redirect_field_name = 'vendor/listings/'
    context = {}

    def get(self, request):
        listings = Business.objects.all().filter(owner_id=request.user.id)
        side = sideBarWidget()
        self.context['categories'] = side['categories']
        self.context['campuses'] = side['campuses']
        self.context['title'] = 'My Listings'
        self.context['listings'] = listings
        self.context['count'] = listings.count()
        self.context['messages'] = CustomerMessage.objects.all()
        self.context['notifications'] = Notification.objects.all()
        self.context['form'] = AddListingForm()
        return render(request, 'vendor/my_listings.html', self.context)

    def post(self, request):
        name = request.POST['name']
        category = request.POST['category']
        campus = request.POST['location']

        VendorBusinessRequest.objects.create(
            vendor_id=request.user.id,
            business_name=name,
            category_id=category,
            campus_id=campus,
        )
        return HttpResponseRedirect(reverse('businessDirectory:vendor-listing'))


# class AddListingView(LoginRequiredMixin,View):
#     login_url = '/vendor/login/'
#     redirect_field_name = 'vendor/listings/'
#
#     context = {}
#
#     def get(self, request):
#         form = AddListingForm()
#         self.context['title'] = 'Add Listings'
#         self.context['form'] = form
#         self.context['messages'] = CustomerMessage.objects.all()
#         self.context['notifications'] = Notification.objects.all()
#         return render(request, 'vendor/add_listing.html', self.context)
#
#     def post(self, request):
#         form = AddListingForm(request.POST)
#         if form.is_valid():
#             # form.save()
#             name = request.POST['name']
#             description = request.POST['description']
#             logo = request.FILES['logo']
#             category = request.POST['category']
#             address = request.POST['address']
#             landmark = request.POST['landmark']
#             location_id = request.POST['location']
#             longitude = request.POST['longitude']
#             latitude = request.POST['latitude']
#             email = request.POST['email']
#             phone = request.POST['phone']
#             website = request.POST['website']
#             owner_id = request.user.id
#
#             Business.objects.create(
#                 name=name,
#                 logo=logo,
#                 landmark=landmark,
#                 email=email,
#                 website=website,
#                 description=description,
#                 location_id=location_id,
#                 address=address,
#                 owner_id=owner_id,
#                 category_id=category,
#                 longitude=longitude,
#                 latitude=latitude,
#                 phone=phone
#             )
#
#             return HttpResponseRedirect(reverse('businessDirectory:vendor-listing'))
#         else:
#             self.context['upload_error'] = 'Error adding business, please try again'
#             return render(request, 'vendor/add_listing.html', self.context)


class ModifyListingView(View):
    context = {}

    def get(self, request, pk):
        self.context['title'] = 'Edit Listing'
        self.context['listing'] = Business.objects.get(id=pk)
        self.context['images'] = Uploads.objects.filter(business_id=pk)
        self.context['messages'] = CustomerMessage.objects.all()
        self.context['notifications'] = Notification.objects.all()
        self.context['user_type'] = 'vendor'
        self.context['api_key'] = get_google_key()
        return render(request, 'vendor/modify_listing.html', self.context)

    def post(self, request, pk):
        if 'edit_business' in request.POST:
            business = Business.objects.get(id=pk)
            if 'logo' in request.FILES:
                business.logo = request.FILES['logo']
            business.description = request.POST['description']
            business.phone = request.POST['phone']
            business.email = request.POST['email']
            business.website = request.POST['website']
            business.address = request.POST['address']
            business.landmark = request.POST['landmark']

            business.save()

        if 'gallery_image' in request.FILES:
            image = request.FILES['gallery_image']
            Uploads.objects.create(
                image_url=image,
                business_id=pk
            )

        return HttpResponseRedirect(reverse('businessDirectory:modify-listing', args=(pk,)))


def deleteBusinessImage(request, pk):
    image = Uploads.objects.get(id=pk)
    business_id = image.business_id
    image.delete()
    return HttpResponseRedirect(reverse('businessDirectory:modify-listing', args=(business_id,)))


def deleteNotification(request, pk):
    notification = Notification.objects.get(id=pk)
    notification.delete()
    return HttpResponseRedirect(reverse('businessDirectory:vendor-notification'))


# =====================================================================
# ============================= CUSTOMERS =============================
# =====================================================================


class UserProfileView(LoginRequiredMixin, View):
    login_url = '/customer/login/'
    redirect_field_name = 'customer/profile/'

    context = {}

    def get(self, request, user_type):
        self.context['title'] = f"{user_type} Profile"
        self.context['user_type'] = user_type
        self.context['messages'] = CustomerMessage.objects.all()
        self.context['notifications'] = Notification.objects.all()
        return render(request, 'user_profile.html', self.context)

    def post(self, request, user_type):
        # edit profile
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        phone = request.POST['phone']

        user = request.user
        if 'photo_url' in request.FILES:
            user.photo_url = request.FILES['photo_url']

        user.first_name = first_name
        user.last_name = last_name
        user.phone = phone
        user.save()

        return render(request, 'user_profile.html', self.context)


class CustomerListingsView(LoginRequiredMixin, View):
    login_url = '/customer/login/'
    redirect_field_name = 'customer/saved-listings/'

    def get(self, request):
        context = {}
        title = 'Customer Saved Listings'
        listings = CustomerSavedListing.objects.filter(customer_id=request.user.id)

        context['title'] = title
        context['listings'] = listings
        context['count'] = listings.count()

        return render(request, 'customer/saved_listings.html', context)


def delete_saved_listing(request, pk):
    # removed saved listing
    listing = CustomerSavedListing.objects.get(id=pk)
    listing.delete()

    return HttpResponseRedirect(reverse('businessDirectory:customer-saved-listings'))


# =====================================================================
# ====================== AUTHENTICATED USERS ==========================
# =====================================================================


def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
    return HttpResponseRedirect(reverse('businessDirectory:home'))


def deleteListingView(request, pk):
    if request.user.is_authenticated:
        business = Business.objects.get(id=pk)
        if request.user.is_admin:
            business.delete()
            return HttpResponseRedirect(reverse('businessDirectory:admin-listing'))
        elif request.user.is_vendor:
            business.delete()
            return HttpResponseRedirect(reverse('businessDirectory:vendor-listing'))
        else:
            return HttpResponseRedirect(reverse('businessDirectory:business-list'))
    else:
        return HttpResponseRedirect(reverse('businessDirectory:home'))


# =====================================================================
# ======================== Helper Methods =============================
# =====================================================================


def sideBarWidget():
    cat = Category.objects.all().order_by('name')
    cam = Campus.objects.all().order_by('name')
    cat_count = []
    campus_count = []

    # getting the number of businesses in each category / campus
    for c in cat:
        cat_count.append(Business.objects.filter(category_id=c.id).count())
    for c in cam:
        campus_count.append(Business.objects.filter(location_id=c.id).count())

    # converting to dictionary to enable easy parallel indexing
    categories = dict(zip(cat, cat_count))
    campuses = dict(zip(cam, campus_count))

    # for side bar
    # top_businesses = Review.objects.all().order_by('star')[1:5:1]
    recent_posts = Business.objects.all().order_by('-added_on')[0:5:1]

    result = {
        'categories': categories,
        'campuses': campuses,
        'recent_posts': recent_posts,
        'cats': cat,
        'cams': cam,
    }
    return result

def get_google_key():
    with open(f"{BASE_DIR}/google.txt", 'r') as file:
        key = file.read()
    return key