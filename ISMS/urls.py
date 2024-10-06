from django.urls import path, include
from ISMS.views import home,login, registration

urlpatterns = [
    path('', home),
    path('login/', login),
    path('registration/', registration),
]