from django.urls import path
from django.views.generic import TemplateView
from . import views

app_name = 'businessDirectory'

urlpatterns = [
    # anonymous
    path('', views.IndexView.as_view(), name='home'),
    path('category/<int:pk>/', views.CategoryView.as_view(), name='category'),
    path('<str:type>/login/', views.LoginView.as_view(), name='login'),
    path('<str:type>/register/', views.RegisterView.as_view(), name='register'),
    path('business/<int:pk>/details/', views.BusinessDetailsView.as_view(), name='business-details'),
    path('business/list/', views.BusinessListView.as_view(), name='business-list'),
    path('campus/business/<int:pk>/', views.CampusBusinessView.as_view(), name='campus-business'),

    # admin
    path('admin/', views.AdminDashboardView.as_view(), name='admin'),
    path('admin/listings/', views.DashboardListingsView.as_view(), name='admin-listing'),
    path('admin/vendor-requests/', views.BusinessRequestView.as_view(), name='vendor-requests'),
    path('admin/vendor-requests/add/<int:pk>', views.addBusinessRequest, name='add-request'),
    path('admin/vendor-requests/delete/<int:pk>', views.deleteBusinessRequest, name='delete-request'),
    path('admin/listings/categories', views.BusinessCategoryView.as_view(), name='admin-categories'),
    path('admin/listings/categories/delete/<int:pk>', views.deleteCategory, name='delete-category'),
    path('admin/users/<str:type>/', views.DashboardUsersView.as_view(), name='users'),

    # vendor
    path('vendor/listings/', views.VendorListingsView.as_view(), name='vendor-listing'),
    path('vendor/notifications/', views.VendorNotificationView.as_view(), name='vendor-notification'),
    path('vendor/messages/', views.VendorMessageView.as_view(), name='vendor-messages'),
    path('vendor/notifications/delete/<int:pk>', views.deleteNotification, name='delete-notification'),
    # path('vendor/listings/add', views.AddListingView.as_view(), name='add-listing'),
    path('vendor/listings/<int:pk>/', views.ModifyListingView.as_view(), name='modify-listing'),
    path('vendor/listings/delete-image/<int:pk>', views.deleteBusinessImage, name='delete-image'),
    # path('vendor/notifications/delete', views.CustomerProfileView.as_view(), name='customer-profile'),

    # customer
    path('customer/saved-listings/', views.CustomerListingsView.as_view(), name='customer-saved-listings'),
    path('customer/saved-listings/delete/<int:pk>/', views.delete_saved_listing, name='customer-delete-saved-listings'),

    # general
    path('logout/', views.logout_view, name='logout'),
    path('delete-listings/<int:pk>/', views.deleteListingView, name='delete-listing'),
    path('<str:user_type>/profile/', views.UserProfileView.as_view(), name='user-profile'),
]
