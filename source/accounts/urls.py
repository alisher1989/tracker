from django.urls import path
from accounts.views import logout_view, login_view, register_view

urlpatterns = [
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', register_view, name='register'),
]


app_name = 'accounts'