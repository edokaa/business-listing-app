from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate, login, logout


from .models import Category, Business, Campus, Review, Uploads, Customer, Vendor


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


class AdminLoginView(View):
    def get(self, request):
        title = "Admin Login"

        context = {
            'title': title,
        }
        return render(request, 'admin/admin-login.html', context)

    def post(self, request):
        pass


class LoginView(View):
    def get(self, request, type):
        title = f"{type} Login"

        context = {
            'title': title,
        }
        return render(request, 'login.html', context)

    def post(self, request):
        pass


class RegisterView(View):
    def get(self, request, type):
        title = f"{type} Register"
        # form = RegisterForm()

        context = {
            'title': title,
            # 'form': form,
        }
        return render(request, 'register.html', context)

    def post(self, request):
        pass


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
        reviews = Review.objects.all().filter(business_id=pk)
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
        }
        return render(request, 'business-detail.html', context)


class DashboardView(View):
    def get(self, request):
        title = 'Admin Dashboard'
        side = sideBarWidget()
        customer_count = Customer.objects.all().count
        vendor_count = Vendor.objects.all().count
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


class DashboardListingsView(View):
    def get(self, request):
        title = 'Admin Dashboard'
        businesses = Business.objects.all().order_by('name')
        side = sideBarWidget()

        context = {
            'title': title,
            'categories': side['categories'],
            'campuses': side['campuses'],
            'recent_posts': side['recent_posts'],
            'businesses': businesses,
        }
        return render(request, 'admin/listing.html', context)


class DashboardUsersView(View):
    def get(self, request, type):
        if type == 'customers':
            users = Customer.objects.all()
            reviews = []
            for customer in users:
                reviews.append(Review.objects.all().filter(customer_id=customer.id).count())
            users = dict(zip(users, reviews))
            user_type = 'Customer'
        else:
            users = Vendor.objects.all()
            vendor_listings = []
            for vendor in users:
                vendor_listings.append(Business.objects.all().filter(owner_id=vendor.id).count())
            users = dict(zip(users, vendor_listings))
            user_type = 'Vendor'
        count = len(users)
        context = {
            'users': users,
            'user_type': user_type,
            'count': count,
        }
        return render(request, 'admin/users.html', context)


class CustomerProfileView(View):
    def get(self, request):
        title = 'Customer profile'
        context = {
            'title': title,
        }
        return render(request, 'customer/../businessDirectory/templates/user_profile.html', context)

    def post(self, request):
        # edit profile
        # modify password
        pass


class CustomerListingsView(View):
    def get(self, request):
        title = 'Customer Saved Listings'
        context = {
            'title': title,
        }
        return render(request, 'customer/saved_listings.html', context)

    def post(self, request):
        # removed saved listing
        pass


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
    recent_posts = Business.objects.all().order_by('-addedon')[0:5:1]

    result = {
        'categories': categories,
        'campuses': campuses,
        'recent_posts': recent_posts,
        'cats': cat,
        'cams': cam,
    }
    return result

# class SideBarView(View):
#     def get(self, request):
#         title = 'Search and post category top ads'
#         cat = Category.objects.all().order_by('name')
#         cam = Campus.objects.all().order_by('name')
#         cat_count = []
#         campus_count = []
#
#         # getting the number of businesses in each category / campus
#         for c in cat:
#             cat_count.append(Business.objects.filter(category_id=c.id).count())
#         for c in cam:
#             campus_count.append(Business.objects.filter(location_id=c.id).count())
#
#         # converting to dictionary to enable easy parallel indexing
#         categories = dict(zip(cat, cat_count))
#         campuses = dict(zip(cam, campus_count))
#
#         context = {
#             'title': title,
#             'categories': categories,
#             'campuses': campuses,
#         }
#         return render(request, 'include/side-bar.html', context)
