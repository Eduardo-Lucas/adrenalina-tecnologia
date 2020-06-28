from django.urls import path
from apps.accounts.views import *


app_name = 'accounts'

urlpatterns = [
    path('register/', registerPage, name="register"),
    path('login/', login_page, name='login'),
    path('logout/', logout_user, name='logout'),


]
