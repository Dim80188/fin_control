from django.urls import path

from .views import *

urlpatterns = [
    # path('register', register, name='register'),
    # path('login', user_login, name='login'),
    path('register', UserRegisterView.as_view(), name='register'),
    path('login', UserLoginView.as_view(), name='login'),
    path('logout', UserLogoutView.as_view(), name='logout'),
    # path('logout', user_logout, name='logout'),
    path('', index, name='home'),
    path('add_costs/', AddCosts.as_view(), name='add_costs'),
    path('add_inkome/', AddInkome.as_view(), name='add_inkome'),
    path('view_all_costs/', AllCosts.as_view(), name='all_costs'),
    path('view_all_inkome/', AllInkome.as_view(), name='all_inkome'),
    path('update_costs/<int:pk>/', UpdateCosts.as_view(), name='update_costs'),
    path('delete_costs/<int:pk>/', DeleteCosts.as_view(), name='delete_costs'),
    path('view_day_costs/', DayCosts.as_view(), name='day_costs'),
    path('view_week_costs/', WeekCosts.as_view(), name='week_costs'),
    path('view_month_costs/', MonthCosts.as_view(), name='month_costs'),
    path('select_period/', select_period, name='select_period'),
    path('view_selected_costs', select_period, name='view_selected_costs'),
]
