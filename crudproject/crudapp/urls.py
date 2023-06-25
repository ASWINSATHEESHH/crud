from django.urls import path
from .views import Home,Contact,Login, Logout_admin, Index, View_Project, Add_Project
from . import views

urlpatterns = [
    path('', Home, name='home'),
    path('contact/',Contact, name='contact'),
    path('admin_login/',Login, name='login'),
    path('logout/',Logout_admin, name='logout_admin'),
    path('index/', Index, name='dashboard'),
    path('viewproject/', View_Project, name='viewproject'),
    path('addproject/', Add_Project, name='addproject'),
    path('deleteproject/<int:pid>/', views.Delete_Project, name='deleteproject'),
]