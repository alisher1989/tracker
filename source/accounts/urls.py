from django.urls import path
from accounts.views import logout_view, login_view, register_view,\
    user_activate_view, UserDetailView

urlpatterns = [
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', register_view, name='register'),
    path('activate/<token>/', user_activate_view, name='user_activate'),
    path('profile/<pk>/', UserDetailView.as_view(), name='user_detail')
]


app_name = 'accounts'